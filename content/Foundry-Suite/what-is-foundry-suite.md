---
title: What is Foundry-Suite
draft: false
tags:
  - foundry_suite
  - governance
  - ecosystem
summary: A local-first, artifact-driven ecosystem of specialized repos where AI collaborates beside the human at the workbench.
audience: mixed
source_repo: michaelljackson101/Foundry-Suite
review: brand-reviewed
---

Foundry-Suite is a local-first system of small, specialized repositories that turn messy inputs into traceable artifacts and publishable outputs.

It is designed to increase creative bandwidth while preserving trust via human-in-the-loop workflows and provenance-first operations.

# What is Foundry-Suite

Status: Active / Evolving

Version: 0.3.2

Last updated: 2026-02-18

Change log:

- 0.3.2: Added Imagination-Foundry narrative integration and clarified its role as upstream intake and routing.
- 0.3.1: Consolidated visual overview into a single canonical map under canon/architecture.
- 0.3.0: Added visual overview diagrams and a lessons learned section.
- 0.2.0: Added suite-owned capabilities (LLM Registry MCP, Foundry Monitor) and introduced document versioning.
- 0.1.0: Initial canon publication.

## Executive overview

Foundry-Suite is a federated, local-first ecosystem of small, specialized repositories that help a human founder collaborate with AI in an artifact-driven way.

It is designed around a simple goal:

- reduce cognitive load for planning, communication, curation, and execution
- increase creative bandwidth for exploration and “what could be” thinking
- preserve trust through human-in-the-loop operation and provenance-first workflows

The core design choice is that AI is treated as a **co-collaborator beside you at the workbench**, not merely a tool on the workbench.

## Visual overview

These diagrams are intentionally lightweight and should stay stable even as the ecosystem evolves.

Canonical map:

- https://github.com/michaelljackson101/Foundry-Suite/blob/main/canon/architecture/foundry_suite_map.md

### Architecture cartography

The suite also maintains a versioned, auto-generated architecture package under `canon/architecture/` in the Foundry-Suite repo.

### Knowledge worker lifecycle and Foundry alignment

```mermaid
flowchart LR
  IDE([Idea]) --> INT([Intent]) --> RES([Research TRACE]) --> DES([Design]) --> BLD([Build]) --> EXP([Explain]) --> PUB([Publish]) --> GOV([Govern]) --> LRN([Learn])
  LRN --> IDE

  IF[Idea-Foundry] --> IDE
  IMF[Imagination-Foundry] --> IDE
  INF[Intent-Foundry] --> INT
  TF[TRACE-Loop-Lite] --> RES

  PF[Prompt-Foundry] --> BLD

  CF[Comms-Foundry] --> PUB
  CV[CV-Foundry] --> PUB
  BF[Brand-Foundry] --> PUB

  FS[[Foundry-Suite]] --> GOV
  HM[[Hints-MCP]] --> GOV
  LF[Learning-Foundry] --> LRN

  classDef concept fill:#F4F4F4,stroke:#666666,color:#111111;
  classDef foundry fill:#E8F5E9,stroke:#2E7D32,color:#111111;
  classDef support fill:#E3F2FD,stroke:#1565C0,color:#111111;

  class IDE,INT,RES,DES,BLD,EXP,PUB,GOV,LRN concept;
  class IF,IMF,INF,TF,PF,CF,CV,BF,LF foundry;
  class FS,HM support;
```

## What we built in the last two weeks

Over roughly two weeks of rapid iteration, the suite matured from a set of experiments into a coherent framework:

- a shared governance anchor (this repository)
- a consistent lifecycle spine (Learning → Idea → Intent → Build → Publish)
- a federated model of cooperating repos (Foundries) and temporary experiments (Labs)
- a practical “contracts over assumptions” approach using MCP tools and structured artifacts
- operational support for discovery, launching, and monitoring of local services
- a suite-owned LLM Registry (MCP) to support cost-effective, task-appropriate model selection
- a suite-owned Foundry Monitor workbench for compliance visibility and operational awareness

The result is not one product or one app.

It is a **methodology and working system** for building and operating an AI-augmented knowledge-work practice.

## The key idea: a craft workshop for knowledge work

Think of each Foundry as a workshop that:

- accepts inputs in a predictable form
- produces outputs as named, reviewable artifacts
- can be invoked via explicit tools or repeatable commands
- remains understandable to humans without requiring hidden context

