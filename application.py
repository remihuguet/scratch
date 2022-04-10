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
    status_code = "200 OK"
    headers = []

    if path in ["/tasks", "/tasks/"]:
        headers.append(("Content-Type", "application/json"))
        response_body = bytes(
            json.dumps({"tasks": [dataclasses.asdict(t) for t in tasks]}, default=str),
            "utf8",
        )
    elif "/tasks/" in path:
        headers.append(("Content-Type", "application/json"))
        task_id = int(path.split("/")[-1])
        try:
            task = next(filter(lambda t: t.id == task_id, tasks))
            response_body = bytes(
                json.dumps(dataclasses.asdict(task), default=str),
                "utf8",
            )
        except StopIteration as e:
            status_code = "404 Not found"
            response_body = bytes(
                json.dumps({"error": f"Task with id {task_id} not found"}), "utf8"
            )
    elif path == "/":
        headers.append(("Content-Type", "text/plain"))
        response_body = b"Hello World!"
    else:
        status_code = "404 Not found"
        headers.append(("Content-Type", "text/plain"))
        response_body = b"Not found"

    headers.append(("Content-Length", str(len(response_body))))
    make_response(status_code, headers)

    return [
        response_body,
    ]
