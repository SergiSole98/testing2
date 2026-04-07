from infrastructure.asana.get_tasks import get_tasks


def run_review_okr() -> str:
    """
    Review OKRs from Asana project.

    Returns main objectives with their key results and pending initiatives.
    """
    objectives = get_tasks()

    output = "## OKR Review\n\n"

    for obj in objectives:
        if obj["completed"]:
            continue

        output += f"### 🎯 {obj['title']}\n"

        pending_krs = []
        for kr in obj["key_results"]:
            if kr["completed"]:
                continue

            pending_initiatives = [
                i for i in kr["initiatives"] if not i["completed"]
            ]

            if pending_initiatives:
                pending_krs.append({
                    "title": kr["title"],
                    "initiatives": [i["title"] for i in pending_initiatives],
                })

        if not pending_krs:
            output += "- ✅ All key results completed\n\n"
            continue

        for kr in pending_krs:
            output += f"\n#### • {kr['title']}\n"
            for initiative in kr["initiatives"]:
                output += f"  - [ ] {initiative}\n"

        output += "\n"

    return output
