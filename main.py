from flask import Flask, request, Response
import requests
from logger import start_log, end_log
from special_api import update_headers, update_json_data
from verify import verify_request

app = Flask(__name__)

REQ_EXCLUDED_HEADERS = ['Host', 'Content-Length', 'username', 'password', 'client_ip', 'Internal-Authentication']
RESP_EXCLUDED_HEADERS = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']

@app.route('/proxy', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy():
    start_log()

    status, response = verify_request(request)
    if not status:
        return response
    
    client_ip = request.headers.get('client-ip')
    headers = {key: value for key, value in request.headers if key not in REQ_EXCLUDED_HEADERS}
    api_url = request.args.get('api_url')

    update_headers(headers, api_url)
    data = update_json_data(request.data, api_url)
    method = request.method

    try:
        resp = requests.request(method, api_url, headers=headers, params=request.args, data=data)
    except requests.exceptions.ConnectionError as e:
        return Response('Host PC does not have Internet. Please contact the administrator.', status=402)

    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in RESP_EXCLUDED_HEADERS]

    response = Response(resp.content, resp.status_code, headers)
    response.headers['Content-Type'] = resp.headers['Content-Type']

    end_log(response, client_ip)
    return response


if __name__ == '__main__':
    app.run(debug=True)