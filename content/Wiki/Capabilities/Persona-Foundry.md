---
id: Persona-Foundry
name: Persona-Foundry
type: wiki-reference
description: Foundry Suite capability for Persona-Foundry.
version: 0.1.0
last_synced: 2026-07-28 15:28:53 UTC
last_synced_date: '2026-07-28'
source_commit_sha: 3c7dace2
status: active
tags:
- foundry/capability
- type/reference
---

# Persona-Foundry

> **Description**: Foundry Suite capability for Persona-Foundry.
> **Version**: `0.1.0` | **Last Synced**: `2026-07-28 15:28:53 UTC` | **Git Commit**: `3c7dace2`

## Overview & Purpose

---

## Architecture & Ecosystem Connections

```mermaid
flowchart LR
    Founder[Founder / Workstation]
    Target["Persona-Foundry Capability"]
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

- **2026-07-28** (`3c7dace2`): Synchronized via Librarian Observer. *docs: update metadata front matter in README.md*

## Founder Notes & Manual Annotations

> *Add custom founder notes, architectural thoughts, or manual annotations here. This section is automatically preserved during periodic wiki delta syncs.*
