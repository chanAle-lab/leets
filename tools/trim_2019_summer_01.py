"""
Trim answer lines and calculation boxes for 2019-summer-01.
Leaves 1 or 2 answer lines and the mark indicator [X].
"""
import os
import fitz
from PIL import Image

qp_path = r'C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded\media_1795090284300_97db84a6.pdf'
repo = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets'
out_dir = os.path.join(repo, 'img', '2019-summer-01')

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

print("Trimming answer lines for 2019-summer-01:")

# q1bi: Calculate time... Time ....... s [3]
crop_and_stitch([
    (2, fitz.Rect(45, 305, 555, 370)),
    (2, fitz.Rect(45, 495, 555, 535))
], 'q1bi.jpg')

# q1bii: Calculate motor rotational speed... Motor rotational speed ....... rpm [3]
crop_and_stitch([
    (2, fitz.Rect(45, 535, 555, 600)),
    (2, fitz.Rect(45, 735, 555, 780))
], 'q1bii.jpg')

# q1biv: Calculate power... Power ....... W [4]
crop_and_stitch([
    (3, fitz.Rect(45, 190, 555, 300)),
    (3, fitz.Rect(45, 465, 555, 515))
], 'q1biv.jpg')

# q1c: 20 dotted lines -> prompt + 2 lines + [9]
crop_and_stitch([
    (4, fitz.Rect(45, 55, 555, 195)),
    (4, fitz.Rect(45, 745, 555, 785))
], 'q1c.jpg')

# q2a: Calculate maximum straight part length... Maximum straight part length ....... mm [3]
crop_and_stitch([
    (5, fitz.Rect(45, 238, 555, 310)),
    (5, fitz.Rect(45, 585, 555, 630))
], 'q2a.jpg')

# q2bii: Calculate mass... Mass ....... g [5]
crop_and_stitch([
    (6, fitz.Rect(45, 305, 555, 420)),
    (6, fitz.Rect(45, 735, 555, 780))
], 'q2bii.jpg')

# q2biii: Calculate volume... Volume ....... mm3 [2]
crop_and_stitch([
    (7, fitz.Rect(45, 55, 555, 140)),
    (7, fitz.Rect(45, 320, 555, 365))
], 'q2biii.jpg')

# q2biv: Calculate minimum allowable diameter... Minimum diameter ....... mm [2]
crop_and_stitch([
    (7, fitz.Rect(45, 365, 555, 425)),
    (7, fitz.Rect(45, 490, 555, 535))
], 'q2biv.jpg')

# q2c: Tennis machine... Initial velocity ....... m s-1 [2]
crop_and_stitch([
    (8, fitz.Rect(45, 55, 555, 180)),
    (8, fitz.Rect(45, 400, 555, 445))
], 'q2c.jpg')

# q3a: 20 dotted lines -> prompt + 2 lines + [9]
crop_and_stitch([
    (9, fitz.Rect(45, 235, 555, 350)),
    (9, fitz.Rect(45, 745, 555, 790))
], 'q3a.jpg')

# q4a: Hover mower casing... 4 lines -> 1 line + [3]
crop_and_stitch([
    (11, fitz.Rect(45, 350, 555, 445)),
    (11, fitz.Rect(45, 515, 555, 550))
], 'q4a.jpg')

# q4c: DC motors vs stepper motors... 8 lines -> 2 lines + [4]
crop_and_stitch([
    (13, fitz.Rect(45, 240, 555, 345)),
    (13, fitz.Rect(45, 445, 555, 490))
], 'q4c.jpg')

# q4ei: Calculate voltage... Voltage ....... V [3]
crop_and_stitch([
    (15, fitz.Rect(45, 380, 555, 450)),
    (15, fitz.Rect(45, 745, 555, 795))
], 'q4ei.jpg')

# q4eii: Calculate ADC value... ADC value ....... [3]
crop_and_stitch([
    (16, fitz.Rect(45, 55, 555, 165)),
    (16, fitz.Rect(45, 585, 555, 630))
], 'q4eii.jpg')

print("Finished trimming 2019-summer-01 answer lines!")
