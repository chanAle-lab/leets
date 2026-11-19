"""
Build OCR H404/01 Principles of Design Engineering - June 2023 (paper id 2023-summer-01).
Total Marks: 80 marks across 25 questions.

Strict Separation & Ingestion Standards:
  - q.image: Question prompt + 1-2 dotted answer lines / final answer prompt + mark allocation [X].
             Giant empty calculation boxes and 10-20 blank dotted lines collapsed/stitched.
  - q.figures: Preamble text, apparatus photos, tables, graphs, and exemplar diagrams.
  - q.markscheme: High-res stitched crops of MS table rows with autotrim of blank table areas.
  - Full KaTeX solutions & curriculum tags in questions.json.
"""

import os, json
import numpy as np
from PIL import Image, ImageDraw
import fitz

BASE_UP = r"C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded"
QP_PATH = os.path.join(BASE_UP, "media_1795110317458_9f0b5576.pdf")
MS_PATH = os.path.join(BASE_UP, "media_1795110317414_cf04d1aa.pdf")

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PID = "2023-summer-01"
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
# Fig 1.1: Personal mini fan photo with labels (Page 2)
stitch_vert([crop_area(qp, 2, 60, 275)], "fig-1-1.jpg")

# Fig 1.2: Variable resistor circuit diagram (Page 4)
stitch_vert([crop_area(qp, 4, 120, 280)], "fig-1-2.jpg")

# Fig 1.3: Microcontroller and MOSFET circuit diagram (Page 5)
stitch_vert([crop_area(qp, 5, 60, 330)], "fig-1-3.jpg")

# Fig 2.1 & 2.2: Conical drill bit photo & cross section (Page 7)
stitch_vert([crop_area(qp, 7, 60, 298)], "fig-2-1.jpg")

# Fig 2.3: Corrugated polymer sheet photo + data table (Page 8)
stitch_vert([crop_area(qp, 8, 60, 440)], "fig-2-3.jpg")

# Fig 3.1: Sheet metal part photo (Page 10)
stitch_vert([crop_area(qp, 10, 230, 485)], "fig-3-1.jpg")

# Fig 4.1: Electric parking brake vs lever comparison photos (Page 13)
stitch_vert([crop_area(qp, 13, 60, 625)], "fig-4-1.jpg")

# Fig 4.2: Mechanical actuator gear system & cable distance diagrams (Page 14)
stitch_vert([crop_area(qp, 14, 60, 685)], "fig-4-2.jpg")

# Fig 4.3: Rotary control knob photo & Output A / B pulse waveforms (Page 17)
stitch_vert([crop_area(qp, 17, 60, 595)], "fig-4-3.jpg")

# Fig 4.4: Microcontroller flowchart algorithm for rotary encoder (Page 18)
stitch_vert([crop_area(qp, 18, 60, 755)], "fig-4-4.jpg")


print("\n--- 2. Cropping Question Prompt Cards (Trimmed Answer Lines) ---")
# 1(a) [2m] - Page 2
stitch_vert([
    crop_area(qp, 2, 282, 360),
    crop_area(qp, 2, 360, 385),
    crop_area(qp, 2, 412, 437),
    crop_area(qp, 2, 440, 472)
], "q1a.jpg")

# 1(b) [2m] - Page 2
stitch_vert([
    crop_area(qp, 2, 478, 515),
    crop_area(qp, 2, 515, 540),
    crop_area(qp, 2, 590, 620)
], "q1b.jpg")

# 1(c) [4m] - Page 3
stitch_vert([
    crop_area(qp, 3, 60, 122),
    crop_area(qp, 3, 122, 147),
    crop_area(qp, 3, 226, 252),
    crop_area(qp, 3, 305, 340)
], "q1c.jpg")

# 1(d)(i) [4m] - Page 4
stitch_vert([
    crop_area(qp, 4, 282, 355),
    crop_area(qp, 4, 595, 630)
], "q1di.jpg")

# 1(d)(ii) [2m] - Page 4
stitch_vert([
    crop_area(qp, 4, 632, 670),
    crop_area(qp, 4, 670, 695),
    crop_area(qp, 4, 748, 775)
], "q1dii.jpg")

# 1(d)(iii) [2m] - Page 5
stitch_vert([
    crop_area(qp, 5, 332, 365),
    crop_area(qp, 5, 365, 395),
    crop_area(qp, 5, 400, 430),
    crop_area(qp, 5, 462, 492)
], "q1diii.jpg")

# 1(d)(iv) [1m] - Page 5
stitch_vert([
    crop_area(qp, 5, 492, 532),
    crop_area(qp, 5, 532, 558),
    crop_area(qp, 5, 572, 602)
], "q1div.jpg")

# 1(d)(v) [2m] - Page 5
stitch_vert([
    crop_area(qp, 5, 602, 646),
    crop_area(qp, 5, 646, 672),
    crop_area(qp, 5, 722, 755)
], "q1dv.jpg")

# 1(e)* [8m] - Page 6
stitch_vert([
    crop_area(qp, 6, 60, 215),
    crop_area(qp, 6, 215, 250),
    crop_area(qp, 6, 765, 800)
], "q1e.jpg")

