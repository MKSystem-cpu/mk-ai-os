# MK AI OS

A modular AI creative-production system for planning, research, video, review, copy, publishing, analytics and brand-specific execution.

**Version:** 1.1.0  
**Status:** Production Foundation

## Active Skills
- Manager
- Planner
- Research
- Video
- Review
- Copy
- Publish
- Analytics
- MK Collection Brand Skill

## Start Here
1. Read `QUICKSTART.md`
2. Call `Manager` when the required Skill is unclear
3. Load `brands/mk-collection/SKILL.md` for MK Collection work
4. Use a Workflow from `workflows/`
5. Validate with `python tools/validate_repository.py`

## Architecture
- `manager/` — routing and orchestration
- `skills/core/` — active worker Skills
- `brands/` — brand rules and identity
- `workflows/` — reusable processes
- `registries/` — system catalog
- `contracts/` — input, output and handoff standards
- `capabilities/` — reusable competencies
- `governance/` — system-wide policies
- `templates/` — module templates

See `GITHUB-UPLOAD-GUIDE.md` for upload instructions.
