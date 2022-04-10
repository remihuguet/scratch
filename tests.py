import requests


def test_hello_world():
    response = requests.get("http://127.0.0.1:8001/")
    assert 200 == response.status_code
    assert "Hello, world!" == response.text


def test_tasks_list():
    response = requests.get("http://127.0.0.1:8001/tasks")
    assert 200 == response.status_code
    assert "tasks" in response.json()
    assert 2 == len(response.json()["tasks"])
    assert "Une tache" == response.json()["tasks"][0]["title"]


def test_tasks_detail():
    response = requests.get("http://127.0.0.1:8001/tasks/134")
    assert 200 == response.status_code
    assert 134 == response.json()["id"]
    assert "Une tache" == response.json()["title"]


def test_404():
    response = requests.get("http://127.0.0.1:8001/flkldkl")
    assert 404 == response.status_code
    response = requests.get("http://127.0.0.1:8001/tasks/28888")
    assert 404 == response.status_code
