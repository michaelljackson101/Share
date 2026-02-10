---
id: share-quartz-digital-garden
name: Share
description: Quartz v4-based digital garden site with publishable Markdown content in content/ and direct-link static assets in content/static/.
owner: Michael Jackson
status: active
kind: quartz_site
created: 2026-02-03
tags: [quartz, digital-garden, publishing, github-pages]
consumers: ["agentic-audit"]
---

# Quartz v4

> “[One] who works with the door open gets all kinds of interruptions, but [they] also occasionally gets clues as to what the world is and what might be important.” — Richard Hamming

Quartz is a set of tools that helps you publish your [digital garden](https://jzhao.xyz/posts/networked-thought) and notes as a website for free.

## About this repository

This repository is a Quartz v4 site used to publish selected Markdown content from `content/` as a digital garden.

It also includes some semi-hidden static assets (including standalone HTML) in `content/static/` that are intended to be accessed via direct link under `/static/` on GitHub Pages.

## Foundry Suite

This repository is part of the **Foundry Suite** federation.

### Canonical reference (Option A)

Set:

- `FOUNDRY_SUITE_HOME=~/Foundry-Suite`

Consult:

- `~/Foundry-Suite/read-this.md`
- `~/Foundry-Suite/canon/index.md`
- `~/Foundry-Suite/canon/constitution/SUITE.md`
- `~/Foundry-Suite/canon/charter/awareness_operating_charter.md`

### Lifecycle metadata

- Lifecycle stage: `Publish`
- Upstream Foundries: `Learning-Foundry`, `Idea-Foundry`, `Brand-Foundry`, `CV-Foundry` (depending on whether the artifact is a note, a narrative/brand page, or a CV/resume asset)
- Downstream Foundries: Public web (GitHub Pages)

### Primary artifacts

- Produces:
  - `content/**/*.md`
  - `content/static/**/*`
  - `quartz.config.ts`
- Consumes:
  - Build outputs emitted to `public/` via `npx quartz build` and GitHub Pages deployment

### MCP

- MCP server: `No`

🔗 Read the documentation and get started: https://quartz.jzhao.xyz/

[Join the Discord Community](https://discord.gg/cRFFHYye7t)

## Sponsors

<p align="center">
  <a href="https://github.com/sponsors/jackyzha0">
    <img src="https://cdn.jsdelivr.net/gh/jackyzha0/jackyzha0/sponsorkit/sponsors.svg" />
  </a>
</p>

<br>

<div align="center">

<!-- brand-footer-start -->

---

**Michael L. Jackson**
[Website](https://michaelljackson101.github.io/Share/index.html) • [GitHub](https://github.com/michaelljackson101) • [LinkedIn](https://www.linkedin.com/in/michaelljackson/)

*Building systems that think.*

<!-- brand-footer-end -->

</div>
