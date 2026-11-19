import fitz, os

qp_path = r'C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded\media_1795090284300_97db84a6.pdf'
ms_path = r'C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded\media_1795090284321_d63b0743.pdf'

qp = fitz.open(qp_path)
ms = fitz.open(ms_path)
out_dir = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets\img\2019-summer-01'
os.makedirs(out_dir, exist_ok=True)

# Question crops
q_specs = {
    'q1a.jpg': (1, fitz.Rect(45, 80, 555, 630)),
    'q1bi.jpg': (2, fitz.Rect(45, 55, 555, 535)),
    'q1bii.jpg': (2, fitz.Rect(45, 535, 555, 785)),
    'q1biii.jpg': (3, fitz.Rect(45, 55, 555, 235)),
    'q1biv.jpg': (3, fitz.Rect(45, 230, 555, 610)),
    'q1bv.jpg': (3, fitz.Rect(45, 600, 555, 790)),
    'q1c.jpg': (4, fitz.Rect(45, 55, 555, 790)),
    'q2a.jpg': (5, fitz.Rect(45, 55, 555, 635)),
    'q2bi.jpg': (6, fitz.Rect(45, 55, 555, 305)),
    'q2bii.jpg': (6, fitz.Rect(45, 300, 555, 785)),
    'q2biii.jpg': (7, fitz.Rect(45, 55, 555, 435)),
    'q2biv.jpg': (7, fitz.Rect(45, 430, 555, 640)),
    'q2c.jpg': (8, fitz.Rect(45, 55, 555, 535)),
    'q3a.jpg': (9, fitz.Rect(45, 55, 555, 790)),
    'q3bi.jpg': (10, fitz.Rect(45, 55, 555, 260)),
    'q3bii.jpg': (10, fitz.Rect(45, 255, 555, 530)),
    'q4a.jpg': (11, fitz.Rect(45, 55, 555, 550)),
    'q4bi.jpg': (12, fitz.Rect(45, 55, 555, 540)),
    'q4bii.jpg': (12, fitz.Rect(45, 535, 555, 760)),
    'q4biii.jpg': (13, fitz.Rect(45, 55, 555, 290)),
    'q4c.jpg': (13, fitz.Rect(45, 280, 555, 680)),
    'q4d.jpg': (14, fitz.Rect(45, 55, 555, 685)),
    'q4ei.jpg': (15, fitz.Rect(45, 55, 555, 795)),
    'q4eii.jpg': (16, fitz.Rect(45, 55, 555, 755)),
    'q4eiii.jpg': (17, fitz.Rect(45, 55, 555, 645)),
}

for name, (pno, rect) in q_specs.items():
    pix = qp[pno].get_pixmap(matrix=fitz.Matrix(2, 2), clip=rect)
    pix.save(os.path.join(out_dir, name))

# Mark scheme crops (MS is landscape 842 x 595 pt)
ms_specs = {
    'ms-1a.jpg': (4, fitz.Rect(40, 60, 800, 290)),
    'ms-1bi.jpg': (4, fitz.Rect(40, 285, 800, 480)),
    'ms-1bii.jpg': (5, fitz.Rect(40, 60, 800, 490)),
    'ms-1biii.jpg': (5, fitz.Rect(40, 480, 800, 575)),
    'ms-1biv.jpg': (6, fitz.Rect(40, 110, 800, 560)),
    'ms-1bv.jpg': (7, fitz.Rect(40, 160, 800, 565)),
    'ms-1c.jpg': (8, fitz.Rect(40, 120, 800, 565)),
    'ms-2a.jpg': (10, fitz.Rect(40, 95, 800, 400)),
    'ms-2bi.jpg': (10, fitz.Rect(40, 395, 800, 565)),
    'ms-2bii.jpg': (11, fitz.Rect(40, 80, 800, 520)),
    'ms-2biii.jpg': (12, fitz.Rect(40, 80, 800, 480)),
    'ms-2biv.jpg': (13, fitz.Rect(40, 80, 800, 395)),
    'ms-2c.jpg': (13, fitz.Rect(40, 390, 800, 560)),
    'ms-3a.jpg': (15, fitz.Rect(40, 80, 800, 565)),
    'ms-3bi.jpg': (16, fitz.Rect(40, 310, 800, 565)),
    'ms-3bii.jpg': (17, fitz.Rect(40, 80, 800, 450)),
    'ms-4a.jpg': (18, fitz.Rect(40, 80, 800, 260)),
    'ms-4bi.jpg': (18, fitz.Rect(40, 255, 800, 415)),
    'ms-4bii.jpg': (18, fitz.Rect(40, 410, 800, 565)),
    'ms-4biii.jpg': (19, fitz.Rect(40, 80, 800, 250)),
    'ms-4c.jpg': (19, fitz.Rect(40, 245, 800, 565)),
    'ms-4d.jpg': (20, fitz.Rect(40, 80, 800, 565)),
    'ms-4ei.jpg': (21, fitz.Rect(40, 100, 800, 470)),
    'ms-4eii.jpg': (22, fitz.Rect(40, 100, 800, 520)),
    'ms-4eiii.jpg': (23, fitz.Rect(40, 100, 800, 550)),
}

for name, (pno, rect) in ms_specs.items():
    pix = ms[pno].get_pixmap(matrix=fitz.Matrix(2, 2), clip=rect)
    pix.save(os.path.join(out_dir, name))

print('Finished cropping all questions and mark schemes!')
