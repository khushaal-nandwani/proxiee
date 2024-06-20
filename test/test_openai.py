from openai import OpenAI
import pytest
from unittest.mock import patch
import requests

# URL for the local proxy
localProxyApi = "http://localhost:5000/proxy"

# Data to send to OpenAI via the proxy
data = {
    'model': "gpt-3.5-turbo",
    'messages': [
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
}

def test_openai_via_proxy():
    '''Test POST request to the proxy API using OpenAI API as an example'''
    response = requests.post(localProxyApi,
                             params={'api_url': 'https://api.openai.com/v1/chat/completions'},
                             headers={'username': 'khushaal', 'password': 'khushaal', 'Content-Type': 'application/json', 'Authorization': 'Bearer api-key'},
                             json=data)
    
    print(response.content)
    
    # Assertions to verify the status code and response content
    assert response.status_code == 200
    response_json = response.json()
    assert 'choices' in response_json  # Check if 'choices' key is in the response
    assert isinstance(response_json['choices'], list)  # Check if 'choices' is a list


def test_openai_model():
    """Tests if changing or sending different models works"""
    response = requests.post(localProxyApi,
                             params={'api_url': 'https://api.openai.com/v1/chat/completions'},
                             headers={'username': 'khushaal', 'password': 'khushaal', 'Content-Type': 'application/json'},
                                json={'model': "gpt-4-turbo", 'messages': [{"role": "user", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."}, {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}]})
    # print(response.content)
    assert response.status_code == 200
    response_json = response.json()
    # print(response_json)


def test_openai_role():
    """Tests if changing or sending different roles works"""
    response = requests.post(localProxyApi,
                             params={'api_url': 'https://api.openai.com/v1/chat/completions'},
                             headers={'username': 'khushaal', 'password': 'khushaal', 'Content-Type': 'application/json'},
                                json={'model': "gpt-3.5-turbo", 'messages': [{"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."}, {"role": "system", "content": "Compose a poem that explains the concept of recursion in programming."}]})
    print(response.content)
    assert response.status_code == 200
    response_json = response.json()
    print(response_json)
    
                                      