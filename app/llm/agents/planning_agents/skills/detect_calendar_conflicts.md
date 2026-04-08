# Detect Calendar Conflicts

## Context
Apply after fetching calendar events, before scheduling. Identifies disordered calendar states that must be resolved before planning proceeds.

## Rules
1. A calendar is disordered if any of the following are true:
   - **Duplicate events**: two or more events with the same title and the same start time.
   - **Overlapping events**: two or more events whose time slots intersect (start of one is before the end of another).
2. If the calendar is disordered, report each conflict clearly: type (duplicate or overlap), event names, and time slots involved.
3. For each conflict, propose one concrete action:
   - Duplicate → delete one of the copies.
   - Overlap → delete one event, shorten one, or move one to a free slot.
4. Do not proceed with scheduling until the user confirms how to resolve each conflict.
5. If no conflicts are found, state it explicitly and continue.
