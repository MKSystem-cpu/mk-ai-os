# Intent Manager

## Intent Schema

```yaml
request_class: direct | managed | continuation | system_update | external_action
primary_outcome: string
deliverables: []
audience: string | unknown
platform: string | unknown
assets: []
constraints: []
approvals: []
active_brand: string | none
blockers: []
```

## Interpretation Rules
- Treat the latest explicit instruction as authoritative.
- Resolve pronouns and “next step” from project state and the latest approved artifact.
- Do not convert preferences into mandatory blockers.
- A short alias such as `Video`, `Review`, or `Manager` is a valid invocation.
- Commands beginning with Feature/Improve/Fix/Refactor/Release are system-update requests.