# 2(a) [4m] - Page 7
stitch_vert([
    crop_area(qp, 7, 300, 360),
    crop_area(qp, 7, 720, 755)
], "q2a.jpg")

# 2(b)(i) [1m] - Page 8
stitch_vert([
    crop_area(qp, 8, 445, 482),
    crop_area(qp, 8, 482, 510)
], "q2bi.jpg")

# 2(b)(ii) [3m] - Page 8
stitch_vert([
    crop_area(qp, 8, 510, 545),
    crop_area(qp, 8, 625, 660)
], "q2bii.jpg")

# 2(b)(iii) [2m] - Page 8
stitch_vert([
    crop_area(qp, 8, 662, 712),
    crop_area(qp, 8, 750, 785)
], "q2biii.jpg")

# 2(b)(iv) [5m] - Page 9
stitch_vert([
    crop_area(qp, 9, 60, 160),
    crop_area(qp, 9, 348, 375)
], "q2biv.jpg")

# 2(b)(v) [3m] - Page 9
stitch_vert([
    crop_area(qp, 9, 375, 555),
    crop_area(qp, 9, 735, 772)
], "q2bv.jpg")

# 3(a)(i) [2m] - Page 10
stitch_vert([
    crop_area(qp, 10, 60, 95),
    crop_area(qp, 10, 95, 120),
    crop_area(qp, 10, 195, 228)
], "q3ai.jpg")

# 3(a)(ii) [4m] - Page 10
stitch_vert([
    crop_area(qp, 10, 488, 532),
    crop_area(qp, 10, 532, 558),
    crop_area(qp, 10, 765, 800)
], "q3aii.jpg")

# 3(b)* [8m] - Page 11
stitch_vert([
    crop_area(qp, 11, 60, 240),
    crop_area(qp, 11, 240, 275),
    crop_area(qp, 12, 765, 800)
], "q3b.jpg")

# 4(a) [2m] - Page 13
stitch_vert([
    crop_area(qp, 13, 632, 670),
    crop_area(qp, 13, 670, 695),
    crop_area(qp, 13, 748, 775)
], "q4a.jpg")

# 4(b)(i) [4m] - Page 15
stitch_vert([
    crop_area(qp, 15, 60, 95),
    crop_area(qp, 15, 430, 465)
], "q4bi.jpg")

# 4(b)(ii) [3m] - Page 15
stitch_vert([
    crop_area(qp, 15, 465, 515),
    crop_area(qp, 15, 710, 748)
], "q4bii.jpg")

# 4(c)(i) [3m] - Page 17
stitch_vert([
    crop_area(qp, 17, 600, 622),
    crop_area(qp, 17, 622, 646),
    crop_area(qp, 17, 742, 768)
], "q4ci.jpg")

# 4(c)(ii) [4m] - Page 19
stitch_vert([
    crop_area(qp, 19, 60, 95),
    crop_area(qp, 19, 95, 120),
    crop_area(qp, 19, 278, 305)
], "q4cii.jpg")

# 4(c)(iii) [3m] - Page 19
stitch_vert([
    crop_area(qp, 19, 305, 448)
], "q4ciii.jpg")

# 4(c)(iv) [2m] - Page 19
stitch_vert([
    crop_area(qp, 19, 448, 578)
], "q4civ.jpg")


print("\n--- 3. Cropping Mark Schemes (Table Rows with Autotrim) ---")
# 1(a) [2m] - MS p8
stitch_vert([autotrim_table(crop_area(ms, 8, 85, 245, x0=45, x1=790))], "ms-1a.jpg")

# 1(b) [2m] - MS p8
stitch_vert([autotrim_table(crop_area(ms, 8, 245, 445, x0=45, x1=790))], "ms-1b.jpg")

# 1(c) [4m] - MS p8-9
stitch_vert([
    crop_area(ms, 8, 445, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 9, 85, 430, x0=45, x1=790))
], "ms-1c.jpg")

# 1(d)(i) [4m] - MS p9-10
stitch_vert([
    crop_area(ms, 9, 430, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 10, 85, 290, x0=45, x1=790))
], "ms-1di.jpg")

# 1(d)(ii) [2m] - MS p10
stitch_vert([autotrim_table(crop_area(ms, 10, 290, 415, x0=45, x1=790))], "ms-1dii.jpg")

# 1(d)(iii) [2m] - MS p10-11
stitch_vert([
    crop_area(ms, 10, 415, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 11, 85, 130, x0=45, x1=790))
], "ms-1diii.jpg")

# 1(d)(iv) [1m] - MS p11
stitch_vert([autotrim_table(crop_area(ms, 11, 130, 258, x0=45, x1=790))], "ms-1div.jpg")

# 1(d)(v) [2m] - MS p11
stitch_vert([autotrim_table(crop_area(ms, 11, 258, 545, x0=45, x1=790))], "ms-1dv.jpg")

# 1(e)* [8m] - MS p12-13
stitch_vert([
    crop_area(ms, 12, 85, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 13, 85, 220, x0=45, x1=790))
], "ms-1e.jpg")

# 2(a) [4m] - MS p14
stitch_vert([autotrim_table(crop_area(ms, 14, 85, 380, x0=45, x1=790))], "ms-2a.jpg")

# 2(b)(i) [1m] - MS p14
stitch_vert([autotrim_table(crop_area(ms, 14, 380, 430, x0=45, x1=790))], "ms-2bi.jpg")

