"""
Trim answer lines and calculation boxes for 2019-summer-as-01.
Leaves 1 or 2 answer lines and the mark indicator [X].
"""
import os
import fitz
from PIL import Image

qp_path = r'C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded\media_1795090284268_4e11c92e.pdf'
repo = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets'
out_dir = os.path.join(repo, 'img', '2019-summer-as-01')

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

print("Trimming answer lines for 2019-summer-as-01:")

# q1cii: Calculate drum speed... Drum speed ....... rev / min [4]
crop_and_stitch([
    (3, fitz.Rect(45, 260, 555, 330)),
    (3, fitz.Rect(45, 510, 555, 560))
], 'q1cii.jpg')

# q1dii: Manufactured in batch of 5000... 20 lines -> prompt + 2 lines + [6]
crop_and_stitch([
    (5, fitz.Rect(45, 55, 555, 210)),
    (5, fitz.Rect(45, 745, 555, 780))
], 'q1dii.jpg')

# q2ai: Convert 150kg to N... [2]
crop_and_stitch([
    (6, fitz.Rect(45, 490, 555, 545)),
    (6, fitz.Rect(45, 640, 555, 690))
], 'q2ai.jpg')

# q2aii: Calculate shaded cross-sectional area... [2]
crop_and_stitch([
    (7, fitz.Rect(45, 55, 555, 140)),
    (7, fitz.Rect(45, 315, 555, 365))
], 'q2aii.jpg')

# q2aiii: Calculate stress in seat post... [3]
crop_and_stitch([
    (7, fitz.Rect(45, 365, 555, 440)),
    (7, fitz.Rect(45, 680, 555, 730))
], 'q2aiii.jpg')

# q2b: Young's Modulus... [5]
crop_and_stitch([
    (8, fitz.Rect(45, 55, 555, 145)),
    (8, fitz.Rect(45, 440, 555, 490))
], 'q2b.jpg')

# q2c: Bicycle hire cost... [3]
crop_and_stitch([
    (8, fitz.Rect(45, 490, 555, 600)),
    (8, fitz.Rect(45, 700, 555, 755))
], 'q2c.jpg')

# q3a: Calculate length x... [3]
crop_and_stitch([
    (9, fitz.Rect(45, 525, 555, 585)),
    (9, fitz.Rect(45, 730, 555, 785))
], 'q3a.jpg')

# q3b: Describe how circuit operates... 18 lines -> 2 lines + [6]
crop_and_stitch([
    (10, fitz.Rect(45, 370, 555, 480)),
    (10, fitz.Rect(45, 745, 555, 785))
], 'q3b.jpg')

# q4b: Discuss ethical and environmental issues... 22 lines -> 2 lines + [9]
crop_and_stitch([
    (15, fitz.Rect(45, 55, 555, 175)),
    (15, fitz.Rect(45, 605, 555, 645))
], 'q4b.jpg')

# q5a: Risk assessments... 10 lines -> 2 lines + [4]
crop_and_stitch([
    (19, fitz.Rect(45, 55, 555, 170)),
    (19, fitz.Rect(45, 380, 555, 420))
], 'q5a.jpg')

# q5b: Legislation... 10 lines -> 2 lines + [4]
crop_and_stitch([
    (19, fitz.Rect(45, 420, 555, 535)),
    (19, fitz.Rect(45, 745, 555, 785))
], 'q5b.jpg')

print("Finished trimming 2019-summer-as-01 answer lines!")
