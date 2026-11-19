"""
Build OCR H404/02 Problem Solving in Design Engineering - Autumn 2021 (paper id 2021-autumn-02).
Total Marks: 70 marks across 8 questions.

Strict Separation & Ingestion Standards:
  - q.image: Question prompt + 1-2 dotted answer lines / final answer prompt + mark allocation [X].
             Giant empty calculation boxes and 10-20 blank dotted lines collapsed/stitched.
  - q.figures: Resource Booklet pages, apparatus photos, tables, graphs, and exemplar diagrams.
  - q.markscheme: High-res stitched crops of MS table rows with autotrim of blank table areas.
  - Full KaTeX solutions & curriculum tags in questions.json.
"""

import os, json
import numpy as np
from PIL import Image, ImageDraw
import fitz

BASE_UP = r"C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded"
QP_PATH = os.path.join(BASE_UP, "media_1795105746516_60b6853e.pdf")
MS_PATH = os.path.join(BASE_UP, "media_1795105746532_04c9f5e4.pdf")
RB_PATH = os.path.join(BASE_UP, "media_1795105746557_208d7d80.pdf")

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PID = "2021-autumn-02"
OUT_IMG = os.path.join(REPO, "img", PID)
os.makedirs(OUT_IMG, exist_ok=True)

qp = fitz.open(QP_PATH)
ms = fitz.open(MS_PATH)
rb = fitz.open(RB_PATH)
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

print("\n--- 1. Cropping Resource Booklet & Exemplar Figures ---")
# Resource Booklet Page 2: Air pollution & Fig. 1
stitch_vert([crop_area(rb, 2, 50, 780)], "rb-p2.jpg")
stitch_vert([crop_area(rb, 2, 480, 710)], "fig-1.jpg")

# Resource Booklet Page 3: Resources & Fig. 2 graph
stitch_vert([crop_area(rb, 3, 50, 780)], "rb-p3.jpg")
stitch_vert([crop_area(rb, 3, 175, 515)], "fig-2.jpg")

# Resource Booklet Page 4: The Snake WEC & Fig. 3
stitch_vert([crop_area(rb, 4, 50, 780)], "rb-p4.jpg")
stitch_vert([crop_area(rb, 4, 115, 510)], "fig-3.jpg")

# Resource Booklet Page 5: Pushrod movement & Fig. 4
stitch_vert([crop_area(rb, 5, 50, 780)], "rb-p5.jpg")
stitch_vert([crop_area(rb, 5, 55, 455)], "fig-4.jpg")

# Resource Booklet Page 6: Brinell Hardness Test & Fig. 5
stitch_vert([crop_area(rb, 6, 50, 780)], "rb-p6.jpg")
stitch_vert([crop_area(rb, 6, 55, 460)], "fig-5.jpg")

# Resource Booklet Page 7: Tether rope & Commercial viability & Fig. 6
stitch_vert([crop_area(rb, 7, 50, 780)], "rb-p7.jpg")
stitch_vert([crop_area(rb, 7, 145, 295)], "fig-6.jpg")

# MS Exemplar diagrams for Question 3
# Mechanism 3:1 multiplication sketch on MS Page 11
stitch_vert([crop_area(ms, 11, 180, 365, x0=130, x1=370)], "ms-3-mechanism.jpg")
# Flowchart on MS Page 12
stitch_vert([crop_area(ms, 12, 140, 450, x0=160, x1=310)], "ms-3-flowchart.jpg")
# Microcontroller / sensor / wireless block diagram on MS Page 13
stitch_vert([crop_area(ms, 13, 260, 320, x0=140, x1=510)], "ms-3-system.jpg")

print("\n--- 2. Cropping Question Prompt Cards (Trimmed Answer Lines) ---")
# Q1* [14m] - Page 2
stitch_vert([
    crop_area(qp, 2, 135, 265),
    crop_area(qp, 2, 268, 290)
], "q1.jpg")

# Q2 [14m] - Page 4
stitch_vert([
    crop_area(qp, 4, 58, 172),
    crop_area(qp, 4, 175, 198)
], "q2.jpg")

# Q3 [16m] - Page 6
stitch_vert([
    crop_area(qp, 6, 58, 536)
], "q3.jpg")

# Q4(a) [3m] - Page 11
stitch_vert([
    crop_area(qp, 11, 58, 360),
    crop_area(qp, 11, 735, 770)
], "q4a.jpg")

