"""
Comprehensive fix for all question images that are missing question prompt text,
starting with dotted lines, or blank.
Also repairs truncated summaries in questions.json.
"""

import os, json, fitz
from PIL import Image

REPO = r"C:\Users\Alexander\.gemini\antigravity\scratch\leets"
UP = r"C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded"

ZOOM = 2.0
mat = fitz.Matrix(ZOOM, ZOOM)

def crop_box(doc, pno, y0, y1, x0=45, x1=555):
    pix = doc[pno].get_pixmap(matrix=mat, clip=fitz.Rect(x0, y0, x1, y1))
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

def stitch(parts, out_path, quality=92):
    w = max(im.width for im in parts)
    h = sum(im.height for im in parts)
    dst = Image.new("RGB", (w, h), (255, 255, 255))
    y = 0
    for im in parts:
        dst.paste(im, (0, y))
        y += im.height
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    dst.save(out_path, quality=quality)
    print(f"  [SAVED] {os.path.basename(out_path)}: {w}x{h}")

# =========================================================================
# 1. 2018-practice-01
# =========================================================================
print("\n--- 1. Fixing 2018-practice-01 ---")
doc_18_01 = fitz.open(os.path.join(UP, "media_1795086229085_87988b59.pdf"))
dir_18_01 = os.path.join(REPO, "img", "2018-practice-01")

# 2(d)(i): Page 11 (index 10), prompt y=315 to 355 + percentage [2] (y=440 to 485)
stitch([
    crop_box(doc_18_01, 10, 315, 355),
    crop_box(doc_18_01, 10, 440, 485)
], os.path.join(dir_18_01, "q2di.jpg"))

# 2(d)(ii): Page 11 (index 10), prompt y=490 to 555 + [2] (y=685 to 725)
stitch([
    crop_box(doc_18_01, 10, 490, 555),
    crop_box(doc_18_01, 10, 685, 725)
], os.path.join(dir_18_01, "q2dii.jpg"))

# 4(b)(ii): Page 15 (index 14), prompt y=570 to 630 + rotational speed [2] (y=720 to 765)
stitch([
    crop_box(doc_18_01, 14, 570, 630),
    crop_box(doc_18_01, 14, 720, 765)
], os.path.join(dir_18_01, "q4bii.jpg"))

# 4(c): Page 16 (index 15), prompt y=250 to 325 + 1: y=330 to 365 + 2: y=435 to 545
stitch([
    crop_box(doc_18_01, 15, 250, 325),
    crop_box(doc_18_01, 15, 330, 365),
    crop_box(doc_18_01, 15, 435, 545)
], os.path.join(dir_18_01, "q4c.jpg"))

# =========================================================================
# 2. 2018-practice-02
# =========================================================================
print("\n--- 2. Fixing 2018-practice-02 ---")
doc_18_02 = fitz.open(os.path.join(UP, "media_1795090170010_0babf2b4.pdf"))
dir_18_02 = os.path.join(REPO, "img", "2018-practice-02")

# 3(b): Page 6 (index 5), prompt y=380 to 415 + length of tie [3] (y=585 to 635)
stitch([
    crop_box(doc_18_02, 5, 380, 415),
    crop_box(doc_18_02, 5, 585, 635)
], os.path.join(dir_18_02, "q3b.jpg"))

# =========================================================================
# 3. 2019-summer-01
# =========================================================================
print("\n--- 3. Fixing 2019-summer-01 ---")
doc_19_01 = fitz.open(os.path.join(UP, "media_1795090284300_97db84a6.pdf"))
dir_19_01 = os.path.join(REPO, "img", "2019-summer-01")

# 3(b)(ii): Page 11 (index 10), prompt y=190 to 225 + 1: y=225 to 265 + 2: y=330 to 445 [4]
stitch([
    crop_box(doc_19_01, 10, 190, 225),
    crop_box(doc_19_01, 10, 225, 265),
    crop_box(doc_19_01, 10, 330, 445)
], os.path.join(dir_19_01, "q3bii.jpg"))

# =========================================================================
# 4. 2019-summer-as-01
# =========================================================================
print("\n--- 4. Fixing 2019-summer-as-01 ---")
doc_19_as = fitz.open(os.path.join(UP, "media_1795090284268_4e11c92e.pdf"))
dir_19_as = os.path.join(REPO, "img", "2019-summer-as-01")

# 1(d)(i): Page 5 (index 4), prompt y=280 to 320 + Metal y=320 to 350 + Reason 1 y=350 to 380 + Reason 2 & [5] y=480 to 630
stitch([
    crop_box(doc_19_as, 4, 280, 350),
    crop_box(doc_19_as, 4, 350, 385),
    crop_box(doc_19_as, 4, 480, 630)
], os.path.join(dir_19_as, "q1di.jpg"))

# 5(b): Page 21 (index 20), prompt y=60 to 110 + 1: y=110 to 160 + 2: y=215 to 330 [4]
stitch([
    crop_box(doc_19_as, 20, 60, 110),
    crop_box(doc_19_as, 20, 110, 160),
    crop_box(doc_19_as, 20, 215, 330)
], os.path.join(dir_19_as, "q5b.jpg"))

