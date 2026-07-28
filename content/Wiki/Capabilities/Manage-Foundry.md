---
id: Manage-Foundry
name: Manage-Foundry
type: wiki-reference
description: Daily cockpit for visibility and prioritization across a local Foundry
  Suite
version: 0.1.0
last_synced: 2026-07-28 15:28:52 UTC
last_synced_date: '2026-07-28'
source_commit_sha: 2c631b58
status: active
tags:
- foundry/capability
- type/reference
---

# Manage-Foundry

> **Description**: Daily cockpit for visibility and prioritization across a local Foundry Suite
> **Version**: `0.1.0` | **Last Synced**: `2026-07-28 15:28:52 UTC` | **Git Commit**: `2c631b58`

## Overview & Purpose

---

## Architecture & Ecosystem Connections

```mermaid
flowchart LR
    Founder[Founder / Workstation]
    Target["Manage-Foundry Capability"]
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

- **2026-07-28** (`2c631b58`): Synchronized via Librarian Observer. *docs: add root-level ARCHITECTURE_DIAGRAMS.md in compliance with Rule 9*

## Founder Notes & Manual Annotations

> *Add custom founder notes, architectural thoughts, or manual annotations here. This section is automatically preserved during periodic wiki delta syncs.*
