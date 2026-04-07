from infrastructure.asana.get_tasks import get_tasks
from application.review.okr_cache import set_objectives, get_objective_by_index


def run_review_okr(selected_index: int = None) -> str:
    """
    Interactive OKR review.

    If selected_index is None: Show list of main objectives
    If selected_index is provided: Show KRs and initiatives for that objective

    Args:
        selected_index: 1-based index of the objective to review

    Returns:
        str: Formatted markdown response
    """
    if selected_index is None:
        return _list_objectives()
    else:
        return _show_objective_details(selected_index)


def _list_objectives() -> str:
    """Fetch and display main objectives."""
    objectives = get_tasks()

    # Filter only incomplete objectives
    pending_objectives = [obj for obj in objectives if not obj["completed"]]

    # Cache for next interaction
    set_objectives(pending_objectives)

    if not pending_objectives:
        return "✅ All objectives are completed!"

    output = "## OKR Review - Select an objective:\n\n"
    for i, obj in enumerate(pending_objectives, 1):
        output += f"{i}. {obj['title']}\n"

    output += "\n*Type the number to see details*"
    return output


def _show_objective_details(index: int) -> str:
    """Show KRs and initiatives for a selected objective."""
    objective = get_objective_by_index(index)

    if not objective:
        return "❌ Invalid selection. Please try again."

    output = f"## {objective['title']}\n\n"

    # Filter incomplete KRs
    pending_krs = [
        kr for kr in objective["key_results"] if not kr["completed"]
    ]

    if not pending_krs:
        output += "✅ All key results completed!\n"
        return output

    for kr in pending_krs:
        output += f"### • {kr['title']}\n"

        # Filter incomplete initiatives
        pending_initiatives = [
            i for i in kr["initiatives"] if not i["completed"]
        ]

        if pending_initiatives:
            for initiative in pending_initiatives:
                output += f"  - [ ] {initiative['title']}\n"
        else:
            output += "  ✅ All initiatives completed\n"

        output += "\n"

    return output
