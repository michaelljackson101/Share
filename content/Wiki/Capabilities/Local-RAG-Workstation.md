---
id: Local-RAG-Workstation
name: Local-RAG-Workstation
type: wiki-reference
description: Workstation UI and API for Local RAG
version: 0.1.0
last_synced: 2026-07-28 15:28:52 UTC
last_synced_date: '2026-07-28'
source_commit_sha: 849377d8
status: active
tags:
- foundry/capability
- type/reference
---

# Local-RAG-Workstation

> **Description**: Workstation UI and API for Local RAG
> **Version**: `0.1.0` | **Last Synced**: `2026-07-28 15:28:52 UTC` | **Git Commit**: `849377d8`

## Overview & Purpose

---

## Architecture & Ecosystem Connections

```mermaid
flowchart LR
    Founder[Founder / Workstation]
    Target["Local-RAG-Workstation Capability"]
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

- **2026-07-28** (`849377d8`): Synchronized via Librarian Observer. *feat(llm-registry): implement federated autonomous LangChain facade and compliance nudges*

## Founder Notes & Manual Annotations

> *Add custom founder notes, architectural thoughts, or manual annotations here. This section is automatically preserved during periodic wiki delta syncs.*
