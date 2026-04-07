# Skill Planner

## Context
Apply when scheduling OKR tasks in Google Calendar. Maps tasks to available time slots respecting work constraints.

## Rules
1. Schedule on any day of the week (Monday–Sunday).
2. Schedule only within 08:30–23:30.
3. Check calendar availability before scheduling — do not overlap existing events.
4. Assign each task to its due date; if the slot is full, schedule the day before.
5. One task per time slot.
6. If no free slot exists for a task, flag it and ask the user to decide: delete an existing event, allow overlap, or skip the task.
7. Go **day by day**: propose slots for all tasks of the current day, wait for the user to confirm or adjust, then move to the next day. Do not show the full week at once.
