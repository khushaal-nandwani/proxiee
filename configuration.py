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