# Q4(b)(i) [3m] - Page 12
stitch_vert([
    crop_area(qp, 12, 58, 172),
    crop_area(qp, 12, 385, 422)
], "q4bi.jpg")

# Q4(b)(ii) [3m] - Page 12
stitch_vert([
    crop_area(qp, 12, 430, 505),
    crop_area(qp, 12, 715, 755)
], "q4bii.jpg")

# Q4(b)(iii) [3m] - Page 13
stitch_vert([
    crop_area(qp, 13, 58, 122),
    crop_area(qp, 13, 375, 412)
], "q4biii.jpg")

# Q5* [14m] - Page 14
stitch_vert([
    crop_area(qp, 14, 58, 288),
    crop_area(qp, 14, 295, 318)
], "q5.jpg")

print("\n--- 3. Cropping Mark Schemes ---")
def ms_box(pno, y0=49, y1=549):
    return autotrim_table(crop_area(ms, pno, y0, y1, x0=36, x1=826))

stitch_vert([ms_box(5), ms_box(6), ms_box(7, 49, 285)], "ms-1.jpg")
stitch_vert([ms_box(8), ms_box(9, 49, 545)], "ms-2.jpg")
stitch_vert([ms_box(10), ms_box(11), ms_box(12), ms_box(13, 49, 546)], "ms-3.jpg")
stitch_vert([ms_box(14, 60, 546)], "ms-4a.jpg")
stitch_vert([ms_box(15, 48, 285)], "ms-4bi.jpg")
stitch_vert([ms_box(15, 285, 545)], "ms-4bii.jpg")
stitch_vert([ms_box(16, 48, 545)], "ms-4biii.jpg")
stitch_vert([ms_box(17), ms_box(18), ms_box(19, 49, 435)], "ms-5.jpg")

print("\n--- 4. Registering Questions in questions.json ---")
P = f"img/{PID}/"

