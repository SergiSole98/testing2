# OKR Audit Framework

## Role
OKR Structure Auditor

## Task
Audit and validate OKR structure compliance against the defined framework to ensure proper hierarchy, timeline alignment, and completeness.

## Expected OKR Structure

### Level 1: Objective
**Purpose**: High-level goal for a quarter or year

**Required Fields**:
- `title`: Clear, inspiring objective statement
- `start_date`: Quarter/period start (YYYY-MM-DD)
- `end_date`: Quarter/period end (YYYY-MM-DD)
- `owner`: Person responsible
- `status`: active/completed/abandoned

**Timeline**: Usually 3-6 months

**Example**:
```
Objective: Scale product to 100k users
Start: 2026-04-01
End: 2026-06-30
Owner: Product Lead
```

---

### Level 2: Key Result (KR)
**Purpose**: Measurable outcome that indicates objective achievement

**Required Fields**:
- `title`: Specific, measurable result
- `metric`: Success measure (e.g., "users", "revenue", "completion rate")
- `current_value`: Starting point
- `target_value`: Goal value
- `start_date`: KR period start (YYYY-MM-DD)
- `end_date`: KR target date (YYYY-MM-DD)
- `owner`: Person responsible
- `progress`: % complete (0-100)

**Timeline**: Same as parent objective or shorter sub-milestones

**Example**:
```
KR: Acquire 5 paying customers
Metric: Customers
Current: 0
Target: 5
Start: 2026-04-01
End: 2026-06-30
Owner: Sales
Progress: 40%
```

---

### Level 3: Initiative
**Purpose**: Major work package that drives KR achievement

**Required Fields**:
- `title`: Initiative name/description
- `description`: What will be done
- `start_date`: Initiative start (YYYY-MM-DD)
- `end_date`: Initiative target date (YYYY-MM-DD)
- `owner`: Person responsible
- `status`: not_started/in_progress/completed/blocked
- `priority`: high/medium/low

**Timeline**: Typically 2-8 weeks, must fit within parent KR timeline

**Example**:
```
Initiative: Customer onboarding sprint
Description: Design and implement frictionless onboarding flow
Start: 2026-04-15
End: 2026-05-15
Owner: Product Manager
Status: in_progress
Priority: high
```

---

### Level 4: Sprint
**Purpose**: Time-boxed development cycle containing related tasks

**Required Fields**:
- `sprint_number`: Sprint identifier (e.g., "Sprint 4")
- `start_date`: Sprint start (YYYY-MM-DD)
- `end_date`: Sprint end (YYYY-MM-DD) - typically 1-2 weeks
- `goals`: Sprint objectives
- `owner`: Scrum master/lead
- `capacity`: Team capacity hours

**Timeline**: Fixed 1-2 week cycles

**Example**:
```
Sprint: Sprint 4
Start: 2026-04-22
End: 2026-05-05
Goals: Complete onboarding UI components
Capacity: 80 hours
Owner: Engineering Lead
```

---

### Level 5: Tasks
**Purpose**: Individual, actionable work items

**Required Fields**:
- `title`: Task description (action-oriented)
- `description`: Detailed requirements
- `start_date`: Task start (YYYY-MM-DD)
- `due_date`: Task deadline (YYYY-MM-DD)
- `assignee`: Person responsible
- `status`: backlog/in_progress/review/completed
- `effort`: Story points or hours (2-13)
- `dependencies`: Blocking tasks (if any)

**Timeline**: Usually 1-5 days per task

**Example**:
```
Task: Design login component
Description: Create Figma mockups for login/signup flow
Start: 2026-04-22
Due: 2026-04-26
Assignee: Designer
Status: in_progress
Effort: 5 points
Dependencies: None
```

---

## Timeline Validation Rules

### Rule 1: Hierarchical Date Alignment
```
Objective:    [start_date] ---- [end_date] (e.g., 3 months)
  └─ KR:      [start_date] -- [end_date]  (within objective dates)
      └─ Init: [start_date] - [end_date]  (within KR dates)
          └─ Sprint: [s] - [e]            (1-2 weeks)
              └─ Tasks: [s] - [e]         (1-5 days)
```

✅ **Valid**: All child dates fit within parent dates
❌ **Invalid**: Task due_date > Initiative end_date

### Rule 2: No Timeline Gaps
- Initiative must start before or on parent KR start
- Initiative must end on or before parent KR end
- Sprint must align with active initiatives
- Tasks must complete within sprint

### Rule 3: Overlapping Allowed
- Multiple KRs can overlap within an objective
- Multiple initiatives can overlap within a KR
- Multiple sprints can run in parallel for different initiatives

---

## Audit Checklist

### ✅ Completeness Check
- [ ] Objective has title, dates, owner
- [ ] All KRs have metrics and target values
- [ ] All initiatives have descriptions and owners
- [ ] All sprints have defined capacity
- [ ] All tasks are assigned with effort estimates

### ✅ Timeline Validation
- [ ] All dates are in YYYY-MM-DD format
- [ ] Child dates fit within parent dates
- [ ] No gaps or overlaps that violate hierarchy
- [ ] Milestones are realistic given effort/capacity

### ✅ Ownership Validation
- [ ] Every level has clear owner
- [ ] No orphaned items without owners
- [ ] Owner has sufficient capacity

### ✅ Progress Tracking
- [ ] KRs have current progress % or status
- [ ] Initiatives have status (not_started/in_progress/completed/blocked)
- [ ] Tasks have status
- [ ] Dates match actual progress

### ✅ Alignment Validation
- [ ] Tasks contribute to sprint goals
- [ ] Sprints contribute to initiative
- [ ] Initiatives contribute to KR
- [ ] KRs contribute to objective

---

## Audit Output Format

For each violation found:

**Level**: [Objective/KR/Initiative/Sprint/Task]
**Item**: [Name]
**Violation**: [Type of violation]
**Current State**: [What is missing/wrong]
**Expected State**: [What should be there]
**Severity**: 🔴 Critical / 🟡 Warning / 🟢 Info

---

## Example: Complete Valid Structure

```
🎯 OBJECTIVE: Scale to 100k users
├─ Start: 2026-04-01
├─ End: 2026-06-30
├─ Owner: Product Lead

  📊 KR 1: Reach 100k signups
  ├─ Target: 100,000 users
  ├─ Current: 35,000
  ├─ Progress: 35%
  ├─ Start: 2026-04-01
  ├─ End: 2026-06-30
  ├─ Owner: Growth Lead

    🚀 Initiative: User acquisition campaign
    ├─ Start: 2026-04-15
    ├─ End: 2026-06-15
    ├─ Owner: Marketing Manager
    ├─ Status: in_progress

      📋 Sprint 4: Paid ad campaign
      ├─ Start: 2026-04-22
      ├─ End: 2026-05-05
      ├─ Capacity: 100 hours
      
        ✓ Task: Launch Facebook ads
        ├─ Start: 2026-04-22
        ├─ Due: 2026-04-26
        ├─ Assignee: Ad Specialist
        ├─ Effort: 8 points
        ├─ Status: in_progress
```

---

## Integration Notes

This framework defines the **ideal structure**. The audit agent will:
1. Compare current OKR state against this framework
2. Identify missing dates, owners, or metrics
3. Flag timeline violations
4. Report completeness percentage
5. Suggest remediation steps
