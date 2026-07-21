from pathlib import Path
import re, sys

root = Path(__file__).resolve().parents[1]
required = [
    'README.md','QUICKSTART.md','OPERATIONS-MANUAL.md','VERSION','CHANGELOG.md',
    'manager/SKILL.md','manager/workflow-engine.md','manager/intent-manager.md',
    'registries/skill-registry.md','registries/workflow-registry.md',
    'contracts/handoff-contract.md','templates/PROJECT-STATE.md'
]
skills = ['planner','research','video','review','copy','publish','analytics']
required += [f'skills/core/{s}/SKILL.md' for s in skills]
workflows = ['video-production','review-production','campaign','product-launch','poster-production','carousel-production','social-content']
required += [f'workflows/{w}/workflow.md' for w in workflows]

errors=[]
for rel in required:
    p=root/rel
    if not p.is_file(): errors.append(f'MISSING {rel}')
    elif rel != 'VERSION' and p.stat().st_size < 120: errors.append(f'TOO_SHORT {rel}')

version=(root/'VERSION').read_text(encoding='utf-8').strip() if (root/'VERSION').exists() else ''
if version != '2.0.0': errors.append(f'VERSION expected 2.0.0, found {version!r}')

for s in skills:
    text=(root/f'skills/core/{s}/SKILL.md').read_text(encoding='utf-8')
    for heading in ['## Mission','## Execution Workflow','## Outputs','## Quality Gate']:
        if heading not in text: errors.append(f'{s}: missing {heading}')
    if 'generic' in text.lower() and 'placeholder' in text.lower():
        errors.append(f'{s}: appears to contain placeholder content')

# detect broken markdown links to local .md files
link_re=re.compile(r'\[[^\]]+\]\((?!https?://|#)([^)]+\.md)(?:#[^)]+)?\)')
for md in root.rglob('*.md'):
    txt=md.read_text(encoding='utf-8',errors='replace')
    for target in link_re.findall(txt):
        if not (md.parent/target).resolve().exists():
            errors.append(f'BROKEN_LINK {md.relative_to(root)} -> {target}')

if errors:
    print('FAILED')
    for e in errors: print('-',e)
    sys.exit(1)

count=sum(1 for p in root.rglob('*') if p.is_file())
print(f'PASS: MK AI OS {version} validated ({count} files)')
