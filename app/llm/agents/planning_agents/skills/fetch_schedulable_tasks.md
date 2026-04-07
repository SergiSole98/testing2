# Fetch Schedulable Tasks

## Context
Apply when retrieving the tasks to plan for a given week from the OKR Asana project (GID `1212356635225063`).

## Goal
Return only the concrete, actionable Tasks with a due date in the target week that belong to the user-selected objective.

## Hierarchy
The OKR structure has exactly 4 levels:
1. **Objective (O)** — top-level goal
2. **Key Result (KR)** — measurable outcome under an objective
3. **Initiative (I)** — project or initiative under a KR
4. **Task** — concrete, actionable item under an initiative ← only this level is schedulable

## Steps
1. Fetch tasks from the **"Objetivos (O)"** section of the project. Display the list and wait for the user to select one.
2. Traverse the hierarchy from the selected objective down through KRs and Initiatives to reach level-4 Tasks.
3. Collect only level-4 Tasks whose due date falls within the target week and are not completed.

## Rules
1. Only level-4 Tasks are schedulable — never Objectives, KRs, or Initiatives.
2. If a task has no due date this week, exclude it from the result.
