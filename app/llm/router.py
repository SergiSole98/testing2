import json
import os


def call_llm(prompt: str) -> str:
    # Mock LLM — replace with real API call later
    p = prompt.lower()
    if any(k in p for k in ["calendar", "evento", "eventos", "agenda"]):
        return '{"action": "run_use_case", "use_case": "fetch_calendar_events"}'
    if any(k in p for k in ["task", "tarea", "tareas"]):
        return '{"action": "run_use_case", "use_case": "fetch_tasks"}'
    if any(k in p for k in ["log", "registro", "registrar"]):
        return '{"action": "run_use_case", "use_case": "log_execution"}'
    if any(k in p for k in ["weekly", "semanal", "semana"]):
        return '{"action": "run_use_case", "use_case": "run_weekly_planning"}'
    if any(k in p for k in ["daily", "diario", "día", "dia"]):
        return '{"action": "run_use_case", "use_case": "run_daily_planning"}'
    if any(k in p for k in ["okr", "review", "revisión", "revision", "feedback", "análisis", "analisis"]):
        return '{"action": "run_use_case", "use_case": "run_review_okr"}'
    return '{"action": "ask_user", "question": "Can you clarify what you want to do?"}'


def route_use_case(user_input: str) -> dict:
    prompt_path = os.path.join(os.path.dirname(__file__), "router_prompt.md")
    with open(prompt_path) as f:
        system_prompt = f.read()

    prompt = f"{system_prompt}\n\nUser input: {user_input}"
    response = call_llm(user_input)

    return json.loads(response)
