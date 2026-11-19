import fitz
import os
from PIL import Image

qp_path = r'C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded\media_1795092837972_f98c422c.pdf'
rb_path = r'C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded\media_1795092838032_29b29c24.pdf'
ms_path = r'C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded\media_1795092838018_53235c2c.pdf'
out_dir = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets\img\2019-summer-02'
os.makedirs(out_dir, exist_ok=True)

qp = fitz.open(qp_path)
rb = fitz.open(rb_path)
ms = fitz.open(ms_path)
mat = fitz.Matrix(2.0, 2.0)

print("--- 1. Cropping Figures from Resource Booklet ---")
figures = [
    # (page_idx, rect, filename)
    (1, fitz.Rect(250, 140, 550, 350), 'fig-1.jpg'),
    (2, fitz.Rect(45, 450, 550, 565), 'fig-2.jpg'),
    (3, fitz.Rect(180, 175, 420, 415), 'fig-3.jpg'),
    (4, fitz.Rect(130, 180, 470, 380), 'fig-4.jpg'),
    (4, fitz.Rect(130, 440, 550, 670), 'fig-5.jpg'),
    (5, fitz.Rect(45, 100, 550, 520), 'fig-6.jpg'),
    (6, fitz.Rect(80, 100, 520, 260), 'fig-7.jpg'),
    (6, fitz.Rect(45, 430, 550, 585), 'fig-8.jpg'),
    (6, fitz.Rect(45, 630, 550, 775), 'fig-9.jpg'),
    (7, fitz.Rect(45, 70, 550, 280), 'fig-10.jpg'),
    (7, fitz.Rect(45, 290, 550, 530), 'fig-11.jpg')
]

for pno, rect, fname in figures:
    pix = rb[pno].get_pixmap(clip=rect, matrix=mat)
    pix.save(os.path.join(out_dir, fname))
    print(f"  Cropped {fname} ({pix.width}x{pix.height})")

print("--- 2. Cropping Exemplar Diagrams from Mark Scheme ---")
# Flowcode & Code
pix_fc = ms[16].get_pixmap(clip=fitz.Rect(40, 50, 780, 440), matrix=mat)
pix_fc.save(os.path.join(out_dir, 'ms-5-flowcode.jpg'))
print(f"  Cropped ms-5-flowcode.jpg ({pix_fc.width}x{pix_fc.height})")

# Gear train schematic
pix_gt = ms[16].get_pixmap(clip=fitz.Rect(40, 330, 420, 550), matrix=mat)
pix_gt.save(os.path.join(out_dir, 'ms-5-gear-train.jpg'))
print(f"  Cropped ms-5-gear-train.jpg ({pix_gt.width}x{pix_gt.height})")

print("--- 3. Cropping Question Prompts from Question Paper ---")
q_crops = [
    # Q1: page 2, y from 130 to 255
    (1, fitz.Rect(40, 130, 555, 255), 'q1.jpg'),
    # Q2: page 4, y from 60 to 235
    (3, fitz.Rect(40, 60, 555, 235), 'q2.jpg'),
    # Q3: page 5, y from 60 to 525
    (4, fitz.Rect(40, 60, 555, 525), 'q3.jpg'),
    # Q4: page 6, y from 60 to 195
    (5, fitz.Rect(40, 60, 555, 195), 'q4.jpg'),
    # Q5: page 8, y from 60 to 480
    (7, fitz.Rect(40, 60, 555, 480), 'q5.jpg'),
    # Q6: page 12, y from 60 to 235
    (11, fitz.Rect(40, 60, 555, 235), 'q6.jpg')
]

for pno, rect, fname in q_crops:
    pix = qp[pno].get_pixmap(clip=rect, matrix=mat)
    pix.save(os.path.join(out_dir, fname))
    print(f"  Cropped {fname} ({pix.width}x{pix.height})")

print("--- 4. Cropping & Stitching Mark Schemes ---")
def stitch_ms(pages_rects, fname):
    imgs = []
    for pno, rect in pages_rects:
        pix = ms[pno].get_pixmap(clip=rect, matrix=mat)
        tmp = os.path.join(out_dir, f'_tmp_{pno}.png')
        pix.save(tmp)
        imgs.append(Image.open(tmp))
    
    total_w = max(im.width for im in imgs)
    total_h = sum(im.height for im in imgs)
    combined = Image.new('RGB', (total_w, total_h), (255, 255, 255))
    curr_y = 0
    for im in imgs:
        combined.paste(im, (0, curr_y))
        curr_y += im.height
    
    out_path = os.path.join(out_dir, fname)
    combined.save(out_path, quality=92)
    # clean tmp
    for pno, _ in pages_rects:
        tmp = os.path.join(out_dir, f'_tmp_{pno}.png')
        if os.path.exists(tmp): os.remove(tmp)
    print(f"  Stitched {fname} ({total_w}x{total_h})")

# MS-1: Pages 5 & 6 (index 4 & 5)
stitch_ms([(4, fitz.Rect(40, 120, 800, 550)), (5, fitz.Rect(40, 60, 800, 530))], 'ms-1.jpg')

# MS-2: Pages 8 & 9 (index 7 & 8)
stitch_ms([(7, fitz.Rect(40, 75, 800, 550)), (8, fitz.Rect(40, 60, 800, 430))], 'ms-2.jpg')

# MS-3: Page 10 (index 9)
stitch_ms([(9, fitz.Rect(40, 75, 800, 550))], 'ms-3.jpg')

# MS-4: Pages 11 & 12 (index 10 & 11)
stitch_ms([(10, fitz.Rect(40, 75, 800, 550)), (11, fitz.Rect(40, 60, 800, 530))], 'ms-4.jpg')

# MS-5: Pages 14 & 15 & 17 (index 13, 14, 16)
stitch_ms([(13, fitz.Rect(40, 75, 800, 550)), (14, fitz.Rect(40, 60, 800, 530)), (16, fitz.Rect(40, 50, 800, 550))], 'ms-5.jpg')

# MS-6: Pages 18 & 19 (index 17 & 18)
stitch_ms([(17, fitz.Rect(40, 120, 800, 550)), (18, fitz.Rect(40, 60, 800, 530))], 'ms-6.jpg')

print("All crops and mark schemes completed successfully!")
