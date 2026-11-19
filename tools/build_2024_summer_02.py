"""
Build OCR H404/02 Problem Solving in Design Engineering - June 2024 (paper id 2024-summer-02).
Total Marks: 70 marks across 8 questions.

Strict Separation & Ingestion Standards:
  - q.image: Question prompt cards with excess blank student answer lines collapsed.
  - q.figures: Full stimulus from Resource Booklet & exemplar mark scheme diagrams.
  - q.markscheme: High-res stitched crops of MS table rows with autotrim.
  - Full KaTeX mathematical solutions & curriculum tags in questions.json.
"""

import os, json
import numpy as np
from PIL import Image, ImageDraw
import fitz

BASE_UP = r"C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded"
QP_PATH = os.path.join(BASE_UP, "media_1795123383300_293be5ff.pdf")
RB_PATH = os.path.join(BASE_UP, "media_1795123383336_82cc0ca6.pdf")
MS_PATH = os.path.join(BASE_UP, "media_1795123383333_48259eea.pdf")

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PID = "2024-summer-02"
OUT_IMG = os.path.join(REPO, "img", PID)
os.makedirs(OUT_IMG, exist_ok=True)

qp = fitz.open(QP_PATH)
rb = fitz.open(RB_PATH)
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
    print(f"  {fname:28s} -> {out.size}")
    return out

print("\n--- 1. Cropping Resource Figures for Paper 2 ---")
# RB p2-3: Play area introduction, legislation & BS EN 1176 standards
stitch_vert([
    crop_area(rb, 2, 50, 780),
    crop_area(rb, 3, 50, 780)
], "rb-legislation-standards.jpg")

# RB p4: Cotton Mill Park case study & proposal (Fig. 4)
stitch_vert([crop_area(rb, 4, 50, 780)], "rb-cotton-mill-park.jpg")

# RB p5: Swing design Fig. 5 & rope specification Fig. 6
stitch_vert([crop_area(rb, 5, 50, 780)], "rb-swing-rope.jpg")

# RB p6: Decorative panel design Fig. 7 & CNC plasma cutter spec Fig. 8
stitch_vert([crop_area(rb, 6, 50, 780)], "rb-panel-plasma.jpg")

# RB p7: MB400 play area gate Fig. 9, LDR Fig. 10 & Solenoid Fig. 11
stitch_vert([crop_area(rb, 7, 50, 780)], "rb-gate-electronics.jpg")

# RB p8: Sustainability considerations (plastic, tyres, timber)
stitch_vert([crop_area(rb, 8, 50, 680)], "rb-sustainability.jpg")

# Exemplars from MS:
# MS p19: Electronic circuit diagram exemplar (Issue 1)
stitch_vert([crop_area(ms, 19, 140, 480, x0=180, x1=620)], "ms-4-circuit-ex1.jpg")

# MS p20: Op-amp comparator circuit diagram exemplar (Issue 1)
stitch_vert([crop_area(ms, 20, 140, 520, x0=180, x1=560)], "ms-4-circuit-ex2.jpg")

# MS p22: Lever / bell-crank amplification mechanism sketch (Issue 2)
stitch_vert([crop_area(ms, 22, 120, 550, x0=180, x1=640)], "ms-4-lever-sketch.jpg")


print("\n--- 2. Cropping Question Prompt Cards ---")
# q1.jpg
stitch_vert([
    crop_area(qp, 2, 85, 298),
    crop_area(qp, 2, 298, 335),
    crop_area(qp, 3, 745, 785)
], "q1.jpg")

# q2.jpg
stitch_vert([
    crop_area(qp, 4, 85, 285),
    crop_area(qp, 4, 285, 320),
    crop_area(qp, 5, 745, 785)
], "q2.jpg")

# q3ai.jpg
stitch_vert([
    crop_area(qp, 6, 60, 220),
    crop_area(qp, 6, 420, 465)
], "q3ai.jpg")

