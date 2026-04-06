from infrastructure.asana.get_tasks import get_tasks
from llm.okr_auditor import audit_kr


def run_okr_audit() -> dict:
    objectives = get_tasks()

    results = []
    for obj in objectives:
        if obj["completed"]:
            continue

        for kr in obj["key_results"]:
            if kr["completed"]:
                continue

            pending_initiatives = [
                i["title"] for i in kr["initiatives"] if not i["completed"]
            ]

            audit = audit_kr(
                objective=obj["title"],
                key_result=kr["title"],
                initiatives=pending_initiatives,
            )
            results.append(audit)

    return {"okr_audit": results}
