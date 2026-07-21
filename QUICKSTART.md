# MK AI OS — Quick Start v2.0

## 1. Call the system

### Let Manager choose
```text
Manager: I need a complete social campaign for this product.
```

### Call a skill directly
```text
Video: Build a 6-shot storyboard and Omni prompts from these assets.
Review: Create a cute lifestyle review overlay poster.
Copy: Write 5 Thai hooks and one final caption.
```

### Update the operating system
```text
Feature: Add a podcast skill.
Improve: Video Skill — require stronger product continuity.
Fix: Review Workflow — remove duplicated overlay instructions.
Refactor: Manager routing — simplify brand loading.
```

## 2. Required execution behavior

1. Start immediately when the brief is sufficient.
2. Ask only when a missing answer would materially change the output.
3. Load only the smallest sufficient set of files.
4. Reuse approved decisions; never restart completed stages.
5. Keep one responsibility per stage.
6. Run the skill's quality gate before delivery.
7. State clearly what was actually created and what still requires user action.

## 3. Standard production flow

```text
Request → Route → Load Brand (optional) → Execute Skill/Workflow → QC → Deliver → Record State
```

## 4. Project continuity

For work that continues across turns, copy `templates/PROJECT-STATE.md` into `projects/<project-slug>/STATE.md`. Update it after each approved milestone.

## 5. GitHub update loop

```text
Receive changed files → Copy into local repository → Review diff → Commit → Push
```

Suggested commit messages:

```text
feat(video): add storyboard continuity rules
fix(review): remove duplicated split instructions
release: MK AI OS v2.0.0
```
