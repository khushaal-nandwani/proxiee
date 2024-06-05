from flask import request
import logging 
import time


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def start_log():
    request.start_time = time.time()


def end_log(response):
    processing_time = time.time() - request.start_time
    client_ip = request.remote_addr
    logger.info(f"Method: {request.method} | Path: {request.path} | Response Code: {response.status_code} | Process Time: {processing_time} | Client IP: {client_ip}")
    return response
