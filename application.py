import dataclasses
import json
from datetime import datetime
from typing import Callable
from urllib import response

from tasks import Task

tasks = [
    Task(
        id=134,
        title="Une tache",
        rank=0,
        created=datetime.now(),
        updated=datetime.now(),
    ),
    Task(
        id=43,
        title="Une tache 2",
        rank=1,
        created=datetime.now(),
        updated=datetime.now(),
    ),
]


def application(request_data: dict, make_response: Callable):

    path = request_data["PATH_INFO"]

    if path in ["/tasks", "/tasks/"]:
        return response(
            200,
            "application/json",
            json.dumps({"tasks": [dataclasses.asdict(t) for t in tasks]}, default=str),
            make_response,
        )
    elif "/tasks/" in path:
        task_id = int(path.split("/")[-1])
        try:
            task = next(filter(lambda t: t.id == task_id, tasks))
            return response(
                200,
                "application/json",
                json.dumps(dataclasses.asdict(task), default=str),
                make_response,
            )
        except StopIteration as e:
            return response(
                404,
                "application/json",
                json.dumps({"error": f"Task with id {task_id} not found"}),
                make_response,
            )
    elif path == "/":
        return response(200, "text/plain", "Hello, world!", make_response)
    else:
        return response(404, "text/plain", "Not found", make_response)


def response(
    status_code: int, content_type: str, response: str, make_response: Callable
):
    STATUS = {
        200: "200 OK",
        404: "404 Not found",
    }
    resp = bytes(response, "utf8")
    headers = [("Content-Type", content_type), ("Content-Length", str(len(resp)))]
    make_response(STATUS[status_code], headers)
    return [resp]
