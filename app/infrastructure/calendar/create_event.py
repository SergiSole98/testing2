import uuid


def create_event(start: str, end: str, title: str) -> dict:
    return {
        "id": f"evt_{uuid.uuid4().hex[:8]}",
        "start": start,
        "end": end,
        "title": title,
    }
