---
id: RFP-Foundry
name: RFP-Foundry
type: wiki-reference
description: Foundry Suite capability for RFP-Foundry.
version: 0.1.0
last_synced: 2026-07-28 15:28:53 UTC
last_synced_date: '2026-07-28'
source_commit_sha: b866d59f
status: active
tags:
- foundry/capability
- type/reference
---

# RFP-Foundry

> **Description**: Foundry Suite capability for RFP-Foundry.
> **Version**: `0.1.0` | **Last Synced**: `2026-07-28 15:28:53 UTC` | **Git Commit**: `b866d59f`

## Overview & Purpose

---

## Architecture & Ecosystem Connections

```mermaid
flowchart LR
    Founder[Founder / Workstation]
    Target["RFP-Foundry Capability"]
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

- **2026-07-28** (`b866d59f`): Synchronized via Librarian Observer. *feat(spawn): auto-register spawned instances in ~/.foundry-suite/local_repos.jsonl*

## Founder Notes & Manual Annotations

> *Add custom founder notes, architectural thoughts, or manual annotations here. This section is automatically preserved during periodic wiki delta syncs.*