# q3aii.jpg
stitch_vert([
    crop_area(qp, 6, 470, 640),
    crop_area(qp, 6, 885, 920)
], "q3aii.jpg")

# q3aiii.jpg
stitch_vert([
    crop_area(qp, 7, 60, 135),
    crop_area(qp, 7, 360, 400)
], "q3aiii.jpg")

# q3b.jpg
stitch_vert([
    crop_area(qp, 7, 410, 640),
    crop_area(qp, 7, 885, 925)
], "q3b.jpg")

# q4.jpg
stitch_vert([
    crop_area(qp, 8, 60, 450)
], "q4.jpg")

# q5.jpg
stitch_vert([
    crop_area(qp, 13, 60, 285),
    crop_area(qp, 13, 285, 320),
    crop_area(qp, 14, 765, 800)
], "q5.jpg")


print("\n--- 3. Cropping Mark Schemes ---")
# ms-1.jpg (MS p8-10)
stitch_vert([
    crop_area(ms, 8, 125, 545, x0=45, x1=790),
    crop_area(ms, 9, 65, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 10, 65, 300, x0=45, x1=790))
], "ms-1.jpg")

# ms-2.jpg (MS p11-13)
stitch_vert([
    crop_area(ms, 11, 125, 545, x0=45, x1=790),
    crop_area(ms, 12, 65, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 13, 65, 300, x0=45, x1=790))
], "ms-2.jpg")

# ms-3ai.jpg (MS p14)
stitch_vert([autotrim_table(crop_area(ms, 14, 85, 545, x0=45, x1=790))], "ms-3ai.jpg")

# ms-3aii.jpg (MS p15)
stitch_vert([autotrim_table(crop_area(ms, 15, 85, 545, x0=45, x1=790))], "ms-3aii.jpg")

# ms-3aiii.jpg (MS p16)
stitch_vert([autotrim_table(crop_area(ms, 16, 85, 545, x0=45, x1=790))], "ms-3aiii.jpg")

# ms-3b.jpg (MS p17)
stitch_vert([autotrim_table(crop_area(ms, 17, 85, 545, x0=45, x1=790))], "ms-3b.jpg")

# ms-4.jpg (MS p18-23)
stitch_vert([
    crop_area(ms, 18, 65, 545, x0=45, x1=790),
    crop_area(ms, 19, 65, 545, x0=45, x1=790),
    crop_area(ms, 20, 65, 545, x0=45, x1=790),
    crop_area(ms, 21, 65, 545, x0=45, x1=790),
    crop_area(ms, 22, 65, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 23, 65, 300, x0=45, x1=790))
], "ms-4.jpg")

# ms-5.jpg (MS p24-26)
stitch_vert([
    crop_area(ms, 24, 65, 545, x0=45, x1=790),
    crop_area(ms, 25, 65, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 26, 65, 300, x0=45, x1=790))
], "ms-5.jpg")


print("\n--- 4. Assembling Questions JSON Entry for 2024-summer-02 ---")

