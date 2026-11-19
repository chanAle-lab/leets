"""
Build OCR H404/01 Principles of Design Engineering - Autumn 2021 (paper id 2021-autumn-01).
Total Marks: 80 marks across 23 subquestions.

Strict Separation & Ingestion Standards:
  - q.image: Question subpart prompt + 1-2 dotted answer lines / final answer prompt + mark allocation [X].
             Giant empty calculation boxes and 10-20 blank dotted lines collapsed/stitched.
  - q.figures: Preamble text, apparatus photos, tables, graphs, and exemplar diagrams.
  - q.markscheme: High-res stitched crops of MS table rows with autotrim of blank table areas.
  - Full KaTeX solutions & curriculum tags in questions.json.
"""

import os, json, re
import numpy as np
from PIL import Image, ImageDraw
import fitz

BASE_UP = r"C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded"
QP_PATH = os.path.join(BASE_UP, "media_1795105746534_6931e352.pdf")
MS_PATH = os.path.join(BASE_UP, "media_1795105746483_10f91230.pdf")

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PID = "2021-autumn-01"
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
    print(f"  {fname:18s} -> {out.size}")
    return out

print("\n--- 1. Cropping Resource Figures ---")
# Fig 1.1: Cordless electric screwdriver
stitch_vert([crop_area(qp, 2, 80, 375)], "fig-1-1.jpg")
# Table 1.2: Specification
stitch_vert([crop_area(qp, 4, 58, 205)], "table-1-2.jpg")
# Fig 1.3: Graph of motor current vs torque
stitch_vert([crop_area(qp, 5, 58, 315)], "fig-1-3.jpg")
# Fig 1.4: Circuit diagram
stitch_vert([crop_area(qp, 6, 58, 310)], "fig-1-4.jpg")
# MS Exemplar 1d: 3D Block Models
stitch_vert([crop_area(ms, 9, 65, 395, x0=135, x1=550)], "ms-1d-diagram.jpg")

# Fig 2.1: Zip-line basic design
stitch_vert([crop_area(qp, 10, 385, 578)], "fig-2-1.jpg")
# Fig 2.2: Zip-line start point details
stitch_vert([crop_area(qp, 11, 58, 285)], "fig-2-2.jpg")

# Fig 3.1 & 3.2: Light bulbs & Table 3.3
stitch_vert([crop_area(qp, 13, 58, 490)], "fig-3-1.jpg")

# Fig 4.1: Electrically powered cool box
stitch_vert([crop_area(qp, 16, 58, 386)], "fig-4-1.jpg")
# Fig 4.2: Handle photograph
stitch_vert([crop_area(qp, 18, 58, 274)], "fig-4-2.jpg")
# MS Exemplar 4dii: Handle failure sketch
stitch_vert([crop_area(ms, 19, 70, 325, x0=140, x1=550)], "ms-4dii-diagram.jpg")
# Table 4.3: Technical specification
stitch_vert([crop_area(qp, 20, 58, 222)], "table-4-3.jpg")
# MS Exemplar 4eii: Testing setup & flowchart
stitch_vert([
    crop_area(ms, 20, 95, 520, x0=140, x1=635),
    crop_area(ms, 21, 105, 500, x0=140, x1=580)
], "ms-4eii-diagram.jpg")

print("\n--- 2. Cropping Question Prompt Cards (Trimmed Answer Lines) ---")
# 1(a)(i) [2m] - Page 2
stitch_vert([crop_area(qp, 2, 375, 565)], "q1ai.jpg")

# 1(a)(ii) [2m] - Page 3
stitch_vert([
    crop_area(qp, 3, 58, 160),
    crop_area(qp, 3, 300, 342)
], "q1aii.jpg")

# 1(b)(i) [4m] - Page 4
stitch_vert([
    crop_area(qp, 4, 228, 280),
    crop_area(qp, 4, 358, 385),
    crop_area(qp, 4, 450, 470)
], "q1bi.jpg")

# 1(b)(ii) [3m] - Page 4
stitch_vert([
    crop_area(qp, 4, 475, 550),
    crop_area(qp, 4, 742, 775, x1=550)
], "q1bii.jpg")

# 1(c)(i) [1m] - Page 5
stitch_vert([crop_area(qp, 5, 335, 375)], "q1ci.jpg")

# 1(c)(ii) [2m] - Page 6
stitch_vert([
    crop_area(qp, 6, 245, 310),
    crop_area(qp, 6, 585, 626)
], "q1cii.jpg")

# 1(c)(iii) [2m] - Page 6
stitch_vert([
    crop_area(qp, 6, 630, 715),
    crop_area(qp, 6, 750, 775)
], "q1ciii.jpg")

# 1(c)(iv) [2m] - Page 7
stitch_vert([
    crop_area(qp, 7, 58, 165),
    crop_area(qp, 7, 210, 235)
], "q1civ.jpg")

# 1(d) [6m] - Page 8
stitch_vert([
    crop_area(qp, 8, 58, 185),
    crop_area(qp, 8, 185, 230),
    crop_area(qp, 8, 770, 780)
], "q1d.jpg")

# 2(a)(i) [2m] - Page 9
stitch_vert([
    crop_area(qp, 9, 68, 225),
    crop_area(qp, 9, 360, 400)
], "q2ai.jpg")

# 2(a)(ii) [3m] - Page 9
stitch_vert([
    crop_area(qp, 9, 415, 498),
    crop_area(qp, 9, 670, 715)
], "q2aii.jpg")

# 2(b)(i) [1m] - Page 10
stitch_vert([
    crop_area(qp, 10, 58, 120),
    crop_area(qp, 10, 168, 210)
], "q2bi.jpg")

