import os
import json
import argparse
from google.oauth2 import service_account
from googleapiclient.discovery import build

CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), "../../../credentials.json")
SCOPES = ["https://www.googleapis.com/auth/calendar"]
CALENDAR_ID = "soleserrallachsergi@gmail.com"


def create_event(title: str, start: str, end: str, description: str = "") -> dict:
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH, scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=credentials)

    body = {
        "summary": title,
        "description": description,
        "start": {"dateTime": start + "Z", "timeZone": "UTC"},
        "end": {"dateTime": end + "Z", "timeZone": "UTC"},
    }

    event = service.events().insert(calendarId=CALENDAR_ID, body=body).execute()

    return {
        "id": event["id"],
        "title": event.get("summary", ""),
        "start": event["start"].get("dateTime"),
        "end": event["end"].get("dateTime"),
        "link": event.get("htmlLink", ""),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a Google Calendar event")
    parser.add_argument("--title", required=True, help="Event title")
    parser.add_argument("--start", required=True, help="Start datetime (ISO 8601, e.g. 2026-04-08T10:00:00)")
    parser.add_argument("--end", required=True, help="End datetime (ISO 8601, e.g. 2026-04-08T11:00:00)")
    parser.add_argument("--description", default="", help="Event description")
    args = parser.parse_args()

    result = create_event(args.title, args.start, args.end, args.description)
    print(json.dumps(result, indent=2, ensure_ascii=False))
