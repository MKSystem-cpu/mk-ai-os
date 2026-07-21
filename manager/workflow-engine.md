# Workflow Engine
## Routing Rules
- Direct skill request: call that skill only unless a prerequisite is genuinely missing.
- Brand request: inject brand module before execution.
- Existing approved artifact: continue from it; do not restart earlier stages.
- Skip completed or unnecessary steps.
- Never include two stages with the same responsibility.

## Default Routes
- Video: Brand (optional) → Video → Copy (only when captions requested)
- Review: Brand (optional) → Review → Copy (only when captions requested)
- Product Launch: Planner → Research → Brand → chosen production skill → Copy → Publish
- Performance problem: Analytics → Research/Planner only when supported by findings
