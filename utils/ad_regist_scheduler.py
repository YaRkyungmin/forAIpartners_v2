from dto.ad_schedule_dto import AdScheduleInfo
from datetime import datetime, timedelta

def should_register_today(schedule: AdScheduleInfo) -> bool:
    today = datetime.today().date()
    last_date = datetime.strptime(schedule.last_update_date, "%Y-%m-%d").date()

    if schedule.automation_cycle == "always":
        return True

    elif schedule.automation_cycle == "every":
        return today != last_date

    elif schedule.automation_cycle == "two":
        return last_date not in [today, today - timedelta(days=1)]

    elif schedule.automation_cycle == "three":
        return (today - last_date).days >= 3