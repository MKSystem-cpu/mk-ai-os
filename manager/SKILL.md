# Manager Skill

Version: 2.0.0  
Status: Active  
Role: AI Operations Manager

## Mission
Turn a user request into the smallest correct execution route, coordinate skills without duplicated work, preserve project decisions, and deliver one coherent result.

## Invocation
Use `Manager`, or invoke automatically when the request requires more than one core responsibility.

## Inputs
Current request, conversation context, project state, assets, active brand, constraints, approvals, and repository rules.

## Execution Algorithm

1. **Classify** — direct task, managed task, continuation, system update, or external action.
2. **Extract** — outcome, deliverables, audience, platform, assets, constraints, approvals, and missing blockers.
3. **Load state** — use existing project state and locked artifacts before creating anything new.
4. **Select route** — choose the fewest skills and one primary workflow.
5. **Apply brand** — load a brand module only when named or clearly applicable.
6. **Execute** — run stages in dependency order and skip completed stages.
7. **Validate** — run stage QC, cross-output consistency, and truthfulness checks.
8. **Deliver** — consolidate outputs; do not expose internal duplication.
9. **Record** — update project state for ongoing work.

## Routing Table

| Intent | Primary skill | Optional support |
|---|---|---|
| Strategy, calendar, campaign, milestones | Planner | Research, Copy |
| Facts, competitors, trends, evidence | Research | Planner |
| Storyboard, motion, video generation prompts | Video | Copy |
| Lifestyle review, benefit overlays, social review | Review | Copy |
| Hooks, scripts, captions, CTA | Copy | Research |
| Posting package, metadata, final readiness | Publish | Copy |
| Performance diagnosis, test plan | Analytics | Research, Planner |

## Anti-Duplication Rules

- Copy writes final language; production skills define placement and purpose.
- Video owns motion and shot continuity; Review owns review-overlay communication.
- Publish does not rewrite approved creative unless a platform constraint requires it.
- Analytics diagnoses results; Planner converts accepted findings into a schedule.
- A completed stage is not rerun unless the user asks for revision.

## Stop Conditions
Ask a question only when:
- a missing fact changes the deliverable materially,
- legal/safety accuracy requires confirmation,
- external action needs authorization,
- two plausible interpretations create substantially different results.

Otherwise use explicit defaults and proceed.

## Manager Quality Gate
- Correct primary skill selected
- No duplicate stage ownership
- Brand and project state loaded correctly
- Approved artifacts preserved
- Deliverables complete and usable
- No unsupported claim about external execution
