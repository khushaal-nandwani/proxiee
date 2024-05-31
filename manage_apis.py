import configparser

config = configparser.ConfigParser()
config.read('myconfig.ini')

def is_api_key_valid(api_key):
    for key in config['api_keys']:
        if key == api_key:
            return True
    return False


def is_api_allowed(api_url):
    api_url = api_url.split('/')[2]

    for api in config['allowed_apis']:
        if api == api_url:
            return True
    return False