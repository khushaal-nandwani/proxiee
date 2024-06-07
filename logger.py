from flask import request
import logging 
import time
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

current_date = datetime.now().strftime("%d_%m_%Y")
log_file_name = f'./logs/proxiee_logs_{current_date}.csv'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler(log_file_name, when='midnight', interval=1, backupCount=7)
logger.addHandler(handler)


def start_log():
    request.start_time = time.time()


def end_log(response, client_ip):
    processing_time = time.time() - request.start_time
    logger.info(f"{request.headers.get('username')},{request.method},{request.args.get('api_url')},{response.status_code},{response.json},{processing_time},{client_ip}")
    return response
