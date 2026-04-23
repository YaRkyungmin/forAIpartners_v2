from dataclasses import dataclass
from typing import List


@dataclass
class OwnerInfo:
    verify_type: str
    owner_type: str
    owner_name: str
    client_name: str
    telecom_name: str
    phone_number: str
    gender: str

    @classmethod
    def map_from_values(cls, values: List[str]) -> "OwnerInfo":
        return cls(verify_type=values[0],
                   owner_type=values[1],
                   owner_name=values[2],
                   client_name=values[3],
                   telecom_name=values[4],
                   phone_number=values[5],
                   gender=values[6])