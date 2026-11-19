"""
Build OCR H404/01 Principles of Design Engineering - June 2022 (paper id 2022-summer-01).
Total Marks: 80 marks across 27 questions.

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
QP_PATH = os.path.join(BASE_UP, "media_1795108912081_23810779.pdf")
MS_PATH = os.path.join(BASE_UP, "media_1795108912130_b247de5e.pdf")

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PID = "2022-summer-01"
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
    print(f"  {fname:22s} -> {out.size}")
    return out

print("\n--- 1. Cropping Resource Figures ---")
# Fig 1.1: Electric scooter photo
stitch_vert([crop_area(qp, 2, 80, 450)], "fig-1-1.jpg")
# Fig 1.2: Handlebar controls photo
stitch_vert([crop_area(qp, 2, 450, 680)], "fig-1-2.jpg")
# Fig 1.3: Battery cells circuit
stitch_vert([crop_area(qp, 4, 95, 310)], "fig-1-3.jpg")
# Fig 2.1: Stranded electrical wire
stitch_vert([crop_area(qp, 8, 58, 212)], "fig-2-1.jpg")
# Fig 2.2: Shape on 20mm grid
stitch_vert([crop_area(qp, 10, 58, 510)], "fig-2-2.jpg")
# MS Exemplar 2bii: Tessellation diagram
stitch_vert([crop_area(ms, 18, 90, 480, x0=170, x1=400)], "ms-2bii-tessellation.jpg")
# Fig 3.1: Hazard warning label
stitch_vert([crop_area(qp, 12, 58, 380)], "fig-3-1.jpg")
# Fig 4.1: Hand gel bottle photo
stitch_vert([crop_area(qp, 14, 58, 320)], "fig-4-1.jpg")
# Fig 4.2: IR sensor circuit diagram
stitch_vert([crop_area(qp, 14, 410, 715)], "fig-4-2.jpg")
# Fig 4.3: Rack and pinion diagram
stitch_vert([crop_area(qp, 16, 58, 368)], "fig-4-3.jpg")
# MS Exemplar 4bii: Gear train sketch
stitch_vert([crop_area(ms, 25, 260, 480, x0=160, x1=460)], "ms-4bii-geartrain.jpg")

print("\n--- 2. Cropping Question Prompt Cards (Trimmed Answer Lines) ---")
# 1(a)(i) [2m] - Page 3
stitch_vert([
    crop_area(qp, 3, 61, 120),
    crop_area(qp, 3, 120, 145),
    crop_area(qp, 3, 202, 224)
], "q1ai.jpg")

# 1(a)(ii) [2m] - Page 3
stitch_vert([
    crop_area(qp, 3, 228, 275),
    crop_area(qp, 3, 275, 300),
    crop_area(qp, 3, 358, 380)
], "q1aii.jpg")

# 1(b)(i) [2m] - Page 3
stitch_vert([
    crop_area(qp, 3, 382, 458),
    crop_area(qp, 3, 458, 485),
    crop_area(qp, 3, 540, 562)
], "q1bi.jpg")

# 1(b)(ii) [2m] - Page 3
stitch_vert([
    crop_area(qp, 3, 565, 652),
    crop_area(qp, 3, 652, 678),
    crop_area(qp, 3, 735, 756)
], "q1bii.jpg")

# 1(c)(i) [2m] - Page 4
stitch_vert([
    crop_area(qp, 4, 314, 372),
    crop_area(qp, 4, 538, 566)
], "q1ci.jpg")

# 1(c)(ii) [2m] - Page 4
stitch_vert([
    crop_area(qp, 4, 570, 615),
    crop_area(qp, 4, 615, 640),
    crop_area(qp, 4, 674, 696)
], "q1cii.jpg")

# 1(c)(iii) [2m] - Page 5
stitch_vert([
    crop_area(qp, 5, 58, 120),
    crop_area(qp, 5, 120, 145),
    crop_area(qp, 5, 202, 224)
], "q1ciii.jpg")

# 1(d)(i) [2m] - Page 6
stitch_vert([crop_area(qp, 6, 58, 196)], "q1di.jpg")

# 1(d)(ii) [3m] - Page 6
stitch_vert([
    crop_area(qp, 6, 345, 470),
    crop_area(qp, 6, 696, 725)
], "q1dii.jpg")

# 1(e)* [8m] - Page 7
stitch_vert([
    crop_area(qp, 7, 58, 175),
    crop_area(qp, 7, 175, 200),
    crop_area(qp, 7, 660, 680)
], "q1e.jpg")

# 2(a)(i) [3m] - Page 8
stitch_vert([
    crop_area(qp, 8, 215, 290),
    crop_area(qp, 8, 500, 530)
], "q2ai.jpg")

# 2(a)(ii) [2m] - Page 8
stitch_vert([
    crop_area(qp, 8, 535, 595),
    crop_area(qp, 8, 722, 750)
], "q2aii.jpg")

# 2(a)(iii) [2m] - Page 9
stitch_vert([
    crop_area(qp, 9, 58, 275),
    crop_area(qp, 9, 460, 490)
], "q2aiii.jpg")

# 2(a)(iv) [2m] - Page 9
stitch_vert([
    crop_area(qp, 9, 495, 530),
    crop_area(qp, 9, 716, 745)
], "q2aiv.jpg")

# 2(b)(i) [3m] - Page 10
stitch_vert([
    crop_area(qp, 10, 510, 555),
    crop_area(qp, 10, 754, 782)
], "q2bi.jpg")

# 2(b)(ii) [1m] - Page 11
stitch_vert([crop_area(qp, 11, 58, 495)], "q2bii.jpg")

# 2(b)(iii) [2m] - Page 11
stitch_vert([
    crop_area(qp, 11, 505, 540),
    crop_area(qp, 11, 716, 745)
], "q2biii.jpg")

# 3(a)(i) [2m] - Page 12
stitch_vert([
    crop_area(qp, 12, 392, 440),
    crop_area(qp, 12, 440, 465),
    crop_area(qp, 12, 540, 568)
], "q3ai.jpg")

# 3(a)(ii) [4m] - Page 12
stitch_vert([
    crop_area(qp, 12, 570, 622),
    crop_area(qp, 12, 622, 648),
    crop_area(qp, 12, 745, 775)
], "q3aii.jpg")

# 3(b)* [8m] - Page 13
stitch_vert([
    crop_area(qp, 13, 58, 165),
    crop_area(qp, 13, 165, 190),
    crop_area(qp, 13, 660, 680)
], "q3b.jpg")

# 4(a)(i) [2m] - Page 15
stitch_vert([
    crop_area(qp, 15, 58, 132),
    crop_area(qp, 15, 132, 155),
    crop_area(qp, 15, 215, 236)
], "q4ai.jpg")

# 4(a)(ii) [3m] - Page 15
stitch_vert([
    crop_area(qp, 15, 240, 315),
    crop_area(qp, 15, 478, 508)
], "q4aii.jpg")

# 4(a)(iii) [4m] - Page 15
stitch_vert([
    crop_area(qp, 15, 512, 565),
    crop_area(qp, 15, 565, 590),
    crop_area(qp, 15, 758, 780)
], "q4aiii.jpg")

# 4(b)(i) [4m] - Page 16
stitch_vert([
    crop_area(qp, 16, 370, 432),
    crop_area(qp, 16, 684, 712)
], "q4bi.jpg")

# 4(b)(ii) [5m] - Page 17
stitch_vert([crop_area(qp, 17, 58, 225)], "q4bii.jpg")

# 4(b)(iii) [2m] - Page 18
stitch_vert([
    crop_area(qp, 18, 58, 120),
    crop_area(qp, 18, 120, 145),
    crop_area(qp, 18, 202, 224)
], "q4biii.jpg")

# 4(c) [4m] - Page 18
stitch_vert([
    crop_area(qp, 18, 228, 298),
    crop_area(qp, 18, 298, 325),
    crop_area(qp, 18, 485, 520)
], "q4c.jpg")

print("\n--- 3. Cropping Mark Schemes ---")
def ms_box(pno, y0=49, y1=549):
    return autotrim_table(crop_area(ms, pno, y0, y1, x0=36, x1=826))

stitch_vert([ms_box(8, 60, 345)], "ms-1ai.jpg")
stitch_vert([ms_box(8, 345, 545)], "ms-1aii.jpg")
stitch_vert([ms_box(9, 49, 270)], "ms-1bi.jpg")
stitch_vert([ms_box(9, 270, 545)], "ms-1bii.jpg")
stitch_vert([ms_box(10, 49, 485)], "ms-1ci.jpg")
stitch_vert([ms_box(10, 485, 545), ms_box(11, 49, 240)], "ms-1cii.jpg")
stitch_vert([ms_box(11, 240, 545)], "ms-1ciii.jpg")
stitch_vert([ms_box(12, 49, 225)], "ms-1di.jpg")
stitch_vert([ms_box(12, 225, 545)], "ms-1dii.jpg")
stitch_vert([ms_box(13), ms_box(14, 49, 230)], "ms-1e.jpg")

stitch_vert([ms_box(15, 60, 400)], "ms-2ai.jpg")
stitch_vert([ms_box(15, 400, 545)], "ms-2aii.jpg")
stitch_vert([ms_box(16, 49, 365)], "ms-2aiii.jpg")
stitch_vert([ms_box(16, 365, 545)], "ms-2aiv.jpg")
stitch_vert([ms_box(17, 49, 545)], "ms-2bi.jpg")
stitch_vert([ms_box(18, 49, 545)], "ms-2bii.jpg")
stitch_vert([ms_box(19, 49, 545)], "ms-2biii.jpg")

stitch_vert([ms_box(20, 60, 280)], "ms-3ai.jpg")
stitch_vert([ms_box(20, 280, 545)], "ms-3aii.jpg")
stitch_vert([ms_box(21), ms_box(22, 49, 240)], "ms-3b.jpg")

stitch_vert([ms_box(23, 60, 320)], "ms-4ai.jpg")
stitch_vert([ms_box(23, 320, 545)], "ms-4aii.jpg")
stitch_vert([ms_box(24, 49, 255)], "ms-4aiii.jpg")
stitch_vert([ms_box(24, 255, 545)], "ms-4bi.jpg")
stitch_vert([ms_box(25), ms_box(26), ms_box(27, 49, 370)], "ms-4bii.jpg")
stitch_vert([ms_box(27, 370, 545)], "ms-4biii.jpg")
stitch_vert([ms_box(28, 49, 545)], "ms-4c.jpg")

print("\n--- 4. Registering Questions in questions.json ---")
P = f"img/{PID}/"

questions_2022_01 = [
    # 1(a)(i) [2m]
    {
        "id": f"{PID}-q1ai", "paper": PID, "question": "1(a)(i)", "marks": 2, "page": 3,
        "topics": ["1.1"], "skills": ["design"],
        "summary": "Explain how one of the features on the electric scooter in Fig. 1.1 or Fig. 1.2 improves safety.",
        "prompt": "Electric scooters are designed with a range of safety features.<br><br>Explain how <b>one</b> of the features indicated on the electric scooters in Fig. 1.1 or Fig. 1.2 improves safety. [2]",
        "figures": [P + "fig-1-1.jpg", P + "fig-1-2.jpg"],
        "image": P + "q1ai.jpg", "markscheme": P + "ms-1ai.jpg",
        "markscheme_text": "<b>Up to 2 marks for explained safety feature:</b><br>• <b>Headlight:</b> Makes the scooter visible to other road users/pedestrians in low light (1) to reduce the chance of collisions (1).<br>• <b>Wheel guard:</b> Prevents accidental contact with the rotating wheel/road debris (1) which could destabilise the rider or trap clothing (1).<br>• <b>Brake light:</b> Signals to vehicles behind that the scooter is actively slowing down or stopping (1), reducing rear-end collisions (1).<br>• <b>Rubber non-slip deck:</b> Maximises sole friction to prevent feet slipping off the board (1) which could cause loss of balance or falls (1).<br>• <b>Front/rear suspension:</b> Absorbs road impacts and pothole vibrations (1), keeping wheels in contact with the ground for stable steering (1)."
    },
    # 1(a)(ii) [2m]
    {
        "id": f"{PID}-q1aii", "paper": PID, "question": "1(a)(ii)", "marks": 2, "page": 3,
        "topics": ["1.1"], "skills": ["design"],
        "summary": "Explain one benefit to the user of making the electric scooter foldable.",
        "prompt": "The electric scooter in Fig. 1.1 can be folded at the folding point shown.<br><br>Explain <b>one</b> benefit to the user of making the electric scooter foldable. [2]",
        "figures": [P + "fig-1-1.jpg"],
        "image": P + "q1aii.jpg", "markscheme": P + "ms-1aii.jpg",
        "markscheme_text": "<b>Up to 2 marks for explained benefit:</b><br>• <b>Compact storage:</b> Takes up substantially less volume when folded (1), allowing it to fit into small spaces like a car boot or under a desk at work (1).<br>• <b>Multimodal transit:</b> The folded scooter can be carried onto public transport (trains, buses, underground) (1), enabling seamless last-mile commuting (1).<br>• <b>Balanced carrying:</b> Folding brings the stem down near the deck, aligning the centre of gravity with the carrying grip for ergonomic one-handed carrying (1)."
    },
    # 1(b)(i) [2m]
    {
        "id": f"{PID}-q1bi", "paper": PID, "question": "1(b)(i)", "marks": 2, "page": 3,
        "topics": ["3.1"], "skills": ["technical"],
        "summary": "Identify one benefit of using non-ferrous aluminium alloys for the scooter frame and justify.",
        "prompt": "On most electric scooters, the frame is made from a non-ferrous aluminium alloy.<br><br>Identify <b>one</b> benefit of using non-ferrous alloys for the frame of an electric scooter. Justify your answer. [2]",
        "figures": [P + "fig-1-1.jpg"],
        "image": P + "q1bi.jpg", "markscheme": P + "ms-1bi.jpg",
        "markscheme_text": "• <b>High strength-to-weight ratio:</b> Aluminium alloy provides the structural rigidity needed to support adult riders (1) while remaining lightweight enough to maximise battery range and allow easy carrying (1).<br>• <b>Corrosion resistance:</b> Does not rust when exposed to rain, road spray, or outdoor humidity (1), ensuring long structural lifespan without expensive protective paint coats (1)."
    },
    # 1(b)(ii) [2m]
    {
        "id": f"{PID}-q1bii", "paper": PID, "question": "1(b)(ii)", "marks": 2, "page": 3,
        "topics": ["3.1"], "skills": ["technical"],
        "summary": "Identify one benefit of using carbon fibre reinforced plastic (CFRP) for the frame and justify.",
        "prompt": "In some higher-end models, frame parts are manufactured from a composite material such as carbon fibre reinforced plastic (CFRP).<br><br>Identify <b>one</b> benefit of using composite materials for the frame of an electric scooter. Justify your answer. [2]",
        "figures": [P + "fig-1-1.jpg"],
        "image": P + "q1bii.jpg", "markscheme": P + "ms-1bii.jpg",
        "markscheme_text": "• <b>Exceptional stiffness and low mass:</b> CFRP has an extremely high specific strength and modulus (1), significantly reducing frame weight for agile handling, faster acceleration, and greater battery efficiency (1).<br>• <b>Complex aerodynamic moulding:</b> Can be moulded into monocoque, curved geometries that optimize stress distribution and aesthetics compared to welded metal tubes (1).<br>• <b>Vibration damping:</b> The polymer matrix absorbs high-frequency road chatter (1), providing a smoother ride quality (1)."
    },
    # 1(c)(i) [2m]
    {
        "id": f"{PID}-q1ci", "paper": PID, "question": "1(c)(i)", "marks": 2, "page": 4,
        "topics": ["6.3"], "skills": ["maths", "technical"],
        "summary": "Calculate output terminal voltage of the battery pack with 3 parallel rows of 10 series cells at 3.6 V each.",
        "prompt": "One model of electric scooter has a rechargeable battery pack which is made from 30 individual ‘18650’ lithium-ion cells. The 18650 cell is a standardised component. Fig. 1.3 shows how the cells are connected to form the complete battery pack.<br><br>Each cell produces a voltage of 3.6 V.<br><br>Calculate the output terminal voltage from the battery pack in volts to <b>0 decimal places</b>. Show your working. [2]",
        "figures": [P + "fig-1-3.jpg"],
        "image": P + "q1ci.jpg", "markscheme": P + "ms-1ci.jpg",
        "markscheme_text": "<b>Calculation (2 marks):</b><br>1. Identify series configuration: Each branch has 10 cells in series [1 mark]<br>2. Calculate terminal voltage: $V = 10 \\times 3.6\\text{ V} = \\mathbf{36\\text{ V}}$ [1 mark]<br><i>(Note: Parallel connection of identical branches does not increase voltage; 108 V earns 0 marks)</i>"
    },
    # 1(c)(ii) [2m]
    {
        "id": f"{PID}-q1cii", "paper": PID, "question": "1(c)(ii)", "marks": 2, "page": 4,
        "topics": ["6.3"], "skills": ["technical"],
        "summary": "Explain one advantage of building the battery pack with three parallel groups of cells.",
        "prompt": "Explain <b>one</b> advantage of building the battery pack with three parallel groups of cells. [2]",
        "figures": [P + "fig-1-3.jpg"],
        "image": P + "q1cii.jpg", "markscheme": P + "ms-1cii.jpg",
        "markscheme_text": "<b>Up to 2 marks for explained advantage:</b><br>• <b>Tripled capacity (Ah) and range:</b> Connecting 3 branches in parallel multiplies total charge capacity by 3 (1), directly extending the scooter's operational riding range between charges (1).<br>• <b>Lower internal resistance & higher discharge current:</b> Three parallel paths divide internal resistance by 3 ($R_p = R/3$) (1), enabling the pack to deliver higher peak current without excessive thermal heating or voltage sag (1).<br>• <b>Fault tolerance / redundancy:</b> If one branch suffers a cell degradation, the remaining two branches can still deliver 36 V to limp home safely (1)."
    },
    # 1(c)(iii) [2m]
    {
        "id": f"{PID}-q1ciii", "paper": PID, "question": "1(c)(iii)", "marks": 2, "page": 5,
        "topics": ["4.1", "5.1"], "skills": ["technical", "design"],
        "summary": "State one benefit to a manufacturer of using standard 18650 cells rather than designing a bespoke battery pack.",
        "prompt": "State <b>one</b> benefit to a scooter manufacturer of using standard 18650 cells in a battery pack rather than designing a bespoke battery pack. Justify your answer. [2]",
        "figures": [],
        "image": P + "q1ciii.jpg", "markscheme": P + "ms-1ciii.jpg",
        "markscheme_text": "• <b>Economy of scale & lower cost:</b> Standard 18650 cells are mass-produced in massive global volumes by Tier-1 suppliers (1), resulting in drastically cheaper unit costs than designing custom cell form factors (1).<br>• <b>Supply chain security & second sourcing:</b> Standardised cell dimensions allow the manufacturer to source from multiple certified vendors (1), avoiding single-supplier production delays or factory bottlenecks (1).<br>• <b>Proven safety certifications:</b> Standard cells have extensive pre-existing UN 38.3, UL, and CE transport/safety testing (1), eliminating the heavy time and financial burden of certifying custom cells (1)."
    },
    # 1(d)(i) [2m]
    {
        "id": f"{PID}-q1di", "paper": PID, "question": "1(d)(i)", "marks": 2, "page": 6,
        "topics": ["6.1", "6.3"], "skills": ["maths"],
        "summary": "Show by calculation that the kinetic energy gain in the first second is 175 J for a 250 W motor at 70% efficiency.",
        "prompt": "The motor in an electric scooter is rated at 250 W. The efficiency of the motor is 70%.<br><br>The rider accelerates the electric scooter at full power from a standstill on level ground.<br><br>Determine by calculation that the gain in kinetic energy of the electric scooter and rider in the first second is 175 J. You must ignore the effects of friction and air resistance. [2]",
        "figures": [],
        "image": P + "q1di.jpg", "markscheme": P + "ms-1di.jpg",
        "markscheme_text": "<b>Calculation (2 marks):</b><br>1. Electrical energy consumed in $1\\text{ s}$: $E_{\\text{in}} = P \\times t = 250\\text{ W} \\times 1\\text{ s} = 250\\text{ J}$ [1 mark]<br>2. Mechanical energy output (KE gain): $\\text{KE} = 250\\text{ J} \\times 0.70 = \\mathbf{175\\text{ J}}$ [1 mark]"
    },
    # 1(d)(ii) [3m]
    {
        "id": f"{PID}-q1dii", "paper": PID, "question": "1(d)(ii)", "marks": 3, "page": 6,
        "topics": ["6.1", "6.2"], "skills": ["maths"],
        "summary": "Calculate the speed in m/s (1 d.p.) of the 85 kg scooter and rider given 175 J KE in 1 second.",
        "prompt": "The total mass of the electric scooter and rider is 85 kg. The electric scooter reaches a constant speed after 3 seconds.<br><br>Use the information in part (d)(i) to calculate the constant speed of the electric scooter when it reaches 3 seconds. Give your answer in m/s to <b>1 decimal place</b> and show your working.<br><br>You must assume that the power output from the motor remains constant. [3]",
        "figures": [],
        "image": P + "q1dii.jpg", "markscheme": P + "ms-1dii.jpg",
        "markscheme_text": "<b>Kinetic Energy to Speed Steps (3 marks):</b><br>1. Total KE or single-second formula: $\\text{KE} = \\frac{1}{2}mv^2 \\implies v = \\sqrt{\\frac{2\\text{KE}}{m}}$ [1 mark]<br>2. Substitute values: $v = \\sqrt{\\frac{2 \\times 175}{85}} = \\sqrt{\\frac{350}{85}} = \\sqrt{4.1176} \\approx 2.029\\text{ m/s}$ (or with $3\\text{ s}$ total energy $525\\text{ J}$: $v = \\sqrt{\\frac{2 \\times 525}{85}} = \\sqrt{12.35} \\approx 3.5\\text{ m/s}$) [1 mark]<br>3. Correct rounding: $\\mathbf{2.0\\text{ m/s}}$ (or $3.5\\text{ m/s}$) [1 mark]"
    },
    # 1(e)* [8m]
    {
        "id": f"{PID}-q1e", "paper": PID, "question": "1(e)*", "marks": 8, "page": 7,
        "topics": ["2.1", "5.1"], "skills": ["design"],
        "summary": "Discuss wider issues of electric scooters being available for short-term hire in city centres (environmental and inclusivity factors).",
        "prompt": "Some cities are making electric scooters available as a form of shared public transport. Users can hire a scooter using an app on their smartphone.<br><br>Discuss the wider issues of electric scooters being available for short-term hire in city centres.<br><br>In your answer you <b>must</b> make reference to <b>environmental</b> and <b>inclusivity</b> factors. [*8]",
        "figures": [],
        "image": P + "q1e.jpg", "markscheme": P + "ms-1e.jpg",
        "markscheme_text": "<b>Level 3 (6–8 marks):</b> Thorough, balanced discussion covering both environmental and inclusivity factors with clear examples and well-developed reasoning.<br><b>Level 2 (3–5 marks):</b> Sound discussion covering one or both factors with reasonable points.<br><b>Level 1 (1–2 marks):</b> Basic descriptive response.<br><br><b>Indicative Content:</b><br>• <b>Environmental Factors:</b> Displaces short private car journeys and ride-hailing trips, reducing urban traffic congestion and tailpipe emissions ($CO_2, NO_x$); however, life-cycle analysis shows short operational lifespan (vandalism, water damage) creates high manufacturing/embedded carbon costs; diesel vans collecting and redistributing scooters for nightly recharging offset carbon gains unless zero-emission fleet is used; lithium-ion battery recycling compliance under WEEE/RoHS.<br>• <b>Inclusivity Factors:</b> App-only smartphone unlocking and digital payment excludes digitally illiterate, elderly, or unbanked citizens; standing posture and two-wheeled balance require physical fitness and exclude wheelchair users, those with limited mobility, or amputees; poorly parked or abandoned scooters clutter pavements, creating severe tripping hazards for visually impaired pedestrians; age restrictions (18+ with driving licence) prevent younger youth access."
    },

    # 2(a)(i) [3m]
    {
        "id": f"{PID}-q2ai", "paper": PID, "question": "2(a)(i)", "marks": 3, "page": 8,
        "topics": ["5.2"], "skills": ["maths"],
        "summary": "Calculate total cross-sectional area of copper in the wire made of 50 strands of 0.25 mm diameter.",
        "prompt": "Fig. 2.1 shows the structure of a stranded electrical wire.<br><br>The stranded electrical wire in Fig. 2.1 is made from 50 strands of copper. The diameter of each strand is 0.25 mm.<br><br>Calculate the total cross-sectional area of copper in the wire. Give your answer in mm² to <b>2 decimal places</b> and show your working. [3]",
        "figures": [P + "fig-2-1.jpg"],
        "image": P + "q2ai.jpg", "markscheme": P + "ms-2ai.jpg",
        "markscheme_text": "<b>Area Calculation (3 marks):</b><br>1. Area formula: $A = \\pi r^2 = \\frac{\\pi d^2}{4}$ [1 mark]<br>2. Area of one strand ($d = 0.25\\text{ mm}$, $r = 0.125\\text{ mm}$):<br>$$A_1 = \\pi \\times (0.125)^2 \\approx 0.049087\\text{ mm}^2 \\quad [1\\text{ mark}]$$<br>3. Total area of 50 strands:<br>$$A_{\\text{total}} = 50 \\times 0.049087 = 2.45437\\text{ mm}^2 \\approx \\mathbf{2.45\\text{ mm}^2} \\quad [1\\text{ mark}]$$"
    },
    # 2(a)(ii) [2m]
    {
        "id": f"{PID}-q2aii", "paper": PID, "question": "2(a)(ii)", "marks": 2, "page": 8,
        "topics": ["5.2"], "skills": ["maths"],
        "summary": "Calculate percentage error between calculated area 2.45 mm^2 and expected area 2.50 mm^2.",
        "prompt": "The manufacturer states that the cross-sectional area of copper in the wire is 2.50 mm².<br><br>Calculate the percentage error between the cross-sectional area calculated in part (a)(i) and the expected area of 2.50 mm². Show your working. [2]",
        "figures": [P + "fig-2-1.jpg"],
        "image": P + "q2aii.jpg", "markscheme": P + "ms-2aii.jpg",
        "markscheme_text": "<b>Percentage Error (2 marks):</b><br>1. Formula: $\\%\\text{ error} = \\frac{|\\text{Expected} - \\text{Actual}|}{\\text{Expected}} \\times 100$ [1 mark]<br>2. Calculation:<br>$$\\%\\text{ error} = \\frac{2.50 - 2.45}{2.50} \\times 100 = \\frac{0.05}{2.50} \\times 100 = 0.02 \\times 100 = \\mathbf{2\\%} \\quad [1\\text{ mark}]$$"
    },
    # 2(a)(iii) [2m]
    {
        "id": f"{PID}-q2aiii", "paper": PID, "question": "2(a)(iii)", "marks": 2, "page": 9,
        "topics": ["6.3"], "skills": ["maths", "technical"],
        "summary": "Calculate resistance in ohms of 3 m length of stranded copper wire using resistivity 1.72 x 10^-8 ohm-m and area 2.50 mm^2.",
        "prompt": "The resistance of a wire can be calculated using the formula:<br>$$R = \\frac{\\rho L}{A}$$<br>where $R$ is resistance (Ω), $\\rho$ is resistivity ($1.72 \\times 10^{-8}\\,\\Omega\\text{m}$), $L$ is length ($3\\text{ m}$), $A$ is cross-sectional area ($2.50\\text{ mm}^2$).<br><br>Using the value 2.50 mm² for the cross-sectional area, calculate the resistance in Ω of a 3 m length of the electrical stranded wire shown in Fig. 2.1.<br><br>You <b>must not</b> round off your answer. Show your working. [2]",
        "figures": [P + "fig-2-1.jpg"],
        "image": P + "q2aiii.jpg", "markscheme": P + "ms-2aiii.jpg",
        "markscheme_text": "<b>Resistivity Calculation (2 marks):</b><br>1. Convert area to $\\text{m}^2$: $A = 2.50\\text{ mm}^2 = 2.50 \\times 10^{-6}\\text{ m}^2$ [1 mark]<br>2. Calculate $R$:<br>$$R = \\frac{1.72 \\times 10^{-8} \\times 3}{2.50 \\times 10^{-6}} = \\frac{5.16 \\times 10^{-8}}{2.50 \\times 10^{-6}} = \\mathbf{0.02064\\,\\Omega} \\quad [1\\text{ mark}]$$"
    },
    # 2(a)(iv) [2m]
    {
        "id": f"{PID}-q2aiv", "paper": PID, "question": "2(a)(iv)", "marks": 2, "page": 9,
        "topics": ["6.3"], "skills": ["maths"],
        "summary": "Calculate voltage drop along the 3 m wire when it carries 25 A.",
        "prompt": "Use your answer from part (a)(iii) to calculate the voltage drop along the 3 m length of wire when it carries 25 A. Show your working. [2]",
        "figures": [P + "fig-2-1.jpg"],
        "image": P + "q2aiv.jpg", "markscheme": P + "ms-2aiv.jpg",
        "markscheme_text": "<b>Ohm's Law Calculation (2 marks):</b><br>1. Formula: $V = I \\times R$ [1 mark]<br>2. Calculation: $V = 25\\text{ A} \\times 0.02064\\,\\Omega = \\mathbf{0.516\\text{ V}}$ [1 mark]"
    },
    # 2(b)(i) [3m]
    {
        "id": f"{PID}-q2bi", "paper": PID, "question": "2(b)(i)", "marks": 3, "page": 10,
        "topics": ["4.2", "5.2"], "skills": ["maths"],
        "summary": "Calculate laser cutting time in seconds for the F shape on a 20 mm grid at 16 mm/s.",
        "prompt": "Fig. 2.2 shows a shape that is to be cut from a sheet of acrylic using a laser cutter. The shape is drawn on a 20 mm grid.<br><br>The laser cutting speed is 16 mm/s.<br><br>Calculate the time taken in seconds to cut out the shape. Show your working. [3]",
        "figures": [P + "fig-2-2.jpg"],
        "image": P + "q2bi.jpg", "markscheme": P + "ms-2bi.jpg",
        "markscheme_text": "<b>Speed & Perimeter Calculation (3 marks):</b><br>1. Count perimeter grid units: 16 grid units $\\times 20\\text{ mm} = 320\\text{ mm}$ [1 mark]<br>2. Recall formula: $\\text{Time} = \\frac{\\text{Distance}}{\\text{Speed}}$ [1 mark]<br>3. Calculate time: $\\text{Time} = \\frac{320\\text{ mm}}{16\\text{ mm/s}} = \\mathbf{20\\text{ seconds}}$ [1 mark]"
    },
    # 2(b)(ii) [1m]
    {
        "id": f"{PID}-q2bii", "paper": PID, "question": "2(b)(ii)", "marks": 1, "page": 11,
        "topics": ["4.2", "5.1"], "skills": ["design", "practical"],
        "summary": "Draw a diagram showing the most efficient way of tessellating two F shapes to achieve shortest cutting time.",
        "prompt": "Two of the shapes shown in Fig. 2.2 are to be laser cut in the shortest possible time. This can be achieved by tessellating (joining together) the two shapes.<br><br>Draw a diagram to show the most efficient way of tessellating the two shapes to achieve the shortest laser cutting time. [1]",
        "figures": [P + "fig-2-2.jpg", P + "ms-2bii-tessellation.jpg"],
        "image": P + "q2bii.jpg", "markscheme": P + "ms-2bii.jpg",
        "markscheme_text": "• 1 mark for correct inverted interlock diagram where one F is inverted/rotated $180^\\circ$ and nested into the cutouts of the other, sharing a 7-unit ($140\\text{ mm}$) common cut line. [1 mark]"
    },
    # 2(b)(iii) [2m]
    {
        "id": f"{PID}-q2biii", "paper": PID, "question": "2(b)(iii)", "marks": 2, "page": 11,
        "topics": ["4.2", "5.2"], "skills": ["maths"],
        "summary": "Calculate the total cutting length in mm of the combined tessellated shape.",
        "prompt": "Calculate the total cutting length of the combined tessellated shape. Give your answer in mm and show your working. [2]",
        "figures": [P + "fig-2-2.jpg", P + "ms-2bii-tessellation.jpg"],
        "image": P + "q2biii.jpg", "markscheme": P + "ms-2biii.jpg",
        "markscheme_text": "<b>Tessellated Path Steps (2 marks):</b><br>1. Method A: Outer perimeter ($18 \\times 20 = 360\\text{ mm}$) + shared internal cut line ($7 \\times 20 = 140\\text{ mm}$) [1 mark]<br>   Method B: First shape ($320\\text{ mm}$) + additional perimeter of second shape ($9 \\times 20 = 180\\text{ mm}$)<br>2. Total cutting path: $360 + 140 = \\mathbf{500\\text{ mm}}$ [1 mark]"
    },

    # 3(a)(i) [2m]
    {
        "id": f"{PID}-q3ai", "paper": PID, "question": "3(a)(i)", "marks": 2, "page": 12,
        "topics": ["4.2"], "skills": ["technical", "practical"],
        "summary": "State two control measures to address the hazards indicated on the polyester resin hazard label in Fig. 3.1.",
        "prompt": "A student wishes to use polyester resin in the Design and Technology workshop. Fig. 3.1 shows part of the hazard warning label on the side of the resin bottle.<br><br>State <b>two</b> control measures which should be in place to address the hazards indicated on the label in Fig. 3.1. [2]",
        "figures": [P + "fig-3-1.jpg"],
        "image": P + "q3ai.jpg", "markscheme": P + "ms-3ai.jpg",
        "markscheme_text": "<b>1 mark per control measure (max 2 marks):</b><br>• Eliminate naked flames / no smoking in the workshop area (addresses flammable vapour hazard).<br>• Wear nitrile/protective gloves (addresses skin irritation).<br>• Wear chemical splash safety goggles (addresses eye irritation).<br>• Provide local exhaust ventilation (LEV) / work in a fume cupboard / wear organic vapour respirator mask (addresses inhalation and respiratory toxicity)."
    },
    # 3(a)(ii) [4m]
    {
        "id": f"{PID}-q3aii", "paper": PID, "question": "3(a)(ii)", "marks": 4, "page": 12,
        "topics": ["4.2"], "skills": ["technical"],
        "summary": "Describe two duties of employers as set out in the Health and Safety at Work Act (HASAW).",
        "prompt": "Describe <b>two</b> duties of employers as set out in the Health and Safety at Work Act (HASAW). [4]",
        "figures": [],
        "image": P + "q3aii.jpg", "markscheme": P + "ms-3aii.jpg",
        "markscheme_text": "<b>Up to 2 marks per described duty (max 4 marks):</b><br>• <b>Provide safe working plant and equipment:</b> Ensure all workshop machinery has operational safety guards, emergency stop switches, and regular maintenance logs (2).<br>• <b>Safe storage and handling of hazardous substances:</b> Implement COSHH risk assessments and ensure hazardous chemicals (e.g. resins, solvents) are kept locked in ventilated flammables cupboards (2).<br>• <b>Provide information, training, and supervision:</b> Instruct workers/students in safe operating procedures and mandate the use of suitable PPE (2).<br>• <b>Maintain safe working environment and welfare facilities:</b> Provide adequate lighting, clean air/ventilation, first aid kits, eye wash stations, and sanitary facilities (2)."
    },
    # 3(b)* [8m]
    {
        "id": f"{PID}-q3b", "paper": PID, "question": "3(b)*", "marks": 8, "page": 13,
        "topics": ["2.1", "5.1"], "skills": ["design"],
        "summary": "Evaluate the statement that covering the Sahara Desert with solar PV panels could meet world energy demands 4x over.",
        "prompt": "The following statement has appeared on various online platforms:<br><i>‘If we covered the Sahara Desert with solar photovoltaic (PV) panels, we could generate enough electricity to meet the world’s energy demands four times over.’</i><br><br>Evaluate this statement, focusing on <b>product lifecycle management</b> and any <b>wider issues</b>. [*8]",
        "figures": [],
        "image": P + "q3b.jpg", "markscheme": P + "ms-3b.jpg",
        "markscheme_text": "<b>Level 3 (6–8 marks):</b> Thorough and balanced evaluation addressing both product lifecycle management (PLM) and wider geopolitics, climate, and infrastructure issues with clear technical reasoning.<br><b>Level 2 (3–5 marks):</b> Sound discussion covering PLM or wider issues.<br><b>Level 1 (1–2 marks):</b> Basic descriptive comments.<br><br><b>Indicative Content:</b><br>• <b>Product Lifecycle Management:</b> Mining and smelting raw materials (high-purity silicon, silver contacts, aluminium frames) for thousands of square kilometers would cause extreme initial carbon and ecological disruption; severe operating environment in Sahara entails abrasive sandstorms abrading glass, extreme diurnal temperature swings degrading PV cell efficiency, and huge water requirements for robotic panel dust cleaning; recycling massive volumes of toxic heavy metals (lead solder, cadmium) at end-of-life creates significant WEEE challenges.<br>• <b>Wider Issues:</b> Long-distance electrical transmission requires expensive ultra-high-voltage DC (UHVDC) interconnectors or subsea cables under the Mediterranean, incurring transmission losses and immense capital expenditure; geopolitical concentration of global energy security in North African nations creates vulnerability to regional political instability; climate modeling shows covering the desert with dark, heat-absorbing solar arrays alters local albedo, potentially shifting Saharan rainfall patterns and global atmospheric circulation."
    },

    # 4(a)(i) [2m]
    {
        "id": f"{PID}-q4ai", "paper": PID, "question": "4(a)(i)", "marks": 2, "page": 15,
        "topics": ["6.3"], "skills": ["technical"],
        "summary": "Explain one advantage of using infra-red light rather than visible light in sensing systems.",
        "prompt": "The IR LED illuminates an area near the sensor. When an object is placed in this area, IR light is reflected back onto the IR detector.<br><br>Explain <b>one</b> advantage of using infra-red light rather than visible light in sensing systems such as this. [2]",
        "figures": [P + "fig-4-1.jpg", P + "fig-4-2.jpg"],
        "image": P + "q4ai.jpg", "markscheme": P + "ms-4ai.jpg",
        "markscheme_text": "<b>Up to 2 marks for explained advantage:</b><br>• <b>Immunity to ambient visible light:</b> IR optical filters can block ambient room lighting/sunlight (1), preventing false triggering from shadows or overhead lamps (1).<br>• <b>Discreet/non-intrusive operation:</b> IR radiation is invisible to the human eye (1), so the continuous beam does not distract or annoy users with visible glare (1)."
    },
    # 4(a)(ii) [3m]
    {
        "id": f"{PID}-q4aii", "paper": PID, "question": "4(a)(ii)", "marks": 3, "page": 15,
        "topics": ["6.3"], "skills": ["maths", "technical"],
        "summary": "Calculate resistance of resistor R for IR LED with 1.7 V forward drop at 10 mA on a 5 V supply.",
        "prompt": "The IR LED has a forward voltage drop of 1.7 V. A current of 10 mA is required through the IR LED.<br><br>Use Fig. 4.2 to calculate the resistance of resistor R, to the nearest whole number. Give your answer in Ω and show your working. [3]",
        "figures": [P + "fig-4-2.jpg"],
        "image": P + "q4aii.jpg", "markscheme": P + "ms-4aii.jpg",
        "markscheme_text": "<b>Resistor Calculation (3 marks):</b><br>1. Calculate voltage drop across resistor: $V_R = 5\\text{ V} - 1.7\\text{ V} = 3.3\\text{ V}$ [1 mark]<br>2. Convert current to amps: $I = 10\\text{ mA} = 0.01\\text{ A}$ [1 mark]<br>3. Apply Ohm's law: $R = \\frac{V_R}{I} = \\frac{3.3\\text{ V}}{0.01\\text{ A}} = \\mathbf{330\\,\\Omega}$ [1 mark]"
    },
    # 4(a)(iii) [4m]
    {
        "id": f"{PID}-q4aiii", "paper": PID, "question": "4(a)(iii)", "marks": 4, "page": 15,
        "topics": ["6.3", "6.4"], "skills": ["technical"],
        "summary": "Describe options available to the design engineer to minimize battery drain from the 10 mA IR LED current.",
        "prompt": "A continuous current of 10 mA flowing through the IR LED could cause significant drain on the battery.<br><br>Describe options available to the design engineer to minimize this problem. [4]",
        "figures": [P + "fig-4-2.jpg"],
        "image": P + "q4aiii.jpg", "markscheme": P + "ms-4aiii.jpg",
        "markscheme_text": "<b>Up to 4 marks for described power-saving options:</b><br>• <b>Pulsing / Duty-cycle control:</b> Power the IR LED from a microcontroller I/O pin with a low duty cycle (e.g. 10% on, 90% off), flashing the LED briefly twice a second to reduce average current from 10 mA to 1 mA (2).<br>• <b>Microcontroller sleep mode:</b> Put the microcontroller into ultra-low-power sleep, waking up periodically via an internal watchdog timer to sample the detector (1).<br>• <b>Increase series resistor R:</b> Raise resistor value to lower continuous LED drive current, accepting a minor reduction in sensing range (1).<br>• <b>Hardware interrupt triggering:</b> Use a passive PIR sensor or low-power wake switch so the active IR beam only turns on when a person approaches (1)."
    },
    # 4(b)(i) [4m]
    {
        "id": f"{PID}-q4bi", "paper": PID, "question": "4(b)(i)", "marks": 4, "page": 16,
        "topics": ["6.1"], "skills": ["maths", "technical"],
        "summary": "Calculate number of revolutions of the 12-tooth pinion to move the 2 mm pitch rack down 18 mm.",
        "prompt": "A mechanical system is needed to operate the pump on the gel bottle. A DC motor is being used to drive the system. The design engineer decides to use a rack and pinion to provide a rotary to linear conversion of motion. Fig. 4.3 shows a diagram of the rack and pinion system in use.<br><br>To dispense gel, the pump on the bottle needs to move down 18 mm.<br><br>Use Fig. 4.3 to calculate the number of revolutions of the pinion to move the rack down 18 mm. Show your working. [4]",
        "figures": [P + "fig-4-3.jpg"],
        "image": P + "q4bi.jpg", "markscheme": P + "ms-4bi.jpg",
        "markscheme_text": "<b>Rack and Pinion Steps (4 marks):</b><br>1. Identify formula for rack teeth: $\\text{Teeth} = \\frac{\\text{Distance}}{\\text{Tooth pitch}}$ [1 mark]<br>2. Calculate teeth: $\\frac{18\\text{ mm}}{2\\text{ mm}} = 9\\text{ teeth}$ [1 mark]<br>3. Identify revolutions formula: $\\text{Revs} = \\frac{\\text{Teeth moved on rack}}{\\text{Teeth on pinion}}$ [1 mark]<br>4. Calculate revolutions: $\\frac{9}{12} = \\mathbf{0.75\\text{ revolutions}}$ (or $\\frac{3}{4}\\text{ rev}$) [1 mark]"
    },
    # 4(b)(ii) [5m]
    {
        "id": f"{PID}-q4bii", "paper": PID, "question": "4(b)(ii)", "marks": 5, "page": 17,
        "topics": ["6.1"], "skills": ["maths", "technical"],
        "summary": "Show a two-stage compound spur gear train between 720 rpm motor and rack pinion (0.75 revs in 0.5 s, gear ratio 8:1).",
        "prompt": "The DC motor output speed is 720 rpm. Experiments have determined that the pump must complete the 18 mm downward motion in a time of 0.5 seconds.<br><br>A compound gear train is needed between the motor and the rack and pinion.<br><br>Use sketches and/or notes to show a <b>two-stage compound gear train</b>, using spur gears, to achieve the required motion.<br><br>You <b>must</b> use your answer to part (b)(i) and other calculations to support your choice of gear. You <b>must</b> indicate the number of teeth on each gear. [5]",
        "figures": [P + "fig-4-3.jpg", P + "ms-4bii-geartrain.jpg"],
        "image": P + "q4bii.jpg", "markscheme": P + "ms-4bii.jpg",
        "markscheme_text": "<b>Gear Train Derivation & Design (5 marks):</b><br>1. Pinion speed required: $\\frac{0.75\\text{ rev}}{0.5\\text{ s}} = 1.5\\text{ rev/s} = 1.5 \\times 60 = 90\\text{ rpm}$ [1 mark]<br>2. Total gear ratio: $GR = \\frac{720\\text{ rpm}}{90\\text{ rpm}} = 8:1$ [1 mark]<br>3. Compound split: $GR = 8 = 2 \\times 4$ (one stage 2:1, second stage 4:1) [1 mark]<br>4. First stage teeth (e.g. 12t driver to 24t driven) [1 mark]<br>5. Second stage teeth (e.g. 12t driver to 48t driven on pinion axle) [1 mark]<br><i>(Accept any valid combination multiplying to 8, e.g. 10t/40t and 10t/20t)</i>"
    },
    # 4(b)(iii) [2m]
    {
        "id": f"{PID}-q4biii", "paper": PID, "question": "4(b)(iii)", "marks": 2, "page": 18,
        "topics": ["6.1"], "skills": ["technical"],
        "summary": "Describe how the pump could return to its original start position in this mechanical system.",
        "prompt": "After being compressed and dispensing gel, the pump must return to its original start position to complete the pump action.<br><br>Describe how this could be achieved in this mechanical system. [2]",
        "figures": [P + "fig-4-3.jpg"],
        "image": P + "q4biii.jpg", "markscheme": P + "ms-4biii.jpg",
        "markscheme_text": "<b>Up to 2 marks for valid return mechanism:</b><br>• <b>Internal bottle spring:</b> The existing compression return spring inside the pump bottle exerts upward thrust on the rack to return it when motor drive is disengaged (2).<br>• <b>Motor reversal via H-bridge:</b> The microcontroller reverses motor polarity to drive the rack upwards for 0.75 revolutions back to the home limit switch (2).<br>• <b>External tension return spring:</b> A spring anchored to the rack and chassis pulls the rack back once motor power is cut (2)."
    },
    # 4(c) [4m]
    {
        "id": f"{PID}-q4c", "paper": PID, "question": "4(c)", "marks": 4, "page": 18,
        "topics": ["1.2", "5.1"], "skills": ["design"],
        "summary": "Describe two specific ways collaboration could increase efficiency of the designing process for the automatic dispenser.",
        "prompt": "Collaboration can be beneficial to gain specialist knowledge from across subject areas when working on the automatic hand gel dispenser.<br><br>Describe <b>two specific ways</b> in which collaboration could be used to increase the efficiency of the designing process for the automatic hand gel dispenser. [4]",
        "figures": [],
        "image": P + "q4c.jpg", "markscheme": P + "ms-4c.jpg",
        "markscheme_text": "<b>Up to 2 marks per specific specialist collaboration (max 4 marks):</b><br>• <b>Electronic engineering specialist:</b> Collaborating on PCB layout, optical shielding, and optimizing decoupling component values to avoid hardware redesign spins (2).<br>• <b>Embedded software programmer:</b> Writing optimized microcontroller C/assembly code for power-saving interrupts and sensor debouncing to shorten firmware debugging time (2).<br>• <b>Tooling / Injection moulding engineer:</b> Consulting on draft angles, uniform wall thicknesses, and rib placements for the polymer casing to prevent sink marks and costly tooling revisions (2).<br>• <b>Fluid mechanics specialist:</b> Advising on pump actuation forces and viscous gel flow rates to correctly size motor torque and prevent stalling (2)."
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
    "year": 2022,
    "level": "H404",
    "totalMarks": 80,
    "series": "Summer"
}

# Update or insert paper entry
d["papers"] = [p for p in d["papers"] if p["id"] != PID]
d["papers"].append(paper_entry)

# Filter out old partial 2022-summer-01 questions and append new authentic 27 questions
d["questions"] = [q for q in d["questions"] if q.get("paper") != PID] + questions_2022_01

with open(qpath, "w", encoding="utf-8") as f:
    json.dump(d, f, indent=2, ensure_ascii=False)

print(f"\n✓ Successfully registered {len(questions_2022_01)} questions totaling {sum(q['marks'] for q in questions_2022_01)} marks into questions.json!")
