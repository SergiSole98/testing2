"""
Temporary cache to store OKR objectives during a session.
Allows user to select an objective by number and track context for evaluations.
"""

_okr_cache = {
    "objectives": None,
    "selected_objective": None,
    "selected_kr": None,
}


def set_objectives(objectives: list) -> None:
    """Store objectives in cache."""
    _okr_cache["objectives"] = objectives


def get_objectives() -> list:
    """Retrieve cached objectives."""
    return _okr_cache.get("objectives") or []


def get_objective_by_index(index: int):
    """Get a specific objective by its index (1-based)."""
    objectives = get_objectives()
    if 0 < index <= len(objectives):
        obj = objectives[index - 1]
        # Store as selected for evaluation context
        set_selected_objective(obj)
        return obj
    return None


def set_selected_objective(objective: dict) -> None:
    """Store the currently selected objective."""
    _okr_cache["selected_objective"] = objective


def get_selected_objective() -> dict:
    """Get the currently selected objective."""
    return _okr_cache.get("selected_objective")


def set_selected_kr(kr: dict) -> None:
    """Store the currently selected Key Result."""
    _okr_cache["selected_kr"] = kr


def get_selected_kr() -> dict:
    """Get the currently selected Key Result."""
    return _okr_cache.get("selected_kr")


def clear_cache() -> None:
    """Clear the cache."""
    _okr_cache["objectives"] = None
    _okr_cache["selected_objective"] = None
    _okr_cache["selected_kr"] = None
