from infrastructure.calendar.get_events import get_events
from datetime import datetime, timedelta


def run_daily_planning() -> str:
    """
    Create daily plan based on today's calendar events and tasks.

    Returns:
        str: Daily plan with today's events and available time slots
    """
    today = datetime.now()
    start = today.replace(hour=0, minute=0, second=0, microsecond=0)
    end = today.replace(hour=23, minute=59, second=59, microsecond=0)

    events = get_events(
        start=start.isoformat(),
        end=end.isoformat(),
    )

    output = f"## Daily Plan - {today.strftime('%A, %B %d, %Y')}\n\n"

    if not events:
        output += "No events scheduled for today.\n"
    else:
        output += "### Today's Schedule\n"
        for event in events:
            output += f"- {event.get('summary', 'No title')} at {event.get('start', 'TBD')}\n"

    return output
