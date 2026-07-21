# MK AI OS

**Version:** 2.0.0  
**Type:** Repository-based AI operating manual and production system  
**Status:** Ready for day-to-day use

MK AI OS coordinates seven core skills, reusable workflows, brand modules, project state, handoffs, and quality gates. It is designed for use inside an AI chat or agent workspace. The repository is the source of truth; the AI reads the relevant files and executes their instructions.

> MK AI OS is not a standalone background application or autonomous server. It is a complete, version-controlled operating system for directing AI work consistently.

## Core Skills

| Command | Responsibility |
|---|---|
| `Manager` | Routes work and coordinates multiple skills |
| `Planner` | Plans campaigns, calendars, milestones, and execution |
| `Research` | Finds, verifies, compares, and summarizes evidence |
| `Video` | Creates storyboard-led video production packages |
| `Review` | Creates lifestyle review and benefit-overlay content |
| `Copy` | Writes hooks, scripts, captions, CTAs, and variants |
| `Publish` | Prepares final platform-ready publishing packages |
| `Analytics` | Diagnoses performance and defines tests |

## Fast Start

Use one of these forms in chat:

```text
Manager: Create a complete launch campaign for [product].
Video: Create a 9-shot vertical product video.
Review: Create a lifestyle review poster series.
Improve: Video Skill — add [rule].
Fix: Review Workflow — remove [problem].
```

The AI should load `manager/SKILL.md`, the selected skill, an applicable workflow, and any named brand module. It should then execute immediately when the brief is sufficient.

## Repository Map

- `manager/` — routing, decisions, state, and orchestration
- `skills/core/` — seven executable skill specifications
- `workflows/` — end-to-end production procedures
- `brands/` — brand-specific rules and identity
- `capabilities/` — reusable specialist methods
- `contracts/` — handoff and output schemas
- `templates/` — ready-to-copy project and delivery templates
- `tools/` — repository validation
- `projects/` — project-state records

See `QUICKSTART.md` for operation and `OPERATIONS-MANUAL.md` for the complete execution standard.
