---
id: RFP-2026-DEMO
name: RFP-2026-DEMO
type: wiki-reference
description: Foundry Suite capability for RFP-2026-DEMO.
version: 0.1.0
last_synced: 2026-07-28 15:28:53 UTC
last_synced_date: '2026-07-28'
source_commit_sha: 51a5225a
status: active
tags:
- foundry/capability
- type/reference
---

# RFP-2026-DEMO

> **Description**: Foundry Suite capability for RFP-2026-DEMO.
> **Version**: `0.1.0` | **Last Synced**: `2026-07-28 15:28:53 UTC` | **Git Commit**: `51a5225a`

## Overview & Purpose

---

## Architecture & Ecosystem Connections

```mermaid
flowchart LR
    Founder[Founder / Workstation]
    Target["RFP-2026-DEMO Capability"]
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

- **2026-07-28** (`51a5225a`): Synchronized via Librarian Observer. *feat: Add Linux shell scripts and Foundry Suite shared env support*

## Founder Notes & Manual Annotations

> *Add custom founder notes, architectural thoughts, or manual annotations here. This section is automatically preserved during periodic wiki delta syncs.*
