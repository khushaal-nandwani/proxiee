from openai import OpenAI
import pytest
from unittest.mock import patch
import requests

# URL for the local proxy
localProxyApi = "http://localhost:5001/proxy"

# Data to send to OpenAI via the proxy
data = {
    'model': "gpt-3.5-turbo",
    'messages': [
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
}

def test_openai_via_proxy():
    response = requests.post(localProxyApi,
                             params={'api_url': 'https://api.openai.com/v1/chat/completions'},
                             headers={'Proxy-Api-Key': 'khushaal', 'Content-Type': 'application/json', 'Authorization': 'Bearer api-key'},
                             json=data)
    
    print(response.content)

    # Assertions to verify the status code and response content
    assert response.status_code == 200
    response_json = response.json()
    assert 'choices' in response_json  # Check if 'choices' key is in the response
    assert isinstance(response_json['choices'], list)  # Check if 'choices' is a list
