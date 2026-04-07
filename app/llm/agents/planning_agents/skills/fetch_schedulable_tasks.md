# Fetch Schedulable Tasks

## Context
Apply when retrieving the tasks to plan for a given week from the OKR Asana project (GID `1212356635225063`).

## Goal
Return only the concrete, actionable Tasks with a due date in the target week that belong to the user-selected objective.

## Steps
1. Fetch tasks from the **"Objetivos (O)"** section of the project. Display the list and wait for the user to select one.
2. Traverse the full hierarchy from the selected objective: Objective → KRs → Initiatives → Tasks.
3. Collect only leaf-node Tasks (items with no children) whose due date falls within the target week and are not completed.

## Rules
1. Only Tasks are schedulable — never Objectives, KRs, or Initiatives.
2. A schedulable Task is a concrete, actionable item (e.g. a Sprint or a specific action). Items that describe a weekly goal or group sub-work (e.g. "Conseguir X esta semana") are Initiatives — do not schedule them.
3. If a task has no due date this week, exclude it from the result.
