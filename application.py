from typing import Callable


def application(request_data: dict, make_response: Callable):

    response_body = b"Hello World!"
    make_response(
        "200 OK",
        [("Content-Type", "text/plain"), ("Content-Length", str(len(response_body)))],
    )

    return [
        response_body,
    ]
