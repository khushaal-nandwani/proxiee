import json 


class SpecialUrlHandler():
    def get_special_key(self, config) -> str:
        return ''

    def add_headers(self, headers, load) -> dict:
        return headers
    
    def modify_data(self, data):
        return data


class OpenAISpecialHandler(SpecialUrlHandler):
    def get_special_key(self, config) -> str:
        """Retrieves the API key for OpenAI API from the config file"""
        return config['special_apis']['api.openai.com']
    
    def add_headers(self, headers, load) -> dict:
        ''' Requires load to be API key'''
        headers['Authorization'] = f'Bearer {load}'
        return headers
    
    def modify_data(self, data):
        data = json.loads(data)
        data['model'] = "gpt-3.5-turbo"
        for message in data['messages']:
	    if message["role"] == "assistant":
		continue
            message['role'] = "user"
        return json.dumps(data)

        


class CoreGSTSpecialHandler(SpecialUrlHandler):
    def get_special_key(self, config) -> str:
        return super().get_special_key(config)

    def add_headers(self, headers, load) -> dict:
        headers['XYZ'] = 'XYZ2'


def url_handler_factory(api_url) -> SpecialUrlHandler:
    api_domain = api_url.split('/')[2]
    if api_domain == 'api.openai.com':
        return OpenAISpecialHandler()
    else:
        return SpecialUrlHandler()