import urllib.request
import json
import os
import argparse

ASANA_TOKEN = os.environ["ASANA_TOKEN"]


def _put(url: str, payload: dict) -> dict:
    data = json.dumps({"data": payload}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {ASANA_TOKEN}",
            "Content-Type": "application/json",
        },
        method="PUT",
    )
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read())


def update_task(task_id: str, name: str = None, completed: bool = None, notes: str = None) -> dict:
    payload = {}
    if name is not None:
        payload["name"] = name
    if completed is not None:
        payload["completed"] = completed
    if notes is not None:
        payload["notes"] = notes

    result = _put(f"https://app.asana.com/api/1.0/tasks/{task_id}", payload)["data"]

    return {
        "id": result["gid"],
        "title": result["name"],
        "completed": result.get("completed", False),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update an Asana task")
    parser.add_argument("--task_id", required=True, help="Task GID to update")
    parser.add_argument("--name", help="New task name")
    parser.add_argument("--completed", type=lambda x: x.lower() == "true", help="Mark as completed (true/false)")
    parser.add_argument("--notes", help="New task notes/description")
    args = parser.parse_args()

    result = update_task(args.task_id, args.name, args.completed, args.notes)
    print(json.dumps(result, indent=2, ensure_ascii=False))
