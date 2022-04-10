import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Task:
    title: str
    rank: int
    created: datetime
    updated: datetime
    description: str | None = None
    completed: bool = False
