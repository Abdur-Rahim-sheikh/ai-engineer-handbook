import pytest
import requests


@pytest.mark.api
def test_jsonplaceholder_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    # params = {"q": "Python programming language", "format": "json"}
    # response = requests.get(url, params=params)
    response = requests.get(url)
    assert response.status_code == 200, "API did not return a successful response"
    data = response.json()
    assert len(data) > 20, "API did not return expected format"
