from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    'README.md','QUICKSTART.md','GITHUB-UPLOAD-GUIDE.md','manager/SKILL.md',
    'brands/mk-collection/SKILL.md','registries/skill-registry.md',
    'registries/workflow-registry.md','contracts/handoff-contract.md'
]
required += [f'skills/core/{s}/SKILL.md' for s in ['planner','research','video','review','copy','publish','analytics']]
missing=[p for p in required if not (root/p).is_file()]
if missing:
    print('FAILED: Missing files:')
    print('\n'.join(missing))
    sys.exit(1)
print(f'PASS: repository validated ({sum(1 for p in root.rglob("*") if p.is_file())} files)')
