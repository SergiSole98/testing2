import os
import json


def audit_kr(objective: str, key_result: str, initiatives: list) -> dict:
    # Mock LLM — replace with real API call later
    prompt_path = os.path.join(os.path.dirname(__file__), "agents", "agent_okr_auditor.md")
    with open(prompt_path) as f:
        _system_prompt = f.read()

    payload = {
        "objective": objective,
        "key_result": key_result,
        "initiatives": initiatives,
    }

    # TODO: replace with real LLM call using _system_prompt and json.dumps(payload)
    aligned = len(initiatives) > 0
    return {
        "kr": key_result,
        "aligned": aligned,
        "assessment": "Initiatives exist but real evaluation requires LLM integration.",
        "gaps": [] if aligned else ["No initiatives defined for this KR"],
        "risks": [] if aligned else ["KR has no execution plan"],
        "actions": ["Connect real LLM to enable full audit"],
    }
