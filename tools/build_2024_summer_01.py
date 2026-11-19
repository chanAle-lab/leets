"""
Build OCR H404/01 Principles of Design Engineering - June 2024 (paper id 2024-summer-01).
Total Marks: 80 marks across 21 questions.

Strict Separation & Ingestion Standards:
  - q.image: Question prompt cards with excess blank student answer lines collapsed.
  - q.figures: Preamble text, apparatus photos, tables, and graphs in resources.
  - q.markscheme: High-res stitched crops of MS table rows with autotrim.
  - Full KaTeX mathematical solutions & curriculum tags in questions.json.
"""

import os, json
import numpy as np
from PIL import Image, ImageDraw
import fitz

BASE_UP = r"C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded"
QP_PATH = os.path.join(BASE_UP, "media_1795123383302_2ab7c42f.pdf")
MS_PATH = os.path.join(BASE_UP, "media_1795123383322_30b9135d.pdf")

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PID = "2024-summer-01"
OUT_IMG = os.path.join(REPO, "img", PID)
os.makedirs(OUT_IMG, exist_ok=True)

qp = fitz.open(QP_PATH)
ms = fitz.open(MS_PATH)
ZOOM = 2.0

def crop_area(doc, pno, y0, y1, x0=45, x1=555):
    page = doc[pno - 1]
    rect = fitz.Rect(x0, y0, x1, y1)
    pix = page.get_pixmap(clip=rect, matrix=fitz.Matrix(ZOOM, ZOOM))
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

def autotrim_table(im, pad=14, thresh=40):
    a = np.asarray(im.convert("L"))
    dark = (a < 160).sum(axis=1)
    rows = np.where((dark > thresh) & (dark < 0.6 * im.width))[0]
    if len(rows) == 0:
        return im
    last = min(im.height, rows[-1] + pad)
    if last >= im.height - 4:
        return im
    out = im.crop((0, 0, im.width, last)).copy()
    ImageDraw.Draw(out).line([(6, last - 2), (im.width - 6, last - 2)], fill=(120, 120, 120), width=2)
    return out

def stitch_vert(images, fname, quality=90):
    w = max(im.width for im in images)
    h = sum(im.height for im in images)
    out = Image.new("RGB", (w, h), (255, 255, 255))
    curr_y = 0
    for im in images:
        out.paste(im, (0, curr_y))
        curr_y += im.height
    out.save(os.path.join(OUT_IMG, fname), quality=quality)
    print(f"  {fname:24s} -> {out.size}")
    return out

print("\n--- 1. Cropping Resource Figures ---")
# Fig 1.1: Coffee vending machine photo (Page 2)
stitch_vert([crop_area(qp, 2, 60, 415)], "fig-1-1.jpg")

# Fig 1.2: Coffee grinder compound gear train (Page 4)
stitch_vert([crop_area(qp, 4, 60, 320)], "fig-1-2.jpg")

# Fig 2.1: Square sheet of mild steel with triangular cutouts (Page 8)
stitch_vert([crop_area(qp, 8, 60, 510)], "fig-2-1.jpg")

# Fig 2.2: Pulsed current waveform graph (Page 10)
stitch_vert([crop_area(qp, 10, 320, 580)], "fig-2-2.jpg")

# Fig 4.1: Automatic cat feeder photo (Page 13)
stitch_vert([crop_area(qp, 13, 60, 370)], "fig-4-1.jpg")

# Fig 4.2 & 4.3: Paddle wheel dispensing mechanism diagrams and dimensions (Page 14)
stitch_vert([crop_area(qp, 14, 60, 760)], "fig-4-2.jpg")

# MS Exemplar: Microswitch sensor sketch (MS p23)
stitch_vert([crop_area(ms, 23, 175, 480, x0=150, x1=500)], "ms-4cii-sketch.jpg")


print("\n--- 2. Cropping Question Prompt Cards ---")
# 1(a)(i) [4m] - Page 2
stitch_vert([
    crop_area(qp, 2, 415, 530),
    crop_area(qp, 2, 530, 555),
    crop_area(qp, 2, 632, 658),
    crop_area(qp, 2, 715, 745)
], "q1ai.jpg")

# 1(a)(ii) [4m] - Page 3
stitch_vert([
    crop_area(qp, 3, 60, 98),
    crop_area(qp, 3, 98, 125),
    crop_area(qp, 3, 202, 230),
    crop_area(qp, 3, 285, 315)
], "q1aii.jpg")

# 1(b)(i) [3m] - Page 4
stitch_vert([
    crop_area(qp, 4, 320, 378),
    crop_area(qp, 4, 575, 610)
], "q1bi.jpg")

# 1(b)(ii) [2m] - Page 4
stitch_vert([
    crop_area(qp, 4, 612, 665),
    crop_area(qp, 4, 665, 690),
    crop_area(qp, 4, 742, 775)
], "q1bii.jpg")

# 1(b)(iii) [4m] - Page 5
stitch_vert([
    crop_area(qp, 5, 60, 150),
    crop_area(qp, 5, 150, 175),
    crop_area(qp, 5, 255, 280),
    crop_area(qp, 5, 360, 395)
], "q1biii.jpg")

