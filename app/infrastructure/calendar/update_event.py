import os
import json
import argparse
from google.oauth2 import service_account
from googleapiclient.discovery import build

CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), "../../../credentials.json")
SCOPES = ["https://www.googleapis.com/auth/calendar"]
CALENDAR_ID = "soleserrallachsergi@gmail.com"


def update_event(event_id: str, title: str = None, start: str = None, end: str = None, description: str = None) -> dict:
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH, scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=credentials)

    event = service.events().get(calendarId=CALENDAR_ID, eventId=event_id).execute()

    if title is not None:
        event["summary"] = title
    if description is not None:
        event["description"] = description
    if start is not None:
        event["start"] = {"dateTime": start + "Z", "timeZone": "UTC"}
    if end is not None:
        event["end"] = {"dateTime": end + "Z", "timeZone": "UTC"}

    updated = service.events().update(calendarId=CALENDAR_ID, eventId=event_id, body=event).execute()

    return {
        "id": updated["id"],
        "title": updated.get("summary", ""),
        "start": updated["start"].get("dateTime"),
        "end": updated["end"].get("dateTime"),
        "link": updated.get("htmlLink", ""),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update a Google Calendar event")
    parser.add_argument("--event_id", required=True, help="Event ID to update")
    parser.add_argument("--title", help="New event title")
    parser.add_argument("--start", help="New start datetime (ISO 8601, e.g. 2026-04-08T10:00:00)")
    parser.add_argument("--end", help="New end datetime (ISO 8601, e.g. 2026-04-08T11:00:00)")
    parser.add_argument("--description", help="New event description")
    args = parser.parse_args()

    result = update_event(args.event_id, args.title, args.start, args.end, args.description)
    print(json.dumps(result, indent=2, ensure_ascii=False))
