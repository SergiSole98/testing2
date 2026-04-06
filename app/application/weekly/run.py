from datetime import datetime, timedelta
from infrastructure.calendar.get_events import get_events


def run_weekly_planning() -> dict:
    today = datetime.now()
    days_until_monday = (7 - today.weekday()) % 7 or 7
    next_monday = today + timedelta(days=days_until_monday)

    start = next_monday.replace(hour=0, minute=0, second=0, microsecond=0)
    end = start + timedelta(days=6, hours=23, minutes=59)

    events = get_events(
        start=start.isoformat(),
        end=end.isoformat(),
    )

    return {"events": events}
