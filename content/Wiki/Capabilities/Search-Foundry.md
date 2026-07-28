---
id: Search-Foundry
name: Search-Foundry
type: wiki-reference
description: Foundry Suite capability for Search-Foundry.
version: 0.1.0
last_synced: 2026-07-28 15:28:53 UTC
last_synced_date: '2026-07-28'
source_commit_sha: 5cb4225c
status: active
tags:
- foundry/capability
- type/reference
---

# Search-Foundry

> **Description**: Foundry Suite capability for Search-Foundry.
> **Version**: `0.1.0` | **Last Synced**: `2026-07-28 15:28:53 UTC` | **Git Commit**: `5cb4225c`

## Overview & Purpose

---

## Key Codebase Modules

- `__init__.py`
- `crawler.py`
- `repo_registry.py`
- `ui.py`
- `vector_engine.py`

## Architecture & Ecosystem Connections

```mermaid
flowchart LR
    Founder[Founder / Workstation]
    Target["Search-Foundry Capability"]
    Vault[("~/Sync_NAS Vault")]
    Founder -->|Interacts via MCP / CLI| Target
    Target -->|Governed Intake| Vault
```

### Related Capabilities

- [[Regenerative-Foundry]]
- [[Obsidian-Foundry]]
- [[Comms-Foundry]]
- [[Share]]

## Revision History

- **2026-07-28** (`5cb4225c`): Synchronized via Librarian Observer. *feat(ui): add context-sensitive help for semantic search limitations*

## Founder Notes & Manual Annotations

> *Add custom founder notes, architectural thoughts, or manual annotations here. This section is automatically preserved during periodic wiki delta syncs.*
