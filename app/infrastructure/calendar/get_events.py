import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), "../../../credentials.json")
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
CALENDAR_ID = "soleserrallachsergi@gmail.com"


def get_events(start: str, end: str) -> list:
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH, scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=credentials)

    result = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=start + "Z",
        timeMax=end + "Z",
        singleEvents=True,
        orderBy="startTime",
    ).execute()

    events = []
    for item in result.get("items", []):
        events.append({
            "id": item["id"],
            "title": item.get("summary", ""),
            "start": item["start"].get("dateTime", item["start"].get("date")),
            "end": item["end"].get("dateTime", item["end"].get("date")),
        })

    return events
