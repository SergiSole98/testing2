def analyze_review(context: dict) -> dict:
    # Mock LLM — replace with real API call later
    return {
        "progress": "medium",
        "issues": [
            "Too many tasks in progress",
            "Lack of prioritization",
        ],
        "recommendations": [
            "Focus on top 3 tasks",
            "Reduce active work",
        ],
    }
