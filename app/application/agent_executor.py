from llm.router import route_use_case
from application.weekly.run import run_weekly_planning
from application.daily.run import run_daily_planning
from application.tasks.run import fetch_tasks
from application.calendar.run import fetch_calendar_events
from application.logging.run import log_execution
from application.review.run import run_review_okr
from application.review.audit import run_okr_audit


USE_CASE_MAP = {
    "run_weekly_planning": run_weekly_planning,
    "run_daily_planning": run_daily_planning,
    "fetch_tasks": fetch_tasks,
    "fetch_calendar_events": fetch_calendar_events,
    "log_execution": log_execution,
    "run_review_okr": run_review_okr,
    "run_okr_audit": run_okr_audit,
}


def agent_executor(user_input: str):
    try:
        decision = route_use_case(user_input)
    except Exception:
        return "Error: could not parse routing decision."

    action = decision.get("action")

    if action == "run_use_case":
        use_case = decision.get("use_case")
        fn = USE_CASE_MAP.get(use_case)
        if fn is None:
            return f"Error: unknown use case '{use_case}'."
        return fn()

    if action == "ask_user":
        return decision.get("question", "Could you clarify?")

    return "Error: invalid routing response."
