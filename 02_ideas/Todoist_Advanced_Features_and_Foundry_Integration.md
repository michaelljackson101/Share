---
tags:
  - foundry
  - tasks
  - todoist
  - architecture
date: 2026-06-30
---

# Todoist Advanced Features & Foundry Integration

With the authoritative task orchestration engine now running on Todoist Pro, we can leverage native features to enhance the Foundry Suite architecture. 

## 1. Kanban Boards (Board View)
Instead of a flat vertical list, projects can be toggled into a **Board View** to organize tasks into visual columns (Sections).

*   **For "Core Projects" (Foundry Development):** Create columns for `Backlog`, `In Progress`, `Waiting/Blocked`, and `To Deploy`. When dictating code ideas to the Voice CLI (Google Tasks), they can land in the Inbox, be sorted to the `Backlog`, and physically dragged across the board.
*   **For "Kentucky Farm":** Group tasks by physical location (e.g., `The Barn`, `The House`, `Equipment Maintenance`) to create a visual map of what needs to be done.

## 2. Custom Filters
Filters allow the use of query language to create custom dashboards spanning multiple projects.

*   **The Deep Work Dashboard:** `(today | overdue) & p1`
    Shows only tasks due today (or overdue) that are Priority 1.
*   **The Weekend Errands View:** `@errand & (today | +7 days)`
    Consolidates tasks from `Admin` and `Carlisle Home` tagged with `@errand` into one list when driving into town.
*   **The Handoff / Waiting List:** `@waiting | @delegated`
    Tracks tasks dispatched to others (e.g., via Liaison-Foundry) so they remain visible while awaiting a reply.

## 3. Reports, Karma, & The Historical Ledger
Todoist features a built-in gamification system called **Karma** to track daily/weekly goals and visualize productivity. 

**The Synergistic Architecture:**
While Todoist's native charts provide a 30-day view of productivity, the self-hosted **Tasks-Foundry Streamlit Dashboard** acts as the permanent ledger. Every task completed on the Todoist Kanban board is quietly logged into the immutable PostgreSQL database by the background daemon, enabling year-over-year historical reporting.
