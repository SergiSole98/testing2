# Skill Planner

## Context
Apply when scheduling OKR tasks in Google Calendar. Maps tasks to available time slots respecting work constraints.

## Rules
1. Schedule on any day of the week (Monday–Sunday).
2. Schedule only within 08:30–23:30.
3. Check calendar availability before scheduling — never propose a slot that is already occupied by an existing calendar event.
4. Assign each task to its due date; if the slot is full, schedule the day before.
5. One event per task; one task per time slot. If two tasks would be assigned to the same slot, suggest merging them into a single task instead of overlapping.
6. If no free slot exists for a task, flag it and ask the user to decide: delete an existing event, allow overlap, or skip the task.
7. Go **day by day**: propose slots for all tasks of the current day, wait for the user to confirm or adjust, then move to the next day. Do not show the full week at once.
