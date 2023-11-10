from typing import List
from dataclasses import dataclass


@dataclass
class Email:
    to: List[str]
    author: str
    date: str
    subject: str
    body: str