# =========================================================================
# 5. 2020-autumn-01
# =========================================================================
print("\n--- 5. Fixing 2020-autumn-01 ---")
doc_20_01 = fitz.open(os.path.join(UP, "media_1795097357720_416191c3.pdf"))
dir_20_01 = os.path.join(REPO, "img", "2020-autumn-01")

# 1(b)(iii): Page 4 (index 3), prompt y=380 to 520 + answer line [4] y=740 to 780
stitch([
    crop_box(doc_20_01, 3, 380, 520),
    crop_box(doc_20_01, 3, 740, 780)
], os.path.join(dir_20_01, "q1biii.jpg"))

# =========================================================================
# 6. 2021-autumn-01
# =========================================================================
print("\n--- 6. Fixing 2021-autumn-01 ---")
doc_21_01 = fitz.open(os.path.join(UP, "media_1795105746534_6931e352.pdf"))
dir_21_01 = os.path.join(REPO, "img", "2021-autumn-01")

# 1(c)(i): Page 6 (index 5), prompt y=60 to 80 + 2 lines + [1] (y=80 to 125, y=145 to 170)
stitch([
    crop_box(doc_21_01, 5, 60, 125),
    crop_box(doc_21_01, 5, 145, 170)
], os.path.join(dir_21_01, "q1ci.jpg"))

# 1(c)(ii): Page 6 (index 5), Fig 1.4 + prompt y=85 to 335 + Voltage line + [2] (y=485 to 525)
stitch([
    crop_box(doc_21_01, 5, 85, 335),
    crop_box(doc_21_01, 5, 485, 525)
], os.path.join(dir_21_01, "q1cii.jpg"))

# 1(c)(iii): Page 6 (index 5), prompt y=530 to 585 + 2 lines + [2] (y=585 to 630, y=750 to 775)
stitch([
    crop_box(doc_21_01, 5, 530, 630),
    crop_box(doc_21_01, 5, 750, 775)
], os.path.join(dir_21_01, "q1ciii.jpg"))

# 2(a)(ii): Page 9 (index 8), tolerance + prompt y=350 to 415 + within tolerance [3] (y=565 to 610)
stitch([
    crop_box(doc_21_01, 8, 350, 415),
    crop_box(doc_21_01, 8, 565, 610)
], os.path.join(dir_21_01, "q2aii.jpg"))

# =========================================================================
# 7. 2022-summer-01
# =========================================================================
print("\n--- 7. Fixing 2022-summer-01 ---")
doc_22_01 = fitz.open(os.path.join(UP, "media_1795108912081_23810779.pdf"))
dir_22_01 = os.path.join(REPO, "img", "2022-summer-01")

# 3(a)(i): Page 12 (index 11), prompt y=380 to 420 + 1: y=420 to 450 + 2: y=470 to 525 [2]
stitch([
    crop_box(doc_22_01, 11, 380, 450),
    crop_box(doc_22_01, 11, 470, 525)
], os.path.join(dir_22_01, "q3ai.jpg"))

# 3(a)(ii): Page 12 (index 11), prompt y=530 to 565 + 1: y=565 to 600 + 2: y=665 to 775 [4]
stitch([
    crop_box(doc_22_01, 11, 530, 600),
    crop_box(doc_22_01, 11, 665, 775)
], os.path.join(dir_22_01, "q3aii.jpg"))

# =========================================================================
# 8. 2023-summer-01
# =========================================================================
print("\n--- 8. Fixing 2023-summer-01 ---")
doc_23_01 = fitz.open(os.path.join(UP, "media_1795110317458_9f0b5576.pdf"))
dir_23_01 = os.path.join(REPO, "img", "2023-summer-01")

# 1(d)(iv): Page 5 (index 4), prompt y=435 to 465 + 1 line + [1] (y=465 to 505)
stitch([
    crop_box(doc_23_01, 4, 435, 505)
], os.path.join(dir_23_01, "q1div.jpg"))

# 1(d)(v): Page 5 (index 4), prompt y=515 to 565 + 2 lines + [2] (y=565 to 600, y=745 to 770)
stitch([
    crop_box(doc_23_01, 4, 515, 600),
    crop_box(doc_23_01, 4, 745, 770)
], os.path.join(dir_23_01, "q1dv.jpg"))

# 3(a)(ii): Page 10 (index 9), sheet metal drawing + prompt y=200 to 520 + 2 lines + [4] (y=520 to 560, y=745 to 775)
stitch([
    crop_box(doc_23_01, 9, 200, 560),
    crop_box(doc_23_01, 9, 745, 775)
], os.path.join(dir_23_01, "q3aii.jpg"))

# =========================================================================
# 9. 2023-summer-02
# =========================================================================
print("\n--- 9. Fixing 2023-summer-02 ---")
doc_23_02 = fitz.open(os.path.join(UP, "media_1795110317476_4679c2e5.pdf"))
dir_23_02 = os.path.join(REPO, "img", "2023-summer-02")

