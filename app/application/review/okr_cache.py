"""
Temporary cache to store OKR objectives during a session.
Allows user to select an objective by number.
"""

_okr_cache = {"objectives": None}


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
        return objectives[index - 1]
    return None


def clear_cache() -> None:
    """Clear the cache."""
    _okr_cache["objectives"] = None
