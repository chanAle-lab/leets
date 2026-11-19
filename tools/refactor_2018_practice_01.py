import fitz, os, json

qp_path = r'C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded\media_1795086229085_87988b59.pdf'
repo = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets'
out_dir = os.path.join(repo, 'img', '2018-practice-01')
os.makedirs(out_dir, exist_ok=True)

qp = fitz.open(qp_path)

# Resource Figures (context preamble + stimulus diagrams)
fig_crops = {
    'fig-1-1.jpg': (1, fitz.Rect(45, 80, 555, 275)),
    'fig-1-2.jpg': (2, fitz.Rect(45, 55, 555, 385)),
    'fig-1-3.jpg': (3, fitz.Rect(45, 55, 555, 320)),
    'fig-1-4.jpg': (3, fitz.Rect(45, 320, 555, 465)),
    'fig-2-1.jpg': (6, fitz.Rect(45, 55, 555, 330)),
    'fig-2-2.jpg': (7, fitz.Rect(45, 55, 555, 360)),
    'fig-2-3.jpg': (8, fitz.Rect(45, 55, 555, 250)),
    'fig-2-4.jpg': (10, fitz.Rect(45, 55, 555, 300)),
    'fig-4-1.jpg': (13, fitz.Rect(45, 55, 555, 340)),
    'fig-4-2.jpg': (14, fitz.Rect(45, 55, 555, 320)),
}

for name, (pno, rect) in fig_crops.items():
    pix = qp[pno].get_pixmap(matrix=fitz.Matrix(2.2, 2.2), clip=rect)
    pix.save(os.path.join(out_dir, name))
    print(f"Saved Practice figure {name}: {pix.width}x{pix.height}")

# Question cards (subpart prompt only)
q_crops = {
    'q1a.jpg':   (1, fitz.Rect(45, 275, 555, 430)),
    'q1b.jpg':   (1, fitz.Rect(45, 430, 555, 675)),
    'q1ci.jpg':  (2, fitz.Rect(45, 385, 555, 785)),
    'q1cii.jpg': (3, fitz.Rect(45, 465, 555, 785)),
    'q1ciii.jpg':(4, fitz.Rect(45, 55, 555, 550)),
    'q1di.jpg':  (4, fitz.Rect(45, 550, 555, 785)),
    'q1dii.jpg': (5, fitz.Rect(45, 55, 555, 340)),
    'q1diii.jpg':(5, fitz.Rect(45, 340, 555, 785)),
    'q2a.jpg':   (6, fitz.Rect(45, 330, 555, 785)),
    'q2b.jpg':   (7, fitz.Rect(45, 360, 555, 785)),
    'q2ci.jpg':  (8, fitz.Rect(45, 250, 555, 550)),
    'q2cii.jpg': (9, fitz.Rect(45, 55, 555, 345)),
    'q2ciii.jpg':(9, fitz.Rect(45, 345, 555, 580)),
    'q2civ.jpg': (9, fitz.Rect(45, 580, 555, 785)),
    'q2di.jpg':  (10, fitz.Rect(45, 300, 555, 620)),
    'q2dii.jpg': (10, fitz.Rect(45, 620, 555, 785)),
    'q3ai.jpg':  (11, fitz.Rect(45, 55, 555, 395)),
    'q3aii.jpg': (11, fitz.Rect(45, 395, 555, 785)),
    'q3b.jpg':   (12, fitz.Rect(45, 55, 555, 785)),
    'q4a.jpg':   (13, fitz.Rect(45, 340, 555, 580)),
    'q4bi.jpg':  (14, fitz.Rect(45, 320, 555, 620)),
    'q4bii.jpg': (14, fitz.Rect(45, 620, 555, 785)),
    'q4biii.jpg':(15, fitz.Rect(45, 55, 555, 550)),
    'q4c.jpg':   (15, fitz.Rect(45, 550, 555, 785)),
    'q4d.jpg':   (16, fitz.Rect(45, 55, 555, 785)),
}

for name, (pno, rect) in q_crops.items():
    pix = qp[pno].get_pixmap(matrix=fitz.Matrix(2.2, 2.2), clip=rect)
    pix.save(os.path.join(out_dir, name))
    print(f"Saved Practice question {name}: {pix.width}x{pix.height}")

# Update questions.json for 2018-practice-01 figure linkages
with open(os.path.join(repo, 'questions.json'), 'r', encoding='utf-8') as f:
    db = json.load(f)

practice_fig_map = {
    '2018-practice-01-q1a': ['img/2018-practice-01/fig-1-1.jpg'],
    '2018-practice-01-q1b': ['img/2018-practice-01/fig-1-1.jpg'],
    '2018-practice-01-q1ci': ['img/2018-practice-01/fig-1-2.jpg'],
    '2018-practice-01-q1cii': ['img/2018-practice-01/fig-1-3.jpg', 'img/2018-practice-01/fig-1-4.jpg'],
    '2018-practice-01-q1ciii': [],
    '2018-practice-01-q1di': [],
    '2018-practice-01-q1dii': [],
    '2018-practice-01-q1diii': ['img/2018-practice-01/ms-1diii-diagram.jpg'],
    '2018-practice-01-q2a': ['img/2018-practice-01/fig-2-1.jpg', 'img/2018-practice-01/ms-2a-diagram.jpg'],
    '2018-practice-01-q2b': ['img/2018-practice-01/fig-2-2.jpg'],
    '2018-practice-01-q2ci': ['img/2018-practice-01/fig-2-3.jpg'],
    '2018-practice-01-q2cii': [],
    '2018-practice-01-q2ciii': [],
    '2018-practice-01-q2civ': [],
    '2018-practice-01-q2di': ['img/2018-practice-01/fig-2-4.jpg'],
    '2018-practice-01-q2dii': ['img/2018-practice-01/fig-2-4.jpg'],
    '2018-practice-01-q3ai': [],
    '2018-practice-01-q3aii': [],
    '2018-practice-01-q3b': [],
    '2018-practice-01-q4a': ['img/2018-practice-01/fig-4-1.jpg'],
    '2018-practice-01-q4bi': ['img/2018-practice-01/fig-4-2.jpg'],
    '2018-practice-01-q4bii': ['img/2018-practice-01/fig-4-2.jpg'],
    '2018-practice-01-q4biii': [],
    '2018-practice-01-q4c': [],
    '2018-practice-01-q4d': [],
}

for q in db['questions']:
    if q['id'] in practice_fig_map:
        q['figures'] = practice_fig_map[q['id']]

with open(os.path.join(repo, 'questions.json'), 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("Successfully refactored 2018-practice-01 crops and question linkages!")
