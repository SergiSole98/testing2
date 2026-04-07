from infrastructure.asana.get_tasks import get_tasks
from application.review.okr_cache import set_objectives, get_objective_by_index


def run_review_okr(selected_index: int = None) -> str:
    """
    Interactive OKR audit system.

    Args:
        selected_index: 1-based index of the objective

    Returns:
        str: Formatted markdown response
    """
    if selected_index is None:
        return _list_objectives()
    return _start_audit(selected_index)


def _list_objectives() -> str:
    """Fetch and display main objectives."""
    objectives = get_tasks()

    pending_objectives = [obj for obj in objectives if not obj["completed"]]
    set_objectives(pending_objectives)

    if not pending_objectives:
        return "✅ All objectives are completed!"

    output = "## OKR Audit - Select an objective:\n\n"
    for i, obj in enumerate(pending_objectives, 1):
        output += f"{i}. {obj['title']}\n"

    output += "\n*Type the number to start the audit*"
    return output


def _start_audit(selected_index: int) -> str:
    """Start the audit process for a selected objective."""
    objective = get_objective_by_index(selected_index)

    if not objective:
        return "❌ Invalid selection. Please try again."

    return objective["title"]
