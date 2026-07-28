---
id: Map-Foundry
name: Map-Foundry
type: wiki-reference
description: Foundry Suite capability for Map-Foundry.
version: 0.1.0
last_synced: 2026-07-28 15:28:52 UTC
last_synced_date: '2026-07-28'
source_commit_sha: 3c0f9017
status: active
tags:
- foundry/capability
- type/reference
---

# Map-Foundry

> **Description**: Foundry Suite capability for Map-Foundry.
> **Version**: `0.1.0` | **Last Synced**: `2026-07-28 15:28:52 UTC` | **Git Commit**: `3c0f9017`

## Overview & Purpose

---

## Key Codebase Modules

- `ui/app.py`

## Architecture & Ecosystem Connections

```mermaid
flowchart LR
    Founder[Founder / Workstation]
    Target["Map-Foundry Capability"]
    Vault[("~/Sync_NAS Vault")]
    Founder -->|Interacts via MCP / CLI| Target
    Target -->|Governed Intake| Vault
```

### Related Capabilities

- [[Search-Foundry]]
- [[Regenerative-Foundry]]
- [[Obsidian-Foundry]]
- [[Comms-Foundry]]
- [[Share]]

## Revision History

- **2026-07-28** (`3c0f9017`): Synchronized via Librarian Observer. *feat: stand up streamlit UI hub, implement quad-view weather radar, and correct WMS layer names*

## Founder Notes & Manual Annotations

> *Add custom founder notes, architectural thoughts, or manual annotations here. This section is automatically preserved during periodic wiki delta syncs.*
