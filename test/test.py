import requests
import pytest

localProxyApi = "http://localhost:5001"

def test_get():
    response = requests.get(localProxyApi + "/proxy",
                            params={'api_url': 'https://api.postalpincode.in/pincode/395007'},
                            headers={'username': 'khushaal', 'password': 'khushaal'}
                            )
    print(response.content)
    assert response.status_code == 200

def test_get_content():
    response = requests.get(localProxyApi + "/proxy",
                            params={'api_url': 'https://jsonplaceholder.typicode.com/todos/1'},
                            headers={'username': 'khushaal', 'password': 'khushaal'}
                            )

    assert response.status_code == 200
    assert response.json() == {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}


def test_post():
    response = requests.post(localProxyApi + "/proxy",
                            params={'api_url': 'https://jsonplaceholder.typicode.com/posts'},
                            headers={'username': 'khushaal', 'password': 'khushaal'},
                            json={'title': 'foo', 'body': 'bar', 'userId': 1}
                            )
    
    print(response.content)
    assert response.status_code == 201
    assert response.json() == {'id': 101, 'title': 'foo', 'body': 'bar', 'userId': 1}
    

def test_put():
    response = requests.put(localProxyApi + "/proxy",
                            params={'api_url': 'https://jsonplaceholder.typicode.com/posts/1'},
                            headers={'username': 'khushaal', 'password': 'khushaal'},
                            json={'id': 1, 'title': 'foo', 'body': 'bar', 'userId': 1}
                            )
    assert response.status_code == 200
    assert response.json() == {'id': 1, 'title': 'foo', 'body': 'bar', 'userId': 1}