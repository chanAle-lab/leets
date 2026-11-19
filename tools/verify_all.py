import json
import os

repo = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets'
with open(os.path.join(repo, 'questions.json'), 'r', encoding='utf-8') as f:
    d = json.load(f)

np = len(d['papers'])
nq = len(d['questions'])
tm = sum(q['marks'] for q in d['questions'])
print('Total papers:', np)
print('Total questions:', nq)
print('Total marks across DB:', tm)

missing = []
for q in d['questions']:
    if 'image' in q:
        p = os.path.join(repo, q['image'])
        if not os.path.exists(p): missing.append((q['id'], 'image', q['image']))
    if 'markscheme' in q:
        p = os.path.join(repo, q['markscheme'])
        if not os.path.exists(p): missing.append((q['id'], 'markscheme', q['markscheme']))
    for fig in q.get('figures', []):
        p = os.path.join(repo, fig)
        if not os.path.exists(p): missing.append((q['id'], 'figure', fig))

print('Missing images count:', len(missing))
if missing:
    for m in missing[:5]: print(' ', m)
else:
    print('VERIFIED: 100% of images, question prompts, mark schemes, and figures exist on disk!')

for p in d['papers']:
    pqs = [q for q in d['questions'] if q.get('paper') == p['id']]
    ptot = sum(q['marks'] for q in pqs)
    if len(pqs) > 0:
        print(f"  {p['id']} ({p['code']}): {len(pqs)} questions, {ptot}/{p['totalMarks']} marks")
