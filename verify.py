from flask import Response
from configuration import is_api_allowed, is_user_valid, is_ip_allowed
import jwt


def verify_request(request):
    authR = _verify_internal_authenticaton(request.headers.get('Interal-Authentication').split()[1])
    if not authR[0]:
        return authR
    
    ipR = _verify_ip(request.remote_addr)
    if not ipR[0]:
        return ipR
    
    credR = _verify_username_password(request.headers.get('username'), request.headers.get('password'))
    if not credR[0]:
        return credR
    
    apiR = _verify_api_url(request.args.get('api_url'))
    if not apiR[0]:
        return apiR
    
    return True, None


def _verify_internal_authenticaton(token):
    try:
        jwt.decode(token, 'AXLL12UUT89557XNHYT', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return False, Response('Token Expired', status=401)
    except jwt.InvalidTokenError:
        return False, Response('Invalid Token', status=401)
    
    return True, None


def _verify_ip(ip):
    if not is_ip_allowed(ip):
        return False, Response('Unauthorized', status=401)
    return True, None


def _verify_username_password(username, password):
    if not (username and password):
        return False, Response('Username or Password Missing', status=400)
    if not is_user_valid(username, password):
        return False, Response('Incorrect Username or Password', status=403)
    return True, None
   
    
def _verify_api_url(api_url):
    if not api_url:
        return False, Response("Missing API URL", status=400)
    if not is_api_allowed(api_url):
        return False, Response("API not allowed", status=403)
    return True, None
    

    