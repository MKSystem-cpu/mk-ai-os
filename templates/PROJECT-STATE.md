# Project State

```yaml
project_id: ""
project_name: ""
version: 1
status: active
active_brand: none
primary_workflow: ""
objective: ""
audience: ""
platform: ""
assets: []
constraints: []
locked_decisions: []
current_stage: ""
next_stage: ""
stages: {}
deliverables: []
open_questions: []
last_updated: ""
```

## Update Rules
- Add only approved or verified decisions to `locked_decisions`.
- Mark a stage complete only when its required output exists.
- Keep `next_stage` equal to the first unfinished dependency.
- Never replace a locked artifact without recording explicit revision approval.
