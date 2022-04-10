import dataclasses
from typing import Callable


@dataclasses.dataclass
class Response:
    data: str
    status_code: int = 200
    content_type: str = "text/plain"

    def __call__(self, make_response: Callable):
        STATUS = {
            200: "200 OK",
            404: "404 Not found",
        }
        resp = bytes(self.data, "utf8")
        headers = [
            ("Content-Type", self.content_type),
            ("Content-Length", str(len(resp))),
        ]
        make_response(STATUS[self.status_code], headers)
        return [resp]
