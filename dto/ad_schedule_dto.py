from dataclasses import dataclass
from typing import List


@dataclass
class AdScheduleInfo:
    automation_cycle: str
    last_update_date: str
    num_of_ads: str

    @classmethod
    def map_from_values(cls, values: List[str]) -> "AdScheduleInfo":
        return cls(automation_cycle=values[0],
                   last_update_date=values[1],
                   num_of_ads=values[2])