The suite is intentionally modular and loosely coupled.

- each repo owns its own internal implementation
- cross-repo interactions happen through artifacts and MCP contracts
- everything is meant to be inspectable and explainable

## What “governance” means here

Foundry-Suite is the governance and canonical anchor. It hosts:

- constitution-level principles and shared mental models
- charters that define expectations for suite citizenship
- templates/prompts that help new repos become suite-aware quickly
- registries that support ecosystem discovery

Detailed implementation patterns (the “how”) live in the centralized Hints-MCP catalog.

## The operating philosophy

### 1) Artifact-first over chat-first

Chat is valuable for exploration, but durable work requires durable artifacts.

The suite pushes work into traceable outputs:

- submissions
- specs
- logs
- reports
- published deliverables

This makes the work:

- reviewable
- auditable
- repeatable
- easy to hand off between repos and agents

### 2) Human-in-the-loop by default

The suite treats autonomy as a spectrum.

A typical pattern is:

- AI proposes
- human approves
- AI executes within clear boundaries
- artifacts are produced with provenance

This reduces anxiety and distrust by making the system legible.

### 3) Provenance and transparency are non-negotiable

The suite prefers:

- explicit inputs and outputs
- named artifacts
- run logs and summaries
- clear records of what changed and why

When something is uncertain, the system should say so.

### 4) Federation over centralization

The suite is deliberately not a monolith.

Federation enables:

- local autonomy
- parallel evolution of components
- resilience when one component is offline
- safe experimentation without destabilizing the whole

### 5) “AI beside you” as a design target

The suite is built to support the lived experience of collaboration:

- you can ask for help drafting, planning, structuring, reviewing, and executing
- the AI can look at the same artifacts you see
- the AI can operate within repeatable pipelines rather than ad-hoc magic

This is a practical path toward a knowledge-worker setting where human and AI operate side-by-side.

## The lifecycle spine

The suite uses a consistent maturity model to orient work:

- Learning: acquire capability and context
- Idea: frame opportunities and proposals
- Intent: commit scope and produce execution-ready specifications
- Build: construct assets and systems
- Publish: package outputs for reuse, portfolio, or distribution

Not all work is linear, but all work fits somewhere on this spine.

## Component map: current state and aspirational direction

This section is intentionally written to be maintainable. It should be updated as capabilities mature.

### Governance anchor

#### Foundry-Suite

Current:

- defines shared principles and expectations
- provides templates/prompts for suite awareness
- hosts canonical registries for repo and service discovery

Aspirational:

- clearer cross-repo contracts under `contracts/`
- an ecosystem registry MCP server to make discovery/querying a first-class operation

### Suite-owned capabilities

These capabilities live under the Foundry-Suite root for practical reasons, but they are positioned as first-class suite infrastructure.

#### LLM Registry

Current:

- provides a single place to encode which model is most cost-effective and capable for a given task
- enables consistent model selection across Foundries even when a workflow requires multiple LLM calls in a chain
- supports a “non-blocking registry” posture where routing guidance is advisory and workflows can fall back safely

Aspirational:

- richer routing policies that account for task difficulty, token budget, context length, and risk
- better observability: usage summaries, cost signals, and model performance feedback loops
- a shared contract so Foundries can request “best model for task” without coupling to any provider

#### Foundry Monitor

Current:

- operational workbench for monitoring, compliance visibility, and suite-level awareness
- acts as a cockpit for identifying drift, gaps, and “what changed” across the ecosystem

Aspirational:

- deeper automated compliance checks and health indicators across repos
- integration with registries (repo + services) and netops for a consolidated operational picture

### Core pipeline Foundries

#### Learning-Foundry

Current:

- structured learning backlog and artifact-driven learning runs
- produces notes and capability artifacts that feed downstream work

Aspirational:

- richer run packaging and publish-ready learning outputs
- tighter integration with downstream Foundries via named artifact contracts

#### Imagination-Foundry

Current:

- captures high-variance inputs as local artifacts
- enriches intake into readable briefs and generates dispatchable work orders for downstream Foundries
- uses HITL gating: work orders are created unaccepted and must be accepted before dispatch
- supports multiple interfaces for the same workflow: MCP tools, CLI, and Streamlit UI
- optionally exports briefs to an Obsidian reading channel

Aspirational:

