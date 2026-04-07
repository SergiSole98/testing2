import json
import os


def call_llm(prompt: str) -> str:
    # Mock LLM — replace with real API call later
    p = prompt.lower().strip()

    # Check for evaluation request (interactive OKR eval)
    if any(k in p for k in ["eval", "evaluar", "evaluate", "evaluation"]):
        return json.dumps({
            "action": "run_use_case",
            "use_case": "run_review_okr",
            "params": {"action": "eval"}
        })

    # Check for simple number input (for OKR selection)
    if p.isdigit():
        return json.dumps({
            "action": "run_use_case",
            "use_case": "run_review_okr",
            "params": {"selected_index": int(p)}
        })

    if any(k in p for k in ["weekly", "semanal", "semana"]):
        return '{"action": "run_use_case", "use_case": "run_weekly_planning"}'
    if any(k in p for k in ["daily", "diario", "día", "dia"]):
        return '{"action": "run_use_case", "use_case": "run_daily_planning"}'
    if any(k in p for k in ["auditar", "audit", "auditoría"]):
        return '{"action": "run_use_case", "use_case": "run_okr_audit"}'
    if any(k in p for k in ["okr", "review", "revisión", "revision", "feedback", "análisis", "analisis"]):
        # Check if user specified audit or review mode
        if any(k in p for k in ["audit", "auditar", "auditoría"]):
            return json.dumps({
                "action": "run_use_case",
                "use_case": "run_review_okr",
                "params": {"mode": "audit"}
            })
        elif any(k in p for k in ["review", "revisar"]):
            return json.dumps({
                "action": "run_use_case",
                "use_case": "run_review_okr",
                "params": {"mode": "review"}
            })
        else:
            return '{"action": "run_use_case", "use_case": "run_review_okr"}'
    return '{"action": "ask_user", "question": "Can you clarify what you want to do?"}'


def route_use_case(user_input: str) -> dict:
    prompt_path = os.path.join(os.path.dirname(__file__), "router_prompt.md")
    with open(prompt_path) as f:
        system_prompt = f.read()

    prompt = f"{system_prompt}\n\nUser input: {user_input}"
    response = call_llm(user_input)

    return json.loads(response)
