class SpecialUrlHandler():
    def get_special_key(self, config) -> str:
        return ''

    def add_headers(self, headers, load) -> dict:
        return headers


class OpenAISpecialHandler(SpecialUrlHandler):
    def get_special_key(self, config) -> str:
        return config['special_apis']['api.openai.com']
    
    def add_headers(self, headers, load) -> dict:
        ''' Requires load to be API key'''
        headers['Authorization'] = f'Bearer {load}'
        return headers


class CoreGSTSpecialHandler(SpecialUrlHandler):
    def get_special_key(self, config) -> str:
        return super().get_special_key(config)

    def add_headers(self, headers, load) -> dict:
        headers['XYZ'] = 'XYZ2'


def get_special_url_handler(api_url) -> SpecialUrlHandler:
    api_domain = api_url.split('/')[2]
    if api_domain == 'api.openai.com':
        return OpenAISpecialHandler()
    else:
        return SpecialUrlHandler()