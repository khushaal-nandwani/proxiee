from flask import Flask, request, Response
import requests
from configuration import is_api_allowed, is_user_valid, get_config
from logger import start_log, end_log
from special_api import *

app = Flask(__name__)

EXCLUDED_HEADERS = ['Host', 'Content-Length', 'username', 'password']

@app.route('/proxy', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy():
    start_log()

    # Validate Username and Password
    username = request.headers.get('username')
    password = request.headers.get('password')
    
    if not (username or password):
        return Response('Username or Password Missing', status=400)

    if not is_user_valid(username, password):
        return Response('Incorrect Username or Password', status=403)

    api_url = request.args.get('api_url')

    if not api_url:
        return Response("Missing API URL", status=400)
    
    if not is_api_allowed(api_url):
        return Response("API not allowed", status=403)

    headers = {key: value for key, value in request.headers if key not in EXCLUDED_HEADERS}
    handle_api = get_special_url_handler(api_url)
    special_key = handle_api.get_special_key(get_config())
    headers = handle_api.add_headers(headers, special_key)
    method = request.method

    try:
        resp = requests.request(method, api_url, headers=headers, params=request.args, data=request.data)
    except requests.exceptions.ConnectionError as e:
        return Response('Host PC does not have Internet. Please contact the administrator.', status=402)


    # Return the exact response received from the external API
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    # Create a response with the same status code and content
    response = Response(resp.content, resp.status_code, headers)
    response.headers['Content-Type'] = resp.headers['Content-Type']

    end_log(response)

    return response


if __name__ == '__main__':
    app.run(debug=True)