# 2*: Page 4 (index 3), prompt y=60 to 180 + 2 lines + [14] (y=180 to 220, y=745 to 775)
stitch([
    crop_box(doc_23_02, 3, 60, 220),
    crop_box(doc_23_02, 3, 745, 775)
], os.path.join(dir_23_02, "q2.jpg"))

# =========================================================================
# 10. 2024-summer-01
# =========================================================================
print("\n--- 10. Fixing 2024-summer-01 ---")
doc_24_01 = fitz.open(os.path.join(UP, "media_1795123383302_2ab7c42f.pdf"))
dir_24_01 = os.path.join(REPO, "img", "2024-summer-01")

# 1(c)(i): Page 6 (index 5), prompt y=62 to 110 + 2 lines + [4] (y=110 to 160, y=265 to 295)
stitch([
    crop_box(doc_24_01, 5, 62, 160),
    crop_box(doc_24_01, 5, 265, 295)
], os.path.join(dir_24_01, "q1ci.jpg"))

# 2(a)(i): Page 8 (index 7), prompt y=435 to 480 + length L [3] (y=560 to 595)
stitch([
    crop_box(doc_24_01, 7, 435, 480),
    crop_box(doc_24_01, 7, 560, 595)
], os.path.join(dir_24_01, "q2ai.jpg"))

# 2(a)(ii): Page 8 (index 7), prompt y=595 to 670 + surface area [2] (y=750 to 780)
stitch([
    crop_box(doc_24_01, 7, 595, 670),
    crop_box(doc_24_01, 7, 750, 780)
], os.path.join(dir_24_01, "q2aii.jpg"))

# 2(b)(ii): Page 10 (index 9), graph Fig 2.2 + prompt y=280 to 540 + Average current [2] (y=600 to 635)
stitch([
    crop_box(doc_24_01, 9, 280, 540),
    crop_box(doc_24_01, 9, 600, 635)
], os.path.join(dir_24_01, "q2bii.jpg"))

# 3(a): Page 11 (index 10), prompt y=280 to 335 + 2 lines + [4] (y=335 to 375, y=515 to 545)
stitch([
    crop_box(doc_24_01, 10, 280, 375),
    crop_box(doc_24_01, 10, 515, 545)
], os.path.join(dir_24_01, "q3a.jpg"))

# 4(b)(ii): Page 15 (index 14), prompt y=445 to 510 + Mass [4] (y=745 to 780)
stitch([
    crop_box(doc_24_01, 14, 445, 510),
    crop_box(doc_24_01, 14, 745, 780)
], os.path.join(dir_24_01, "q4bii.jpg"))

# 4(c)(i): Page 16 (index 15), prompt y=62 to 115 + 2 lines + [2] (y=115 to 155, y=215 to 240)
stitch([
    crop_box(doc_24_01, 15, 62, 155),
    crop_box(doc_24_01, 15, 215, 240)
], os.path.join(dir_24_01, "q4ci.jpg"))

# =========================================================================
# 11. 2024-summer-02
# =========================================================================
print("\n--- 11. Fixing 2024-summer-02 ---")
doc_24_02 = fitz.open(os.path.join(UP, "media_1795123383300_293be5ff.pdf"))
dir_24_02 = os.path.join(REPO, "img", "2024-summer-02")

# 2*: Page 4 (index 3), prompt y=60 to 180 + 2 lines + [14] (y=180 to 220, y=745 to 780)
stitch([
    crop_box(doc_24_02, 3, 60, 220),
    crop_box(doc_24_02, 3, 745, 780)
], os.path.join(dir_24_02, "q2.jpg"))

# 3(b): Page 7 (index 6), prompt y=345 to 550 + time [3] (y=695 to 735)
stitch([
    crop_box(doc_24_02, 6, 345, 550),
    crop_box(doc_24_02, 6, 695, 735)
], os.path.join(dir_24_02, "q3b.jpg"))

# =========================================================================
# 12. Fix Truncated summaries and page numbers in questions.json
# =========================================================================
print("\n--- 12. Cleaning questions.json ---")
q_json_path = os.path.join(REPO, "questions.json")
with open(q_json_path, "r", encoding="utf-8") as f:
    d = json.load(f)

fixed_count = 0
for q in d["questions"]:
    # 1. Fix truncated summary
    s = q.get("summary", "")
    if s.endswith("...") or s.endswith(".."):
        # derive clean summary from prompt
        p = q.get("prompt", "")
        # strip HTML tags
        import re
        clean_p = re.sub(r'<[^>]+>', ' ', p).strip()
        # remove [X] mark at end
        clean_p = re.sub(r'\s*\[\d+\]\s*$', '', clean_p).strip()
        if clean_p:
            q["summary"] = clean_p
            fixed_count += 1
            
    # 2. Fix page number for 2019 AS 5(b)
    if q["id"] == "2019-summer-as-01-q5b":
        q["page"] = 21
    elif q["id"] == "2019-summer-as-01-q1di":
        q["page"] = 5

with open(q_json_path, "w", encoding="utf-8") as f:
    json.dump(d, f, indent=2)

print(f"Fixed {fixed_count} truncated summaries in questions.json")
print("All problem question crops cleanly re-generated!")
