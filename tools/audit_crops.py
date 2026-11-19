import json
import os

repo = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets'
with open(os.path.join(repo, 'questions.json'), 'r', encoding='utf-8') as f:
    d = json.load(f)

for pid in ['2019-summer-01', '2018-practice-01', '2019-summer-as-01', '2019-summer-02']:
    qs = [q for q in d['questions'] if q.get('paper') == pid]
    print(f'=== {pid} ({len(qs)} questions) ===')
    for q in qs:
        print(f"  {q['id']}: img={q.get('image')} figs={q.get('figures', [])}")
