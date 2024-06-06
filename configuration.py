import configparser

config = configparser.ConfigParser()
config.read('myconfig.ini')

def is_api_allowed(api_url):
    api_url = api_url.split('/')[2]

    for api in config['allowed_apis']:
        if api == api_url:
            return True
    return False


def is_user_valid(username, password):
    for user in config['users']:
        if user == username and config['users'][user] == password:
            return True
    return False


def is_url_special(api_url) -> str:
    api_url = api_url.split('/')[2]

    for api in config['special_apis']:
        if api == api_url:
            return config['special_apis'][api]
    return ''

def get_config():
    return config

def is_ip_allowed(ip_given):
    for ip in config['allowed_ips']:
        if ip == ip_given:
            return True
    return False