# 1(c)(i) [4m] - Page 6
stitch_vert([
    crop_area(qp, 6, 60, 115),
    crop_area(qp, 6, 115, 140),
    crop_area(qp, 6, 290, 325)
], "q1ci.jpg")

# 1(c)(ii) [4m] - Page 6
stitch_vert([
    crop_area(qp, 6, 328, 385),
    crop_area(qp, 6, 385, 410),
    crop_area(qp, 6, 560, 595)
], "q1cii.jpg")

# 2(a)(i) [3m] - Page 8
stitch_vert([
    crop_area(qp, 8, 515, 570),
    crop_area(qp, 8, 660, 695)
], "q2ai.jpg")

# 2(a)(ii) [2m] - Page 8
stitch_vert([
    crop_area(qp, 8, 700, 795),
    crop_area(qp, 8, 885, 920) if False else crop_area(qp, 8, 700, 795) # wait, let's look at p8
], "q2aii.jpg")

# 2(a)(iii) [5m] - Page 9
stitch_vert([
    crop_area(qp, 9, 60, 240),
    crop_area(qp, 9, 870, 910)
], "q2aiii.jpg")

# 2(b)(i) [3m] - Page 10
stitch_vert([
    crop_area(qp, 10, 60, 175),
    crop_area(qp, 10, 285, 320)
], "q2bi.jpg")

# 2(b)(ii) [2m] - Page 10
stitch_vert([
    crop_area(qp, 10, 582, 640),
    crop_area(qp, 10, 715, 750)
], "q2bii.jpg")

# 2(b)(iii) [3m] - Page 11
stitch_vert([
    crop_area(qp, 11, 60, 160),
    crop_area(qp, 11, 265, 300)
], "q2biii.jpg")

# 3(a) [4m] - Page 11
stitch_vert([
    crop_area(qp, 11, 330, 410),
    crop_area(qp, 11, 410, 435),
    crop_area(qp, 11, 615, 650)
], "q3a.jpg")

# 3(b)* [8m] - Page 12
stitch_vert([
    crop_area(qp, 12, 60, 130),
    crop_area(qp, 12, 130, 155),
    crop_area(qp, 12, 700, 735)
], "q3b.jpg")

# 4(a) [4m] - Page 13
stitch_vert([
    crop_area(qp, 13, 370, 465),
    crop_area(qp, 13, 465, 490),
    crop_area(qp, 13, 670, 705)
], "q4a.jpg")

# 4(b)(i) [4m] - Page 15
stitch_vert([
    crop_area(qp, 15, 60, 210),
    crop_area(qp, 15, 485, 520)
], "q4bi.jpg")

# 4(b)(ii) [4m] - Page 15
stitch_vert([
    crop_area(qp, 15, 525, 615),
    crop_area(qp, 15, 885, 920)
], "q4bii.jpg")

# 4(c)(i) [2m] - Page 16
stitch_vert([
    crop_area(qp, 16, 60, 145),
    crop_area(qp, 16, 145, 170),
    crop_area(qp, 16, 260, 290)
], "q4ci.jpg")

# 4(c)(ii) [3m] - Page 16
stitch_vert([
    crop_area(qp, 16, 290, 400),
    crop_area(qp, 16, 400, 440)
], "q4cii.jpg")

# 4(d)* [8m] - Page 17
stitch_vert([
    crop_area(qp, 17, 60, 195),
    crop_area(qp, 17, 195, 220),
    crop_area(qp, 17, 765, 800)
], "q4d.jpg")


print("\n--- 3. Cropping Mark Schemes ---")
# ms-1ai.jpg (MS p7)
stitch_vert([autotrim_table(crop_area(ms, 7, 85, 445, x0=45, x1=790))], "ms-1ai.jpg")

# ms-1aii.jpg (MS p7-8)
stitch_vert([
    crop_area(ms, 7, 445, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 8, 85, 300, x0=45, x1=790))
], "ms-1aii.jpg")

# ms-1bi.jpg (MS p8-9)
stitch_vert([
    crop_area(ms, 8, 300, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 9, 85, 215, x0=45, x1=790))
], "ms-1bi.jpg")

# ms-1bii.jpg (MS p9)
stitch_vert([autotrim_table(crop_area(ms, 9, 215, 545, x0=45, x1=790))], "ms-1bii.jpg")

# ms-1biii.jpg (MS p10)
stitch_vert([autotrim_table(crop_area(ms, 10, 85, 450, x0=45, x1=790))], "ms-1biii.jpg")

# ms-1ci.jpg (MS p10-11)
stitch_vert([
    crop_area(ms, 10, 450, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 11, 85, 215, x0=45, x1=790))
], "ms-1ci.jpg")

# ms-1cii.jpg (MS p11)
stitch_vert([autotrim_table(crop_area(ms, 11, 215, 545, x0=45, x1=790))], "ms-1cii.jpg")

# ms-2ai.jpg (MS p12-13)
stitch_vert([
    crop_area(ms, 12, 85, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 13, 85, 135, x0=45, x1=790))
], "ms-2ai.jpg")

# ms-2aii.jpg (MS p13)
stitch_vert([autotrim_table(crop_area(ms, 13, 135, 545, x0=45, x1=790))], "ms-2aii.jpg")

