# Publishing Contract (Share Digital Garden)

## Purpose

This repository is the public-facing publishing surface for Michael Jackson’s digital garden.

Goals:

- Share useful, credible knowledge with peers.
- Promote the Foundry-Suite ecosystem.
- Promote Michael professionally as an AI practitioner and systems thinker.
- Do not publish the “full recipe” (sensitive implementation details, internal-only architecture, or anything that creates avoidable security or reputational risk).

## Roles

- Garden steward (structure + policy): This repo’s maintainer.
- Brand editorial review: Brand-Foundry.
- CV/career artifact ownership: CV-Foundry.

## Lanes

### Lane A (fast publish)

Allowed without Brand-Foundry review:

- Notes under `content/Notes/**` that are framed as learnings and include a short teaser summary.

### Lane B (brand-reviewed)

Requires Brand-Foundry review before publishing:

- `content/About/**`
- `content/Portfolio/**`
- `content/Foundry-Suite/**`
- Any page that is linked from the home page as a primary call-to-action
- Any resume/one-pager landing page content

## Escalation policy

If a contributor repo believes an exception is needed (e.g., disclosing more details than normal), escalate to Michael for explicit approval.

## Minimum quality bar (public pages)

Each published page should:

- Start with a 2–4 sentence teaser summary.
- State who the page is for (peers, leaders, recruiters, mixed).
- Use specific, concrete language.
- Avoid sensitive detail. Prefer abstractions and examples.

## Recommended frontmatter

For public pages under `content/`, prefer:

- `title`
- `draft` (default `true` until ready)
- `tags`
- `summary`
- `audience` (`technical` | `executive` | `mixed`)
- `source_repo`
- `review` (`self-published` | `brand-reviewed`)

## Handoff pattern (from other repos)

Contributor repos should provide:

- A single Markdown page ready to copy into `Share/content/...`
- Any supporting static assets for `Share/content/static/...`
- A short changelog note describing what changed and why

## Operational notes

- Use `./quartz-sync.sh --check` to see if a sync is needed.
- Use `./quartz-sync.sh "<message>"` to commit + pull + push via Quartz sync.
