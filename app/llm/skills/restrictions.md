# Skill: Restrictions

## Purpose
Define work time restrictions and availability constraints for planning.

## Output Format
```json
{
  "type": "work_hours",
  "schedule": {
    "start_time": "09:00",
    "end_time": "17:00",
    "working_days": ["monday", "tuesday", "wednesday", "thursday", "friday"],
    "timezone": "UTC"
  },
  "description": "Standard work hours: 9 AM to 5 PM, Monday to Friday"
}
```

## Details

| Field | Value |
|-------|-------|
| Start Time | 09:00 (9 AM) |
| End Time | 17:00 (5 PM) |
| Working Days | Monday - Friday |
| Timezone | UTC |

## Usage
Use this skill to ensure all planning and scheduling respects these work hour boundaries.