# 2(b)(ii) [3m] - MS p14
stitch_vert([autotrim_table(crop_area(ms, 14, 430, 545, x0=45, x1=790))], "ms-2bii.jpg")

# 2(b)(iii) [2m] - MS p15
stitch_vert([autotrim_table(crop_area(ms, 15, 85, 545, x0=45, x1=790))], "ms-2biii.jpg")

# 2(b)(iv) [5m] - MS p16
stitch_vert([autotrim_table(crop_area(ms, 16, 85, 310, x0=45, x1=790))], "ms-2biv.jpg")

# 2(b)(v) [3m] - MS p16
stitch_vert([autotrim_table(crop_area(ms, 16, 310, 545, x0=45, x1=790))], "ms-2bv.jpg")

# 3(a)(i) [2m] - MS p17
stitch_vert([autotrim_table(crop_area(ms, 17, 85, 400, x0=45, x1=790))], "ms-3ai.jpg")

# 3(a)(ii) [4m] - MS p17-18
stitch_vert([
    crop_area(ms, 17, 400, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 18, 85, 235, x0=45, x1=790))
], "ms-3aii.jpg")

# 3(b)* [8m] - MS p18-20
stitch_vert([
    crop_area(ms, 18, 235, 545, x0=45, x1=790),
    crop_area(ms, 19, 85, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 20, 85, 380, x0=45, x1=790))
], "ms-3b.jpg")

# 4(a) [2m] - MS p21
stitch_vert([autotrim_table(crop_area(ms, 21, 85, 545, x0=45, x1=790))], "ms-4a.jpg")

# 4(b)(i) [4m] - MS p22
stitch_vert([autotrim_table(crop_area(ms, 22, 85, 545, x0=45, x1=790))], "ms-4bi.jpg")

# 4(b)(ii) [3m] - MS p23
stitch_vert([autotrim_table(crop_area(ms, 23, 85, 545, x0=45, x1=790))], "ms-4bii.jpg")

# 4(c)(i) [3m] - MS p24
stitch_vert([autotrim_table(crop_area(ms, 24, 85, 545, x0=45, x1=790))], "ms-4ci.jpg")

# 4(c)(ii) [4m] - MS p25
stitch_vert([autotrim_table(crop_area(ms, 25, 85, 300, x0=45, x1=790))], "ms-4cii.jpg")

# 4(c)(iii) [3m] - MS p25
stitch_vert([autotrim_table(crop_area(ms, 25, 300, 545, x0=45, x1=790))], "ms-4ciii.jpg")

# 4(c)(iv) [2m] - MS p26
stitch_vert([autotrim_table(crop_area(ms, 26, 85, 280, x0=45, x1=790))], "ms-4civ.jpg")

print("\n--- 4. Assembling Questions JSON Entry ---")

