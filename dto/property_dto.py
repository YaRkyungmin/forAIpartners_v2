from dataclasses import dataclass
from typing import List


@dataclass
class PropertyInfo:
    building_type: str
    city_name: str
    district_name: str
    dong_name: str
    address: str
    dong_number: str
    floor_number: str
    room_number: str
    deal_type: str
    sell_price: str
    lease_price: str
    deposit_price: str
    monthly_price: str
    room_type: str

    @classmethod
    def map_from_values(cls, values: List[str]) -> "PropertyInfo":
        return cls(building_type=values[0],
                   city_name=values[1],
                   district_name=values[2],
                   dong_name=values[3],
                   address=values[4],
                   dong_number=values[5],
                   floor_number=values[6],
                   room_number=values[7],
                   deal_type=values[8],
                   sell_price=values[9],
                   lease_price=values[10],
                   deposit_price=values[11],
                   monthly_price=values[12],
                   room_type=values[13])