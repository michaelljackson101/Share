---
id: Radio-Foundry
name: Radio-Foundry
type: wiki-reference
description: Foundry Suite capability for Radio-Foundry.
version: 0.1.0
last_synced: 2026-07-28 15:28:53 UTC
last_synced_date: '2026-07-28'
source_commit_sha: ae015ded
status: active
tags:
- foundry/capability
- type/reference
---

# Radio-Foundry

> **Description**: Foundry Suite capability for Radio-Foundry.
> **Version**: `0.1.0` | **Last Synced**: `2026-07-28 15:28:53 UTC` | **Git Commit**: `ae015ded`

## Overview & Purpose

---

## Architecture & Ecosystem Connections

```mermaid
flowchart LR
    Founder[Founder / Workstation]
    Target["Radio-Foundry Capability"]
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

- **2026-07-28** (`ae015ded`): Synchronized via Librarian Observer. *feat: implement experimental runs, update intent and README for HP mini monitoring topology*

## Founder Notes & Manual Annotations

> *Add custom founder notes, architectural thoughts, or manual annotations here. This section is automatically preserved during periodic wiki delta syncs.*