new_questions = [
    {
        "id": "2023-h404-01-q1a",
        "paper": PID,
        "question_number": "1(a)",
        "marks": 2,
        "topic": "Materials & Polymers",
        "question": "The flexible stem of the personal mini fan is covered with PVC. PVC is a thermo softening polymer. Identify two reasons why a thermo softening polymer is a suitable material for the flexible stem.",
        "image": f"img/{PID}/q1a.jpg",
        "figures": [f"img/{PID}/fig-1-1.jpg"],
        "markscheme": f"img/{PID}/ms-1a.jpg",
        "markscheme_text": "**Two marks** (one mark for each valid point explained):\n- Can be repeatedly bent, flexed, and adjusted without fatiguing, cracking, or permanently fracturing.\n- Can be easily injection moulded or extruded over the internal flexible metal wire armature.\n- Electrically insulating, protecting the user from any internal live wires.\n- Comfortable tactile feel, resistant to moisture/sweat, and non-toxic for everyday domestic handling."
    },
    {
        "id": "2023-h404-01-q1b",
        "paper": PID,
        "question_number": "1(b)",
        "marks": 2,
        "topic": "Mechanical Systems & Bearings",
        "question": "Explain why bearings are needed in mechanical systems such as those used in the personal mini fan.",
        "image": f"img/{PID}/q1b.jpg",
        "figures": [f"img/{PID}/fig-1-1.jpg"],
        "markscheme": f"img/{PID}/ms-1b.jpg",
        "markscheme_text": "**Two marks** for explaining the function of bearings:\n- Bearings locate and support the rotating motor shaft/fan hub, constraining radial and axial runout.\n- They reduce friction and wear between rotating parts and the housing, reducing power consumption, minimizing heat generation, and maximizing motor efficiency and lifespan."
    },
    {
        "id": "2023-h404-01-q1c",
        "paper": PID,
        "question_number": "1(c)",
        "marks": 4,
        "topic": "Product Architecture & Power Standards",
        "question": "The personal mini fan is powered by plugging it into a USB socket. Explain one benefit to the user and one benefit to the manufacturer of designing the personal mini fan to be powered by plugging it into a USB socket.",
        "image": f"img/{PID}/q1c.jpg",
        "figures": [f"img/{PID}/fig-1-1.jpg"],
        "markscheme": f"img/{PID}/ms-1c.jpg",
        "markscheme_text": "**Four marks** (up to 2 marks per benefit with explanation in context):\n\n**Benefit to user (2 marks):**\n- Universal compatibility: USB ports are ubiquitous across laptops, PCs, power banks, and phone chargers, allowing the fan to be operated anywhere without carrying dedicated power adapters or replacing batteries.\n\n**Benefit to manufacturer (2 marks):**\n- Standardised power supply (5 V DC) eliminates the need to include or safety-certify internal mains transformers or bulky battery compartments, significantly lowering manufacturing, tooling, and shipping costs."
    },
    {
        "id": "2023-h404-01-q1di",
        "paper": PID,
        "question_number": "1(d)(i)",
        "marks": 4,
        "topic": "Electrical Calculations & Power Dissipation",
        "question": "When variable resistor VR1 is set at 20 \\(\\Omega\\), the fan runs at half maximum speed with a current of 250 mA. Calculate the power dissipated in variable resistor VR1 when set at 20 \\(\\Omega\\). Give your answer in W and show your working.",
        "image": f"img/{PID}/q1di.jpg",
        "figures": [f"img/{PID}/fig-1-2.jpg"],
        "markscheme": f"img/{PID}/ms-1di.jpg",
        "markscheme_text": "**Four marks total:**\n\n1. Convert current to amperes:  \n   $$I = 250\\text{ mA} = 0.25\\text{ A}$$\n\n2. Recall and apply Ohm's law:  \n   $$V = I \\times R = 0.25\\text{ A} \\times 20\\text{ }\\Omega = 5.0\\text{ V}$$\n\n3. Calculate electrical power dissipated:  \n   $$P = I \\times V = 0.25\\text{ A} \\times 5.0\\text{ V} = \\mathbf{1.25\\text{ W}}$$\n\n*(Alternatively using \\(P = I^2 R\\): \\(P = (0.25)^2 \\times 20 = 0.0625 \\times 20 = \\mathbf{1.25\\text{ W}}\\))*"
    },
    {
        "id": "2023-h404-01-q1dii",
        "paper": PID,
        "question_number": "1(d)(ii)",
        "marks": 2,
        "topic": "Energy Efficiency & Thermal Management",
        "question": "Use your result from part d(i) to explain why using a variable resistor is not an efficient way of controlling the speed of a DC motor.",
        "image": f"img/{PID}/q1dii.jpg",
        "figures": [f"img/{PID}/fig-1-2.jpg"],
        "markscheme": f"img/{PID}/ms-1dii.jpg",
        "markscheme_text": "**Two marks** for explanation:\n- The variable resistor achieves speed reduction by dropping excess voltage and dissipating \\(1.25\\text{ W}\\) directly as wasted heat energy into the environment.\n- This wastes electrical energy from the USB supply/host device and can cause unwanted heating inside a small plastic device."
    },
    {
        "id": "2023-h404-01-q1diii",
        "paper": PID,
        "question_number": "1(d)(iii)",
        "marks": 2,
        "topic": "Electronic Components & Power Switching",
        "question": "Identify component Q and explain its function in the circuit.",
        "image": f"img/{PID}/q1diii.jpg",
        "figures": [f"img/{PID}/fig-1-3.jpg"],
        "markscheme": f"img/{PID}/ms-1diii.jpg",
        "markscheme_text": "**Two marks:**\n- **Identification (1 mark):** MOSFET (N-channel Field Effect Transistor) / Transistor / Solid-state switch.\n- **Function (1 mark):** Amplifies the low-current logic signal from the microcontroller output pin to switch the higher motor operating current on and off."
    },
    {
        "id": "2023-h404-01-q1div",
        "paper": PID,
        "question_number": "1(d)(iv)",
        "marks": 1,
        "topic": "Inductive Loads & Flyback Protection",
        "question": "Identify one reason for including diode D in the circuit.",
        "image": f"img/{PID}/q1div.jpg",
        "figures": [f"img/{PID}/fig-1-3.jpg"],
        "markscheme": f"img/{PID}/ms-1div.jpg",
        "markscheme_text": "**One mark:**\n- Protects switching transistor Q by safely dissipating back EMF / inductive kickback voltage spikes generated across the motor windings when switched off."
    },
    {
        "id": "2023-h404-01-q1dv",
        "paper": PID,
        "question_number": "1(d)(v)",
        "marks": 2,
        "topic": "Microcontrollers & Embedded Control",
        "question": "Despite the increased complexity, explain one reason why a designer might choose to use a microcontroller to control the motor.",
        "image": f"img/{PID}/q1dv.jpg",
        "figures": [f"img/{PID}/fig-1-3.jpg"],
        "markscheme": f"img/{PID}/ms-1dv.jpg",
        "markscheme_text": "**Two marks** for reason with development:\n- Allows Pulse Width Modulation (PWM) speed control, which maintains motor torque and achieves high power efficiency without dissipating heat.\n- Enables advanced programmable user features such as multi-speed presets, soft start, auto-off timers, or single push-button cycle control."
    },
    {
        "id": "2023-h404-01-q1e",
        "paper": PID,
        "question_number": "1(e)*",
        "marks": 8,
        "topic": "Sustainable Design & End-of-Life Disposal",
        "question": "The personal mini fan sells online for less than £4.00. It is classed as a novelty electrical item with an expected life of less than one year. Discuss the role of the designer in ensuring novelty electrical items of this type are disposed of responsibly at the end of their lives.",
        "image": f"img/{PID}/q1e.jpg",
        "figures": [f"img/{PID}/fig-1-1.jpg"],
        "markscheme": f"img/{PID}/ms-1e.jpg",
        "markscheme_text": "**Level of Response (8 marks):**\n\n- **Level 3 (6–8 marks):** Comprehensive, critically evaluative analysis covering product design strategies for responsible disposal, circular design, and legal frameworks.\n- **Level 2 (3–5 marks):** Competent discussion identifying relevant design strategies and disposal challenges.\n- **Level 1 (1–2 marks):** Basic points mentioning recycling or reducing waste.\n\n**Key Indicative Content:**\n- **Design for Disassembly (DfD):** Using snap-fits instead of permanent adhesives or ultrasonic welding so casing, motor, PCB, and wires can be separated easily in recycling facilities.\n- **Material Choice & Identification:** Moulding standardised polymer resin codes (e.g. PP, ABS) directly into plastic parts; avoiding composite or overmoulded blends that contaminate recycling streams.\n- **WEEE Directive & Labelling:** Including the crossed-out wheelie bin symbol and user disposal guidance.\n- **Design for Longevity:** Upgrading critical wear points (e.g. durable switches, modular replaceable blades) to extend the lifespan beyond novelty single-season use.\n- **Product Take-back & Circular Economy:** Facilitating deposit-return or manufacturer take-back schemes."
    },
    {
        "id": "2023-h404-01-q2a",
        "paper": PID,
        "question_number": "2(a)",
        "marks": 4,
        "topic": "Trigonometry & Engineering Geometry",
        "question": "Calculate the taper angle \\(\\theta\\) in degrees for the conical drill bit shown in Fig. 2.2. Give your answer to 1 decimal place and show your working.",
        "image": f"img/{PID}/q2a.jpg",
        "figures": [f"img/{PID}/fig-2-1.jpg"],
        "markscheme": f"img/{PID}/ms-2a.jpg",
        "markscheme_text": "**Four marks total:**\n\n1. Calculate the opposite side length (radius difference):  \n   $$\\text{Opposite} = \\frac{20\\text{ mm} - 8\\text{ mm}}{2} = 6.0\\text{ mm} \\quad [1]$$\n\n2. Identify hypotenuse:  \n   $$\\text{Hypotenuse} = 45\\text{ mm} \\quad [1]$$\n\n3. Set up sine trigonometric ratio:  \n   $$\\sin\\theta = \\frac{\\text{Opposite}}{\\text{Hypotenuse}} = \\frac{6.0}{45} = 0.1333 \\quad [1]$$\n\n4. Solve for \\(\\theta\\):  \n   $$\\theta = \\arcsin(0.1333) = 7.662^\\circ \\approx \\mathbf{7.7^\\circ} \\quad [1]$$"
    },
    {
        "id": "2023-h404-01-q2bi",
        "paper": PID,
        "question_number": "2(b)(i)",
        "marks": 1,
        "topic": "Manufacturing Processes & Polymers",
        "question": "Identify the industrial manufacturing process for corrugated polymer sheets of the type shown.",
        "image": f"img/{PID}/q2bi.jpg",
        "figures": [f"img/{PID}/fig-2-3.jpg"],
        "markscheme": f"img/{PID}/ms-2bi.jpg",
        "markscheme_text": "**One mark:**\n- **Extrusion** (profile extrusion / twin-wall sheet extrusion)."
    },
    {
        "id": "2023-h404-01-q2bii",
        "paper": PID,
        "question_number": "2(b)(ii)",
        "marks": 3,
        "topic": "Engineering Calculations & Volumetrics",
        "question": "Use the data in the table to calculate the volume of one flute in the corrugated polymer sheet. Give your answer in cm3 and show your working.",
        "image": f"img/{PID}/q2bii.jpg",
        "figures": [f"img/{PID}/fig-2-3.jpg"],
        "markscheme": f"img/{PID}/ms-2bii.jpg",
        "markscheme_text": "**Three marks total:**\n\n1. Internal cross-sectional area of one flute:  \n   $$\\text{Area} = 7.0\\text{ mm} \\times 7.0\\text{ mm} = 49.0\\text{ mm}^2 = 0.49\\text{ cm}^2 \\quad [1]$$\n\n2. Length of sheet:  \n   $$L = 500\\text{ mm} = 50.0\\text{ cm} \\quad [1]$$\n\n3. Calculate volume in \\(\\text{cm}^3\\):  \n   $$V = 0.49\\text{ cm}^2 \\times 50.0\\text{ cm} = \\mathbf{24.5\\text{ cm}^3} \\quad [1]$$\n   *(or \\(49\\text{ mm}^2 \\times 500\\text{ mm} = 24\\,500\\text{ mm}^3 = 24.5\\text{ cm}^3\\))*"
    },
    {
        "id": "2023-h404-01-q2biii",
        "paper": PID,
        "question_number": "2(b)(iii)",
        "marks": 2,
        "topic": "Volumetrics & Sheet Profiling",
        "question": "Use the data in the table and your answer to part (b)(ii) to calculate the total volume of all flutes in the corrugated polymer sheet. Give your answer in cm3 and show your working.",
        "image": f"img/{PID}/q2biii.jpg",
        "figures": [f"img/{PID}/fig-2-3.jpg"],
        "markscheme": f"img/{PID}/ms-2biii.jpg",
        "markscheme_text": "**Two marks total:**\n\n1. Number of flutes in 500 mm (0.5 m) width:  \n   $$N = \\frac{134}{2} = 67\\text{ flutes} \\quad [1]$$\n\n2. Total volume of all flutes:  \n   $$V_{\\text{total}} = 67 \\times 24.5\\text{ cm}^3 = \\mathbf{1641.5\\text{ cm}^3} \\quad [1]$$"
    },
    {
        "id": "2023-h404-01-q2biv",
        "paper": PID,
        "question_number": "2(b)(iv)",
        "marks": 5,
        "topic": "Solar Thermal Energy & Power Calculations",
        "question": "On a sunny day, the corrugated polymer sheet absorbs the sun's energy at a rate of 2.0 kW per m2. You will need to use the data in the table on page 8. Determine by calculation that the energy absorbed by the corrugated polymer sheet over a period of 15 minutes is 450 000 J. Show your working.",
        "image": f"img/{PID}/q2biv.jpg",
        "figures": [f"img/{PID}/fig-2-3.jpg"],
        "markscheme": f"img/{PID}/ms-2biv.jpg",
        "markscheme_text": "**Five marks total:**\n\n1. Calculate surface area in \\(\\text{m}^2\\):  \n   $$\\text{Area} = 0.5\\text{ m} \\times 0.5\\text{ m} = 0.25\\text{ m}^2 \\quad [1]$$\n\n2. Calculate power absorbed:  \n   $$P = 2.0\\text{ kW/m}^2 \\times 0.25\\text{ m}^2 = 0.5\\text{ kW} = 500\\text{ W} \\quad [1]$$\n\n3. Convert time to seconds:  \n   $$t = 15\\text{ minutes} \\times 60 = 900\\text{ s} \\quad [1]$$\n\n4. Apply energy formula \\(E = P \\times t\\):  \n   $$E = 500\\text{ W} \\times 900\\text{ s} \\quad [1]$$\n\n5. Final result confirmation:  \n   $$E = \\mathbf{450\\,000\\text{ J}} \\quad [1]$$"
    },
    {
        "id": "2023-h404-01-q2bv",
        "paper": PID,
        "question_number": "2(b)(v)",
        "marks": 3,
        "topic": "Thermodynamics & Specific Heat Capacity",
        "question": "It is assumed that all heat absorbed is transferred to the water. Calculate the temperature rise of the water to the nearest °C in the corrugated polymer sheet over a period of 15 minutes. Use information in part (iv) and the formula Q = mcΔT (m = 1.642 kg, c = 4200 J/kg°C). Show your working.",
        "image": f"img/{PID}/q2bv.jpg",
        "figures": [f"img/{PID}/fig-2-3.jpg"],
        "markscheme": f"img/{PID}/ms-2bv.jpg",
        "markscheme_text": "**Three marks total:**\n\n1. Rearrange formula for temperature change:  \n   $$\\Delta T = \\frac{Q}{m \\times c} \\quad [1]$$\n\n2. Substitute known values:  \n   $$\\Delta T = \\frac{450\\,000\\text{ J}}{1.642\\text{ kg} \\times 4200\\text{ J/(kg}\\cdot^\\circ\\text{C)}} = \\frac{450\\,000}{6896.4} = 65.25^\\circ\\text{C} \\quad [1]$$\n\n3. State answer to nearest whole °C:  \n   $$\\Delta T = \\mathbf{65^\\circ\\text{C}} \\quad [1]$$"
    },
    {
        "id": "2023-h404-01-q3ai",
        "paper": PID,
        "question_number": "3(a)(i)",
        "marks": 2,
        "topic": "Composite Materials & Textile Reinforcement",
        "question": "Describe, with an example, a way in which textiles can be used for reinforcement in engineered designs.",
        "image": f"img/{PID}/q3ai.jpg",
        "figures": [],
        "markscheme": f"img/{PID}/ms-3ai.jpg",
        "markscheme_text": "**Two marks** (one mark for description, one mark for valid engineered example):\n- **Description (1 mark):** Woven or knitted high-strength fibres (carbon, aramid/Kevlar, glass) are embedded within a thermosetting resin matrix to resist tensile stresses and inhibit crack propagation.\n- **Example (1 mark):** Carbon fibre reinforced polymer (CFRP) in bicycle frames/aerospace spars, or Kevlar plies embedded in tyre carcasses to resist punctures and high-speed centrifugal expansion."
    },
    {
        "id": "2023-h404-01-q3aii",
        "paper": PID,
        "question_number": "3(a)(ii)",
        "marks": 4,
        "topic": "Sheet Metal Fabrication & Batch Production",
        "question": "Describe the industrial manufacturing processes which would have been used to produce the sheet metal part shown (batch of 5000).",
        "image": f"img/{PID}/q3aii.jpg",
        "figures": [f"img/{PID}/fig-3-1.jpg"],
        "markscheme": f"img/{PID}/ms-3aii.jpg",
        "markscheme_text": "**Four marks** (up to 4 marks for detailing the sequence of industrial stages):\n- **1. Cutting internal slots/features:** CNC turret punch or CNC laser cutting machine to pierce internal slots and holes while flat.\n- **2. Profiling perimeter blank:** CNC shearing or laser profiling to cut the outer net boundary.\n- **3. Bending / Flanging:** CNC hydraulic press brake with punch-and-die tooling (or dedicated stamping press formers) to create precise right-angle bends.\n- **4. Finishing:** Deburring followed by powder coating, anodising (if aluminium), or electroplating for corrosion resistance and aesthetic durability."
    },
    {
        "id": "2023-h404-01-q3b",
        "paper": PID,
        "question_number": "3(b)*",
        "marks": 8,
        "topic": "Historical Pioneers & Technological Advancements",
        "question": "Historically, significant advances in design engineering have often been brought about by a key technical advancement. Choose one key technical advancement. Identify the key figure who brought about this technical advancement and evaluate how this technical advancement, along with the influence of the key figure, influenced design engineering.",
        "image": f"img/{PID}/q3b.jpg",
        "figures": [],
        "markscheme": f"img/{PID}/ms-3b.jpg",
        "markscheme_text": "**Level of Response (8 marks):**\n\n- **Level 3 (6–8 marks):** Clear, detailed understanding of a specific technical advancement, accurate attribution to a key historical pioneer, and comprehensive evaluation of short- and long-term impacts on design engineering.\n- **Level 2 (3–5 marks):** Sound understanding of the chosen advancement and pioneer with moderate evaluation.\n- **Level 1 (1–2 marks):** Basic identification of an inventor/invention with superficial commentary.\n\n**Exemplar Case Studies:**\n- **Guglielmo Marconi / Nikola Tesla (Wireless Radio Communication):** Enabled untethered signal transmission, transforming maritime safety, radar, telecommunications, and modern IoT/wireless sensor networks.\n- **Jack Kilby / Robert Noyce (Integrated Circuit):** Revolutionised electronic engineering by miniaturising transistors onto semiconductor silicon, enabling microprocessors, embedded control, and computing.\n- **James Watt (Separate Condenser Steam Engine):** Multiplied thermal efficiency, powering the Industrial Revolution, automated machinery, and establishing modern mechanical engineering."
    },
    {
        "id": "2023-h404-01-q4a",
        "paper": PID,
        "question_number": "4(a)",
        "marks": 2,
        "topic": "Automotive Systems & User Ergonomics",
        "question": "Explain one reason why a manufacturer might choose to install an electric parking brake rather than a lever-operated parking brake in a car.",
        "image": f"img/{PID}/q4a.jpg",
        "figures": [f"img/{PID}/fig-4-1.jpg"],
        "markscheme": f"img/{PID}/ms-4a.jpg",
        "markscheme_text": "**Two marks** for reason and justification:\n- **Cabin ergonomics & packaging:** Replacing the mechanical lever with an electronic switch frees substantial space in the center console for cup holders, wireless phone charging trays, or armrest storage.\n- **Automated driver assistance & accessibility:** Seamless integration with ECU allows automatic hold on hills, automatic release upon acceleration, and effortless operation for drivers with limited physical hand strength."
    },
    {
        "id": "2023-h404-01-q4bi",
        "paper": PID,
        "question_number": "4(b)(i)",
        "marks": 4,
        "topic": "Kinematics & Trigonometric Geometry",
        "question": "Use the information on page 14 to calculate distance L. Give your answer to the nearest mm and show your working.",
        "image": f"img/{PID}/q4bi.jpg",
        "figures": [f"img/{PID}/fig-4-2.jpg"],
        "markscheme": f"img/{PID}/ms-4bi.jpg",
        "markscheme_text": "**Four marks total:**\n\n1. Halve the given apex angle:  \n   $$\\text{Half angle} = \\frac{72^\\circ}{2} = 36^\\circ \\quad [1]$$\n\n2. Set up right-angled triangle with radius 40 mm:  \n   $$\\frac{L}{2} = 40 \\times \\sin(36^\\circ) \\quad [1]$$\n\n3. Calculate half distance:  \n   $$\\frac{L}{2} = 40 \\times 0.5878 = 23.51\\text{ mm} \\quad [1]$$\n\n4. Double and round to nearest whole mm:  \n   $$L = 2 \\times 23.51 = 47.02\\text{ mm} \\approx \\mathbf{47\\text{ mm}} \\quad [1]$$\n\n*(Cosine rule method: \\(L^2 = 40^2 + 40^2 - 2(40)(40)\\cos(72^\\circ) = 3200 - 3200(0.3090) = 2211.15 \\implies L = 47.02\\text{ mm} \\approx \\mathbf{47\\text{ mm}}\\))*"
    },
    {
        "id": "2023-h404-01-q4bii",
        "paper": PID,
        "question_number": "4(b)(ii)",
        "marks": 3,
        "topic": "Gear Trains & Worm Drives",
        "question": "Use the information on page 14 to calculate the number of revolutions of the worm wheel that are required to rotate the output gear through an angle of 72°. Show your working.",
        "image": f"img/{PID}/q4bii.jpg",
        "figures": [f"img/{PID}/fig-4-2.jpg"],
        "markscheme": f"img/{PID}/ms-4bii.jpg",
        "markscheme_text": "**Three marks total:**\n\n1. Calculate output gear revolutions:  \n   $$\\text{Output gear} = \\frac{72^\\circ}{360^\\circ} = 0.2\\text{ revolutions} \\quad [1]$$\n\n2. Apply compound gear ratio (60t / 15t = 4:1):  \n   $$\\text{Compound gear revolutions} = 0.2 \\times \\frac{60}{15} = 0.2 \\times 4 = 0.8\\text{ revolutions} \\quad [1]$$\n\n3. Multiply by worm wheel tooth count (60t single start):  \n   $$\\text{Worm screw revolutions} = 0.8 \\times 60 = \\mathbf{48\\text{ revolutions}} \\quad [1]$$"
    },
    {
        "id": "2023-h404-01-q4ci",
        "paper": PID,
        "question_number": "4(c)(i)",
        "marks": 3,
        "topic": "Sensors & Rotary Encoders",
        "question": "Describe how incremental rotary encoders can benefit design engineers.",
        "image": f"img/{PID}/q4ci.jpg",
        "figures": [f"img/{PID}/fig-4-3.jpg"],
        "markscheme": f"img/{PID}/ms-4ci.jpg",
        "markscheme_text": "**Three marks** (up to 3 marks for describing benefits):\n- **Direction and position sensing:** Quadrature 90° out-of-phase output pulses allow microcontrollers to reliably detect both speed of rotation and direction (clockwise vs anticlockwise).\n- **Continuous 360° infinite rotation:** Lacks physical mechanical end-stops, allowing a single dial to browse long menus or adjust settings across multiple modes.\n- **Digital reliability & tactile detents:** Offers crisp click feedback without electrical potentiometer wiper wear, providing durable, bounce-free digital integration."
    },
    {
        "id": "2023-h404-01-q4cii",
        "paper": PID,
        "question_number": "4(c)(ii)",
        "marks": 4,
        "topic": "Control Flow & Quadrature Decoding",
        "question": "Use the information on pages 17 and 18 to describe how the system provides audible feedback to the user when the control knob is rotated clockwise.",
        "image": f"img/{PID}/q4cii.jpg",
        "figures": [f"img/{PID}/fig-4-3.jpg", f"img/{PID}/fig-4-4.jpg"],
        "markscheme": f"img/{PID}/ms-4cii.jpg",
        "markscheme_text": "**Four marks total:**\n- When turned clockwise, Output A goes high before Output B (1).\n- Flowchart reaches the decision diamond 'Is input A high?' and branches YES (1).\n- It then reaches 'Is input B high?' which is currently NO (1).\n- This routes execution to the left branch, executing 'High beep for 0.2s', providing immediate audible feedback to the driver (1)."
    },
    {
        "id": "2023-h404-01-q4ciii",
        "paper": PID,
        "question_number": "4(c)(iii)",
        "marks": 3,
        "topic": "Binary Counters & Microcontroller Variables",
        "question": "The flowchart program is restarted from the START command and the control knob is rotated five clicks clockwise. Write down the values of variables A, B and C after the fifth click.",
        "image": f"img/{PID}/q4ciii.jpg",
        "figures": [f"img/{PID}/fig-4-4.jpg"],
        "markscheme": f"img/{PID}/ms-4ciii.jpg",
        "markscheme_text": "**Three marks:**\n- The program functions as a 3-bit binary counter where C is bit 2 ($2^2=4$), B is bit 1 ($2^1=2$), and A is bit 0 ($2^0=1$).\n- Starting at 0, five clockwise clicks increment the counter to $5_{10} = 101_2$:\n  - **Variable A = 1** (1 mark)\n  - **Variable B = 0** (1 mark)\n  - **Variable C = 1** (1 mark)"
    },
    {
        "id": "2023-h404-01-q4civ",
        "paper": PID,
        "question_number": "4(c)(iv)",
        "marks": 2,
        "topic": "Binary Counters & Logic Decrementing",
        "question": "The control knob is then rotated two clicks anticlockwise. Write down the new values of variables A, B and C.",
        "image": f"img/{PID}/q4civ.jpg",
        "figures": [f"img/{PID}/fig-4-4.jpg"],
        "markscheme": f"img/{PID}/ms-4civ.jpg",
        "markscheme_text": "**Two marks:**\n- Two anticlockwise clicks decrement the binary count from 5 down to 3 ($5 - 2 = 3_{10} = 011_2$):\n  - **Variable A = 1**\n  - **Variable B = 1**\n  - **Variable C = 0**"
    }
]

print(f"Total new questions: {len(new_questions)}")
tot_m = sum(q['marks'] for q in new_questions)
print(f"Total marks for 2023-summer-01: {tot_m}/80 marks")
assert tot_m == 80, f"Marks mismatch: expected 80, got {tot_m}"

# Update questions.json
qpath = os.path.join(REPO, "questions.json")
with open(qpath, "r", encoding="utf-8") as f:
    db = json.load(f)

# Filter out old placeholders for 2023-summer-01
db["questions"] = [q for q in db["questions"] if q.get("paper") != PID]
db["questions"].extend(new_questions)

with open(qpath, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Successfully saved {len(new_questions)} questions into questions.json for {PID}!")
