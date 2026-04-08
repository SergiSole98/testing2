import urllib.request
import urllib.parse
import json
import os
import argparse

ASANA_TOKEN = os.environ["ASANA_TOKEN"]
PROJECT_GID = "1212356635225063"


def _post(url: str, payload: dict) -> dict:
    data = json.dumps({"data": payload}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {ASANA_TOKEN}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read())


def create_task(name: str, parent_id: str = None, notes: str = "") -> dict:
    payload = {
        "name": name,
        "notes": notes,
        "projects": [PROJECT_GID],
    }
    if parent_id:
        payload["parent"] = parent_id

    result = _post("https://app.asana.com/api/1.0/tasks", payload)["data"]

    return {
        "id": result["gid"],
        "title": result["name"],
        "completed": result.get("completed", False),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create an Asana task")
    parser.add_argument("--name", required=True, help="Task name")
    parser.add_argument("--parent_id", help="Parent task GID (to create as subtask)")
    parser.add_argument("--notes", default="", help="Task notes/description")
    args = parser.parse_args()

    result = create_task(args.name, args.parent_id, args.notes)
    print(json.dumps(result, indent=2, ensure_ascii=False))
