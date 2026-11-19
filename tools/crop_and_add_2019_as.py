import fitz, os, json

qp_path = r'C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded\media_1795090284268_4e11c92e.pdf'
ms_path = r'C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded\media_1795090284295_465aaf3c.pdf'

qp = fitz.open(qp_path)
ms = fitz.open(ms_path)
out_dir = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets\img\2019-summer-as-01'
os.makedirs(out_dir, exist_ok=True)

# 1. Figures
figures = {
    'fig-1-1.jpg': (1, fitz.Rect(180, 130, 420, 360)),
    'fig-1-2.jpg': (2, fitz.Rect(170, 130, 440, 340)),
    'fig-1-3.jpg': (3, fitz.Rect(170, 90, 440, 270)),
    'fig-1-4.jpg': (4, fitz.Rect(180, 100, 420, 320)),
    'fig-2-1.jpg': (6, fitz.Rect(150, 100, 460, 330)),
    'fig-2-2.jpg': (6, fitz.Rect(200, 430, 410, 560)),
    'fig-3-1.jpg': (9, fitz.Rect(120, 100, 490, 305)),
    'fig-3-2.jpg': (9, fitz.Rect(150, 350, 450, 600)),
    'fig-3-3.jpg': (10, fitz.Rect(80, 110, 520, 410)),
    'fig-3-4.jpg': (11, fitz.Rect(100, 110, 500, 320)),
    'fig-3-5.jpg': (12, fitz.Rect(100, 130, 520, 380)),
    'fig-4-1.jpg': (13, fitz.Rect(140, 110, 470, 370)),
    'fig-4-2.jpg': (14, fitz.Rect(100, 110, 500, 280)),
    'fig-4-3.jpg': (17, fitz.Rect(70, 140, 520, 290)),
    'fig-4-4.jpg': (17, fitz.Rect(70, 330, 530, 540)),
}

for name, (pno, rect) in figures.items():
    pix = qp[pno].get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=rect)
    pix.save(os.path.join(out_dir, name))

# Exemplar diagrams from MS
pix_fc = ms[13].get_pixmap(matrix=fitz.Matrix(2, 2), clip=fitz.Rect(160, 100, 420, 390))
pix_fc.save(os.path.join(out_dir, 'ms-3ci-flowchart.jpg'))

img_data = ms.extract_image(67)
with open(os.path.join(out_dir, 'ms-4aii-circuit.jpg'), 'wb') as f:
    f.write(img_data['image'])

pix_prop = ms[19].get_pixmap(matrix=fitz.Matrix(2, 2), clip=fitz.Rect(70, 95, 600, 530))
pix_prop.save(os.path.join(out_dir, 'ms-4cii-propeller.jpg'))

# 2. Question crops
q_crops = {
    'q1a.jpg': (1, fitz.Rect(45, 80, 555, 600)),
    'q1bi.jpg': (1, fitz.Rect(45, 590, 555, 700)),
    'q1bii.jpg': (1, fitz.Rect(45, 695, 555, 800)),
    'q1ci.jpg': (2, fitz.Rect(45, 60, 555, 600)),
    'q1cii.jpg': (3, fitz.Rect(45, 60, 555, 660)),
    'q1di.jpg': (4, fitz.Rect(45, 60, 555, 670)),
    'q1dii.jpg': (5, fitz.Rect(45, 60, 555, 790)),
    'q2ai.jpg': (6, fitz.Rect(45, 60, 555, 790)),
    'q2aii.jpg': (7, fitz.Rect(45, 60, 555, 430)),
    'q2aiii.jpg': (7, fitz.Rect(45, 425, 555, 790)),
    'q2b.jpg': (8, fitz.Rect(45, 60, 555, 570)),
    'q2c.jpg': (8, fitz.Rect(45, 565, 555, 790)),
    'q3a.jpg': (9, fitz.Rect(45, 60, 555, 790)),
    'q3b.jpg': (10, fitz.Rect(45, 60, 555, 790)),
    'q3ci.jpg': (11, fitz.Rect(45, 60, 555, 790)),
    'q3cii.jpg': (12, fitz.Rect(45, 60, 555, 730)),
    'q4ai.jpg': (13, fitz.Rect(45, 60, 555, 640)),
    'q4aii.jpg': (14, fitz.Rect(45, 60, 555, 790)),
    'q4b.jpg': (15, fitz.Rect(45, 60, 555, 790)),
    'q4ci.jpg': (16, fitz.Rect(45, 60, 555, 340)),
    'q4cii.jpg': (17, fitz.Rect(45, 60, 555, 790)),
    'q5a.jpg': (19, fitz.Rect(45, 60, 555, 790)),
    'q5b.jpg': (20, fitz.Rect(45, 60, 555, 410)),
}

for name, (pno, rect) in q_crops.items():
    pix = qp[pno].get_pixmap(matrix=fitz.Matrix(2, 2), clip=rect)
    pix.save(os.path.join(out_dir, name))

# 3. Mark scheme crops
ms_crops = {
    'ms-1a.jpg': (3, fitz.Rect(40, 60, 800, 270)),
    'ms-1bi.jpg': (3, fitz.Rect(40, 265, 800, 440)),
    'ms-1bii.jpg': (3, fitz.Rect(40, 435, 800, 565)),
    'ms-1ci.jpg': (4, fitz.Rect(40, 60, 800, 350)),
    'ms-1cii.jpg': (4, fitz.Rect(40, 345, 800, 565)),
    'ms-1di.jpg': (5, fitz.Rect(40, 260, 800, 565)),
    'ms-1dii.jpg': (6, fitz.Rect(40, 80, 800, 565)),
    'ms-2ai.jpg': (8, fitz.Rect(40, 70, 800, 240)),
    'ms-2aii.jpg': (8, fitz.Rect(40, 235, 800, 400)),
    'ms-2aiii.jpg': (8, fitz.Rect(40, 395, 800, 565)),
    'ms-2b.jpg': (9, fitz.Rect(40, 80, 800, 500)),
    'ms-2c.jpg': (10, fitz.Rect(40, 70, 800, 350)),
    'ms-3a.jpg': (11, fitz.Rect(40, 70, 800, 380)),
    'ms-3b.jpg': (12, fitz.Rect(40, 70, 800, 350)),
    'ms-3ci.jpg': (12, fitz.Rect(40, 345, 800, 565)),
    'ms-3cii.jpg': (13, fitz.Rect(40, 210, 800, 450)),
    'ms-4ai.jpg': (14, fitz.Rect(40, 70, 800, 270)),
    'ms-4aii.jpg': (14, fitz.Rect(40, 265, 800, 565)),
    'ms-4b.jpg': (16, fitz.Rect(40, 70, 800, 565)),
    'ms-4ci.jpg': (17, fitz.Rect(40, 220, 800, 460)),
    'ms-4cii.jpg': (17, fitz.Rect(40, 455, 800, 565)),
    'ms-5a.jpg': (20, fitz.Rect(40, 70, 800, 565)),
    'ms-5b.jpg': (21, fitz.Rect(40, 240, 800, 565)),
}

for name, (pno, rect) in ms_crops.items():
    pix = ms[pno].get_pixmap(matrix=fitz.Matrix(2, 2), clip=rect)
    pix.save(os.path.join(out_dir, name))

print('Finished cropping all H004/01 assets!')
