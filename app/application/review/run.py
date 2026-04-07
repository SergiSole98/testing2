from infrastructure.asana.get_tasks import get_tasks
from application.review.okr_cache import set_objectives, get_objective_by_index, set_selected_kr, get_selected_objective, get_selected_kr
from application.review.evaluate import run_evaluate_okr


def run_review_okr(selected_index: int = None, action: str = None, mode: str = None) -> str:
    """
    Interactive OKR review and audit system.

    Modes:
    - None (first call): Ask user if they want to audit or review
    - 'review': Show KRs and initiatives (evaluation mode)
    - 'audit': Conversational audit with probing questions

    Args:
        selected_index: 1-based index of the objective
        action: Optional action ('eval' for evaluation)
        mode: Optional mode ('audit' or 'review')

    Returns:
        str: Formatted markdown response
    """
    if mode == "audit":
        return _start_audit(selected_index)
    elif action == "eval":
        return _evaluate_selected_kr()
    elif selected_index is None:
        if mode is None:
            return _ask_mode()
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
        # Store the first KR for evaluation context
        if pending_krs:
            set_selected_kr(pending_krs[0])

    output += "\n---\n**Want a detailed evaluation?** Type: `eval`"
    return output


def _ask_mode() -> str:
    """Ask user if they want to audit or review OKRs."""
    return """## OKR Options

Choose your mode:

**1. Audit** 🔍
- Deep analysis of your OKRs
- Probing questions about alignment and feasibility
- Strategic recommendations
- Best for: Understanding if your OKRs are on track

**2. Review** 📊
- Quick overview of progress
- Evaluation of current initiatives
- Status check
- Best for: Daily/weekly progress tracking

Type: `audit` or `review`"""


def _start_audit(selected_index: int) -> str:
    """Start the audit process for a selected objective."""
    objective = get_objective_by_index(selected_index)

    if not objective:
        return "❌ Invalid selection. Please try again."

    # This would invoke the OKR Audit Agent
    # For now, return the beginning of the audit
    audit_start = f"""
## 🔍 OKR Audit - Deep Dive

🎯 **OBJECTIVE**: {objective['title']}
- Start Date: [from Asana]
- Due Date: [from Asana]

Now let's audit this objective thoroughly.

**Phase 1: Understanding the Context**

1. What is the business/personal reason for this objective?
2. What problem are you solving?
3. What does success look like in concrete terms?

*Reply to continue with the audit...*

---

**Note**: Full audit with conversational AI coming soon. This requires Claude API integration for interactive questioning.
"""

    return audit_start


def _evaluate_selected_kr() -> str:
    """Evaluate the currently selected KR."""
    objective = get_selected_objective()
    kr = get_selected_kr()

    if not objective or not kr:
        return "❌ No KR selected. Please select an objective first by typing a number."

    kr_title = kr["title"]
    initiative_titles = [i["title"] for i in kr["initiatives"] if not i["completed"]]

    if not initiative_titles:
        return f"ℹ️ All initiatives for '{kr_title}' are completed. No evaluation needed."

    # Evaluate the first pending initiative
    initiative_title = initiative_titles[0]
    objective_title = objective["title"]

    evaluation = run_evaluate_okr(
        kr_title=kr_title,
        initiative_title=initiative_title,
        objective_title=objective_title
    )

    return evaluation