# 2(b)(ii) [2m] - Page 10
stitch_vert([
    crop_area(qp, 10, 212, 252),
    crop_area(qp, 10, 342, 385)
], "q2bii.jpg")

# 2(c)(i) [3m] - Page 10
stitch_vert([
    crop_area(qp, 10, 580, 630),
    crop_area(qp, 10, 735, 778)
], "q2ci.jpg")

# 2(c)(ii) [4m] - Page 11
stitch_vert([
    crop_area(qp, 11, 290, 335),
    crop_area(qp, 11, 735, 770)
], "q2cii.jpg")

# 2(c)(iii) [4m] - Page 12
stitch_vert([
    crop_area(qp, 12, 58, 172),
    crop_area(qp, 12, 555, 595)
], "q2ciii.jpg")

# 3(a)(i) [2m] - Page 13
stitch_vert([crop_area(qp, 13, 492, 642)], "q3ai.jpg")

# 3(a)(ii)* [8m] - Page 14
stitch_vert([
    crop_area(qp, 14, 58, 198),
    crop_area(qp, 14, 202, 225),
    crop_area(qp, 14, 695, 718)
], "q3aii.jpg")

# 3(b) [4m] - Page 15
stitch_vert([
    crop_area(qp, 15, 58, 132),
    crop_area(qp, 15, 138, 160),
    crop_area(qp, 15, 242, 264),
    crop_area(qp, 15, 320, 352)
], "q3b.jpg")

# 4(a) [2m] - Page 16
stitch_vert([
    crop_area(qp, 16, 390, 465),
    crop_area(qp, 16, 468, 510),
    crop_area(qp, 16, 515, 572)
], "q4a.jpg")

# 4(b)(i) [1m] - Page 16
stitch_vert([crop_area(qp, 16, 578, 626)], "q4bi.jpg")

# 4(b)(ii) [2m] - Page 16
stitch_vert([
    crop_area(qp, 16, 630, 680),
    crop_area(qp, 16, 680, 705),
    crop_area(qp, 16, 750, 775)
], "q4bii.jpg")

# 4(c) [4m] - Page 17
stitch_vert([
    crop_area(qp, 17, 58, 150),
    crop_area(qp, 17, 150, 175),
    crop_area(qp, 17, 254, 278),
    crop_area(qp, 17, 332, 365)
], "q4c.jpg")

# 4(d)(i) [4m] - Page 18
stitch_vert([
    crop_area(qp, 18, 275, 325),
    crop_area(qp, 18, 325, 350),
    crop_area(qp, 18, 492, 514)
], "q4di.jpg")

# 4(d)(ii) [2m] - Page 18
stitch_vert([crop_area(qp, 18, 518, 770)], "q4dii.jpg")

# 4(e)(i) [2m] - Page 20
stitch_vert([
    crop_area(qp, 20, 225, 260),
    crop_area(qp, 20, 398, 440)
], "q4ei.jpg")

# 4(e)(ii) [6m] - Page 21
stitch_vert([crop_area(qp, 21, 58, 200)], "q4eii.jpg")

print("\n--- 3. Cropping Mark Schemes ---")
def ms_box(pno, y0=49, y1=549):
    return autotrim_table(crop_area(ms, pno, y0, y1, x0=36, x1=826))

stitch_vert([ms_box(5, 60, 240)], "ms-1ai.jpg")
stitch_vert([ms_box(5, 240, 520)], "ms-1aii.jpg")
stitch_vert([ms_box(5, 520, 550), ms_box(6, 49, 195)], "ms-1bi.jpg")
stitch_vert([ms_box(6, 195, 545)], "ms-1bii.jpg")
stitch_vert([ms_box(7, 60, 95)], "ms-1ci.jpg")
stitch_vert([ms_box(7, 95, 235)], "ms-1cii.jpg")
stitch_vert([ms_box(7, 235, 380)], "ms-1ciii.jpg")
stitch_vert([ms_box(7, 380, 545)], "ms-1civ.jpg")
stitch_vert([ms_box(8), ms_box(9, 49, 395)], "ms-1d.jpg")

stitch_vert([ms_box(9, 395, 545)], "ms-2ai.jpg")
stitch_vert([ms_box(10, 49, 230)], "ms-2aii.jpg")
stitch_vert([ms_box(10, 230, 350)], "ms-2bi.jpg")
stitch_vert([ms_box(10, 350, 545)], "ms-2bii.jpg")
stitch_vert([ms_box(11, 49, 545)], "ms-2ci.jpg")
stitch_vert([ms_box(12, 49, 545)], "ms-2cii.jpg")
stitch_vert([ms_box(13, 49, 420)], "ms-2ciii.jpg")

stitch_vert([ms_box(13, 420, 545)], "ms-3ai.jpg")
stitch_vert([ms_box(14), ms_box(15), ms_box(16, 49, 350)], "ms-3aii.jpg")
stitch_vert([ms_box(16, 350, 545)], "ms-3b.jpg")

stitch_vert([ms_box(17, 49, 270)], "ms-4a.jpg")
stitch_vert([ms_box(17, 270, 390)], "ms-4bi.jpg")
stitch_vert([ms_box(17, 390, 545)], "ms-4bii.jpg")
stitch_vert([ms_box(18, 49, 290)], "ms-4c.jpg")
stitch_vert([ms_box(18, 290, 545)], "ms-4di.jpg")
stitch_vert([ms_box(19, 49, 330)], "ms-4dii.jpg")
stitch_vert([ms_box(19, 330, 545)], "ms-4ei.jpg")
stitch_vert([ms_box(20), ms_box(21, 49, 545)], "ms-4eii.jpg")

print("\n--- 4. Registering Questions in questions.json ---")
P = f"img/{PID}/"

