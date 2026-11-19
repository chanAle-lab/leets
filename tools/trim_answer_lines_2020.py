"""
Trim student answer lines and blank calculation boxes for 2020-autumn-01.
Leaves 1 or 2 answer lines and the mark indicator [X].
"""
import os
import fitz
from PIL import Image

qp_path = r'C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded\media_1795097357720_416191c3.pdf'
repo = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets'
out_dir = os.path.join(repo, 'img', '2020-autumn-01')

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

print("Trimming answer lines for 2020-autumn-01:")

# 1ai: Keep compact
pix = qp[1].get_pixmap(matrix=mat, clip=fitz.Rect(45, 60, 555, 455))
pix.save(os.path.join(out_dir, 'q1ai.jpg'))
print(f"  q1ai.jpg: {pix.width}x{pix.height}")

# 1aii: Trim 8 lines to 1 line per subpart + [4]
crop_and_stitch([
    (1, fitz.Rect(45, 455, 555, 580)),
    (1, fitz.Rect(45, 615, 555, 715))
], 'q1aii.jpg')

# 1bi: Trim 4 lines to 1 line + [2]
crop_and_stitch([
    (3, fitz.Rect(45, 60, 555, 155)),
    (3, fitz.Rect(45, 195, 555, 230))
], 'q1bi.jpg')

# 1bii: Trim calculation box to prompt + answer line + [2]
crop_and_stitch([
    (3, fitz.Rect(45, 235, 555, 275)),
    (3, fitz.Rect(45, 345, 555, 395))
], 'q1bii.jpg')

# 1biii: Trim calculation box to prompt + answer line + [4]
crop_and_stitch([
    (3, fitz.Rect(45, 395, 555, 520)),
    (3, fitz.Rect(45, 740, 555, 780))
], 'q1biii.jpg')

# 1biv: Trim 6 lines to 1 line per subpart + [4]
crop_and_stitch([
    (4, fitz.Rect(45, 60, 555, 225)),
    (4, fitz.Rect(45, 285, 555, 430))
], 'q1biv.jpg')

# 1bv: Trim giant 550pt box to prompt + answer line + [4]
crop_and_stitch([
    (5, fitz.Rect(45, 60, 555, 205)),
    (5, fitz.Rect(45, 730, 555, 775))
], 'q1bv.jpg')

# 1bvi: Trim 18 lines to 2 lines + [6]
crop_and_stitch([
    (6, fitz.Rect(45, 60, 555, 225)),
    (6, fitz.Rect(45, 620, 555, 655))
], 'q1bvi.jpg')

# 2a: Trim calculation box to prompt + answer line + [3]
crop_and_stitch([
    (8, fitz.Rect(45, 475, 555, 585)),
    (8, fitz.Rect(45, 745, 555, 780))
], 'q2a.jpg')

# 2bi: Trim calculation box to prompt + answer line + [2]
crop_and_stitch([
    (9, fitz.Rect(45, 355, 555, 445)),
    (9, fitz.Rect(45, 610, 555, 645))
], 'q2bi.jpg')

# 2bii: Trim calculation box to prompt + answer line + [4]
crop_and_stitch([
    (10, fitz.Rect(45, 270, 555, 385)),
    (10, fitz.Rect(45, 740, 555, 775))
], 'q2bii.jpg')

# 2biii: Trim 4 lines to 1 line + [2]
crop_and_stitch([
    (11, fitz.Rect(45, 60, 555, 155)),
    (11, fitz.Rect(45, 210, 555, 245))
], 'q2biii.jpg')

# 2biv: Trim multi-section response lines to 1 line per section + [5]
crop_and_stitch([
    (11, fitz.Rect(45, 240, 555, 365)),
    (11, fitz.Rect(45, 420, 555, 545))
], 'q2biv.jpg')

# 3a: Trim 6 lines to 1 line per subpart + [4]
crop_and_stitch([
    (12, fitz.Rect(45, 60, 555, 205)),
    (12, fitz.Rect(45, 250, 555, 375))
], 'q3a.jpg')

# 3b: Trim 24 lines to 2 lines + [8]
crop_and_stitch([
    (13, fitz.Rect(45, 60, 555, 145)),
    (13, fitz.Rect(45, 680, 555, 715))
], 'q3b.jpg')

# 4ai: Trim calculation box to prompt + answer line + [2]
crop_and_stitch([
    (16, fitz.Rect(45, 255, 555, 335)),
    (16, fitz.Rect(45, 485, 555, 520))
], 'q4ai.jpg')

# 4aii: Trim calculation box to prompt + answer line + [2]
crop_and_stitch([
    (16, fitz.Rect(45, 520, 555, 570)),
    (16, fitz.Rect(45, 740, 555, 775))
], 'q4aii.jpg')

# 4bi: Trim calculation box to prompt + formula + answer line + [4]
crop_and_stitch([
    (17, fitz.Rect(45, 60, 555, 355)),
    (17, fitz.Rect(45, 745, 555, 780))
], 'q4bi.jpg')

# 4bii: Trim calculation box to prompt + answer line + [3]
crop_and_stitch([
    (18, fitz.Rect(45, 260, 555, 355)),
    (18, fitz.Rect(45, 680, 555, 715))
], 'q4bii.jpg')

# 4biii: Already compact
pix = qp[18].get_pixmap(matrix=mat, clip=fitz.Rect(45, 715, 555, 775))
pix.save(os.path.join(out_dir, 'q4biii.jpg'))
print(f"  q4biii.jpg: {pix.width}x{pix.height}")

# 4c: Trim 16 lines to 2 lines + [6]
crop_and_stitch([
    (20, fitz.Rect(45, 60, 555, 220)),
    (20, fitz.Rect(45, 635, 555, 670))
], 'q4c.jpg')

# 4di: Already compact
pix = qp[21].get_pixmap(matrix=mat, clip=fitz.Rect(45, 60, 555, 145))
pix.save(os.path.join(out_dir, 'q4di.jpg'))
print(f"  q4di.jpg: {pix.width}x{pix.height}")

# 4dii: Trim 6 lines to 2 lines + [4]
crop_and_stitch([
    (21, fitz.Rect(45, 145, 555, 260)),
    (21, fitz.Rect(45, 380, 555, 415))
], 'q4dii.jpg')

print("Finished trimming 2020-autumn-01 answer lines!")
