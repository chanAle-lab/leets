import fitz, os, json

qp_path = r'C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded\media_1795090284268_4e11c92e.pdf'
repo = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets'
out_dir = os.path.join(repo, 'img', '2019-summer-as-01')
os.makedirs(out_dir, exist_ok=True)

qp = fitz.open(qp_path)

# Resource Figures (context preamble + stimulus diagrams)
fig_crops = {
    'fig-1-1.jpg': (1, fitz.Rect(45, 80, 555, 340)),
    'fig-1-2.jpg': (2, fitz.Rect(45, 55, 555, 310)),
    'fig-1-3.jpg': (3, fitz.Rect(45, 55, 555, 260)),
    'fig-1-4.jpg': (4, fitz.Rect(45, 55, 555, 280)),
    'fig-2-1.jpg': (6, fitz.Rect(45, 55, 555, 330)),
    'fig-2-2.jpg': (6, fitz.Rect(45, 330, 555, 490)),
    'fig-3-1.jpg': (9, fitz.Rect(45, 55, 555, 275)),
    'fig-3-2.jpg': (9, fitz.Rect(45, 275, 555, 525)),
    'fig-3-3.jpg': (10, fitz.Rect(45, 55, 555, 370)),
    'fig-3-4.jpg': (11, fitz.Rect(45, 55, 555, 365)),
    'fig-3-5.jpg': (12, fitz.Rect(45, 55, 555, 275)),
    'fig-4-1.jpg': (13, fitz.Rect(45, 55, 555, 335)),
    'fig-4-2.jpg': (14, fitz.Rect(45, 55, 555, 255)),
    'fig-4-3.jpg': (17, fitz.Rect(45, 55, 555, 275)),
    'fig-4-4.jpg': (17, fitz.Rect(45, 275, 555, 475)),
}

for name, (pno, rect) in fig_crops.items():
    pix = qp[pno].get_pixmap(matrix=fitz.Matrix(2.2, 2.2), clip=rect)
    pix.save(os.path.join(out_dir, name))
    print(f"Saved AS figure {name}: {pix.width}x{pix.height}")

# Question cards (subpart prompt only)
q_crops = {
    'q1a.jpg':   (1, fitz.Rect(45, 340, 555, 500)),
    'q1bi.jpg':  (1, fitz.Rect(45, 500, 555, 595)),
    'q1bii.jpg': (1, fitz.Rect(45, 595, 555, 685)),
    'q1ci.jpg':  (2, fitz.Rect(45, 310, 555, 495)),
    'q1cii.jpg': (3, fitz.Rect(45, 260, 555, 560)),
    'q1di.jpg':  (4, fitz.Rect(45, 280, 555, 570)),
    'q1dii.jpg': (5, fitz.Rect(45, 55, 555, 780)),
    'q2ai.jpg':  (6, fitz.Rect(45, 490, 555, 690)),
    'q2aii.jpg': (7, fitz.Rect(45, 55, 555, 365)),
    'q2aiii.jpg':(7, fitz.Rect(45, 365, 555, 730)),
    'q2b.jpg':   (8, fitz.Rect(45, 55, 555, 490)),
    'q2c.jpg':   (8, fitz.Rect(45, 490, 555, 755)),
    'q3a.jpg':   (9, fitz.Rect(45, 525, 555, 785)),
    'q3b.jpg':   (10, fitz.Rect(45, 370, 555, 785)),
    'q3ci.jpg':  (11, fitz.Rect(45, 365, 555, 785)),
    'q3cii.jpg': (12, fitz.Rect(45, 55, 555, 785)),
    'q4ai.jpg':  (13, fitz.Rect(45, 335, 555, 535)),
    'q4aii.jpg': (14, fitz.Rect(45, 255, 555, 780)),
    'q4b.jpg':   (15, fitz.Rect(45, 55, 555, 645)),
    'q4ci.jpg':  (16, fitz.Rect(45, 55, 555, 280)),
    'q4cii.jpg': (17, fitz.Rect(45, 475, 555, 785)),
    'q5a.jpg':   (19, fitz.Rect(45, 55, 555, 420)),
    'q5b.jpg':   (19, fitz.Rect(45, 420, 555, 785)),
}

for name, (pno, rect) in q_crops.items():
    pix = qp[pno].get_pixmap(matrix=fitz.Matrix(2.2, 2.2), clip=rect)
    pix.save(os.path.join(out_dir, name))
    print(f"Saved AS question {name}: {pix.width}x{pix.height}")

# Update questions.json for 2019-summer-as-01 figure linkages
with open(os.path.join(repo, 'questions.json'), 'r', encoding='utf-8') as f:
    db = json.load(f)

as_fig_map = {
    '2019-summer-as-01-q1a': ['img/2019-summer-as-01/fig-1-1.jpg'],
    '2019-summer-as-01-q1bi': [],
    '2019-summer-as-01-q1bii': [],
    '2019-summer-as-01-q1ci': ['img/2019-summer-as-01/fig-1-2.jpg'],
    '2019-summer-as-01-q1cii': ['img/2019-summer-as-01/fig-1-3.jpg'],
    '2019-summer-as-01-q1di': ['img/2019-summer-as-01/fig-1-4.jpg'],
    '2019-summer-as-01-q1dii': ['img/2019-summer-as-01/fig-1-4.jpg'],
    '2019-summer-as-01-q2ai': ['img/2019-summer-as-01/fig-2-1.jpg', 'img/2019-summer-as-01/fig-2-2.jpg'],
    '2019-summer-as-01-q2aii': ['img/2019-summer-as-01/fig-2-2.jpg'],
    '2019-summer-as-01-q2aiii': ['img/2019-summer-as-01/fig-2-2.jpg'],
    '2019-summer-as-01-q2b': ['img/2019-summer-as-01/fig-2-2.jpg'],
    '2019-summer-as-01-q2c': [],
    '2019-summer-as-01-q3a': ['img/2019-summer-as-01/fig-3-1.jpg', 'img/2019-summer-as-01/fig-3-2.jpg'],
    '2019-summer-as-01-q3b': ['img/2019-summer-as-01/fig-3-3.jpg'],
    '2019-summer-as-01-q3ci': ['img/2019-summer-as-01/fig-3-4.jpg', 'img/2019-summer-as-01/ms-3ci-flowchart.jpg'],
    '2019-summer-as-01-q3cii': ['img/2019-summer-as-01/fig-3-5.jpg'],
    '2019-summer-as-01-q4ai': ['img/2019-summer-as-01/fig-4-1.jpg'],
    '2019-summer-as-01-q4aii': ['img/2019-summer-as-01/fig-4-2.jpg', 'img/2019-summer-as-01/ms-4aii-circuit.jpg'],
    '2019-summer-as-01-q4b': ['img/2019-summer-as-01/fig-4-1.jpg'],
    '2019-summer-as-01-q4ci': ['img/2019-summer-as-01/fig-4-1.jpg'],
    '2019-summer-as-01-q4cii': ['img/2019-summer-as-01/fig-4-3.jpg', 'img/2019-summer-as-01/fig-4-4.jpg', 'img/2019-summer-as-01/ms-4cii-propeller.jpg'],
    '2019-summer-as-01-q5a': [],
    '2019-summer-as-01-q5b': [],
}

for q in db['questions']:
    if q['id'] in as_fig_map:
        q['figures'] = as_fig_map[q['id']]

with open(os.path.join(repo, 'questions.json'), 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("Successfully refactored 2019-summer-as-01 crops and question linkages!")
