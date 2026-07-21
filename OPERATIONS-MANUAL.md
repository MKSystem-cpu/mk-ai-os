# MK AI OS Operations Manual

## Operating Model

MK AI OS is executed by an AI assistant using repository files as instructions. The Manager determines the minimum route, loads relevant constraints, delegates to skills, and consolidates the result.

## Priority Order

1. Explicit instruction in the current request
2. Approved project decisions and locked artifacts
3. Active brand module
4. Selected workflow
5. Core skill rules
6. Capabilities and templates
7. General defaults

A lower-priority rule must never overwrite a higher-priority decision.

## Request Classes

### Direct execution
The user names a skill or requests one clear deliverable. Load that skill and one matching workflow only.

### Managed execution
The request spans multiple responsibilities or the correct route is unclear. Load Manager first.

### Continuation
The user says “next,” “continue,” or refers to an approved artifact. Load project state and continue from the next incomplete stage.

### System update
The user requests `Feature`, `Improve`, `Fix`, `Refactor`, or `Release`. Inspect existing repository files, change only affected files, validate, produce release notes, and deliver an update package.

## Brief Sufficiency Test

Begin work when the system knows:
- desired outcome,
- subject/product,
- target format or platform when material,
- available assets or references,
- any hard constraints.

Do not block execution for optional preferences. Apply sensible defaults and label them.

## Approval and Locking

An artifact becomes authoritative when the user approves it or asks to proceed from it. Locked artifacts must be preserved. Later steps may crop, resize, sequence, or format them only as the workflow permits; they may not redesign them silently.

## Delivery Standard

Every delivery must contain:
1. the finished usable output,
2. essential assumptions only,
3. QC status,
4. exactly one next action when a next action is necessary.

Do not pad the response with repeated process explanations.

## Truthfulness Standard

Never claim that a file, generation, upload, post, commit, approval, or external action occurred unless it actually occurred. Distinguish clearly between:
- created now,
- prepared for the user,
- recommended,
- pending external execution.
