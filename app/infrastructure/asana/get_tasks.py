import urllib.request
import json
import os
import argparse

ASANA_TOKEN = os.environ["ASANA_TOKEN"]
OBJECTIVES_SECTION_ID = "1212356635225064"


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {ASANA_TOKEN}"})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read())


def _fetch_initiatives(kr_id: str) -> list:
    url = (
        f"https://app.asana.com/api/1.0/tasks/{kr_id}/subtasks"
        f"?opt_fields=name,completed"
    )
    data = _get(url)["data"]
    return [
        {"id": t["gid"], "title": t["name"], "completed": t["completed"]}
        for t in data
    ]


def _fetch_key_results(objective_id: str) -> list:
    url = (
        f"https://app.asana.com/api/1.0/tasks/{objective_id}/subtasks"
        f"?opt_fields=name,completed"
    )
    data = _get(url)["data"]
    key_results = []
    for kr in data:
        initiatives = _fetch_initiatives(kr["gid"])
        key_results.append({
            "id": kr["gid"],
            "title": kr["name"],
            "completed": kr["completed"],
            "initiatives": initiatives,
        })
    return key_results


def get_tasks() -> list:
    url = (
        f"https://app.asana.com/api/1.0/sections/{OBJECTIVES_SECTION_ID}/tasks"
        f"?opt_fields=name,completed"
    )
    data = _get(url)["data"]

    objectives = []
    for obj in data:
        key_results = _fetch_key_results(obj["gid"])
        objectives.append({
            "id": obj["gid"],
            "title": obj["name"],
            "completed": obj["completed"],
            "key_results": key_results,
        })

    return objectives


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Fetch Asana OKRs")
    parser.add_argument("--completed", type=lambda x: x.lower() == "true", default=None, help="Filter by completed status (true/false)")
    parser.add_argument("--objective_id", help="Fetch a single objective by GID")
    args = parser.parse_args()

    if args.objective_id:
        from get_tasks import _fetch_key_results
        obj_url = f"https://app.asana.com/api/1.0/tasks/{args.objective_id}?opt_fields=name,completed"
        obj_data = _get(obj_url)["data"]
        result = [{
            "id": obj_data["gid"],
            "title": obj_data["name"],
            "completed": obj_data["completed"],
            "key_results": _fetch_key_results(args.objective_id),
        }]
    else:
        result = get_tasks()

    if args.completed is not None:
        result = [o for o in result if o["completed"] == args.completed]

    print(json.dumps(result, indent=2, ensure_ascii=False))
