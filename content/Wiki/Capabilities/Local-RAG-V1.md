---
id: Local-RAG-V1
name: Local-RAG-V1
type: wiki-reference
description: Local RAG service (FAISS + FastAPI) with Streamlit UI
version: 0.1.0
last_synced: 2026-07-28 15:28:52 UTC
last_synced_date: '2026-07-28'
source_commit_sha: 6b64937d
status: active
tags:
- foundry/capability
- type/reference
---

# Local-RAG-V1

> **Description**: Local RAG service (FAISS + FastAPI) with Streamlit UI
> **Version**: `0.1.0` | **Last Synced**: `2026-07-28 15:28:52 UTC` | **Git Commit**: `6b64937d`

## Overview & Purpose

---

## Key Codebase Modules

- `localrag/__init__.py`
- `localrag/chat/__init__.py`
- `localrag/chat/provider.py`
- `localrag/config.py`
- `localrag/embeddings/__init__.py`
- `localrag/embeddings/provider.py`
- `localrag/ingestion/__init__.py`
- `localrag/ingestion/chunking.py`
- `localrag/ingestion/loaders.py`
- `localrag/kb/__init__.py`

## Architecture & Ecosystem Connections

```mermaid
flowchart LR
    Founder[Founder / Workstation]
    Target["Local-RAG-V1 Capability"]
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

- **2026-07-28** (`6b64937d`): Synchronized via Librarian Observer. *feat(llm-registry): implement federated autonomous LangChain facade and compliance nudges*

## Founder Notes & Manual Annotations

> *Add custom founder notes, architectural thoughts, or manual annotations here. This section is automatically preserved during periodic wiki delta syncs.*
