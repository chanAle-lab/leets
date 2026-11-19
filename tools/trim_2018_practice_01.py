"""
Trim answer lines and calculation boxes for 2018-practice-01.
Leaves 1 or 2 answer lines and the mark indicator [X].
"""
import os
import fitz
from PIL import Image

qp_path = r'C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded\media_1795086229085_87988b59.pdf'
repo = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets'
out_dir = os.path.join(repo, 'img', '2018-practice-01')

qp = fitz.open(qp_path)
mat = fitz.Matrix(2.2, 2.2)

def crop_and_stitch(parts, filename):
    imgs = []
    for pno, rect in parts:
        pix = qp[pno].get_pixmap(matrix=mat, clip=rect)
        imgs.append(Image.frombytes('RGB', [pix.width, pix.height], pix.samples))
    w = max(im.width for im in imgs)
    h = sum(im.height for im in imgs)
    dst = Image.new('RGB', (w, h), (255, 255, 255))
    y = 0
    for im in imgs:
        dst.paste(im, (0, y))
        y += im.height
    dst.save(os.path.join(out_dir, filename), quality=95)
    print(f"  {filename}: {w}x{h}")

print("Trimming answer lines for 2018-practice-01:")

# q1ci: Discuss possible limitations... 16 lines -> 2 lines + [6]
crop_and_stitch([
    (2, fitz.Rect(45, 385, 555, 480)),
    (2, fitz.Rect(45, 745, 555, 785))
], 'q1ci.jpg')

# q2b: Calculate distance S... [4]
crop_and_stitch([
    (7, fitz.Rect(45, 360, 555, 450)),
    (7, fitz.Rect(45, 745, 555, 785))
], 'q2b.jpg')

# q2cii: Calculate cross sectional area of wire... [3]
crop_and_stitch([
    (9, fitz.Rect(45, 55, 555, 175)),
    (9, fitz.Rect(45, 300, 555, 345))
], 'q2cii.jpg')

# q2ciii: Calculate extension... [3]
crop_and_stitch([
    (9, fitz.Rect(45, 345, 555, 435)),
    (9, fitz.Rect(45, 540, 555, 580))
], 'q2ciii.jpg')

# q2di: Calculate mean body mass... [3]
crop_and_stitch([
    (10, fitz.Rect(45, 300, 555, 410)),
    (10, fitz.Rect(45, 580, 555, 620))
], 'q2di.jpg')

# q3b: Discuss lifecycle assessment... 25 lines -> 2 lines + [8]
crop_and_stitch([
    (12, fitz.Rect(45, 55, 555, 210)),
    (12, fitz.Rect(45, 745, 555, 785))
], 'q3b.jpg')

# q4c: Discuss DC motor vs stepper... 8 lines -> 2 lines + [4]
crop_and_stitch([
    (15, fitz.Rect(45, 550, 555, 650)),
    (15, fitz.Rect(45, 745, 555, 785))
], 'q4c.jpg')

# q4d: Destructive and non-destructive testing... 25 lines -> 2 lines + [8]
crop_and_stitch([
    (16, fitz.Rect(45, 55, 555, 160)),
    (16, fitz.Rect(45, 745, 555, 785))
], 'q4d.jpg')

print("Finished trimming 2018-practice-01 answer lines!")
