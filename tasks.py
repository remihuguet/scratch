import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Task:
    id: int
    title: str
    rank: int
    created: datetime
    updated: datetime
    description: str | None = None
    completed: bool = False


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
