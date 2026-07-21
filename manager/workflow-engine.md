# Workflow Engine

Version: 2.0.0

## Route Selection

1. Prefer a direct skill route for one clear deliverable.
2. Use an end-to-end workflow when the request requires linked stages.
3. Use Manager orchestration when multiple skills have distinct responsibilities.
4. Load a brand module before creative execution, not after.
5. Continue from the first incomplete stage in project state.

## Default Routes

- **Video production:** Brand optional → Video Workflow → Copy only for spoken/caption assets → Publish only when requested
- **Review production:** Brand optional → Review Workflow → Copy only for final caption variants → Publish only when requested
- **Campaign:** Planner → Research when evidence is needed → production skill(s) → Copy → Publish
- **Product launch:** Planner → Research → Brand → chosen creative workflow → Copy → Publish → Analytics measurement plan
- **Performance improvement:** Analytics → Research only for unresolved causes → Planner for accepted test schedule

## Stage State

Each stage is one of:
`not_started`, `in_progress`, `needs_approval`, `approved`, `blocked`, `complete`.

Only `not_started`, `in_progress`, or explicitly revised stages may execute.
