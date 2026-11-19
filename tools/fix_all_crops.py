"""
Precision crop script to trim excess student answer space and fix bad crops:
1. 2020-autumn-01:
   - q1ai.jpg: intro + smart object + network + communication protocol + [3].
   - q1aii.jpg: prompt + 2 lines + [4].
2. 2019-summer-as-01:
   - q3ci.jpg: prompt + small drawing space + [4]. Put Fig 3.4 in figures.
   - q3cii.jpg: prompt + 1 line + [2]. Put Fig 3.5 in figures.
   - q4aii.jpg: prompt + 2 lines + [4].
   - q1di.jpg: prompt + 2 lines + [3].
   - q4cii.jpg: prompt + 2 lines + [3].
3. 2019-summer-01:
   - q4d.jpg: prompt + system diagram to complete + [4].
   - q4eiii.jpg: prompt + 60pt box + [3].
4. 2018-practice-01:
   - Trim answer lines for: 1(a), 1(b), 1(c)(ii), 1(c)(iii), 1(d)(i), 1(d)(ii), 1(d)(iii), 2(a), 2(c)(i), 3(a)(i), 3(a)(ii), 4(b)(i), 4(b)(iii).
5. 2019-summer-02:
   - Ensure clean bounds for 3 and 5 without clipping.
"""

import os, json
import fitz
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
    print(f"  Saved {os.path.basename(out_path)}: {w}x{h}")

# =========================================================================
# 1. 2020-autumn-01
# =========================================================================
print("\n--- 1. Fixing 2020-autumn-01 crops ---")
doc_2020_01 = fitz.open(os.path.join(UP, "media_1795097357720_416191c3.pdf"))
dir_2020_01 = os.path.join(REPO, "img", "2020-autumn-01")

# q1ai: intro + smart object + network + communication protocol + [3]
stitch([
    crop_box(doc_2020_01, 1, 85, 208),
    crop_box(doc_2020_01, 1, 220, 260),
    crop_box(doc_2020_01, 1, 273, 312),
    crop_box(doc_2020_01, 1, 325, 376)
], os.path.join(dir_2020_01, "q1ai.jpg"))

# q1aii: prompt (y=385 to 455) + 1-2 dotted lines (470 to 508) + [4] (595 to 615)
stitch([
    crop_box(doc_2020_01, 1, 385, 455),
    crop_box(doc_2020_01, 1, 470, 508),
    crop_box(doc_2020_01, 1, 595, 615)
], os.path.join(dir_2020_01, "q1aii.jpg"))

# =========================================================================
# 2. 2019-summer-as-01
# =========================================================================
print("\n--- 2. Fixing 2019-summer-as-01 crops ---")
doc_as = fitz.open(os.path.join(UP, "media_1795090284268_4e11c92e.pdf"))
dir_as = os.path.join(REPO, "img", "2019-summer-as-01")

# Fig 3.4 (page 12, y=60 to 285)
stitch([crop_box(doc_as, 11, 60, 290)], os.path.join(dir_as, "fig-3-4.jpg"))

# q3ci: page 12, y=295 to 345 (prompt) + small clean drawing box + [4] (y=745 to 780)
stitch([
    crop_box(doc_as, 11, 295, 345),
    crop_box(doc_as, 11, 345, 420),
    crop_box(doc_as, 11, 745, 780)
], os.path.join(dir_as, "q3ci.jpg"))

# Fig 3.5 (page 13, y=115 to 345)
stitch([crop_box(doc_as, 12, 115, 345)], os.path.join(dir_as, "fig-3-5.jpg"))

# q3cii: page 13, y=60 to 110 (prompt) + y=565 to 615 (Resistance ... and [2])
stitch([
    crop_box(doc_as, 12, 60, 110),
    crop_box(doc_as, 12, 565, 615)
], os.path.join(dir_as, "q3cii.jpg"))

# q4aii: page 15, prompt + 2 lines + [4]
stitch([
    crop_box(doc_as, 14, 60, 145),
    crop_box(doc_as, 14, 380, 425)
], os.path.join(dir_as, "q4aii.jpg"))

# q1di: page 3
stitch([
    crop_box(doc_as, 2, 450, 520),
    crop_box(doc_as, 2, 600, 640)
], os.path.join(dir_as, "q1di.jpg"))

# q4cii: page 17-18
stitch([
    crop_box(doc_as, 17, 60, 140),
    crop_box(doc_as, 17, 340, 385)
], os.path.join(dir_as, "q4cii.jpg"))

# =========================================================================
# 3. 2019-summer-01
# =========================================================================
print("\n--- 3. Fixing 2019-summer-01 crops ---")
doc_19_01 = fitz.open(os.path.join(UP, "media_1795090284300_97db84a6.pdf"))
dir_19_01 = os.path.join(REPO, "img", "2019-summer-01")

# q4d: page 15, y=60 to 675 (complete system diagram + [4])
stitch([crop_box(doc_19_01, 14, 60, 680)], os.path.join(dir_19_01, "q4d.jpg"))

# q4eiii: page 18, y=60 to 100 (prompt) + 70pt box + [3]
stitch([
    crop_box(doc_19_01, 17, 60, 100),
    crop_box(doc_19_01, 17, 100, 180),
    crop_box(doc_19_01, 17, 500, 535)
], os.path.join(dir_19_01, "q4eiii.jpg"))

# =========================================================================
# 4. 2018-practice-01
# =========================================================================
print("\n--- 4. Fixing 2018-practice-01 crops ---")
doc_18_01 = fitz.open(os.path.join(UP, "media_1795086229085_87988b59.pdf"))
dir_18_01 = os.path.join(REPO, "img", "2018-practice-01")

