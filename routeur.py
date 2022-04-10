import views


def routeur(path: str):
    if path in ["/tasks", "/tasks/"]:
        return views.tasks_list
    elif "/tasks/" in path:
        return views.task_detail
    elif path == "/":
        return views.hello_world
    else:
        return views.not_found
