from datetime import datetime
from typing import Callable

from routeur import routeur


def application(request_data: dict, make_response: Callable):
    path = request_data["PATH_INFO"]
    view_function = routeur(path=path)

    response = view_function(request_data)

    return response(make_response)
