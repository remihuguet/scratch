import dataclasses
import json
from datetime import datetime

from response import Response
import tasks


def not_found(request_data: dict):
    return Response(status_code=404, data="Not found")


def hello_world(request_data: dict):
    return Response(data="Hello, world!")


def tasks_list(request_data: dict):
    return Response(
        content_type="application/json",
        data=json.dumps(
            {"tasks": [dataclasses.asdict(t) for t in tasks.tasks]}, default=str
        ),
    )


def task_detail(request_data: dict):
    task_id = int(request_data["PATH_INFO"].split("/")[-1])
    try:
        task = next(filter(lambda t: t.id == task_id, tasks.tasks))
        return Response(
            content_type="application/json",
            data=json.dumps(dataclasses.asdict(task), default=str),
        )
    except StopIteration as e:
        return Response(
            status_code=404,
            content_type="application/json",
            data=json.dumps({"error": f"Task with id {task_id} not found"}),
        )
