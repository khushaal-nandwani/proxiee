from flask import Flask, request, jsonify, Response
import requests
from manage_apis import is_api_key_valid, is_api_allowed
import logging
import time

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def log_request(response):
    processing_time = time.time() - request.start_time
    client_ip = request.remote_addr
    logger.info(f"{request.method} {request.path} {response.status_code} {processing_time} {client_ip}")
    return response


@app.route('/proxy', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy():
    start_timer()
    # API Key Validation
    proxy_api_key = request.headers.get('Proxy-Api-Key')

    if not proxy_api_key:
        return Response("Missing Proxy-Api-Key", status=400)

    if not is_api_key_valid(proxy_api_key):   
        return Response("Invalid Proxy-Api-Key", status=403)

    # API URL Validation       
    api_url = request.args.get('api_url')

    if not api_url:
        return Response("Missing API URL", status=400)
    
    if not is_api_allowed(api_url):
        return Response("API not allowed", status=403)
    
    # payload = request.get_json()
    # test a payload api

    headers = {key: value for key, value in request.headers if key not in ['Host', 'Content-Length', 'Proxy-Api-Key']}

    method = request.method
    
    resp = requests.request(method, api_url, headers=headers, params=request.args, data=request.data)

    # Return the exact response received from the external API
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    # Create a response with the same status code and content
    response = Response(resp.content, resp.status_code, headers)
    response.headers['Content-Type'] = resp.headers['Content-Type']

    log_request(response)

    return response


if __name__ == '__main__':
    app.run(debug=True)