new_questions = [
    {
        "id": "2024-h404-02-q1",
        "paper": PID,
        "question_number": "1*",
        "marks": 12,
        "topic": "Legislation & Industry Standards",
        "question": "Since the 5th century BC there has been evidence of play equipment used for the enjoyment of children. Whilst the basic concept has remained the same the technologies and legislation behind this equipment have changed significantly. A manufacturing company wishing to enter the play area market would need to explore relevant legislation and design standards. Critically examine the benefits of exploring legislation and associated design standards when entering a new market such as the play area market. In your answer you must consider the benefits to: • a manufacturing company • any other relevant stakeholders. Refer to information on pages 2 and 3 of the Resource Booklet.",
        "image": f"img/{PID}/q1.jpg",
        "figures": [f"img/{PID}/rb-legislation-standards.jpg"],
        "markscheme": f"img/{PID}/ms-1.jpg",
        "markscheme_text": "**Level of Response (12 marks):**\n\n- **Level 4 (10–12 marks):** Comprehensive, critically evaluative examination demonstrating clear understanding of statutory legislation (Occupiers' Liability Acts 1957 & 1984, Health and Safety at Work Act 1974) and voluntary British Standards (BS EN 1176). Fully evaluates impacts across at least three distinct stakeholder groups (manufacturing company, play area managers/local authorities, and children/parents).\n- **Level 3 (7–9 marks):** Good discussion of legislative and standardisation benefits across multiple stakeholders.\n- **Level 2 (4–6 marks):** Sufficient discussion identifying some legal and safety benefits.\n- **Level 1 (1–3 marks):** Basic points on safety or preventing injuries.\n\n**Key Indicative Content:**\n- **Benefits to Manufacturing Company:**\n  - **Legal compliance & liability protection:** Conforming to BS EN 1176 provides a recognised benchmark of due diligence, drastically mitigating product liability lawsuits and catastrophic recall costs.\n  - **Commercial advantage & market entry:** Local authorities, schools, and commercial developers mandate BS EN 1176 compliance in procurement tenders; certification unlocks premium pricing and builds brand trust.\n  - **Engineering clarity:** Standards provide explicit design limits (finger entrapment dimensions, free height of fall, impact-absorbing surfacing parameters, structural load safety factors).\n- **Benefits to Play Area Managers (Councils / Parks):**\n  - Meeting statutory duties under the Occupiers' Liability Acts protects managers from negligence claims in the event of an accident.\n  - Establishes standardised maintenance schedules, inspection logs, and replacement part specifications.\n- **Benefits to End Users (Children & Parents):**\n  - Reassurance that equipment is made from non-toxic, structurally tested, weather-resilient materials designed to prevent head/neck entrapment and fall injuries, encouraging active outdoor play."
    },
    {
        "id": "2024-h404-02-q2",
        "paper": PID,
        "question_number": "2*",
        "marks": 14,
        "topic": "Design for Manufacture (DFM) & Play Equipment",
        "question": "Page 4 in the Resource Booklet contains a case study for a series of play areas which were proposed for Cotton Mill Park. When designing the play equipment for Cotton Mill Park, designing for manufacture (DFM) played a key role. With specific reference to the Cotton Mill Park case study, discuss the considerations a Design Engineer would have to make in relation to DFM. In your answer you must consider the 4 key areas of DFM: 1) Planning 2) Scale of Production 3) Repair and Maintenance 4) Product Life. Refer to information on page 4 of the Resource Booklet.",
        "image": f"img/{PID}/q2.jpg",
        "figures": [f"img/{PID}/rb-cotton-mill-park.jpg"],
        "markscheme": f"img/{PID}/ms-2.jpg",
        "markscheme_text": "**Level of Response (14 marks):**\n\n- **Level 4 (12–14 marks):** Comprehensive, well-structured discussion addressing all four core DFM areas with specific application to the Cotton Mill Park case study (outdoor public play structures, recycled polymers, modular architecture).\n- **Level 3 (9–11 marks):** Good understanding of DFM covering at least three areas in relation to play equipment.\n- **Level 2 (5–8 marks):** Sufficient discussion covering at least two areas.\n- **Level 1 (1–4 marks):** Basic commentary with limited DFM insight.\n\n**Key Indicative Content Across 4 DFM Areas:**\n- **1. Planning:**\n  - Site survey and ground topography assessment (incorporating natural landscape, trees, drainage, and soil bearing capacity).\n  - CAD modelling, finite element stress analysis (FEA), and full-scale rapid prototyping of critical joints prior to costly production.\n- **2. Scale of Production:**\n  - Public play parks are one-off or small-batch installations tailored to specific local themes.\n  - Implementing a **modular architecture** (standardised posts, universal bracket collars, interchangeable platform decks, modular slides/climbers) allows bespoke layouts while achieving economies of scale in component manufacture.\n- **3. Repair and Maintenance:**\n  - Designing with standardised, off-the-shelf fasteners and replaceable wear parts (chains, shackles, swing bearings, rope terminations).\n  - Utilising tamper-resistant security fixings (e.g. Torx with center pin) to prevent vandalism, while allowing council maintenance crews easy access using standard municipal tools.\n  - Designing surfaces that resist graffiti and can be jet-washed without surface degradation.\n- **4. Product Life:**\n  - Material selection for harsh outdoor weather: Using recycled polymers (rPET/HDPE lumber) that simulate timber aesthetics without rotting, splintering, or needing periodic chemical preservatives.\n  - Galvanised and powder-coated steel posts with minimum 15–20 year design life, ensuring long-term structural integrity and resistance to UV embrittlement."
    },
    {
        "id": "2024-h404-02-q3ai",
        "paper": PID,
        "question_number": "3(a)(i)",
        "marks": 2,
        "topic": "Cross-Sectional Area Calculations",
        "question": "The designers of Cotton Mill Park have developed a design for a single swing shown on Page 5 of the Resource Booklet. The swing requires two ropes made from recycled polymer bottles. Calculate the cross-sectional area of the rope. Give your answer in m2 to 3 significant figures. Show your working. Use the formula: cross-sectional area = (π d^2) / 4. Refer to information on page 5 in the Resource Booklet, specifically Fig. 6.",
        "image": f"img/{PID}/q3ai.jpg",
        "figures": [f"img/{PID}/rb-swing-rope.jpg"],
        "markscheme": f"img/{PID}/ms-3ai.jpg",
        "markscheme_text": "**Two marks total:**\n\n1. Convert rope diameter to metres:  \n   $$d = 12\\text{ mm} = 0.012\\text{ m} \\quad [1]$$\n\n2. Calculate cross-sectional area in \\(\\text{m}^2\\) to 3 significant figures:  \n   $$A = \\frac{\\pi d^2}{4} = \\frac{\\pi \\times (0.012)^2}{4} = \\frac{\\pi \\times 1.44 \\times 10^{-4}}{4} = 1.13097 \\times 10^{-4}\\text{ m}^2 \\approx \\mathbf{1.13 \\times 10^{-4}\\text{ m}^2} \\quad [1]$$\n   *(or using \\(A = \\pi r^2 = \\pi \\times 0.006^2 = \\mathbf{1.13 \\times 10^{-4}\\text{ m}^2}\\))*"
    },
    {
        "id": "2024-h404-02-q3aii",
        "paper": PID,
        "question_number": "3(a)(ii)",
        "marks": 4,
        "topic": "Static Loads & Tensile Stress",
        "question": "A child with a mass of 78 kg sits on the swing seat, without swinging. Determine by calculation that the stress in one of the swing ropes is 3.39 MPa. Show your working. You must use your answer from part (a)(i) and the following information: 1 MPa = 1 × 106 N/m2, Gravitational field strength = 9.81 N/kg, stress = force / cross-sectional area.",
        "image": f"img/{PID}/q3aii.jpg",
        "figures": [f"img/{PID}/rb-swing-rope.jpg"],
        "markscheme": f"img/{PID}/ms-3aii.jpg",
        "markscheme_text": "**Four marks total:**\n\n1. Calculate total weight of the child:  \n   $$W = m \\times g = 78\\text{ kg} \\times 9.81\\text{ N/kg} = 765.18\\text{ N} \\quad [1]$$\n\n2. Calculate force acting on one of the two swing ropes:  \n   $$F = \\frac{W}{2} = \\frac{765.18\\text{ N}}{2} = 382.59\\text{ N} \\quad [1]$$\n\n3. Calculate tensile stress using \\(\\sigma = F / A\\):  \n   $$\\sigma = \\frac{382.59\\text{ N}}{1.13097 \\times 10^{-4}\\text{ m}^2} = 3\\,382\\,848\\text{ N/m}^2 \\quad [1]$$\n\n4. Convert to MPa and confirm:  \n   $$\\sigma = \\frac{3\\,382\\,848}{10^6} = \\mathbf{3.39\\text{ MPa}} \\quad (\\text{rounded to 2 d.p.}) \\quad [1]$$"
    },
    {
        "id": "2024-h404-02-q3aiii",
        "paper": PID,
        "question_number": "3(a)(iii)",
        "marks": 3,
        "topic": "Young's Modulus & Elastic Extension",
        "question": "Calculate the extension of a swing rope caused by a stress of 3.39 MPa. Give your answer in mm to 1 decimal place. Show your working. Refer to the information on page 5 of the Resource Booklet, specifically Fig. 5 and Fig. 6.",
        "image": f"img/{PID}/q3aiii.jpg",
        "figures": [f"img/{PID}/rb-swing-rope.jpg"],
        "markscheme": f"img/{PID}/ms-3aiii.jpg",
        "markscheme_text": "**Three marks total:**\n\n1. Calculate tensile strain using Young's modulus ($E = 480\\text{ MPa}$):  \n   $$\\varepsilon = \\frac{\\text{Stress}}{E} = \\frac{3.39\\text{ MPa}}{480\\text{ MPa}} = \\frac{3.39 \\times 10^6}{480 \\times 10^6} = 0.0070625 \\quad [1]$$\n\n2. Determine original length of rope from Fig. 5 dimensions:  \n   $$L_0 = 2010\\text{ mm} - 500\\text{ mm} = 1510\\text{ mm} \\quad [1]$$\n\n3. Calculate extension in mm to 1 decimal place:  \n   $$\\Delta L = L_0 \\times \\varepsilon = 1510\\text{ mm} \\times 0.0070625 = 10.664\\text{ mm} \\approx \\mathbf{10.7\\text{ mm}} \\quad [1]$$"
    },
    {
        "id": "2024-h404-02-q3b",
        "paper": PID,
        "question_number": "3(b)",
        "marks": 3,
        "topic": "CNC Machining & Toolpath Cutting Time",
        "question": "The manufacturer wants to add decorative panels to one of the play areas. The design of one of the decorative panels is shown on page 6 of the Resource Booklet. The panels will be cut from 12 mm thick aluminium using a MolsCat CNC plasma cutter. The specification for the plasma cutter is given on page 6 of the Resource Booklet. Calculate the time it would take for the MolsCat CNC plasma cutter to cut out one of the decorative panels. In your calculation include the cutting of the perimeter of the panel and the cutting of the inlay section. Give your answer in minutes and show your working. The inlay path length is 1260 mm. Refer to information on page 6 of the Resource Booklet, specifically Fig. 7 and Fig. 8.",
        "image": f"img/{PID}/q3b.jpg",
        "figures": [f"img/{PID}/rb-panel-plasma.jpg"],
        "markscheme": f"img/{PID}/ms-3b.jpg",
        "markscheme_text": "**Three marks total:**\n\n1. Calculate outside perimeter cutting path (700 mm × 500 mm):  \n   $$\\text{Outside path} = (2 \\times 700\\text{ mm}) + (2 \\times 500\\text{ mm}) = 1400 + 1000 = 2400\\text{ mm} \\quad [1]$$\n\n2. Calculate total toolpath cutting length:  \n   $$\\text{Total path} = 2400\\text{ mm} + 1260\\text{ mm} = 3660\\text{ mm} = 3.660\\text{ m} \\quad [1]$$\n\n3. Calculate machining time from cutting speed at 12 mm ($0.6\\text{ m/min}$):  \n   $$\\text{Time} = \\frac{\\text{Total path}}{\\text{Feed rate}} = \\frac{3.660\\text{ m}}{0.6\\text{ m/min}} = \\mathbf{6.1\\text{ minutes}} \\quad [1]$$"
    },
    {
        "id": "2024-h404-02-q4",
        "paper": PID,
        "question_number": "4",
        "marks": 16,
        "topic": "Electronic & Mechanical System Design",
        "question": "Designers are asked to modify the MB400 play area gate so that it locks during the hours of darkness. The design engineers have two issues that need to be overcome: Issue 1: An electronic system is required that will activate the LA080Z linear solenoid during the hours of darkness (when light falls to 10 lux and unlock at 100 lux), running off 12 volts using the NSL-19M51 LDR. Candidates must NOT use a microcontroller. Issue 2: The developers have discovered that the movement of the LA080Z linear solenoid (8 mm stroke) is not enough to move the bolt to lock the gate. The bolt needs to move through a distance of 24 mm. A mechanical system is required which will amplify the output motion of the linear solenoid to the required amount. Use annotated sketches and/or notes to determine suitable technical solutions that overcome the two issues identified. Refer to information on page 7 of the Resource Booklet.",
        "image": f"img/{PID}/q4.jpg",
        "figures": [
            f"img/{PID}/rb-gate-electronics.jpg",
            f"img/{PID}/ms-4-circuit-ex1.jpg",
            f"img/{PID}/ms-4-circuit-ex2.jpg",
            f"img/{PID}/ms-4-lever-sketch.jpg"
        ],
        "markscheme": f"img/{PID}/ms-4.jpg",
        "markscheme_text": "**16 marks total (8 marks for Issue 1 + 8 marks for Issue 2):**\n\n**Issue 1: Electronic System (8 marks - NO microcontroller allowed):**\n- **Input Potential Divider (2 marks):**\n  - LDR (NSL-19M51) placed in potential divider with a fixed/variable pull-up resistor.\n  - At 10 lux $R_{\\text{LDR}} = 20\\text{ k}\\Omega$; at 100 lux $R_{\\text{LDR}} = 5\\text{ k}\\Omega$.\n  - Resistor chosen in range $10\\text{ k}\\Omega$ to $22\\text{ k}\\Omega$ (or multi-turn potentiometer) so midpoint voltage swings reliably between light and dark.\n- **Process Circuit (3 marks):**\n  - Analogue comparator (e.g. LM741 / LM393 op-amp) comparing LDR divider voltage with a reference voltage set by a potentiometer.\n  - Alternatively, a Schmitt trigger comparator circuit to provide hysteresis between the 10 lux (lock) and 100 lux (unlock) thresholds, preventing switch chatter.\n- **Output Driver & Solenoid Protection (3 marks):**\n  - Power MOSFET (or Darlington pair / NPN transistor) capable of driving the $12\\text{V}$ solenoid current.\n  - Flyback protection diode connected in reverse-parallel across the solenoid coil to suppress inductive kickback voltages.\n\n**Issue 2: Mechanical Motion Amplification (8 marks):**\n- **Velocity Ratio & Distance Calculation (2 marks):**  \n  $$\\text{VR} = \\frac{\\text{Effort distance}}{\\text{Load distance}} = \\frac{8\\text{ mm}}{24\\text{ mm}} = \\frac{1}{3} \\quad (1:3\\text{ amplification})$$\n- **Mechanism Architecture & Lever Arms (2 marks):**\n  - Class 1 lever / bell-crank pivoted about a fixed fulcrum pin.\n  - Fulcrum-to-effort distance is exactly $1/3$ of the fulcrum-to-load distance (e.g. $x$ and $3x$, or $25\\text{ mm}$ and $75\\text{ mm}$).\n- **Linkages & Retaining Details (2 marks):**\n  - Solenoid plunger attached to short lever arm via a clevis pin and slotted link to accommodate angular arc motion without binding.\n  - Long arm linked to locking bolt sliding inside low-friction guide bushings (bronze or nylon).\n- **Feasibility & Direction Correctness (2 marks):**\n  - Correct motion sense: when solenoid pulls/pushes upon darkness, bolt extends into the gate frame striking plate to lock securely."
    },
    {
        "id": "2024-h404-02-q5",
        "paper": PID,
        "question_number": "5*",
        "marks": 16,
        "topic": "Sustainable Design & Material Circularity",
        "question": "Developers and local residents are keen for new children's outdoor public play areas to be built from sustainable materials. Discuss the sustainability issues relating to materials choice when developing new children's outdoor public play areas. In your answer you must consider: • recycling considerations • up-cycling possibilities • material availability • cost implications. Refer to information on page 8 of the Resource Booklet and also information from your own studies or experience.",
        "image": f"img/{PID}/q5.jpg",
        "figures": [f"img/{PID}/rb-sustainability.jpg"],
        "markscheme": f"img/{PID}/ms-5.jpg",
        "markscheme_text": "**Level of Response (16 marks):**\n\n- **Level 4 (13–16 marks):** Comprehensive, critically evaluative discussion exploring both positive environmental benefits and practical technical/commercial drawbacks across all four prompted areas (recycling, upcycling, material availability, cost implications), supported by specific engineering materials (e.g. rPET, rubber mulch from scrap tyres, reclaimed railway sleepers, FSC-certified timber).\n- **Level 3 (9–12 marks):** Good discussion covering at least three sustainability areas with relevant examples.\n- **Level 2 (5–8 marks):** Sufficient discussion covering at least two areas.\n- **Level 1 (1–4 marks):** Basic commentary on recycling or environmentally friendly materials.\n\n**Key Indicative Content Across 4 Prompt Areas:**\n- **1. Recycling Considerations:**\n  - Post-consumer polymers (HDPE milk jugs, PET bottles) sorted, shredded, and extruded into dense plastic lumber for climbing decks, posts, and swings.\n  - End-of-life scrap vehicle tyres granulated into rubber mulch or bonded with polyurethane resin for wet-pour safety surfacing, absorbing impact energy while diverting tyres from landfills.\n  - Challenges: Higher energy and sorting costs for contaminated recycled feedstocks; pigment limitations.\n- **2. Up-cycling Possibilities:**\n  - Repurposing untreated or reclaimed hardwood railway sleepers into retaining borders, sandpits, and seating benches.\n  - Embedding whole tyres as crawling tunnels, step platforms, or earth-retaining terraces, minimizing remanufacturing energy.\n  - Aesthetic uniqueness: Weathered patina provides organic play character that blends into park settings.\n- **3. Material Availability & Supply Chains:**\n  - Local availability: Using locally sourced municipal timber or domestic scrap reduces transport haulage carbon emissions compared to importing exotic hardwoods from abroad.\n  - Consistency of supply: Natural reclaimed items (sleepers, fallen timber) have irregular dimensions, requiring bespoke manual craftsmanship rather than automated mass production.\n- **4. Cost Implications:**\n  - Recycled plastic lumber has higher initial raw material procurement costs than virgin softwood, but dramatically lowers 20-year Life Cycle Cost (LCC) by eliminating rot, splintering, painting, and chemical preservative treatments.\n  - Insurance & certification costs: Reclaimed materials must undergo rigorous structural load testing and safety checks to ensure compliance with BS EN 1176."
    }
]

print(f"Total new questions: {len(new_questions)}")
tot_m = sum(q['marks'] for q in new_questions)
print(f"Total marks for 2024-summer-02: {tot_m}/70 marks")
assert tot_m == 70, f"Marks mismatch: expected 70, got {tot_m}"

# Update questions.json
qpath = os.path.join(REPO, "questions.json")
with open(qpath, "r", encoding="utf-8") as f:
    db = json.load(f)

# Filter out old placeholders for 2024-summer-02
db["questions"] = [q for q in db["questions"] if q.get("paper") != PID]
db["questions"].extend(new_questions)

with open(qpath, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Successfully saved {len(new_questions)} questions into questions.json for {PID}!")