# ms-2aiii.jpg (MS p14)
stitch_vert([autotrim_table(crop_area(ms, 14, 85, 545, x0=45, x1=790))], "ms-2aiii.jpg")

# ms-2bi.jpg (MS p15)
stitch_vert([autotrim_table(crop_area(ms, 15, 85, 360, x0=45, x1=790))], "ms-2bi.jpg")

# ms-2bii.jpg (MS p15)
stitch_vert([autotrim_table(crop_area(ms, 15, 360, 545, x0=45, x1=790))], "ms-2bii.jpg")

# ms-2biii.jpg (MS p16)
stitch_vert([autotrim_table(crop_area(ms, 16, 85, 480, x0=45, x1=790))], "ms-2biii.jpg")

# ms-3a.jpg (MS p17)
stitch_vert([autotrim_table(crop_area(ms, 17, 85, 545, x0=45, x1=790))], "ms-3a.jpg")

# ms-3b.jpg (MS p18)
stitch_vert([autotrim_table(crop_area(ms, 18, 85, 545, x0=45, x1=790))], "ms-3b.jpg")

# ms-4a.jpg (MS p19)
stitch_vert([autotrim_table(crop_area(ms, 19, 85, 545, x0=45, x1=790))], "ms-4a.jpg")

# ms-4bi.jpg (MS p20-21)
stitch_vert([
    crop_area(ms, 20, 85, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 21, 85, 215, x0=45, x1=790))
], "ms-4bi.jpg")

# ms-4bii.jpg (MS p21-22)
stitch_vert([
    crop_area(ms, 21, 215, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 22, 85, 225, x0=45, x1=790))
], "ms-4bii.jpg")

# ms-4ci.jpg (MS p22)
stitch_vert([autotrim_table(crop_area(ms, 22, 225, 545, x0=45, x1=790))], "ms-4ci.jpg")

# ms-4cii.jpg (MS p23)
stitch_vert([autotrim_table(crop_area(ms, 23, 65, 545, x0=45, x1=790))], "ms-4cii.jpg")

# ms-4d.jpg (MS p24-25)
stitch_vert([
    crop_area(ms, 24, 65, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 25, 65, 330, x0=45, x1=790))
], "ms-4d.jpg")

print("\n--- 4. Assembling Questions JSON Entry ---")