questions_2021_02 = [
    # Q1* [14m]
    {
        "id": f"{PID}-q1", "paper": PID, "question": "1*", "marks": 14, "page": 2,
        "topics": ["2.1", "5.1"], "skills": ["design"],
        "summary": "Discuss the impact that technological progression has had on the environment since the First Industrial Revolution.",
        "prompt": "Since the First Industrial Revolution, technology has been advancing at an increasing pace. For every advancement, there are consequences.<br><br>Discuss the impact that technological progression has had on the environment.<br><br>You <b>must</b> use your own examples of the effects that technological progression has had on the environment.<br><br>Refer to information on pages 2 and 3 of the Resource Booklet for additional support. [*14]",
        "figures": [P + "rb-p2.jpg", P + "fig-1.jpg", P + "rb-p3.jpg", P + "fig-2.jpg"],
        "image": P + "q1.jpg", "markscheme": P + "ms-1.jpg",
        "markscheme_text": "<b>Level 4 (11–14 marks):</b> Comprehensive discussion of environmental impacts with detailed analysis across energy, pollution, and resource depletion. Wide range of relevant technical examples.<br><b>Level 3 (7–10 marks):</b> Good discussion covering most key aspects with relevant examples.<br><b>Level 2 (4–6 marks):</b> Satisfactory discussion but lacks depth.<br><b>Level 1 (1–3 marks):</b> Limited descriptive comments.<br><br><b>Indicative Content:</b><br>• <b>Pollution:</b> Emissions of greenhouse gases ($CO_2$, $NO_x$, $SO_2$) leading to atmospheric warming, smog, and acid rain; chemical discharges and plastic pollution into aquatic ecosystems.<br>• <b>Natural Resource Depletion:</b> Unsustainable extraction of finite fossil fuels (oil, gas, coal), deforestation for industrial timber and agriculture, depletion of rare earth minerals (neodymium, lithium, cobalt) for consumer electronics.<br>• <b>Energy Consumption Growth:</b> Industrial automation, cloud data centres, electrified transport, and artificial heating/cooling escalating global primary energy demand as charted in Fig. 2.<br>• <b>Technological Solutions:</b> Rise of renewable energy (wind, solar, wave), circular economy closed-loop manufacturing, and environmental legislation mitigating legacy damage."
    },
    # Q2 [14m]
    {
        "id": f"{PID}-q2", "paper": PID, "question": "2", "marks": 14, "page": 4,
        "topics": ["2.1", "5.1"], "skills": ["design"],
        "summary": "Critically examine ways design engineers reduce environmental impacts of a chosen product across its 5 lifecycle stages.",
        "prompt": "Design engineers play an important role in the design of future technological products. They have the ability to minimise the negative impact that products have on the environment.<br><br>With reference to a product of your choice, critically examine the ways in which a design engineer can reduce the negative impact of that product on the environment throughout its lifecycle (raw material extraction, manufacture, distribution, use, disposal).<br><br>Refer to information on page 3 of the Resource Booklet. [14]",
        "figures": [P + "rb-p3.jpg"],
        "image": P + "q2.jpg", "markscheme": P + "ms-2.jpg",
        "markscheme_text": "<b>Level 4 (11–14 marks):</b> Comprehensive critical evaluation of ways design engineers reduce environmental impacts across all 5 lifecycle stages with clear justifications and specific technical strategies.<br><b>Level 3 (7–10 marks):</b> Good critical evaluation covering most lifecycle stages.<br><b>Level 2 (4–6 marks):</b> Adequate evaluation covering some stages.<br><b>Level 1 (1–3 marks):</b> Basic descriptive response.<br><br><b>Lifecycle Stages & Indicative Strategies:</b><br>• <b>1. Raw material extraction:</b> Selecting sustainably sourced, renewable, or post-consumer recycled materials (e.g. bio-based polymers, recycled aluminium); reducing raw material mass via generative design.<br>• <b>2. Manufacture:</b> Designing for minimal scrap / near-net-shape processing (injection moulding, additive manufacturing); reducing embedded energy and eliminating toxic solvents/finishes.<br>• <b>3. Distribution:</b> Designing compact, flat-pack, or nested geometries to maximise shipping pallet density and minimise logistics fuel; replacing plastic packaging with biodegradable mycelium or pulp.<br>• <b>4. Use phase:</b> Maximising operational energy efficiency (low-power microcontrollers, LED lighting, high thermal insulation); extending product durability via modular, easily replaceable wear components.<br>• <b>5. Disposal / End-of-Life:</b> Design for Disassembly (DfD) using standard fasteners rather than permanent adhesives; moulding SPI polymer resin codes for rapid robotic sorting; establishing circular take-back schemes."
    },
    # Q3 [16m]
    {
        "id": f"{PID}-q3", "paper": PID, "question": "3", "marks": 16, "page": 6,
        "topics": ["6.1", "6.3", "6.4"], "skills": ["technical", "design"],
        "summary": "Determine technical solutions for The Snake WEC: 3:1 frequency multiplying reciprocating-to-rotary mechanism, and wireless telemetry microcontroller counter.",
        "prompt": "An engineering company is developing a wave energy converter (WEC) to generate renewable electricity from the kinetic energy of waves on the sea. The name given to the prototype WEC is ‘The Snake’.<br><br>The Snake WEC is described on pages 4 and 5 of the Resource Booklet. The Snake is a modular product aimed at entrepreneurs who are interested in venturing into the renewable energy industry.<br><br>The design engineers have two issues to overcome:<br><b>Issue 1:</b> When on the sea, the movement of The Snake segments creates reciprocating motion of a pushrod shown in Fig. 4. A mechanical system is required to convert this input reciprocating motion into an output rotary motion to turn the generator axle and multiply the frequency by three (for each reciprocation, generator shaft rotates 3 times).<br><b>Issue 2:</b> Each prototype unit will contain a microcontroller system to record the total number of pushrod reciprocations, to be collected via wireless technology by engineers in a boat. A system diagram and a program flowchart are required, showing how an identified sensor detects pushrod reciprocations, records count, and transmits data wirelessly.<br><br>Use sketches and/or notes to determine suitable technical solutions that overcome the two issues identified.<br><br>Refer to information on pages 4 and 5 of the Resource Booklet. [16]",
        "figures": [P + "rb-p4.jpg", P + "fig-3.jpg", P + "rb-p5.jpg", P + "fig-4.jpg", P + "ms-3-mechanism.jpg", P + "ms-3-flowchart.jpg", P + "ms-3-system.jpg"],
        "image": P + "q3.jpg", "markscheme": P + "ms-3.jpg",
        "markscheme_text": "<b>Award up to 8 marks for Issue 1 and up to 8 marks for Issue 2 (Total 16 marks):</b><br><br><b>Issue 1 Breakdown (8 marks):</b><br>• <b>Reciprocating to Rotary conversion (4 marks):</b> Rack and pinion mechanism or slider-crank / scotch yoke arrangement clearly sketched and annotated; bidirectional clutch / freewheel / one-way sprag bearing mechanism to maintain unidirectional rotation.<br>• <b>3:1 Frequency Multiplication (4 marks):</b> Gear train with exact $3:1$ ratio (e.g. 60-tooth driver gear driving 20-tooth pinion, or 36T to 12T), or pulley/sprocket system with $3:1$ diameter ratio; correct gear meshing and axle bearings labelled.<br><br><b>Issue 2 Breakdown (8 marks):</b><br>• <b>Sensor & System Diagram (3 marks):</b> Identifies valid sensor (magnetic reed switch / Hall effect sensor with magnet on pushrod, optical interrupter, or limit microswitch); shows pushrod sensor inputting to microcontroller, outputting to wireless transmitter module (Bluetooth Low Energy, RF transceiver 433/868 MHz, or Wi-Fi).<br>• <b>Program Flowchart / Logic (5 marks):</b> Clear flowchart with Start block, initialising count `C = 0`, polling loop checking if sensor activated; debouncing delay/state check; incrementing counter `C = C + 1`; checking for wireless interrogation signal from boat; transmitting total count packet; looping back continually."
    },
    # Q4(a) [3m]
    {
        "id": f"{PID}-q4a", "paper": PID, "question": "4(a)", "marks": 3, "page": 11,
        "topics": ["3.1", "5.2"], "skills": ["maths", "technical"],
        "summary": "Calculate Brinell Hardness Number (BHN) for F=10 kN, D=10 mm, Di=0.60 mm and evaluate pushrod suitability (3900-4100 MPa).",
        "prompt": "During the development of The Snake prototype WEC described on pages 4 and 5 of the Resource Booklet, the design engineers used destructive testing techniques on materials in order to check their properties.<br><br>They chose to use the Brinell Hardness Test which is described on page 6 of the Resource Booklet.<br><br>When one material was tested, the following results were obtained:<br>• Force applied $F = 10\\text{ kN}$<br>• Indenter diameter $D = 10\\text{ mm}$<br>• Indentation diameter $D_i = 0.60\\text{ mm}$<br><br>The engineers require a material with a Brinell Hardness Number (BHN) between <b>3900 MPa</b> and <b>4100 MPa</b> for the pushrod.<br><br>Determine, by calculation, whether the material being tested is suitable for the pushrod. State <b>Yes</b> or <b>No</b> and show your working.<br><br>Refer to information on page 6 of the Resource Booklet. [3]",
        "figures": [P + "rb-p6.jpg", P + "fig-5.jpg"],
        "image": P + "q4a.jpg", "markscheme": P + "ms-4a.jpg",
        "markscheme_text": "<b>BHN Formula & Calculation (3 marks):</b><br>1. Formula from Resource Booklet:<br>$$\\text{BHN} = 102 \\times \\frac{2F}{\\pi D\\left(D - \\sqrt{D^2 - D_i^2}\\right)}$$<br>2. Substitute values ($F = 10\\text{ kN}$, $D = 10\\text{ mm}$, $D_i = 0.60\\text{ mm}$):<br>$$\\sqrt{D^2 - D_i^2} = \\sqrt{10^2 - 0.60^2} = \\sqrt{100 - 0.36} = \\sqrt{99.64} \\approx 9.98198\\text{ mm}$$<br>$$D - \\sqrt{D^2 - D_i^2} = 10 - 9.98198 = 0.018016\\text{ mm}$$<br>$$\\text{Denominator} = \\pi \\times 10 \\times 0.018016 = 0.565997$$<br>$$\\text{BHN} = 102 \\times \\frac{20}{0.565997} = 102 \\times 35.3359 = \\mathbf{3604\\text{ MPa}} \\quad (\\text{allow } 3600\\text{ to } 3605\\text{ MPa}) \\quad [2\\text{ marks}]$$<br>3. Suitability judgment: Since $3604\\text{ MPa}$ does not lie within the required range of $3900 - 4100\\text{ MPa}$, the material is <b>not suitable</b>. Answer: <b>No</b> [1 mark]"
    },
    # Q4(b)(i) [3m]
    {
        "id": f"{PID}-q4bi", "paper": PID, "question": "4(b)(i)", "marks": 3, "page": 12,
        "topics": ["5.2"], "skills": ["maths"],
        "summary": "Calculate the diameter in mm of the polymer rope given cross-sectional area of 2.84 x 10^-4 m^2.",
        "prompt": "During use at sea, The Snake described on pages 4 and 5 of the Resource Booklet is tethered to a fixed buoy by a rope as shown in Fig. 3. The design engineers responsible for The Snake want to calculate the diameter of the polymer rope.<br><br>Data for the rope under investigation is given in Fig. 6 on page 7 of the Resource Booklet ($A = 2.84 \\times 10^{-4}\\text{ m}^2$).<br><br>Calculate the diameter in mm of the polymer rope. Give your answer to <b>1 decimal place</b> and show your working. [3]",
        "figures": [P + "rb-p4.jpg", P + "fig-3.jpg", P + "rb-p7.jpg", P + "fig-6.jpg"],
        "image": P + "q4bi.jpg", "markscheme": P + "ms-4bi.jpg",
        "markscheme_text": "<b>Diameter Calculation (3 marks):</b><br>1. Area of circular cross-section: $A = \\frac{\\pi d^2}{4} \\implies d = \\sqrt{\\frac{4A}{\\pi}}$ [1 mark]<br>2. Substitute area $A = 2.84 \\times 10^{-4}\\text{ m}^2$:<br>$$d = \\sqrt{\\frac{4 \\times 2.84 \\times 10^{-4}}{\\pi}} = \\sqrt{\\frac{0.001136}{\\pi}} = \\sqrt{0.0003616} \\approx 0.019016\\text{ m} \\quad [1\\text{ mark}]$$<br>3. Convert to millimetres: $d = 0.019016 \\times 1000 = \\mathbf{19.0\\text{ mm}}$ (to 1 d.p.) [1 mark]"
    },
    # Q4(b)(ii) [3m]
    {
        "id": f"{PID}-q4bii", "paper": PID, "question": "4(b)(ii)", "marks": 3, "page": 12,
        "topics": ["6.2"], "skills": ["maths", "technical"],
        "summary": "Calculate tensile stress in N/m^2 in the polymer rope under a tensile force of 4200 N.",
        "prompt": "Tests have been carried out to determine that the average tensile force in the polymer rope will be 4200 N.<br><br>Calculate the tensile stress (in N/m²) in the polymer rope when the tensile force is 4200 N. Give your answer in N/m² and show your working. [3]",
        "figures": [P + "rb-p7.jpg", P + "fig-6.jpg"],
        "image": P + "q4bii.jpg", "markscheme": P + "ms-4bii.jpg",
        "markscheme_text": "<b>Tensile Stress Calculation (3 marks):</b><br>1. Recall formula: $\\sigma = \\frac{F}{A}$ [1 mark]<br>2. Substitute values ($F = 4200\\text{ N}$, $A = 2.84 \\times 10^{-4}\\text{ m}^2$):<br>$$\\sigma = \\frac{4200}{2.84 \\times 10^{-4}} = \\frac{4200}{0.000284} \\quad [1\\text{ mark}]$$<br>3. Calculate stress: $\\sigma = \\mathbf{14\\,788\\,732\\text{ N/m}^2}$ (allow $1.48 \\times 10^7\\text{ N/m}^2$ or $14.79\\text{ MPa}$) [1 mark]"
    },
    # Q4(b)(iii) [3m]
    {
        "id": f"{PID}-q4biii", "paper": PID, "question": "4(b)(iii)", "marks": 3, "page": 13,
        "topics": ["6.2"], "skills": ["maths", "technical"],
        "summary": "Calculate the extension of the 20 m polymer rope in metres using Young's modulus E = 1.3 x 10^9 N/m^2.",
        "prompt": "When the polymer rope is under tension it will stretch.<br><br>Calculate the extension of the polymer rope in m when the stress is at the value you calculated in part (b)(ii) ($\\sigma = 14\\,788\\,732\\text{ N/m}^2$, $L_0 = 20\\text{ m}$, $E = 1.3 \\times 10^9\\text{ N/m}^2$).<br><br>Give your answer to <b>3 decimal places</b> and show your working. [3]",
        "figures": [P + "rb-p7.jpg", P + "fig-6.jpg"],
        "image": P + "q4biii.jpg", "markscheme": P + "ms-4biii.jpg",
        "markscheme_text": "<b>Young's Modulus & Extension Steps (3 marks):</b><br>1. Recall relationships: $E = \\frac{\\text{Stress}}{\\text{Strain}} \\implies \\epsilon = \\frac{\\sigma}{E}$ [1 mark]<br>2. Calculate strain $\\epsilon$:<br>$$\\epsilon = \\frac{14\\,788\\,732}{1.3 \\times 10^9} \\approx 0.0113759 \\quad [1\\text{ mark}]$$<br>3. Calculate extension $\\Delta L = \\epsilon \\times L_0$ ($L_0 = 20\\text{ m}$):<br>$$\\Delta L = 0.0113759 \\times 20 = 0.2275\\text{ m} \\approx \\mathbf{0.228\\text{ m}} \\quad (\\text{to 3 d.p.}) \\quad [1\\text{ mark}]$$"
    },
    # Q5* [14m]
    {
        "id": f"{PID}-q5", "paper": PID, "question": "5*", "marks": 14, "page": 14,
        "topics": ["2.2", "5.1"], "skills": ["design"],
        "summary": "Critically evaluate any three factors influencing the commercial viability of The Snake WEC prototype.",
        "prompt": "The Snake WEC described on pages 4 and 5 of the Resource Booklet is a prototype product in the development stage.<br><br>The stakeholders of The Snake are concerned about its commercial viability and have asked for an evaluation of a range of factors:<br>• how well the product performs<br>• technical difficulty of manufacture and materials selection<br>• cost and profits<br>• maintenance requirements<br>• size and appearance.<br><br>Choose <b>any three</b> factors from the list above. Critically evaluate the ways in which they influence the commercial viability of The Snake.<br><br>Use information on pages 4, 5 and 7 of the Resource Booklet. [*14]",
        "figures": [P + "rb-p4.jpg", P + "fig-3.jpg", P + "rb-p5.jpg", P + "fig-4.jpg", P + "rb-p7.jpg"],
        "image": P + "q5.jpg", "markscheme": P + "ms-5.jpg",
        "markscheme_text": "<b>Level 4 (11–14 marks):</b> Comprehensive critical evaluation of 3 chosen factors with direct, detailed references to The Snake WEC, offshore deployment realities, and commercial financial viability.<br><b>Level 3 (7–10 marks):</b> Good critical evaluation of 3 factors with clear application.<br><b>Level 2 (4–6 marks):</b> Adequate evaluation of factors with general points.<br><b>Level 1 (1–3 marks):</b> Limited descriptive response.<br><br><b>Indicative Content for Factors:</b><br>• <b>How well the product performs:</b> Electrical power generation output (kWh) depends on ocean wave frequency and wave amplitude; irregular wave cycles cause fluctuating generation requiring complex onboard power conditioning; prototype efficiency vs theoretical maximum.<br>• <b>Technical difficulty of manufacture & materials selection:</b> Marine-grade materials essential (corrosion-resistant stainless steel 316, marine bronze, UV-stabilised composite polymers, antifouling coatings); dynamic waterproof seals around reciprocating pushrods must withstand high hydrostatic pressure without leaking; large fabrication tolerances.<br>• <b>Costs and profits:</b> High capital expenditure (CapEx) for tooling, fabrication, and specialised offshore towing vessels; long return on investment (payback period) reliant on government renewable feed-in tariffs; competitive levelized cost of energy (LCOE) compared to offshore wind and solar.<br>• <b>Maintenance requirements:</b> Offshore maintenance is notoriously hazardous and weather-dependent; salt encrustation, bio-fouling (barnacles/seaweed), and tether rope fatigue wear; remote wireless telemetry helps condition monitoring to avoid catastrophic offshore failure.<br>• <b>Size and appearance:</b> Low visual profile on the horizon reduces coastal NIMBY objections compared to towering wind turbines; modular scalable length allows flexible expansion based on client budget."
    }
]

# Update questions.json
qpath = os.path.join(REPO, "questions.json")
with open(qpath, "r", encoding="utf-8") as f:
    d = json.load(f)

paper_entry = {
    "id": PID,
    "code": "H404/02",
    "unit": "Problem Solving in Design Engineering",
    "year": 2021,
    "level": "H404",
    "totalMarks": 70,
    "series": "Autumn"
}

# Update or insert paper entry
d["papers"] = [p for p in d["papers"] if p["id"] != PID]
d["papers"].append(paper_entry)

# Filter out old 2021-autumn-02 questions and append new authentic 8 questions
d["questions"] = [q for q in d["questions"] if q.get("paper") != PID] + questions_2021_02

with open(qpath, "w", encoding="utf-8") as f:
    d_out = json.dump(d, f, indent=2, ensure_ascii=False)

print(f"\n✓ Successfully registered {len(questions_2021_02)} questions totaling {sum(q['marks'] for q in questions_2021_02)} marks into questions.json!")
