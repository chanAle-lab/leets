import fitz, os, json

qp_path = r'C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded\media_1795090284300_97db84a6.pdf'
repo = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets'
out_dir = os.path.join(repo, 'img', '2019-summer-01')
os.makedirs(out_dir, exist_ok=True)

qp = fitz.open(qp_path)

# Resource Figures (context preamble + stimulus diagrams)
fig_crops = {
    'fig-1-1.jpg': (1, fitz.Rect(45, 80, 555, 420)),
    'fig-1-2.jpg': (2, fitz.Rect(45, 55, 555, 305)),
    'fig-2-1.jpg': (5, fitz.Rect(45, 55, 555, 238)),
    'fig-2-2.jpg': (6, fitz.Rect(45, 55, 555, 245)),
    'fig-3.jpg':   (9, fitz.Rect(45, 55, 555, 235)),
    'fig-4-1.jpg': (11, fitz.Rect(45, 55, 555, 350)),
    'fig-4-2.jpg': (12, fitz.Rect(45, 55, 555, 395)),
    'fig-4-3.jpg': (15, fitz.Rect(45, 55, 555, 380)),
}

for name, (pno, rect) in fig_crops.items():
    pix = qp[pno].get_pixmap(matrix=fitz.Matrix(2.2, 2.2), clip=rect)
    pix.save(os.path.join(out_dir, name))
    print(f"Saved figure {name}: {pix.width}x{pix.height}")

# Question cards (subpart prompt only)
q_crops = {
    'q1a.jpg':   (1, fitz.Rect(45, 420, 555, 628)),
    'q1bi.jpg':  (2, fitz.Rect(45, 305, 555, 535)),
    'q1bii.jpg': (2, fitz.Rect(45, 535, 555, 780)),
    'q1biii.jpg':(3, fitz.Rect(45, 55, 555, 190)),
    'q1biv.jpg': (3, fitz.Rect(45, 190, 555, 515)),
    'q1bv.jpg':  (3, fitz.Rect(45, 515, 555, 785)),
    'q1c.jpg':   (4, fitz.Rect(45, 55, 555, 785)),
    'q2a.jpg':   (5, fitz.Rect(45, 238, 555, 630)),
    'q2bi.jpg':  (6, fitz.Rect(45, 245, 555, 305)),
    'q2bii.jpg': (6, fitz.Rect(45, 305, 555, 780)),
    'q2biii.jpg':(7, fitz.Rect(45, 55, 555, 365)),
    'q2biv.jpg': (7, fitz.Rect(45, 365, 555, 535)),
    'q2c.jpg':   (8, fitz.Rect(45, 55, 555, 445)),
    'q3a.jpg':   (9, fitz.Rect(45, 235, 555, 790)),
    'q3bi.jpg':  (10, fitz.Rect(45, 55, 555, 260)),
    'q3bii.jpg': (10, fitz.Rect(45, 260, 555, 530)),
    'q4a.jpg':   (11, fitz.Rect(45, 350, 555, 550)),
    'q4bi.jpg':  (12, fitz.Rect(45, 395, 555, 540)),
    'q4bii.jpg': (12, fitz.Rect(45, 540, 555, 695)),
    'q4biii.jpg':(13, fitz.Rect(45, 55, 555, 240)),
    'q4c.jpg':   (13, fitz.Rect(45, 240, 555, 490)),
    'q4d.jpg':   (14, fitz.Rect(45, 55, 555, 685)),
    'q4ei.jpg':  (15, fitz.Rect(45, 380, 555, 795)),
    'q4eii.jpg': (16, fitz.Rect(45, 55, 555, 630)),
    'q4eiii.jpg':(17, fitz.Rect(45, 55, 555, 540)),
}

for name, (pno, rect) in q_crops.items():
    pix = qp[pno].get_pixmap(matrix=fitz.Matrix(2.2, 2.2), clip=rect)
    pix.save(os.path.join(out_dir, name))
    print(f"Saved question {name}: {pix.width}x{pix.height}")

# Update questions.json to ensure figure linkages match
with open(os.path.join(repo, 'questions.json'), 'r', encoding='utf-8') as f:
    db = json.load(f)

# Ensure figure associations
fig_map = {
    '2019-summer-01-q1a': ['img/2019-summer-01/fig-1-1.jpg'],
    '2019-summer-01-q1bi': ['img/2019-summer-01/fig-1-2.jpg'],
    '2019-summer-01-q1bii': ['img/2019-summer-01/fig-1-2.jpg'],
    '2019-summer-01-q1biii': ['img/2019-summer-01/fig-1-2.jpg'],
    '2019-summer-01-q1c': ['img/2019-summer-01/fig-1-1.jpg'],
    '2019-summer-01-q2a': ['img/2019-summer-01/fig-2-1.jpg'],
    '2019-summer-01-q2bi': ['img/2019-summer-01/fig-2-2.jpg'],
    '2019-summer-01-q2bii': ['img/2019-summer-01/fig-2-2.jpg'],
    '2019-summer-01-q2biii': ['img/2019-summer-01/fig-2-2.jpg'],
    '2019-summer-01-q2biv': ['img/2019-summer-01/fig-2-2.jpg'],
    '2019-summer-01-q3a': ['img/2019-summer-01/fig-3.jpg'],
    '2019-summer-01-q4a': ['img/2019-summer-01/fig-4-1.jpg'],
    '2019-summer-01-q4bi': ['img/2019-summer-01/fig-4-2.jpg'],
    '2019-summer-01-q4bii': ['img/2019-summer-01/fig-4-2.jpg'],
    '2019-summer-01-q4biii': ['img/2019-summer-01/fig-4-2.jpg'],
    '2019-summer-01-q4d': ['img/2019-summer-01/ms-4d-system-diagram.jpg'],
    '2019-summer-01-q4ei': ['img/2019-summer-01/fig-4-3.jpg'],
    '2019-summer-01-q4eii': ['img/2019-summer-01/fig-4-3.jpg'],
    '2019-summer-01-q4eiii': ['img/2019-summer-01/ms-4eiii-flowchart.jpg'],
}

for q in db['questions']:
    if q['id'] in fig_map:
        q['figures'] = fig_map[q['id']]

with open(os.path.join(repo, 'questions.json'), 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("Successfully refactored 2019-summer-01 crops and question linkages!")