# q1a: P1, prompt y=275 to 310, 1: 315 to 345, 2: 365 to 425 [2]
stitch([crop_box(doc_18_01, 1, 275, 310), crop_box(doc_18_01, 1, 315, 345), crop_box(doc_18_01, 1, 365, 425)], os.path.join(dir_18_01, "q1a.jpg"))

# q1b: P1, prompt y=430 to 505, 1: 510 to 535, 2: 560 to 585, 3: 612 to 670 [3]
stitch([crop_box(doc_18_01, 1, 430, 505), crop_box(doc_18_01, 1, 510, 535), crop_box(doc_18_01, 1, 560, 585), crop_box(doc_18_01, 1, 612, 670)], os.path.join(dir_18_01, "q1b.jpg"))

# q1cii: P3, y=55 to 500 + angle [3]
stitch([crop_box(doc_18_01, 3, 55, 500), crop_box(doc_18_01, 3, 690, 730)], os.path.join(dir_18_01, "q1cii.jpg"))

# q1ciii: P4, y=55 to 180 + 2 lines + [2]
stitch([crop_box(doc_18_01, 4, 55, 180), crop_box(doc_18_01, 4, 180, 220), crop_box(doc_18_01, 4, 260, 285)], os.path.join(dir_18_01, "q1ciii.jpg"))

# q1di: P4, y=285 to 350 + 2 lines + [2]
stitch([crop_box(doc_18_01, 4, 285, 350), crop_box(doc_18_01, 4, 350, 390), crop_box(doc_18_01, 4, 430, 455)], os.path.join(dir_18_01, "q1di.jpg"))

# q1dii: P4, y=455 to 495 + 2 lines + [2]
stitch([crop_box(doc_18_01, 4, 455, 495), crop_box(doc_18_01, 4, 495, 535), crop_box(doc_18_01, 4, 575, 600)], os.path.join(dir_18_01, "q1dii.jpg"))

# q1diii: P5, y=55 to 160 + drawing box + [4]
stitch([crop_box(doc_18_01, 5, 55, 160), crop_box(doc_18_01, 5, 160, 260), crop_box(doc_18_01, 5, 755, 790)], os.path.join(dir_18_01, "q1diii.jpg"))

# q2a: P6, y=55 to 370 + grid + [3]
stitch([crop_box(doc_18_01, 6, 55, 370), crop_box(doc_18_01, 6, 370, 500), crop_box(doc_18_01, 6, 680, 710)], os.path.join(dir_18_01, "q2a.jpg"))

# q2ci: P8, y=55 to 305 + force [2]
stitch([crop_box(doc_18_01, 8, 55, 305), crop_box(doc_18_01, 8, 455, 500)], os.path.join(dir_18_01, "q2ci.jpg"))

# q3ai: P11, y=55 to 120 + 2 lines + [2]
stitch([crop_box(doc_18_01, 11, 55, 120), crop_box(doc_18_01, 11, 120, 160), crop_box(doc_18_01, 11, 200, 225)], os.path.join(dir_18_01, "q3ai.jpg"))

# q3aii: P11, y=225 to 250 + 2 lines + [4]
stitch([crop_box(doc_18_01, 11, 225, 250), crop_box(doc_18_01, 11, 250, 290), crop_box(doc_18_01, 11, 430, 460)], os.path.join(dir_18_01, "q3aii.jpg"))

# q4bi: P14, y=360 to 400 + 3 items + [3]
stitch([crop_box(doc_18_01, 14, 360, 400), crop_box(doc_18_01, 14, 400, 425), crop_box(doc_18_01, 14, 450, 475), crop_box(doc_18_01, 14, 505, 565)], os.path.join(dir_18_01, "q4bi.jpg"))

# q4biii: P15, y=55 to 95 + 2 lines + [4]
stitch([crop_box(doc_18_01, 15, 55, 95), crop_box(doc_18_01, 15, 95, 135), crop_box(doc_18_01, 15, 225, 250)], os.path.join(dir_18_01, "q4biii.jpg"))

# =========================================================================
# 5. 2019-summer-02
# =========================================================================
print("\n--- 5. Fixing 2019-summer-02 crops ---")
doc_19_02 = fitz.open(os.path.join(UP, "media_1795092837972_f98c422c.pdf"))
dir_19_02 = os.path.join(REPO, "img", "2019-summer-02")

# q3: page index 4 (page 5), prompt + formula (y=60 to 435) + minimum panels [6] (y=725 to 772)
stitch([crop_box(doc_19_02, 4, 60, 435), crop_box(doc_19_02, 4, 725, 772)], os.path.join(dir_19_02, "q3.jpg"))

# q5: page index 7 (page 8), complete prompt with Issue 1 & Issue 2 and [16] (y=60 to 475)
stitch([crop_box(doc_19_02, 7, 60, 475)], os.path.join(dir_19_02, "q5.jpg"))

# Update questions.json for 2019 AS figures if needed
q_json_path = os.path.join(REPO, "questions.json")
with open(q_json_path, "r", encoding="utf-8") as f:
    d = json.load(f)

for q in d["questions"]:
    if q["id"] == "2019-summer-as-01-q3ci":
        if "img/2019-summer-as-01/fig-3-4.jpg" not in q.get("figures", []):
            q["figures"] = ["img/2019-summer-as-01/fig-3-4.jpg"]
    elif q["id"] == "2019-summer-as-01-q3cii":
        if "img/2019-summer-as-01/fig-3-5.jpg" not in q.get("figures", []):
            q["figures"] = ["img/2019-summer-as-01/fig-3-5.jpg"]

with open(q_json_path, "w", encoding="utf-8") as f:
    json.dump(d, f, indent=2)

print("\nAll problem crops fixed and questions.json updated successfully!")
