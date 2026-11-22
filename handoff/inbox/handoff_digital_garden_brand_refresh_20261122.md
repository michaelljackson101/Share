# Handoff Notice: Digital Garden Quartz Layout Brand Refresh

- **Date**: 2026-11-22
- **Source**: Brand-Foundry (Sovereign Brand & Narrative Authority)
- **Target**: Share (Digital Garden Maintainers & Sub-Agents)
- **Governance Reference**: [`Hints-Foundry` Catalog Rule 10: `catalog/governance/ecosystem_rule_10_external_branding_and_profiles_contract.md`](file:///home/michael/CascadeProjects/Hints-Foundry/catalog/governance/ecosystem_rule_10_external_branding_and_profiles_contract.md)
- **Authoritative Standards**: 
  - [`Brand-Foundry/standards/brand_kit.yml`](file:///home/michael/CascadeProjects/Brand-Foundry/standards/brand_kit.yml)
  - [`Brand-Foundry/standards/footers.yml`](file:///home/michael/CascadeProjects/Brand-Foundry/standards/footers.yml)
- **Public CDN Asset Root**: `https://michaelljackson101.github.io/Share/static/logos/`

---

## 🎯 Executive Context: Digital Garden Brand Coherence

The `Share` repository hosts Michael Jackson's public digital garden published via Quartz 4 to GitHub Pages (`https://michaelljackson101.github.io/Share`). While `quartz.config.ts` successfully aligns with Foundry Suite dark/light theme tokens, the layout components currently feature default upstream Quartz links (`jackyzha0/quartz` and Discord) and lack the canonical Foundry Suite anvil emblem.

---

## 🛠️ Requested Actions for Share

1. **Quartz Footer Refresh**:
   - In `quartz.layout.ts`, replace generic Discord/Quartz links in `sharedPageComponents.footer` with the canonical Foundry Suite ecosystem footer:
     - **Author**: Michael L. Jackson
     - **Links**: [Website/Home](https://michaelljackson101.github.io/Share/index.html) • [GitHub](https://github.com/michaelljackson101) • [LinkedIn](https://www.linkedin.com/in/michaelljackson/)
     - **Tagline**: *"Building systems that think."*
2. **Page Title / Header Icon**:
   - In `quartz.layout.ts`, incorporate the micro anvil mark (`static/logos/foundry_logo_32.png`) into the header or alongside `Component.PageTitle()`.
3. **Favicon**:
   - Confirm `static/logos/foundry_logo_32.png` is configured as the site favicon in Quartz head configuration.

