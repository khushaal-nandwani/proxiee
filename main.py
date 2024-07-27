import subprocess
from flask import Flask, request, Response
import requests
from configuration import get_bat_file
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



@app.route('/merge', methods=['GET'])
def merge():
    bat_file, _ = get_bat_file()

    if not bat_file:
        return Response('Batch File not found', status=500)

    from_remote = request.args.get('from')
    to_remote = request.args.get('to')
    branch = request.args.get('branch')

    if not from_remote or not to_remote or not branch:
        return Response("Missing parameters", status=400)

    bat_command = f'{bat_file} {from_remote} {to_remote} {branch}'

    result = subprocess.run(bat_command, shell=True, check=True, text=True, capture_output=True, timeout=5) 
    return Response(result.stdout, status=200)

if __name__ == '__main__':
    app.run(debug=True)