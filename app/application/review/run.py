from infrastructure.asana.get_tasks import get_tasks


def run_review_okr() -> dict:
    objectives = get_tasks()

    result = []
    for obj in objectives:
        if obj["completed"]:
            continue

        pending_krs = []
        for kr in obj["key_results"]:
            if kr["completed"]:
                continue

            pending_initiatives = [
                i for i in kr["initiatives"] if not i["completed"]
            ]

            pending_krs.append({
                "title": kr["title"],
                "initiatives": [i["title"] for i in pending_initiatives],
            })

        result.append({
            "objective": obj["title"],
            "key_results": pending_krs,
        })

    return {"okr_review": result}
