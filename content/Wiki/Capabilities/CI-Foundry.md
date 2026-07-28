---
id: CI-Foundry
name: CI-Foundry
type: wiki-reference
description: Competitive Intelligence (CI) Foundry
version: 0.4.0
last_synced: 2026-07-28 15:28:51 UTC
last_synced_date: '2026-07-28'
source_commit_sha: 733b518f
status: active
tags:
- foundry/capability
- type/reference
---

# CI-Foundry

> **Description**: Competitive Intelligence (CI) Foundry
> **Version**: `0.4.0` | **Last Synced**: `2026-07-28 15:28:51 UTC` | **Git Commit**: `733b518f`

## Overview & Purpose

---

## CLI Entrypoints

- `obsidian-foundry run`
- `obsidian-foundry bootstrap`

## Key Codebase Modules

- `ci_foundry/__init__.py`
- `ci_foundry/adapters.py`
- `ci_foundry/cli.py`
- `ci_foundry/llm.py`
- `ci_foundry/normalizers.py`
- `ci_foundry/run_naming.py`
- `ci_foundry/settings.py`
- `ci_foundry/storage.py`
- `ci_foundry/workflow.py`

## Architecture & Ecosystem Connections

```mermaid
flowchart LR
    Founder[Founder / Workstation]
    Target["CI-Foundry Capability"]
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

- **2026-07-28** (`733b518f`): Synchronized via Librarian Observer. *feat(llm-registry): implement federated autonomous LangChain facade and compliance nudges*

## Founder Notes & Manual Annotations

> *Add custom founder notes, architectural thoughts, or manual annotations here. This section is automatically preserved during periodic wiki delta syncs.*
