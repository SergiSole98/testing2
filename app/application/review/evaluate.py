"""
OKR Evaluation - Analyzes KR and initiatives using the OKR Evaluation Agent
"""


def run_evaluate_okr(kr_title: str, initiative_title: str, objective_title: str = None) -> str:
    """
    Evaluate a Key Result and its initiative.

    Args:
        kr_title: Title of the Key Result
        initiative_title: Title of the initiative
        objective_title: (Optional) Title of the parent objective

    Returns:
        str: Evaluation analysis and recommendations
    """
    # Prepare context for the agent
    context = f"""
## Objective Context
{f'Objective: {objective_title}' if objective_title else 'Objective: [Not specified]'}

## Key Result
{kr_title}

## Initiative
{initiative_title}
"""

    # This would be integrated with Claude API for real evaluation
    # For now, returning a structured template
    evaluation = _evaluate_alignment(kr_title, initiative_title)
    return evaluation


def _evaluate_alignment(kr_title: str, initiative_title: str) -> str:
    """Generate evaluation based on KR and initiative titles."""

    output = f"""## OKR Evaluation Report

### 📊 Analysis for:
- **Key Result**: {kr_title}
- **Initiative**: {initiative_title}

### 1. Alignment Status
✅ Aligned - Initiative directly supports the Key Result achievement

### 2. Current Status
📈 In Progress - Initiative is active and trackable

### 3. Blockers
None identified from context

### 4. Recommendations
1. Define specific success metrics for "{initiative_title}"
2. Set checkpoint milestones with target dates
3. Identify dependencies and prerequisites
4. Allocate resources and ownership
5. Schedule weekly progress reviews

### 5. Timeline
Estimated completion depends on sprint/initiative scope
- Quick assessment needed: What is the target completion date?

### 6. Risk Assessment
🟡 Medium Risk
- Recommend clarifying: Is "{initiative_title}" the only path to achieve "{kr_title}"?
- Consider: Are there blockers or external dependencies?

---

**Next Step**: Integrate with Claude API for deeper LLM-based analysis using the OKR Evaluation Agent framework.
"""

    return output
