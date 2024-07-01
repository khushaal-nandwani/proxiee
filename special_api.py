import json 
from configuration import get_headers_for 


def update_headers(request_headers, api_url):
    """Updates the existing headers as per the ones given the myconfig.ini. If the header is already present, it is overwritten."""
    headers = get_headers_for(api_url)
    for header in headers:
        request_headers[header] = headers[header]
    
def update_json_data(json_data, api_url):
    url = api_url.split('/')[2]
    if not url == "api.openai.com":
        return json_data
    else:
        data = json.loads(json_data)    
        data['model'] = "gpt-3.5-turbo"
        for message in data['messages']:
            if message['role'] == "assistant":
                continue
            message['role'] = "user"

    return json.dumps(data)