- expand the dispatcher path from preview-only to optional execution by invoking downstream MCP tools
- stronger artifact lifecycle management across intake, brief, and work order artifacts
- add test coverage for artifact IO, acceptance toggling, and LLM fallback behavior

#### Idea-Foundry

Current:

- intake and shaping of opportunities into structured submissions
- bridges raw ideas into handoff-ready packets for downstream execution

Aspirational:

- more standardized intake schemas and automated quality checks
- stronger “idea → intent” handoff automation with explicit gating

#### Intent-Foundry

Current:

- turns human intent into traceable, execution-ready artifacts and runs
- supports workflow steps and packaging into executive-ready bundles

Aspirational:

- more reusable intent archetypes
- richer validation and policy guardrails

### Cross-cutting Foundries

#### TRACE-Loop-Lite

Current:

- local-first research pipeline emphasizing evidence, narrative, and explainability
- exports knowledge artifacts for reuse and publishing

Aspirational:

- deeper synthesis and stronger packaging for downstream “publish” consumption

#### Brand-Foundry

Current:

- advisory posture for narrative, positioning, and polish
- helps maintain coherent voice and messaging without auto-editing by default

Aspirational:

- more structured brand guidance artifacts and checklists
- opt-in automation with strong review gates

#### CV-Foundry

Current:

- produces tailored career artifacts from canonical sources
- supports publishing into Share outputs

Aspirational:

- more generalized “portfolio packaging” for multiple artifact types

#### Comms-Foundry

Current:

- turns an idea into a canonical Markdown artifact and routes derived outputs
- emphasizes safety guardrails for publishing actions

Aspirational:

- richer distribution policies and repeatable campaign packaging

#### Prompt-Foundry

Current:

- organizes, validates, and assembles reusable prompts
- supports a UI/workbench model for operating prompt assets

Aspirational:

- stronger test harnesses and prompt provenance workflows

### Supporting capability repos

#### Hints-MCP

Current:

- centralized “how-to” library of approved patterns
- semantic search for quick retrieval during builds and audits

Aspirational:

- more formal promotion workflow from workbench notes into approved hints

#### Agentic-MCP

Current:

- general-purpose operational tools
- enables agents to take reliable, repeatable actions

Aspirational:

- expanded safe automation primitives and better audit trails

#### Local-Repos-MCP and ProjectSetup-MCP

Current:

- scaffolding and compliance enforcement for new repos
- discovery and launch conventions

Aspirational:

- standardized birth pipeline so new repos become suite-aware by default

#### netops-control-plane

Current:

- port governance and service orchestration to reduce collisions
- supports a policy of dynamic ports and avoiding hardcoding

Aspirational:

- tighter integration with dashboard launchers and service registries

#### Share

Current:

- publishing endpoint for shareable artifacts

Aspirational:

- richer publication workflows and feedback loops into the suite

## Why this is valuable

Foundry-Suite is valuable because it makes collaboration with AI safer and more productive in day-to-day knowledge work:

- it reduces the overhead of “figuring out where things go”
- it provides repeatable pipelines instead of ad-hoc chat transcripts
- it makes AI actions inspectable through artifacts and logs
- it increases trust by keeping humans in control of decisions that matter

It also functions as a learning accelerator:

- each iteration produces reusable patterns
- the ecosystem becomes more navigable over time
- experimentation is encouraged without sacrificing governance

## How to engage with the suite

If you are inside a repo that claims membership:

- start at `FOUNDRY_SUITE_HOME/read-this.md`
- consult the suite constitution and awareness charter
- adopt suite-awareness in your README
- prefer MCP tool calls and artifact handoffs over direct cross-repo edits

## Lessons learned so far

This section is intended to accumulate practical learnings without becoming a long narrative.

### What worked

- Keeping governance stable while allowing fast iteration in workbenches.
- Treating work as artifacts with provenance rather than relying on chat logs.
- Using MCP as a contracts layer to keep repos loosely coupled.

### What we had to correct

- Hardcoding ports does not scale; runtime-assigned ports with a policy layer is the safer default.
- Suite awareness needs a machine-readable registry to avoid tribal knowledge.

### What we are standardizing next

- A consistent capability report per repo for cockpit-style visibility.
- Lightweight run status exposure so unfinished work can be discovered without opening each UI.

## Maintenance notes

This document is intentionally written to evolve.

When updating it:

- keep claims grounded in what exists today
- distinguish “current” from “aspirational” explicitly
- favor concrete examples and named artifacts over slogans
