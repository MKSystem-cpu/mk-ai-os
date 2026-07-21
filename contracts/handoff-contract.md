# Handoff Contract v2.0

```yaml
from_skill: ""
to_skill: ""
project_id: ""
objective: ""
audience: ""
platform: ""
active_brand: none
verified_facts: []
assets: []
locked_decisions: []
constraints: []
completed_outputs: []
requested_output: ""
open_blockers: []
```

## Rules
- Pass only relevant, verified context.
- Never overwrite locked decisions silently.
- Do not ask the user for information already contained in the handoff.
- The receiving skill owns only its stated requested output.
