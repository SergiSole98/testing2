# Audit Gate Skill

## Context

When an agent produces a draft spec (agent, skill, etc.) that must pass compliance before delivery, use this gate pattern to ensure quality and standards adherence.

## Rules

1. Draft the full spec according to the relevant standard (writing_agent_skill.md, writing_skill_skills.md, etc.).
2. Submit the draft to the designated auditor agent (e.g., Axel for agents; use auditor specified in task).
3. If auditor flags violations, apply all corrections immediately; do not deliver incomplete corrections.
4. If auditor confirms compliance, deliver the Output format as-is.
5. If original intent is ambiguous during rewrite, ask for clarification before proceeding.

## Reference

**Auditor Agents:**
- `Agents/agente_axel_auditor.md` — Audits agents against writing_agent_skill.md standards.
- (Sofia or other auditors follow same pattern: read → check → report violations → rewrite or confirm)

**Standards to reference during draft:**
- `Skills/writing_agent_skill.md` — Agent structure.
- `Skills/writing_skill_skills.md` — Skill structure.
- `Skills/prompt_syntax.md` — Text formatting.