questions_2021_01 = [
    # 1(a)(i) [2m]
    {
        "id": f"{PID}-q1ai", "paper": PID, "question": "1(a)(i)", "marks": 2, "page": 2,
        "topics": ["1.1"], "skills": ["design"],
        "summary": "Identify two ways in which the electric screwdriver has been designed to be an inclusive and easy-to-use product.",
        "prompt": "Designers often aim to make their products inclusive so that they are easy-to-use by a wide range of users.<br><br>Identify <b>two</b> ways in which the electric screwdriver in Fig. 1.1 has been designed to be an inclusive and easy-to-use product. [2]",
        "figures": [P + "fig-1-1.jpg"],
        "image": P + "q1ai.jpg", "markscheme": P + "ms-1ai.jpg",
        "markscheme_text": "<b>1 mark per valid design feature (max 2 marks):</b><br>• The product can be used in either the left or right hand (ambidextrous design).<br>• The product has the bare minimum controls (just on/off trigger and reverse switch).<br>• No language barriers as controls are intuitive without complex visible text labelling.<br>• Intuitive operation requiring no instruction manual.<br>• Ergonomically contoured handle designed to fit comfortably in one hand with soft grip.<br>• Illumination light helps users with impaired or non-perfect eyesight in dark work spaces."
    },
    # 1(a)(ii) [2m]
    {
        "id": f"{PID}-q1aii", "paper": PID, "question": "1(a)(ii)", "marks": 2, "page": 3,
        "topics": ["5.1"], "skills": ["maths"],
        "summary": "Calculate the average time in seconds to manufacture one electric screwdriver given 1,000,000 units per year.",
        "prompt": "One million electric screwdrivers are manufactured every year using a high-volume production process.<br><br>The production runs continually for 365 days per year.<br><br>Calculate the average time in seconds to manufacture <b>one</b> electric screwdriver. Give your answer to <b>2 decimal places</b>. Show your working. [2]",
        "figures": [],
        "image": P + "q1aii.jpg", "markscheme": P + "ms-1aii.jpg",
        "markscheme_text": "<b>Method & Calculation (2 marks):</b><br>1. Calculate seconds in one year: $365 \\times 24 \\times 60 \\times 60 = 31\\,536\\,000\\text{ s}$ [1 mark]<br>2. Calculate time per unit: $\\frac{31\\,536\\,000}{1\\,000\\,000} = \\mathbf{31.54\\text{ seconds}}$ (to 2 d.p.) [1 mark]"
    },
    # 1(b)(i) [4m]
    {
        "id": f"{PID}-q1bi", "paper": PID, "question": "1(b)(i)", "marks": 4, "page": 4,
        "topics": ["6.1"], "skills": ["technical"],
        "summary": "Explain two reasons why the designer chose to use an epicyclic gearbox in the electric screwdriver.",
        "prompt": "The specification for the electric screwdriver is given in Table 1.2. The electric screwdriver uses an epicyclic gear system.<br><br>Explain <b>two</b> reasons why the designer chose to use an epicyclic gearbox in this product. [4]",
        "figures": [P + "table-1-2.jpg"],
        "image": P + "q1bi.jpg", "markscheme": P + "ms-1bi.jpg",
        "markscheme_text": "<b>Up to 2 marks per explained reason (max 4 marks):</b><br>• <b>Torque multiplication:</b> A gearbox is needed to increase torque output because raw high-speed motor torque is very small.<br>• <b>Co-linear shafts:</b> Epicyclic gearboxes have inline (co-linear) input and output shafts, enabling a slim, cylindrical screwdriver casing.<br>• <b>High torque capacity:</b> Load is distributed across multiple planet gears sharing the mesh, allowing compact gears to transmit high torque (4.5 Nm).<br>• <b>Compact volume:</b> High gear reduction in a small physical envelope allows a lightweight handheld tool."
    },
    # 1(b)(ii) [3m]
    {
        "id": f"{PID}-q1bii", "paper": PID, "question": "1(b)(ii)", "marks": 3, "page": 4,
        "topics": ["6.1"], "skills": ["maths", "technical"],
        "summary": "Calculate the rotational speed of the motor in rpm for a two-stage 7:1 epicyclic gearbox with 215 rpm output.",
        "prompt": "The epicyclic gearbox in the electric screwdriver consists of two identical stages. Each stage has a gear ratio of 7:1.<br><br>Use the information in Table 1.2 to calculate the rotational speed of the motor in the electric screwdriver. Give your answer in rpm and show your working. [3]",
        "figures": [P + "table-1-2.jpg"],
        "image": P + "q1bii.jpg", "markscheme": P + "ms-1bii.jpg",
        "markscheme_text": "<b>Calculation Steps (3 marks):</b><br>1. Total compound gear ratio: $GR = 7 \\times 7 = 49:1$ [1 mark]<br>2. Recall formula: $\\text{Input Speed} = GR \\times \\text{Output Speed}$ [1 mark]<br>3. Calculate motor speed: $\\text{Motor Speed} = 49 \\times 215 = \\mathbf{10\\,535\\text{ rpm}}$ [1 mark]"
    },
    # 1(c)(i) [1m]
    {
        "id": f"{PID}-q1ci", "paper": PID, "question": "1(c)(i)", "marks": 1, "page": 5,
        "topics": ["6.3"], "skills": ["technical", "maths"],
        "summary": "Use the graph in Fig. 1.3 to identify motor current when torque load is 0.04 Nm.",
        "prompt": "Use Fig. 1.3 to identify the current of the motor when the load on the motor is 0.04 Nm. [1]",
        "figures": [P + "fig-1-3.jpg"],
        "image": P + "q1ci.jpg", "markscheme": P + "ms-1ci.jpg",
        "markscheme_text": "• Read from graph at $0.04\\text{ Nm}$: $\\mathbf{1.25\\text{ A}}$ (allow 1.20 to 1.30 A) [1 mark]"
    },
    # 1(c)(ii) [2m]
    {
        "id": f"{PID}-q1cii", "paper": PID, "question": "1(c)(ii)", "marks": 2, "page": 6,
        "topics": ["6.3"], "skills": ["maths", "technical"],
        "summary": "Calculate the voltage across the 0.1 ohm sense resistor when motor current is 2.5 A.",
        "prompt": "Calculate the voltage across the 0.1 Ω resistor when the motor current is 2.5 A. Show your working. [2]",
        "figures": [P + "fig-1-4.jpg"],
        "image": P + "q1cii.jpg", "markscheme": P + "ms-1cii.jpg",
        "markscheme_text": "<b>Ohm's Law Calculation (2 marks):</b><br>1. Recall formula: $V = I \\times R$ [1 mark]<br>2. Calculation: $V = 2.5\\text{ A} \\times 0.1\\,\\Omega = \\mathbf{0.25\\text{ V}}$ [1 mark]"
    },
    # 1(c)(iii) [2m]
    {
        "id": f"{PID}-q1ciii", "paper": PID, "question": "1(c)(iii)", "marks": 2, "page": 6,
        "topics": ["6.3"], "skills": ["technical"],
        "summary": "Explain one reason why a capacitor is used in electronic systems.",
        "prompt": "Component c in Fig. 1.4 is a capacitor.<br><br>Explain <b>one</b> reason why a capacitor is used in electronic systems. [2]",
        "figures": [P + "fig-1-4.jpg"],
        "image": P + "q1ciii.jpg", "markscheme": P + "ms-1ciii.jpg",
        "markscheme_text": "<b>1 mark for function, 1 mark for explanation/effect (max 2 marks):</b><br>• <b>DC blocking / AC coupling:</b> Blocks direct current while allowing AC or signal pulses to pass.<br>• <b>Smoothing / Filtering:</b> Filters out unwanted high-frequency electrical noise and motor brush spikes from the signal line.<br>• <b>Decoupling / Supply stabilization:</b> Stores charge and discharges rapidly to stabilise power supply lines and prevent transient voltage drops during motor turn-on."
    },
    # 1(c)(iv) [2m]
    {
        "id": f"{PID}-q1civ", "paper": PID, "question": "1(c)(iv)", "marks": 2, "page": 7,
        "topics": ["6.3"], "skills": ["technical"],
        "summary": "Describe the effect the amplifier with voltage gain of 4 will have on the voltage signal.",
        "prompt": "The output voltage signal from the circuit in Fig. 1.4 is fed into an amplifier subsystem with a voltage gain of 4.<br><br>Describe the effect the amplifier will have on the voltage signal. [2]",
        "figures": [P + "fig-1-4.jpg"],
        "image": P + "q1civ.jpg", "markscheme": P + "ms-1civ.jpg",
        "markscheme_text": "• 1st mark: The amplifier will increase / magnify the amplitude of the voltage signal [1 mark]<br>• 2nd mark: The voltage signal will be multiplied by a factor of 4 (e.g. $0.25\\text{ V} \\to 1.0\\text{ V}$) [1 mark]"
    },
    # 1(d) [6m]
    {
        "id": f"{PID}-q1d", "paper": PID, "question": "1(d)", "marks": 6, "page": 8,
        "topics": ["1.2", "4.2"], "skills": ["practical", "design"],
        "summary": "Annotated sketches and notes showing how a non-functional 3D block model of the cordless screwdriver could be made.",
        "prompt": "During the development of an electric screwdriver, 3D block models would be made to test ergonomic factors and to communicate ideas with stakeholders.<br><br>Use annotated sketches and/or notes to show how a non-functional model of an electric screwdriver, such as the type shown in Fig. 1.1, could be made.<br><br>Identify any relevant equipment, materials and processes. [6]",
        "figures": [P + "fig-1-1.jpg", P + "ms-1d-diagram.jpg"],
        "image": P + "q1d.jpg", "markscheme": P + "ms-1d.jpg",
        "markscheme_text": "<b>Level 3 (5–6 marks):</b> Good detail of end-to-end process using technical terms, relevant equipment, and materials. Clear annotated sketches.<br><b>Level 2 (3–4 marks):</b> Sound detail with some technical terms and relevant stages.<br><b>Level 1 (1–2 marks):</b> Basic/limited.<br><br><b>Indicative Content:</b><br>• <b>Materials:</b> High-density modelling foam (styrofoam/polyurethane), MDF, clay, 3D printing filament (PLA/ABS), primer, filler, spray paint.<br>• <b>Equipment:</b> Hot-wire cutter, coping/bandsaw, rasps, files, glasspaper/sandpaper, CAD software, 3D printer or CNC router, spray booth.<br>• <b>Process:</b> Rough outline cut using hot wire/bandsaw; hand-sculpted with files and rasps to ergonomic profile; surfaces filled and fine-sanded; primed and spray painted to represent actual materials and textured over-moulding."
    },

    # 2(a)(i) [2m]
    {
        "id": f"{PID}-q2ai", "paper": PID, "question": "2(a)(i)", "marks": 2, "page": 9,
        "topics": ["4.2", "5.2"], "skills": ["maths", "practical"],
        "summary": "Convert 1/4 inch to mm and identify the most suitable drill bit from 3 mm to 8 mm.",
        "prompt": "A metal part is being manufactured using an old working drawing which has measurements in inches. A hole is required with a diameter of ¼ inch.<br><br>The drill bits available are: 3 mm, 4 mm, 5 mm, 6 mm, 7 mm, 8 mm.<br><br>(i) Assuming 1 inch = 25.4 mm, identify the drill bit that will drill a hole closest to the required size. Show your working. [2]",
        "figures": [],
        "image": P + "q2ai.jpg", "markscheme": P + "ms-2ai.jpg",
        "markscheme_text": "• Convert $\\frac{1}{4}$ inch: $0.25 \\times 25.4 = \\mathbf{6.35\\text{ mm}}$ [1 mark]<br>• Closest drill bit: $\\mathbf{6\\text{ mm}}$ (difference is 0.35 mm vs 0.65 mm for 7 mm) [1 mark]"
    },
    # 2(a)(ii) [3m]
    {
        "id": f"{PID}-q2aii", "paper": PID, "question": "2(a)(ii)", "marks": 3, "page": 9,
        "topics": ["5.2"], "skills": ["maths"],
        "summary": "Determine whether the 6 mm drill bit is within the +/- 5% tolerance for a 1/4 inch hole.",
        "prompt": "The tolerance for the ¼ inch hole is ± 5%.<br><br>Determine whether the drill bit you specified in part (a)(i) would produce a hole that is within this tolerance. State Yes or No. Show your working. [3]",
        "figures": [],
        "image": P + "q2aii.jpg", "markscheme": P + "ms-2aii.jpg",
        "markscheme_text": "<b>Tolerance Evaluation (3 marks):</b><br>1. Lower tolerance limit calculation: $95\\%$ of nominal $= 0.95 \\times 6.35 = 6.0325\\text{ mm}$ (or $6.35 - 0.3175 = 6.0325\\text{ mm}$) [2 marks]<br>2. Evaluation & conclusion: Since $6.0\\text{ mm} < 6.0325\\text{ mm}$, it is below the lower limit. The answer is **No** [1 mark]"
    },
    # 2(b)(i) [1m]
    {
        "id": f"{PID}-q2bi", "paper": PID, "question": "2(b)(i)", "marks": 1, "page": 10,
        "topics": ["5.2"], "skills": ["maths"],
        "summary": "Calculate the probability of a gear being faulty in a batch of 5000 with 80 faulty.",
        "prompt": "A polymer moulding manufacturer produced a batch of 5000 gears. Each gear was inspected and 80 gears were found to be faulty.<br><br>Calculate the probability of a gear being faulty in the batch. [1]",
        "figures": [],
        "image": P + "q2bi.jpg", "markscheme": P + "ms-2bi.jpg",
        "markscheme_text": "• Probability: $P = \\frac{80}{5000} = \\mathbf{0.016}$ (do not accept percentage or fraction) [1 mark]"
    },
    # 2(b)(ii) [2m]
    {
        "id": f"{PID}-q2bii", "paper": PID, "question": "2(b)(ii)", "marks": 2, "page": 10,
        "topics": ["5.2"], "skills": ["maths"],
        "summary": "Calculate the minimum number of gears that should be inspected to find one faulty gear.",
        "prompt": "Use your answer to part (b)(i) to calculate the minimum number of gears which should be inspected if the probability of a faulty gear remains the same. Show your working. [2]",
        "figures": [],
        "image": P + "q2bii.jpg", "markscheme": P + "ms-2bii.jpg",
        "markscheme_text": "• Number of gears: $\\frac{1}{P} = \\frac{1}{0.016} = 62.5$ [1 mark]<br>• Rounded up to whole integer: $\\mathbf{63\\text{ gears}}$ [1 mark]"
    },
    # 2(c)(i) [3m]
    {
        "id": f"{PID}-q2ci", "paper": PID, "question": "2(c)(i)", "marks": 3, "page": 10,
        "topics": ["6.2"], "skills": ["maths"],
        "summary": "Calculate the height h of the zip-line end point given a 2.8 m start, 30 m run, and 2.5 degree slope.",
        "prompt": "Fig. 2.1 shows the basic design for a zip-line for a children’s play park.<br><br>Calculate the height h in m. Give your answer to <b>1 decimal place</b> and show your working. Assume that the zip-line does not sag. [3]",
        "figures": [P + "fig-2-1.jpg"],
        "image": P + "q2ci.jpg", "markscheme": P + "ms-2ci.jpg",
        "markscheme_text": "<b>Trigonometric Calculation (3 marks):</b><br>1. Drop in height $y$: $\\tan(2.5^\\circ) = \\frac{y}{30}$ [1 mark]<br>2. Calculate $y$: $y = 30 \\times \\tan(2.5^\\circ) \\approx 1.3099\\text{ m}$ [1 mark]<br>3. Calculate final height $h$: $h = 2.8 - 1.3099 = 1.4901\\text{ m} \\approx \\mathbf{1.5\\text{ m}}$ [1 mark]"
    },
    # 2(c)(ii) [4m]
    {
        "id": f"{PID}-q2cii", "paper": PID, "question": "2(c)(ii)", "marks": 4, "page": 11,
        "topics": ["6.2"], "skills": ["maths"],
        "summary": "Calculate distance d at the zip-line support pole using the sine rule.",
        "prompt": "Fig. 2.2 shows construction details of the start point for the zip-line.<br><br>Calculate the distance d in m. Give your answer to <b>2 decimal places</b> and show your working. [4]",
        "figures": [P + "fig-2-2.jpg"],
        "image": P + "q2cii.jpg", "markscheme": P + "ms-2cii.jpg",
        "markscheme_text": "<b>Sine Rule Steps (4 marks):</b><br>1. Find third angle at apex: $A = 180^\\circ - 66^\\circ - 69^\\circ = 45^\\circ$ [1 mark]<br>2. Apply sine rule: $\\frac{d}{\\sin(66^\\circ)} = \\frac{3}{\\sin(45^\\circ)}$ [1 mark]<br>3. Rearrange: $d = \\frac{3 \\times \\sin(66^\\circ)}{\\sin(45^\\circ)}$ [1 mark]<br>4. Calculate: $d = \\frac{3 \\times 0.9135}{0.7071} = \\mathbf{3.88\\text{ m}}$ (to 2 d.p.) [1 mark]"
    },
    # 2(c)(iii) [4m]
    {
        "id": f"{PID}-q2ciii", "paper": PID, "question": "2(c)(iii)", "marks": 4, "page": 12,
        "topics": ["5.2"], "skills": ["maths"],
        "summary": "Calculate the probability of zip-line failure over a 25-year period (300 days/year, 1 in 25000 daily failure chance).",
        "prompt": "A risk assessment is carried out on the zip-line for the children’s play park. The assessment suggests there is a 1 in 25 000 chance of failure each day it is used.<br><br>Calculate the probability of failure over a 25-year period if the zip-line is used for 300 days per year.<br><br>Give your answer as a <b>percentage</b> and show your working. [4]",
        "figures": [],
        "image": P + "q2ciii.jpg", "markscheme": P + "ms-2ciii.jpg",
        "markscheme_text": "<b>Cumulative Probability Calculation (4 marks):</b><br>1. Daily probability of zero failure: $P(\\text{no failure}) = 1 - \\frac{1}{25\\,000} = 0.99996$ [1 mark]<br>2. Total days of use: $n = 300 \\times 25 = 7500\\text{ days}$ [1 mark]<br>3. Probability of zero failure over 25 years: $(0.99996)^{7500} \\approx 0.7408$ (or $0.74$) [1 mark]<br>4. Probability of at least one failure: $1 - 0.74 = 0.26 = \\mathbf{26\\%}$ (allow 25.9% to 26%) [1 mark]"
    },

    # 3(a)(i) [2m]
    {
        "id": f"{PID}-q3ai", "paper": PID, "question": "3(a)(i)", "marks": 2, "page": 13,
        "topics": ["1.1", "2.2"], "skills": ["design"],
        "summary": "Identify two design features of the LED bulb influenced by the style and function of the incandescent bulb.",
        "prompt": "In the 1980s, electric lighting was mainly provided by incandescent light bulbs. Incandescent light bulbs have now generally been replaced by light emitting diode (LED) light bulbs.<br><br>Identify <b>two</b> design features of the LED light bulb which have been influenced by the style and function of the incandescent light bulb. [2]",
        "figures": [P + "fig-3-1.jpg"],
        "image": P + "q3ai.jpg", "markscheme": P + "ms-3ai.jpg",
        "markscheme_text": "<b>1 mark per identified feature (max 2 marks):</b><br>• Same screw fitting / bayonet cap base (e.g. E27 Edison screw) for backward compatibility with existing domestic lamp holders.<br>• Similar physical dimensions and pear/globe bulb profile.<br>• Equivalent light output luminosity (800 lumens vs 820 lumens) to replace 60 W bulbs without modifying ambient light levels.<br>• Omni-directional light distribution diffuser dome mimicking transparent glass globe."
    },
    # 3(a)(ii)* [8m]
    {
        "id": f"{PID}-q3aii", "paper": PID, "question": "3(a)(ii)*", "marks": 8, "page": 14,
        "topics": ["2.1", "2.2", "5.1"], "skills": ["design"],
        "summary": "Discuss the impact of changing from incandescent to LED light bulbs on industry, user lifestyle, and the environment.",
        "prompt": "In 2009 the European Union (EU) began to ban the sale of incandescent light bulbs, forcing consumers to change to LED light bulbs.<br><br>Discuss the impact of changing from incandescent light bulbs to LED light bulbs.<br><br>In your answer you <b>must</b> refer to the impact on:<br>• industry<br>• the lifestyle of users<br>• the environment. [*8]",
        "figures": [P + "fig-3-1.jpg"],
        "image": P + "q3aii.jpg", "markscheme": P + "ms-3aii.jpg",
        "markscheme_text": "<b>Level 3 (6–8 marks):</b> Thorough discussion covering all 3 contexts (industry, user lifestyle, environment) with clear logical reasoning and substantiated examples.<br><b>Level 2 (3–5 marks):</b> Sound discussion covering at least 2 contexts.<br><b>Level 1 (1–2 marks):</b> Basic descriptive comments.<br><br><b>Indicative Content:</b><br>• <b>Industry:</b> Massive capital retooling from simple glass blowing and filament winding to automated surface-mount PCB assembly, semiconductor fabrication, and heatsink casting; retraining workforce; supply chain shifts towards electronic driver components.<br>• <b>User Lifestyle:</b> Vastly reduced frequency of bulb replacement due to 25,000-hour lifespan vs 1,200 hours; lower electricity bills (9 W vs 60 W saves >80% energy); smart lighting integration (colour tuning, mobile app dimming, IoT home automation).<br>• <b>Environment:</b> Drastic reduction in electricity generation demands cuts fossil fuel combustion and greenhouse gas emissions; however, disposal of LED circuitry involves electronic waste (WEEE) containing complex silicon, driver ICs, and aluminium heatsinks, requiring specialist recycling compared to inert tungsten."
    },
    # 3(b) [4m]
    {
        "id": f"{PID}-q3b", "paper": PID, "question": "3(b)", "marks": 4, "page": 15,
        "topics": ["5.1"], "skills": ["design"],
        "summary": "Describe two methods used by manufacturers to create more demand and maintain longer product popularity across the lifecycle.",
        "prompt": "The marketing lifecycle of a successful product can be divided into initial demand, growth in popularity and decline over time.<br><br>Describe <b>two</b> methods used by manufacturers to create more demand and maintain a longer product popularity. [4]",
        "figures": [],
        "image": P + "q3b.jpg", "markscheme": P + "ms-3b.jpg",
        "markscheme_text": "<b>Up to 2 marks per method (max 4 marks):</b><br>• <b>Incremental innovation & feature updates:</b> Regularly releasing updated versions with improved features, software updates, or new colourways/aesthetic trims to stimulate repeat purchases.<br>• <b>Celebrity endorsement & promotional marketing:</b> High-profile advertising campaigns, social media influencer partnerships, and viral marketing to boost brand awareness.<br>• <b>Product extensions & accessories:</b> Releasing complementary add-ons, attachments, or modular upgrades that extend usability.<br>• <b>Repositioning & re-branding:</b> Refreshing packaging, logos, and target demographics to enter new market segments."
    },

    # 4(a) [2m]
    {
        "id": f"{PID}-q4a", "paper": PID, "question": "4(a)", "marks": 2, "page": 16,
        "topics": ["3.1", "4.1"], "skills": ["technical"],
        "summary": "Identify two properties of thermo softening polymers which make them suitable for parts in an electrically powered cool box.",
        "prompt": "The electrically powered cool box shown in Fig. 4.1 is manufactured from multiple materials. Several different thermo softening polymers and several different metals are used.<br><br>Identify <b>two</b> properties of thermo softening polymers which make them suitable for the manufacture of parts in an electrically powered cool box. [2]",
        "figures": [P + "fig-4-1.jpg"],
        "image": P + "q4a.jpg", "markscheme": P + "ms-4a.jpg",
        "markscheme_text": "<b>1 mark per qualified property (max 2 marks):</b><br>• <b>Low thermal conductivity:</b> Insulates internal compartment against ambient heat transfer.<br>• <b>High impact resistance (toughness):</b> Withstands knocks, drops, and rough handling during portable outdoor transit.<br>• <b>Thermo-plasticity:</b> Softens when heated allowing complex ergonomic shapes, ribs, and double-wall casings to be injection moulded or blow moulded.<br>• <b>Corrosion resistance:</b> Impermeable to moisture and food spills, easy to wipe clean and hygienic.<br>• <b>High strength-to-weight ratio:</b> Keeps the portable unit light enough to carry when loaded."
    },
    # 4(b)(i) [1m]
    {
        "id": f"{PID}-q4bi", "paper": PID, "question": "4(b)(i)", "marks": 1, "page": 16,
        "topics": ["3.1"], "skills": ["technical"],
        "summary": "Identify one part in an electrically powered cool box that would be made from metal.",
        "prompt": "Identify <b>one</b> part in an electrically powered cool box that would be made from metal. [1]",
        "figures": [P + "fig-4-1.jpg"],
        "image": P + "q4bi.jpg", "markscheme": P + "ms-4bi.jpg",
        "markscheme_text": "• Any valid metal component: Peltier heatsink, fan motor shaft/windings, electrical wiring, fasteners/screws, handle pivot pins, PCB copper tracks. [1 mark]"
    },
    # 4(b)(ii) [2m]
    {
        "id": f"{PID}-q4bii", "paper": PID, "question": "4(b)(ii)", "marks": 2, "page": 16,
        "topics": ["3.1"], "skills": ["technical"],
        "summary": "State a metal used to manufacture the chosen cool box part and a property that makes it suitable.",
        "prompt": "State a metal that would be used to manufacture the part of the electrically powered cool box you have identified in part (b)(i). State a property of this metal that would make it suitable for use. [2]",
        "figures": [P + "fig-4-1.jpg"],
        "image": P + "q4bii.jpg", "markscheme": P + "ms-4bii.jpg",
        "markscheme_text": "• 1 mark for appropriate metal, 1 mark for matching property:<br>  - Heatsink: <b>Aluminium</b> → high thermal conductivity to dissipate heat rapidly from Peltier element.<br>  - Wires / PCB: <b>Copper</b> → high electrical conductivity.<br>  - Fasteners / Screws: <b>Steel / Stainless steel</b> → high tensile shear strength and thread hardness."
    },
    # 4(c) [4m]
    {
        "id": f"{PID}-q4c", "paper": PID, "question": "4(c)", "marks": 4, "page": 17,
        "topics": ["2.1", "5.1"], "skills": ["design"],
        "summary": "Describe two ways a manufacturer can ensure the cool box is successfully recovered and processed under EOL legislation.",
        "prompt": "End of life (EOL) legislation requires producers to be responsible for their products when they become waste.<br><br>Describe <b>two</b> ways in which a manufacturer can try to ensure that products, such as the electrically powered cool box, can be successfully recovered and effectively processed when they reach the end of their life. [4]",
        "figures": [],
        "image": P + "q4c.jpg", "markscheme": P + "ms-4c.jpg",
        "markscheme_text": "<b>Up to 2 marks per described method (max 4 marks):</b><br>• <b>Design for Disassembly (DfD):</b> Using snap fits, accessible screws, and modular sub-assemblies so polymers, electronics, and metals can be quickly separated without cutting or destruction.<br>• <b>Material marking & labelling:</b> Moulding standard ISO polymer identification codes (e.g. SPI resin codes >PP<, >ABS<) on plastic shells to facilitate sorting at recycling centres.<br>• <b>Product take-back & trade-in schemes:</b> Providing prepaid return postage or discounts on new models when consumers return old units to certified recovery centres."
    },
    # 4(d)(i) [4m]
    {
        "id": f"{PID}-q4di", "paper": PID, "question": "4(d)(i)", "marks": 4, "page": 18,
        "topics": ["1.1", "3.1", "6.2"], "skills": ["technical", "design"],
        "summary": "Describe how the performance of the polymer handle is enhanced by the visible design features in Fig. 4.2.",
        "prompt": "A photograph of the polymer handle of the electrically powered cool box is shown in Fig. 4.2.<br><br>The performance of the handle is enhanced by the design features visible in Fig. 4.2.<br><br>Describe how the performance of the handle is enhanced by its design. [4]",
        "figures": [P + "fig-4-2.jpg"],
        "image": P + "q4di.jpg", "markscheme": P + "ms-4di.jpg",
        "markscheme_text": "<b>Up to 4 marks for justified design features:</b><br>• <b>Truss / Cross-rib webbing:</b> Internal diagonal triangulation significantly increases bending stiffness (second moment of area) while minimizing polymer wall thickness and mass.<br>• <b>Material optimization & sink prevention:</b> Ribbed web prevents sink marks during injection moulding and cuts raw material volume, reducing cost and weight.<br>• <b>Flared ergonomic grip section:</b> Wider central span distributes carrying pressure across the palm to lower contact stress.<br>• <b>Textured grip:</b> Web openings and textured finish improve tactile grip friction even when carrying with wet hands."
    },
    # 4(d)(ii) [2m]
    {
        "id": f"{PID}-q4dii", "paper": PID, "question": "4(d)(ii)", "marks": 2, "page": 18,
        "topics": ["6.2"], "skills": ["technical"],
        "summary": "Sketch a diagram showing the likely mode of failure of the overloaded handle, marking the acting forces.",
        "prompt": "The handle is likely to break if the electrically powered cool box is carried when it is overloaded.<br><br>Sketch a diagram to show the likely mode of failure of the handle. Mark the forces acting on the handle. [2]",
        "figures": [P + "fig-4-2.jpg", P + "ms-4dii-diagram.jpg"],
        "image": P + "q4dii.jpg", "markscheme": P + "ms-4dii.jpg",
        "markscheme_text": "• 1 mark for sketch showing valid failure mode (tensile failure at central underside or shear fracture at hinge pivot brackets).<br>• 1 mark for clearly indicating opposing forces (upward lift force at centre and downward weight forces from cool box body at both ends)."
    },
    # 4(e)(i) [2m]
    {
        "id": f"{PID}-q4ei", "paper": PID, "question": "4(e)(i)", "marks": 2, "page": 20,
        "topics": ["6.3"], "skills": ["maths"],
        "summary": "Calculate the current in amps when the 42 W cool box is plugged into a 12 V supply.",
        "prompt": "Table 4.3 shows the technical specification for an electrically powered cool box.<br><br>Calculate the current in amps when the electrically powered cool box is plugged into a 12 V supply. Show your working. [2]",
        "figures": [P + "table-4-3.jpg"],
        "image": P + "q4ei.jpg", "markscheme": P + "ms-4ei.jpg",
        "markscheme_text": "<b>Power Formula Calculation (2 marks):</b><br>1. Recall formula: $I = \\frac{P}{V}$ [1 mark]<br>2. Substitute values: $I = \\frac{42\\text{ W}}{12\\text{ V}} = \\mathbf{3.5\\text{ A}}$ [1 mark]"
    },
    # 4(e)(ii) [6m]
    {
        "id": f"{PID}-q4eii", "paper": PID, "question": "4(e)(ii)", "marks": 6, "page": 21,
        "topics": ["5.2", "6.4", "6.5"], "skills": ["technical", "practical"],
        "summary": "Annotated sketches/notes outlining a prototype test to evaluate the 18 °C temperature reduction criterion.",
        "prompt": "At the prototype stage of development, the electrically powered cool box would be tested to ensure that it meets the technical specification.<br><br>Use annotated sketches and/or notes to:<br>• outline a test that could be carried out on the prototype electrically powered cool box to evaluate the maximum cooling criteria specified in Table 4.3<br>• identify any relevant equipment required<br>• show how the results would be used to assess the suitability of the prototype. [6]",
        "figures": [P + "table-4-3.jpg", P + "ms-4eii-diagram.jpg"],
        "image": P + "q4eii.jpg", "markscheme": P + "ms-4eii.jpg",
        "markscheme_text": "<b>Level 3 (5–6 marks):</b> Valid and rigorous test measuring both internal and external temperatures over time until thermal equilibrium; valid equipment identified (thermocouple/thermistor temperature probes, data logger/microcontroller, timer); clear explanation of evaluating $\\Delta T = T_{\\text{ext}} - T_{\\text{int}} \\ge 18^\\circ\\text{C}$.<br><b>Level 2 (3–4 marks):</b> Sound test with reasonable equipment and method.<br><b>Level 1 (1–2 marks):</b> Basic test description."
    }
]

# Update questions.json
qpath = os.path.join(REPO, "questions.json")
with open(qpath, "r", encoding="utf-8") as f:
    d = json.load(f)

paper_entry = {
    "id": PID,
    "code": "H404/01",
    "unit": "Principles of Design Engineering",
    "year": 2021,
    "level": "H404",
    "totalMarks": 80,
    "series": "Autumn"
}

# Update or insert paper entry
d["papers"] = [p for p in d["papers"] if p["id"] != PID]
d["papers"].append(paper_entry)

# Filter out old 2021-autumn-01 questions and append new authentic 23 questions
d["questions"] = [q for q in d["questions"] if q.get("paper") != PID] + questions_2021_01

with open(qpath, "w", encoding="utf-8") as f:
    json.dump(d, f, indent=2, ensure_ascii=False)

print(f"\n✓ Successfully registered {len(questions_2021_01)} questions totaling {sum(q['marks'] for q in questions_2021_01)} marks into questions.json!")
