import fitz, os

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

# 2. MS exemplar sketches (MS is landscape 842 x 595)
ms_exemplars = {
    'ms-3ci-flowchart.jpg': (13, fitz.Rect(160, 100, 420, 390)),
    'ms-4aii-circuit.jpg': (14, fitz.Rect(180, 520, 490, 860)), # wait check height
    'ms-4cii-propeller.jpg': (19, fitz.Rect(70, 100, 600, 530)),
}

# Crop page 14 flowchart
pix_fc = ms[13].get_pixmap(matrix=fitz.Matrix(2, 2), clip=fitz.Rect(160, 100, 420, 390))
pix_fc.save(os.path.join(out_dir, 'ms-3ci-flowchart.jpg'))

# Crop page 15 circuit
pix_circ = ms[14].get_pixmap(matrix=fitz.Matrix(2, 2), clip=fitz.Rect(170, 520, 490, 860)) # wait ms is 842 wide, 595 high
pix_circ_real = ms[14].get_pixmap(matrix=fitz.Matrix(2, 2), clip=fitz.Rect(175, 520, 495, 590)) # let's check rect
# Crop page 20 propeller
pix_prop = ms[19].get_pixmap(matrix=fitz.Matrix(2, 2), clip=fitz.Rect(70, 95, 600, 530))
pix_prop.save(os.path.join(out_dir, 'ms-4cii-propeller.jpg'))

print('Cropped figures and exemplars for H004/01!')
