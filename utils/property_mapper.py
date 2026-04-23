from typing import List

from dto.ad_schedule_dto import AdScheduleInfo
from dto.owner_dto import OwnerInfo
from dto.property_dto import PropertyInfo


def map_ad_schedule_from_google_sheet(values: List[str]):
    return AdScheduleInfo.map_from_values(values[22:25])

def map_property_info_from_google_sheet(values: List[str]):
    return PropertyInfo.map_from_values(values[1:15])

def map_owner_info_from_google_sheet(values: List[str]):
    return OwnerInfo.map_from_values(values[15:22])