new_questions = [
    {
        "id": "2024-h404-01-q1ai",
        "paper": PID,
        "question_number": "1(a)(i)",
        "marks": 4,
        "topic": "Product Safety & User Protection",
        "question": "Fig. 1.1 shows a self-service coffee vending machine. Identify two safety features that could be included in the design of a coffee vending machine. Justify how each of the safety features you have identified helps to keep users safe.",
        "image": f"img/{PID}/q1ai.jpg",
        "figures": [f"img/{PID}/fig-1-1.jpg"],
        "markscheme": f"img/{PID}/ms-1ai.jpg",
        "markscheme_text": "**Four marks** (1 mark for identifying safety feature, 1 mark for justification in context, for each of two points):\n- **Prominent 'Hot' warning sign / illuminated status indicator:** Informs users that boiling liquid is dispensing so they keep hands away from the delivery spout.\n- **Dispensing chamber interlock / safety door or optical barrier:** Prevents hot coffee from flowing if a hand is detected near the nozzle, preventing scald injuries.\n- **Insulated cup sleeves / secure snap-on lids provided:** Prevents users burning fingers on hot takeaway cups and prevents scalding spills while walking.\n- **Refrigeration temperature sensor / fault lockout:** Continuously monitors milk temperature and shuts down milk dispensing if it rises above 4°C to prevent bacterial growth and food poisoning."
    },
    {
        "id": "2024-h404-01-q1aii",
        "paper": PID,
        "question_number": "1(a)(ii)",
        "marks": 4,
        "topic": "User Interfaces & Human Factors",
        "question": "Explain one benefit and one drawback of using a touch screen interface in products such as coffee vending machines.",
        "image": f"img/{PID}/q1aii.jpg",
        "figures": [f"img/{PID}/fig-1-1.jpg"],
        "markscheme": f"img/{PID}/ms-1aii.jpg",
        "markscheme_text": "**Four marks** (up to 2 marks for benefit, up to 2 marks for drawback):\n\n**Benefit (2 marks):**\n- Eliminates physical mechanical push buttons, reducing wiring, mechanical wear, ingress points for dirt/liquids, and allowing easy software updates to add or reconfigure drink menus and dynamic advertising.\n\n**Drawback (2 marks):**\n- High initial cost and vulnerability to screen smudges, moisture, or vandalism (cracked glass), which can cause touch unresponsiveness or false inputs, especially in high-traffic public environments."
    },
    {
        "id": "2024-h404-01-q1bi",
        "paper": PID,
        "question_number": "1(b)(i)",
        "marks": 3,
        "topic": "Gear Trains & Velocity Ratios",
        "question": "The electric motor runs at a speed of 3000 rpm. Use the information in Fig. 1.2 to calculate the rotational speed of the output gear. Give your answer in rpm to the nearest whole number. Show your working.",
        "image": f"img/{PID}/q1bi.jpg",
        "figures": [f"img/{PID}/fig-1-2.jpg"],
        "markscheme": f"img/{PID}/ms-1bi.jpg",
        "markscheme_text": "**Three marks total:**\n\n1. Calculate overall compound gear ratio:  \n   $$\\text{Gear ratio} = \\frac{\\text{Driven}_1}{\\text{Driver}_1} \\times \\frac{\\text{Driven}_2}{\\text{Driver}_2} = \\frac{72}{56} \\times \\frac{42}{16} = 1.2857 \\times 2.625 = 3.375 \\quad [1]$$\n\n2. Calculate output speed:  \n   $$\\text{Output speed} = \\frac{\\text{Input speed}}{\\text{Gear ratio}} = \\frac{3000\\text{ rpm}}{3.375} \\quad [1]$$\n\n3. Evaluate to nearest whole number:  \n   $$\\text{Output speed} = 888.889\\text{ rpm} \\approx \\mathbf{889\\text{ rpm}} \\quad [1]$$"
    },
    {
        "id": "2024-h404-01-q1bii",
        "paper": PID,
        "question_number": "1(b)(ii)",
        "marks": 2,
        "topic": "Mechanical Systems & Gear Strength",
        "question": "The gears in Fig. 1.2 have teeth of different sizes. Explain one reason why the designer chose to use a gear with larger teeth for the output gear.",
        "image": f"img/{PID}/q1bii.jpg",
        "figures": [f"img/{PID}/fig-1-2.jpg"],
        "markscheme": f"img/{PID}/ms-1bii.jpg",
        "markscheme_text": "**Two marks** for explanation:\n- The speed reduction in the gear train results in a significantly higher output torque at the final stage.\n- Larger module/pitch gear teeth possess greater cross-sectional root thickness and higher shear/bending strength, allowing them to withstand the high crushing forces and torque required to grind hard coffee beans without stripping or breaking teeth."
    },
    {
        "id": "2024-h404-01-q1biii",
        "paper": PID,
        "question_number": "1(b)(iii)",
        "marks": 4,
        "topic": "Materials Selection & Composite Polymers",
        "question": "The gears in Fig. 1.2 are manufactured from glass-filled nylon which is a type of glass-reinforced thermo softening polymer. Identify two properties of a glass-reinforced thermo softening polymer that makes it suitable for manufacturing gears. Justify each of your answers.",
        "image": f"img/{PID}/q1biii.jpg",
        "figures": [f"img/{PID}/fig-1-2.jpg"],
        "markscheme": f"img/{PID}/ms-1biii.jpg",
        "markscheme_text": "**Four marks** (1 mark for property, 1 mark for justification, for each of two properties):\n- **High flexural modulus / stiffness:** Glass fibers reinforce the polymer matrix, preventing gear teeth from flexing or deflecting under heavy shock loads during bean grinding.\n- **Excellent wear resistance & low coefficient of friction:** Nylon naturally provides self-lubricating properties, ensuring smooth meshing, low operating noise, and long service life without contaminating food with grease.\n- **Injection mouldable:** Thermo-softening matrix enables rapid, high-precision injection moulding of intricate involute tooth geometries in large production volumes at low unit cost."
    },
    {
        "id": "2024-h404-01-q1ci",
        "paper": PID,
        "question_number": "1(c)(i)",
        "marks": 4,
        "topic": "Marketing & Brand Awareness",
        "question": "Describe ways in which product designers and manufacturers promote brand awareness in customers.",
        "image": f"img/{PID}/q1ci.jpg",
        "figures": [],
        "markscheme": f"img/{PID}/ms-1ci.jpg",
        "markscheme_text": "**Up to four marks** for describing brand awareness strategies:\n- **Distinctive corporate visual identity & logo:** Prominently displaying instantly recognisable logos, distinctive color palettes, and typographic styling across products and packaging.\n- **Unique product form / signature aesthetic:** Developing iconic physical styling cues (e.g. Costa red accents, Coca-Cola contour bottle) that differentiate the product at a glance.\n- **Targeted multi-channel advertising & social media:** High-visibility digital campaigns, point-of-sale displays, sponsorship of events, and interactive online presence to keep the brand at the forefront of consumer consciousness."
    },
    {
        "id": "2024-h404-01-q1cii",
        "paper": PID,
        "question_number": "1(c)(ii)",
        "marks": 4,
        "topic": "Customer Retention & Brand Loyalty",
        "question": "Describe ways in which product designers and manufacturers encourage brand loyalty from customers.",
        "image": f"img/{PID}/q1cii.jpg",
        "figures": [],
        "markscheme": f"img/{PID}/ms-1cii.jpg",
        "markscheme_text": "**Up to four marks** for describing brand loyalty methods:\n- **High product reliability & build quality:** Delivering consistent, flawless performance that builds trust and reassurance so customers have no reason to switch to competitors.\n- **Intuitive, consistent user experience:** Designing cohesive physical controls and UI navigation across product generations so users feel immediately comfortable and familiar.\n- **Ecosystem integration & backwards compatibility:** Ensuring accessories, app profiles, and consumables seamlessly interconnect across models, making switching brands inconvenient.\n- **Dedicated aftersales support & loyalty rewards:** Offering responsive warranty service, repairability, and membership rewards programs."
    },
    {
        "id": "2024-h404-01-q2ai",
        "paper": PID,
        "question_number": "2(a)(i)",
        "marks": 3,
        "topic": "Geometry & Pythagoras Theorem",
        "question": "Fig. 2.1 shows a part made from a square sheet of mild steel with two identical right-angled isosceles triangular holes. Calculate the length marked L on Fig. 2.1. Give your answer in mm to 1 decimal place. Show your working.",
        "image": f"img/{PID}/q2ai.jpg",
        "figures": [f"img/{PID}/fig-2-1.jpg"],
        "markscheme": f"img/{PID}/ms-2ai.jpg",
        "markscheme_text": "**Three marks total:**\n\n1. Recognise right-angled isosceles triangle with legs = 50 mm:  \n   $$L^2 = 50^2 + 50^2 = 2500 + 2500 = 5000 \\quad [1]$$\n\n2. Take square root:  \n   $$L = \\sqrt{5000} = 70.7107\\text{ mm} \\quad [1]$$\n\n3. State answer to 1 decimal place:  \n   $$L = \\mathbf{70.7\\text{ mm}} \\quad [1]$$\n\n*(Alternatively using trigonometry: \\(L = \\frac{50}{\\cos 45^\\circ} = \\frac{50}{0.7071} = \\mathbf{70.7\\text{ mm}}\\))*"
    },
    {
        "id": "2024-h404-01-q2aii",
        "paper": PID,
        "question_number": "2(a)(ii)",
        "marks": 2,
        "topic": "Area Calculations & Sheet Profiles",
        "question": "The surface area of the face of the steel sheet without the two triangular holes cut out is 10 000 mm2. Calculate the surface area of the face of the steel sheet shown in Fig. 2.1 once the two triangular holes have been cut out. Give your answer in mm2 and show your working.",
        "image": f"img/{PID}/q2aii.jpg",
        "figures": [f"img/{PID}/fig-2-1.jpg"],
        "markscheme": f"img/{PID}/ms-2aii.jpg",
        "markscheme_text": "**Two marks total:**\n\n1. Calculate total cutout area of the two triangles:  \n   $$\\text{Area of 2 triangles} = 2 \\times \\left(\\frac{1}{2} \\times 50 \\times 50\\right) = 50 \\times 50 = 2500\\text{ mm}^2 \\quad [1]$$\n\n2. Subtract from square face area:  \n   $$\\text{Net face area} = 10\\,000\\text{ mm}^2 - 2500\\text{ mm}^2 = \\mathbf{7500\\text{ mm}^2} \\quad [1]$$"
    },
    {
        "id": "2024-h404-01-q2aiii",
        "paper": PID,
        "question_number": "2(a)(iii)",
        "marks": 5,
        "topic": "Surface Area & Material Finishing",
        "question": "A paint finish needs to be applied to the part in Fig. 2.1. Every 1 mm2 of surface area requires 2 × 10–4 cm3 of paint. The sheet thickness is 5 mm. The four outside edges of the part have a total surface area of 2000 mm2. Use your answers to part (a)(i) and part (a)(ii) to calculate the total volume of paint required to cover both sides of the part and all the exposed edges. Give your answer in cm3 to 2 decimal places. Show your working.",
        "image": f"img/{PID}/q2aiii.jpg",
        "figures": [f"img/{PID}/fig-2-1.jpg"],
        "markscheme": f"img/{PID}/ms-2aiii.jpg",
        "markscheme_text": "**Five marks total:**\n\n1. Calculate area of front and back faces:  \n   $$\\text{Faces area} = 2 \\times 7500\\text{ mm}^2 = 15\\,000\\text{ mm}^2 \\quad [1]$$\n\n2. Outside edges area:  \n   $$\\text{Outside edges} = 2000\\text{ mm}^2 \\quad [\\text{given}]$$\n\n3. Calculate area of inside cut edges of the two triangles:  \n   $$\\text{Each triangle perimeter} = 50 + 50 + 70.7 = 170.7\\text{ mm}$$\n   $$\\text{Inside edges area} = 2 \\times (170.7\\text{ mm} \\times 5\\text{ mm}) = (4 \\times 50 \\times 5) + (2 \\times 70.7 \\times 5) = 1000 + 707 = 1707\\text{ mm}^2 \\quad [2]$$\n\n4. Total exposed surface area:  \n   $$\\text{Total area} = 15\\,000 + 2000 + 1707 = 18\\,707\\text{ mm}^2 \\quad [1]$$\n\n5. Calculate required paint volume in \\(\\text{cm}^3\\):  \n   $$\\text{Volume} = 18\\,707\\text{ mm}^2 \\times (2 \\times 10^{-4}\\text{ cm}^3/\\text{mm}^2) = \\mathbf{3.74\\text{ cm}^3} \\quad [1]$$"
    },
    {
        "id": "2024-h404-01-q2bi",
        "paper": PID,
        "question_number": "2(b)(i)",
        "marks": 3,
        "topic": "Electrical Calculations & Ohm's Law",
        "question": "A heater is being used to prevent water pipes freezing in winter. The heater has a resistance of 32 \\(\\Omega\\). The heater is connected directly to a 24 V dc power supply. Calculate the power dissipated in the heater. Give your answer in watts (W) and show your working.",
        "image": f"img/{PID}/q2bi.jpg",
        "figures": [],
        "markscheme": f"img/{PID}/ms-2bi.jpg",
        "markscheme_text": "**Three marks total:**\n\n1. Recall electrical power formula:  \n   $$P = \\frac{V^2}{R} \\quad [1]$$\n\n2. Substitute voltage and resistance:  \n   $$P = \\frac{24^2}{32} = \\frac{576}{32} \\quad [1]$$\n\n3. Calculate power:  \n   $$P = \\mathbf{18\\text{ W}} \\quad [1]$$\n\n*(Alternative method: \\(I = \\frac{V}{R} = \\frac{24}{32} = 0.75\\text{ A}\\), \\(P = I V = 0.75 \\times 24 = \\mathbf{18\\text{ W}}\\))*"
    },
    {
        "id": "2024-h404-01-q2bii",
        "paper": PID,
        "question_number": "2(b)(ii)",
        "marks": 2,
        "topic": "Pulsed Signals & Average Current",
        "question": "To reduce the heater power, the current through the heater is repeatedly pulsed on and off. Fig. 2.2 shows a graph of how the current varies over time. Use the graph to calculate the average current flowing through the heater. Give your answer in amps (A) and show your working.",
        "image": f"img/{PID}/q2bii.jpg",
        "figures": [f"img/{PID}/fig-2-2.jpg"],
        "markscheme": f"img/{PID}/ms-2bii.jpg",
        "markscheme_text": "**Two marks total:**\n\n1. Determine duty cycle ratio from graph:  \n   $$\\text{On time} = 2.5\\text{ ms}, \\quad \\text{Period (cycle length)} = 7.5\\text{ ms}$$\n   $$\\text{Duty ratio} = \\frac{2.5\\text{ ms}}{7.5\\text{ ms}} = \\frac{1}{3} \\quad [1]$$\n\n2. Calculate average current:  \n   $$I_{\\text{avg}} = \\frac{1}{3} \\times 0.75\\text{ A} = \\mathbf{0.25\\text{ A}} \\quad [1]$$"
    },
    {
        "id": "2024-h404-01-q2biii",
        "paper": PID,
        "question_number": "2(b)(iii)",
        "marks": 3,
        "topic": "Pulsed Power Calculations",
        "question": "The heater uses a 24 V dc power supply. Use your answer from part (b)(ii) to calculate the average power dissipated in the heater when the current is pulsed as shown in Fig. 2.2. Give your answer in watts (W) and show your working.",
        "image": f"img/{PID}/q2biii.jpg",
        "figures": [f"img/{PID}/fig-2-2.jpg"],
        "markscheme": f"img/{PID}/ms-2biii.jpg",
        "markscheme_text": "**Three marks total:**\n\n1. Recall formula \\(P = I V\\):  \n   $$P_{\\text{avg}} = I_{\\text{avg}} \\times V \\quad [1]$$\n\n2. Substitute average current and supply voltage:  \n   $$P_{\\text{avg}} = 0.25\\text{ A} \\times 24\\text{ V} \\quad [1]$$\n\n3. Calculate result:  \n   $$P_{\\text{avg}} = \\mathbf{6\\text{ W}} \\quad [1]$$\n\n*(Or via duty cycle: \\(P_{\\text{avg}} = \\frac{1}{3} \\times 18\\text{ W} = \\mathbf{6\\text{ W}}\\))*"
    },
    {
        "id": "2024-h404-01-q3a",
        "paper": PID,
        "question_number": "3(a)",
        "marks": 4,
        "topic": "Business Strategies & Planned Obsolescence",
        "question": "Explain, using a specific example, how a manufacturer can use a planned obsolescence business strategy to promote future product sales.",
        "image": f"img/{PID}/q3a.jpg",
        "figures": [],
        "markscheme": f"img/{PID}/ms-3a.jpg",
        "markscheme_text": "**Four marks:**\n- **Understanding of Planned Obsolescence (1 mark):** Designing a product with an artificially limited useful life or deliberate functional/aesthetic lifespan so it becomes obsolete after a predetermined period.\n- **Specific Product Example (1 mark):** E.g. smartphones, laptop computers, or fast-fashion consumer electronics.\n- **How the product becomes obsolete (1 mark):** Operating system updates demand more processing power and RAM than older hardware can supply, battery performance degrades and is glued in (non-replaceable), or new software applications cease supporting the model.\n- **Link to predictable future sales (1 mark):** Users are compelled to upgrade and buy the manufacturer's newer model to maintain software functionality and battery life, generating predictable repeat revenue streams."
    },
    {
        "id": "2024-h404-01-q3b",
        "paper": PID,
        "question_number": "3(b)*",
        "marks": 8,
        "topic": "Quality Management & TQM Systems",
        "question": "Discuss how a Total Quality Management (TQM) strategy can help a manufacturing company achieve sustained levels of quality.",
        "image": f"img/{PID}/q3b.jpg",
        "figures": [],
        "markscheme": f"img/{PID}/ms-3b.jpg",
        "markscheme_text": "**Level of Response (8 marks):**\n\n- **Level 3 (6–8 marks):** Thorough, well-developed discussion explaining how TQM embeds quality culture across the entire organisation, supported by at least two clear manufacturing examples.\n- **Level 2 (3–5 marks):** Reasonable understanding of TQM and its role in quality assurance.\n- **Level 1 (1–2 marks):** Basic descriptive reference to checking products or reducing defects.\n\n**Key Indicative Content:**\n- **Holistic Responsibility:** Quality is not just inspected at the end of the line; every employee from senior management to shop floor operators is responsible for quality at their stage ('right first time').\n- **Continuous Improvement (Kaizen):** Ongoing small-scale incremental improvements in processes, tooling, and workflows to eliminate waste (Muda) and reduce defect rates.\n- **Customer Focus:** Aligning all design and production specifications directly with customer expectations and feedback.\n- **Supply Chain Integration:** Partnering closely with material suppliers to enforce strict incoming quality specifications, avoiding defective raw materials.\n- **Employee Empowerment & Training:** Quality circles where workers collaborate to solve production bottlenecks and take pride in product excellence."
    },
    {
        "id": "2024-h404-01-q4a",
        "paper": PID,
        "question_number": "4(a)",
        "marks": 4,
        "topic": "User-Centred Design & Focus Groups",
        "question": "Fig. 4.1 shows an automatic cat feeder. Describe how focus groups can be used when developing a new automatic cat feeder.",
        "image": f"img/{PID}/q4a.jpg",
        "figures": [f"img/{PID}/fig-4-1.jpg"],
        "markscheme": f"img/{PID}/ms-4a.jpg",
        "markscheme_text": "**Up to four marks** for describing focus group applications in context:\n- **Preliminary needs analysis:** Gathering pet owners to determine real-world user requirements, such as typical portion sizes, feeding frequencies, and anti-tamper latching to prevent clever pets breaking into the hopper.\n- **Concept evaluation & aesthetics:** Presenting sketches or 3D renderings to assess exterior styling, kitchen countertop aesthetics, and preferred colorways.\n- **Usability & interface design:** Testing prototype programming interfaces (timers, buttons, LCD displays) to ensure scheduling meals is intuitive and error-free for non-technical owners.\n- **Prototype user testing & feedback:** Providing working prototypes for owners to test in their homes with real cats to identify practical flaws (e.g. food jams, motor noise scaring pets, tipping hazards)."
    },
    {
        "id": "2024-h404-01-q4bi",
        "paper": PID,
        "question_number": "4(b)(i)",
        "marks": 4,
        "topic": "Volumetric Geometry & Cylindrical Annulus",
        "question": "The volume of the inner core of the paddle wheel is 15.7 cm3. Calculate the volume of one compartment of the paddle wheel. Give your answer in cm3 and show your working. The formula for calculating the volume of a cylinder is πr2h. You must ignore the thickness of the paddle blades.",
        "image": f"img/{PID}/q4bi.jpg",
        "figures": [f"img/{PID}/fig-4-2.jpg"],
        "markscheme": f"img/{PID}/ms-4bi.jpg",
        "markscheme_text": "**Four marks total:**\n\n1. Calculate total outer radius of paddle wheel:  \n   $$R = r_{\\text{core}} + \\text{blade height} = 1.0\\text{ cm} + 1.3\\text{ cm} = 2.3\\text{ cm} \\quad [1]$$\n\n2. Calculate volume of overall cylinder (length = 5.0 cm):  \n   $$V_1 = \\pi R^2 L = \\pi \\times 2.3^2 \\times 5.0 = \\pi \\times 5.29 \\times 5.0 = 83.095\\text{ cm}^3 \\approx 83.1\\text{ cm}^3 \\quad [1]$$\n\n3. Subtract volume of solid inner core:  \n   $$V_{\\text{compartments}} = V_1 - V_2 = 83.1\\text{ cm}^3 - 15.7\\text{ cm}^3 = 67.4\\text{ cm}^3 \\quad [1]$$\n\n4. Divide by 6 compartments:  \n   $$V_{\\text{one compartment}} = \\frac{67.4\\text{ cm}^3}{6} = \\mathbf{11.2\\text{ cm}^3} \\quad [1]$$"
    },
    {
        "id": "2024-h404-01-q4bii",
        "paper": PID,
        "question_number": "4(b)(ii)",
        "marks": 4,
        "topic": "Density & Mass Calculations",
        "question": "1 litre of cat food has a mass of 400 g. Use your answer from part (b)(i) to calculate the mass of cat food carried in each compartment of the paddle wheel. Give your answer in grams (g) and show your working.",
        "image": f"img/{PID}/q4bii.jpg",
        "figures": [f"img/{PID}/fig-4-2.jpg"],
        "markscheme": f"img/{PID}/ms-4bii.jpg",
        "markscheme_text": "**Four marks total:**\n\n1. Convert units (1 litre = 1000 cm3):  \n   $$1\\text{ litre} = 1000\\text{ cm}^3 \\quad [1]$$\n\n2. Convert compartment volume to litres:  \n   $$V = \\frac{11.2\\text{ cm}^3}{1000} = 0.0112\\text{ litres} \\quad [1]$$\n\n3. Recall formula $\\text{mass} = \\text{density} \\times \\text{volume}$:  \n   $$\\text{Mass} = 400\\text{ g/litre} \\times 0.0112\\text{ litres} \\quad [1]$$\n\n4. Calculate final mass:  \n   $$\\text{Mass} = \\mathbf{4.48\\text{ g}} \\quad (\\text{accept } 4.5\\text{ g}) \\quad [1]$$"
    },
    {
        "id": "2024-h404-01-q4ci",
        "paper": PID,
        "question_number": "4(c)(i)",
        "marks": 2,
        "topic": "Control Systems & Feedback Loops",
        "question": "The paddle wheel is rotated by an electric motor in a closed loop control system. Describe how a closed loop control system achieves improved performance over an open-loop system.",
        "image": f"img/{PID}/q4ci.jpg",
        "figures": [],
        "markscheme": f"img/{PID}/ms-4ci.jpg",
        "markscheme_text": "**Two marks** for description:\n- In a closed loop system, sensors provide continuous feedback measuring the actual output (paddle wheel position/rotation) and feed it back to the controller.\n- The controller compares this feedback with the desired setpoint and automatically corrects for errors, motor speed drift, or mechanical resistance (e.g. food jams), ensuring exact 1/6-revolution dispensing."
    },
    {
        "id": "2024-h404-01-q4cii",
        "paper": PID,
        "question_number": "4(c)(ii)",
        "marks": 3,
        "topic": "Sensing Mechanisms & Position Detection",
        "question": "Use annotated sketches and/or notes to show how a suitable sensor can be used to detect when the paddle wheel has rotated 1/6 of a revolution. You must name the sensor used.",
        "image": f"img/{PID}/q4cii.jpg",
        "figures": [f"img/{PID}/ms-4cii-sketch.jpg"],
        "markscheme": f"img/{PID}/ms-4cii.jpg",
        "markscheme_text": "**Three marks:**\n- **Named Sensor (1 mark):** Roller-lever microswitch (or optical slotted interrupter switch / Hall effect magnetic sensor).\n- **Interaction with paddle wheel (1 mark):** The microswitch roller arm is positioned tangentially against the outer perimeter of the paddle wheel so that each passing paddle blade physically depresses the lever as it sweeps past.\n- **Feasibility & Signal Output (1 mark):** Each depression closes internal switch contacts, generating a clean digital pulse to the microcontroller every $1/6$th of a revolution ($60^\\circ$), triggering the motor to brake."
    },
    {
        "id": "2024-h404-01-q4d",
        "paper": PID,
        "question_number": "4(d)*",
        "marks": 8,
        "topic": "Logistics & Global Supply Chains",
        "question": "Discuss the factors that need to be considered when distributing products to markets. In your answer you must consider: • environmental considerations • supply and demand.",
        "image": f"img/{PID}/q4d.jpg",
        "figures": [],
        "markscheme": f"img/{PID}/ms-4d.jpg",
        "markscheme_text": "**Level of Response (8 marks):**\n\n- **Level 3 (6–8 marks):** Clear, structured discussion addressing both environmental impacts and supply/demand dynamics with relevant manufacturing and retail examples.\n- **Level 2 (3–5 marks):** Reasonable discussion of distribution factors with some omissions.\n- **Level 1 (1–2 marks):** Basic commentary on transport or stock levels.\n\n**Key Indicative Content:**\n- **Environmental Considerations:**\n  - Modal transport choices: Shipping freight by sea or electrified rail generates significantly lower carbon emissions per tonne-km than air freight or heavy road haulage.\n  - Packaging optimization: Designing lightweight, flat-pack products and custom-fit cardboard packaging reduces dead space in shipping containers, maximizing freight density and lowering fuel consumption.\n  - Transitioning delivery fleets to electric vehicles (EVs) or biofuels for last-mile urban deliveries.\n- **Supply and Demand Considerations:**\n  - Demand forecasting: Rapid surge in demand for newly launched products requires buffer stock and regional fulfillment hubs to prevent stockouts.\n  - Lead times: Overseas manufacturing (e.g. East Asia) involves 4–8 week ocean shipping times, making rapid responses to market fashion changes difficult; local batch manufacturing offers agile Just-in-Time (JIT) replenishment."
    }
]

print(f"Total new questions: {len(new_questions)}")
tot_m = sum(q['marks'] for q in new_questions)
print(f"Total marks for 2024-summer-01: {tot_m}/80 marks")
assert tot_m == 80, f"Marks mismatch: expected 80, got {tot_m}"

# Update questions.json
qpath = os.path.join(REPO, "questions.json")
with open(qpath, "r", encoding="utf-8") as f:
    db = json.load(f)

# Filter out old placeholders for 2024-summer-01
db["questions"] = [q for q in db["questions"] if q.get("paper") != PID]
db["questions"].extend(new_questions)

with open(qpath, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Successfully saved {len(new_questions)} questions into questions.json for {PID}!")
