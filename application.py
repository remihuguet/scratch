from typing import Callable


def application(request_data: dict, make_response: Callable):

    response_body = b"<h1>Hello World!</h1>"
    make_response(
        "200 OK",
        [("Content-Type", "text/html"), ("Content-Length", str(len(response_body)))],
    )

    return [
        response_body,
    ]
