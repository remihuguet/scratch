import dataclasses
import json
from datetime import datetime
from typing import Callable

from tasks import Task


def application(request_data: dict, make_response: Callable):

    path = request_data["PATH_INFO"]
    headers = []

    if path == "/tasks":
        tasks = [
            Task(
                title="Une tache",
                rank=0,
                created=datetime.now(),
                updated=datetime.now(),
            ),
            Task(
                title="Une tache 2",
                rank=1,
                created=datetime.now(),
                updated=datetime.now(),
            ),
        ]
        headers.append(("Content-Type", "application/json"))
        response_body = bytes(
            json.dumps({"tasks": [dataclasses.asdict(t) for t in tasks]}, default=str),
            "utf8",
        )
    else:
        headers.append(("Content-Type", "text/plain"))
        response_body = b"Hello World!"

    headers.append(("Content-Length", str(len(response_body))))
    make_response("200 OK", headers)

    return [
        response_body,
    ]
