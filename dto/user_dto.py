from dataclasses import dataclass
from typing import List

@dataclass
class UserInfo:
    id: str
    password: str

    @classmethod
    def map_from_values(cls, values: List[str]) -> "UserInfo":
        return cls(id=values[0],
                   password=values[1])