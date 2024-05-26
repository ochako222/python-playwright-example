from typing import TypedDict
from enum import Enum

class User(TypedDict):
    user_name: str
    password: str


# Enum example
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3



