"""
Build OCR H404/02 Problem Solving in Design Engineering - June 2022 (paper id 2022-summer-02).
Total Marks: 70 marks across 7 questions.

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
QP_PATH = os.path.join(BASE_UP, "media_1795108912123_d1293bcb.pdf")
MS_PATH = os.path.join(BASE_UP, "media_1795108912152_92658b1a.pdf")
RB_PATH = os.path.join(BASE_UP, "media_1795108912179_fd8792f2.pdf")

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PID = "2022-summer-02"
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
    print(f"  {fname:22s} -> {out.size}")
    return out

print("\n--- 1. Cropping Resource Booklet & Exemplar Figures ---")
# Resource Booklet Page 2: Stand-up Paddle Boarding & Fig. 1
stitch_vert([crop_area(rb, 2, 50, 780)], "rb-p2.jpg")
stitch_vert([crop_area(rb, 2, 115, 315)], "fig-1.jpg")

# Resource Booklet Page 3: Types of Paddle Boards & Fig. 2
stitch_vert([crop_area(rb, 3, 50, 780)], "rb-p3.jpg")
stitch_vert([crop_area(rb, 3, 55, 575)], "fig-2.jpg")

# Resource Booklet Page 4: Stance & Choice of Paddle & Fig. 3
stitch_vert([crop_area(rb, 4, 50, 780)], "rb-p4.jpg")
stitch_vert([crop_area(rb, 4, 130, 525)], "fig-3.jpg")

# Resource Booklet Page 5: Materials, Blade Shapes, Anthropometrics & Figs. 4, 5, 6
stitch_vert([crop_area(rb, 5, 50, 780)], "rb-p5.jpg")
stitch_vert([crop_area(rb, 5, 55, 280)], "fig-4.jpg")
stitch_vert([crop_area(rb, 5, 280, 525)], "fig-5.jpg")
stitch_vert([crop_area(rb, 5, 525, 800)], "fig-6.jpg")

# Resource Booklet Page 6: Board Sizing, Archimedes & Fig. 7
stitch_vert([crop_area(rb, 6, 50, 780)], "rb-p6.jpg")
stitch_vert([crop_area(rb, 6, 480, 700)], "fig-7.jpg")

# Resource Booklet Page 7: Inflating, NW20 Pump & Figs. 8, 9, 10
stitch_vert([crop_area(rb, 7, 50, 780)], "rb-p7.jpg")
stitch_vert([crop_area(rb, 7, 55, 230)], "fig-8.jpg")
stitch_vert([crop_area(rb, 7, 240, 555)], "fig-9.jpg")
stitch_vert([crop_area(rb, 7, 560, 760)], "fig-10.jpg")

# Resource Booklet Page 8: PB Speedometer, GENIE-14 & Figs. 11, 12
stitch_vert([crop_area(rb, 8, 50, 780)], "rb-p8.jpg")
stitch_vert([crop_area(rb, 8, 135, 305)], "fig-11.jpg")
stitch_vert([crop_area(rb, 8, 340, 555)], "fig-12.jpg")

# MS Exemplar diagrams for Question 4
# Sensor attachment sketches on MS Page 16
stitch_vert([crop_area(ms, 16, 75, 525, x0=130, x1=320)], "ms-4-sensor-sketches.jpg")
# Circuit diagram on MS Page 17
stitch_vert([crop_area(ms, 17, 155, 310, x0=130, x1=480)], "ms-4-circuit.jpg")
# Program flowchart on MS Page 18
stitch_vert([crop_area(ms, 18, 45, 525, x0=130, x1=400)], "ms-4-flowchart.jpg")

print("\n--- 2. Cropping Question Prompt Cards (Trimmed Answer Lines) ---")
# Q1* [14m] - Page 2
stitch_vert([
    crop_area(qp, 2, 95, 260),
    crop_area(qp, 2, 260, 285)
], "q1.jpg")

# Q2 [14m] - Page 4
stitch_vert([
    crop_area(qp, 4, 58, 200),
    crop_area(qp, 4, 200, 225)
], "q2.jpg")

# Q3(a) [6m] - Page 6
stitch_vert([
    crop_area(qp, 6, 58, 200),
    crop_area(qp, 6, 640, 675)
], "q3a.jpg")

# Q3(b)(i) [3m] - Page 7
stitch_vert([
    crop_area(qp, 7, 58, 215),
    crop_area(qp, 7, 450, 485)
], "q3bi.jpg")

# Q3(b)(ii) [3m] - Page 7
stitch_vert([
    crop_area(qp, 7, 485, 555),
    crop_area(qp, 7, 730, 765)
], "q3bii.jpg")

# Q4 [16m] - Page 8
stitch_vert([
    crop_area(qp, 8, 58, 480)
], "q4.jpg")

# Q5* [14m] - Page 12
stitch_vert([
    crop_area(qp, 12, 58, 145),
    crop_area(qp, 12, 145, 170)
], "q5.jpg")

print("\n--- 3. Cropping Mark Schemes ---")
def ms_box(pno, y0=49, y1=549):
    return autotrim_table(crop_area(ms, pno, y0, y1, x0=36, x1=826))

stitch_vert([ms_box(8), ms_box(9), ms_box(10, 49, 480)], "ms-1.jpg")
stitch_vert([ms_box(11), ms_box(12, 49, 545)], "ms-2.jpg")
stitch_vert([ms_box(13, 49, 545)], "ms-3a.jpg")
stitch_vert([ms_box(14, 48, 295)], "ms-3bi.jpg")
stitch_vert([ms_box(14, 295, 545)], "ms-3bii.jpg")
stitch_vert([ms_box(15), ms_box(16), ms_box(17), ms_box(18, 49, 545)], "ms-4.jpg")
stitch_vert([ms_box(19), ms_box(20, 49, 450)], "ms-5.jpg")

print("\n--- 4. Registering Questions in questions.json ---")
P = f"img/{PID}/"

questions_2022_02 = [
    # Q1* [14m]
    {
        "id": f"{PID}-q1", "paper": PID, "question": "1*", "marks": 14, "page": 2,
        "topics": ["1.1", "5.1"], "skills": ["design"],
        "summary": "Critically examine factors a company developing a new stand-up paddle board needs to consider, referencing different stakeholders.",
        "prompt": "Stand-up paddle boarding (SUP) has become popular in recent years with a rapid growth in the number of people trying out the sport, leading to an increase in sales of stand-up paddle boards.<br><br>The market now boasts a large selection of stand-up paddle boards with prices ranging from a few hundred pounds to thousands of pounds.<br><br>Critically examine the factors that a company looking to develop a new stand-up paddle board would need to consider, making specific reference to the different stakeholders affected.<br><br>Refer to information on page 2 and page 3 of the Resource Booklet. [*14]",
        "figures": [P + "rb-p2.jpg", P + "fig-1.jpg", P + "rb-p3.jpg", P + "fig-2.jpg"],
        "image": P + "q1.jpg", "markscheme": P + "ms-1.jpg",
        "markscheme_text": "<b>Level 4 (12–14 marks):</b> Comprehensive examination of factors across multiple user groups (recreational, intermediate, professional, hire clubs) and stakeholders (swimmers, coastguard, retailers, manufacturers). Clear, developed narrative covering design, economic, safety, and manufacturing considerations.<br><b>Level 3 (9–11 marks):</b> Good examination covering at least two considerations and two stakeholders with relevant detail.<br><b>Level 2 (5–8 marks):</b> Sufficient examination but lacks depth.<br><b>Level 1 (1–4 marks):</b> Limited descriptive comments.<br><br><b>Indicative Content:</b><br>• <b>Stakeholder User Groups:</b> Beginners require affordable, wide, high-stability inflatable boards with minimal setup friction; intermediate riders look for customizable fin boxes and touring hulls; pro racers demand ultra-stiff, lightweight rigid foam/GRP or carbon boards; hire centres/clubs prioritize extreme tear resistance, repairability, and high UV longevity.<br>• <b>Operating Environments:</b> Local flat-water rivers/canals require weed-resistant fins; open sea requires rockered bows to handle chop and safety leashes for tidal drift.<br>• <b>Manufacturing & Economics:</b> Drop-stitch PVC double-layer welding vs single-layer cost trade-offs; seasonal supply-and-demand spikes leading to winter inventory holding; market saturation prompting development of accessory ecosystems (paddles, dry bags, buoyancy aids, electric pumps).<br>• <b>Safety & Regulation:</b> Integration of high-visibility safety graphics, ISO-compliant buoyancy aids, quick-release ankle/waist leashes, and clear maritime navigation warnings."
    },
    # Q2 [14m]
    {
        "id": f"{PID}-q2", "paper": PID, "question": "2", "marks": 14, "page": 4,
        "topics": ["1.1", "3.1"], "skills": ["design", "technical"],
        "summary": "Identify design features and anthropometric/material data for designing a successful SUP paddle.",
        "prompt": "Selecting the correct paddle for riding a stand-up paddle board is vital for an efficient paddling action and to reduce the strain on the user’s back.<br><br>Use the information on page 4 and page 5 of the Resource Booklet to identify the design features and relevant data which a design engineer would need to consider when designing a successful paddle for the SUP market.<br><br>Your response <b>must</b> refer to ergonomic and anthropometric requirements as well as the use of materials in the paddle construction. You may use annotated sketches to explain your response. [14]",
        "figures": [P + "rb-p4.jpg", P + "fig-3.jpg", P + "rb-p5.jpg", P + "fig-4.jpg", P + "fig-5.jpg", P + "fig-6.jpg"],
        "image": P + "q2.jpg", "markscheme": P + "ms-2.jpg",
        "markscheme_text": "<b>Level 4 (12–14 marks):</b> Comprehensive coverage of all 3 paddle assemblies (Handle, Shaft, Blade) with precise anthropometric percentile application (5th–95th percentiles for height, grip reach, fist height) and sound material evaluation.<br><b>Level 3 (8–11 marks):</b> Good coverage of at least 2 parts with clear anthropometric and material references.<br><b>Level 2 (4–7 marks):</b> Sufficient understanding but limited data application.<br><b>Level 1 (1–3 marks):</b> Basic comments.<br><br><b>Technical Areas to Cover:</b><br>• <b>Paddle Handle:</b> Ergonomically contoured T-grip or palm grip sized for hand breadth percentiles; non-slip textured elastomer overmoulding; angled offset to align with wrist biomechanics.<br>• <b>Paddle Shaft:</b> Sizing formula ($L = \\text{user height} + 20\\text{ cm}$); adjustable telescoping 2-piece / 3-piece breakdown mechanism with lever-cam lock to accommodate 5th percentile females to 95th percentile males; material choice: budget aluminium (3 kg), intermediate GRP (1.3 kg), premium CFRP (<1 kg) for fatigue reduction and high stiffness.<br>• <b>Paddle Blade:</b> Teardrop shape wider at bottom for instant catch in flat water/surfing; dihedral spine and curved scoop to stabilize water flow and prevent flutter; blade surface area ($550 - 612\\text{ cm}^2$) matched to user cadence and strength."
    },
    # Q3(a) [6m]
    {
        "id": f"{PID}-q3a", "paper": PID, "question": "3(a)", "marks": 6, "page": 6,
        "topics": ["6.2"], "skills": ["maths", "technical"],
        "summary": "Determine by calculation the most suitable stand-up paddle board from Fig. 7 for an 80 kg user carrying 15 kg gear in sea water.",
        "prompt": "Stand-up paddle boards are made in different sizes to suit the weight of the user and the load they wish to carry. The Resource Booklet contains data for five stand-up paddle boards.<br><br>A user has a mass of 80 kg and they will also carry a backpack of mass 12 kg and a paddle of mass 3 kg. They will use the stand-up paddle board in the sea.<br><br>Determine by calculation the most suitable stand-up paddle board for this user, ignoring the weight of the paddle board.<br><br>Refer to Fig. 7 and the information on page 6 of the Resource Booklet. [6]",
        "figures": [P + "rb-p6.jpg", P + "fig-7.jpg"],
        "image": P + "q3a.jpg", "markscheme": P + "ms-3a.jpg",
        "markscheme_text": "<b>Archimedes Principle Sizing Steps (6 marks):</b><br>1. Total load mass: $M = 80\\text{ kg} + 12\\text{ kg} + 3\\text{ kg} = \\mathbf{95\\text{ kg}}$ [1 mark]<br>2. Total weight force: $W = M \\times g = 95 \\times 9.81 = \\mathbf{931.95\\text{ N}}$ [1 mark]<br>3. Rearrange buoyant force equation: $B = \\rho V g \\implies V = \\frac{B}{\\rho g}$ [1 mark]<br>4. Calculate displaced water volume (sea water $\\rho = 1025\\text{ kg/m}^3$):<br>$$V = \\frac{931.95}{1025 \\times 9.81} = \\frac{931.95}{10055.25} \\approx 0.09268\\text{ m}^3 \\quad [1\\text{ mark}]$$<br>5. Convert to litres and apply half-submerged rule:<br>$$V_{\\text{displaced}} = 0.09268 \\times 1000 = 92.68\\text{ litres (or 93 L)}$$<br>$$\\text{Total board volume required} = 2 \\times 92.68 = \\mathbf{185.36\\text{ litres (or 186 L)}} \\quad [1\\text{ mark}]$$<br>6. Select matching board from Fig. 7:<br><b>Board-14</b> has a volume of $185\\text{ litres}$ (closest match to 185.4 L). Answer: <b>Board-14</b> [1 mark]"
    },
    # Q3(b)(i) [3m]
    {
        "id": f"{PID}-q3bi", "paper": PID, "question": "3(b)(i)", "marks": 3, "page": 7,
        "topics": ["6.2"], "skills": ["maths"],
        "summary": "Estimate the time in seconds for the NW20 pump to inflate Board-16 (250 L) to 0.8 bar using Fig. 9.",
        "prompt": "The NW20 air pump, described on page 7 of the Resource Booklet, has been specifically designed to inflate a stand-up paddle board and is run from a 12 V car battery.<br><br>The NW20 air pump is being used to inflate Board-16 to the pressure shown in Fig. 7 on page 6 of the Resource booklet.<br><br>Using Fig. 9 as the basis for your calculations, estimate the time taken for the NW20 air pump to inflate Board-16 to the required pressure. Give your answer in seconds (s) and show your working.<br><br>You will need to use the information on page 6 and page 7 of the Resource Booklet. [3]",
        "figures": [P + "rb-p6.jpg", P + "fig-7.jpg", P + "rb-p7.jpg", P + "fig-9.jpg"],
        "image": P + "q3bi.jpg", "markscheme": P + "ms-3bi.jpg",
        "markscheme_text": "<b>Inflation Time Steps (3 marks):</b><br>1. Identify target pressure and baseline time from Fig. 9: Target pressure for Board-16 is $0.8\\text{ bar}$. Time to fill a $100\\text{ litre}$ vessel to $0.8\\text{ bar} = \\mathbf{40\\text{ seconds}}$ [1 mark]<br>2. Scale volume ratio: Volume of Board-16 is $250\\text{ litres}$. Ratio $= \\frac{250}{100} = \\mathbf{2.5\\times}$ [1 mark]<br>3. Calculate total time: $\\text{Time} = 2.5 \\times 40\\text{ s} = \\mathbf{100\\text{ seconds}}$ [1 mark]"
    },
    # Q3(b)(ii) [3m]
    {
        "id": f"{PID}-q3bii", "paper": PID, "question": "3(b)(ii)", "marks": 3, "page": 7,
        "topics": ["6.3"], "skills": ["maths"],
        "summary": "Calculate electrical energy used in joules by the NW20 pump to fill Board-16 to required pressure.",
        "prompt": "Use your answer from part (b)(i) and the information on page 7 of the Resource Booklet to calculate the electrical energy used by the NW20 air pump to fill Board-16 to the required pressure. Give your answer in joules (J) to <b>0 decimal places</b> and show your working. [3]",
        "figures": [P + "rb-p7.jpg", P + "fig-10.jpg"],
        "image": P + "q3bii.jpg", "markscheme": P + "ms-3bii.jpg",
        "markscheme_text": "<b>Energy Formula Steps (3 marks):</b><br>1. Convert current to amps: $I = 10\\,000\\text{ mA} = \\mathbf{10\\text{ A}}$ [1 mark]<br>2. Extract values: $V = 12\\text{ V}$, $t = 100\\text{ s}$ [1 mark]<br>3. Apply energy formula: $E = V \\times I \\times t = 12\\text{ V} \\times 10\\text{ A} \\times 100\\text{ s} = \\mathbf{12\\,000\\text{ J}}$ (or $12\\text{ kJ}$) [1 mark]"
    },
    # Q4 [16m]
    {
        "id": f"{PID}-q4", "paper": PID, "question": "4", "marks": 16, "page": 8,
        "topics": ["6.3", "6.4"], "skills": ["technical", "design"],
        "summary": "Determine technical solutions for the PB Speedometer: removable sensor mounting & detection, and GENIE-14 circuit & 5-LED bar graph flowchart.",
        "prompt": "A start-up company wishes to develop an electronic Paddle Board (PB) Speedometer which gives an indication to the user of the speed that the stand-up paddle board is travelling through the water. Information for the proposed product is given on page 8 of the Resource Booklet.<br><br>The design engineers have been instructed to solve the following two issues to help with the development of the PB Speedometer.<br><b>Issue 1:</b> To measure the speed that the stand-up paddle board travels through the water, a suitable sensor needs to be designed. This sensor must be able to be firmly attached to an inflated stand-up paddle board but must be removable when the stand-up paddle board is deflated and packed away. The electronic output signal from the sensor will be processed by a microcontroller.<br><b>Issue 2:</b> The signal from the sensor will be processed by a GENIE-14 microcontroller and the speed of the stand-up paddle board will be displayed to the user on a 5-LED bar graph display. Details of the GENIE-14 microcontroller and the bar graph display are shown on page 8 of the Resource Booklet. A circuit diagram and a program flowchart are required to enable the PB Speedometer system to function as described. The circuit diagram must show how the sensor and the five LEDs are connected to the microcontroller. The program flowchart should indicate how increasing speed causes more LEDs to light.<br><br>Use sketches and/or notes to determine suitable technical solutions that overcome the two issues identified. Refer to information on page 8 of the Resource Booklet. [16]",
        "figures": [P + "rb-p8.jpg", P + "fig-11.jpg", P + "fig-12.jpg", P + "ms-4-sensor-sketches.jpg", P + "ms-4-circuit.jpg", P + "ms-4-flowchart.jpg"],
        "image": P + "q4.jpg", "markscheme": P + "ms-4.jpg",
        "markscheme_text": "<b>Award up to 8 marks for Issue 1 and up to 8 marks for Issue 2 (Total 16 marks):</b><br><br><b>Issue 1 Breakdown (8 marks):</b><br>• <b>Sensor Design & Operation (4 marks):</b> Identifies valid mechanism: miniature water impeller driving a tiny DC generator to produce variable DC voltage (Method 1), or magnetic paddle wheel triggering a reed switch/Hall effect sensor to produce speed-proportional frequency pulses (Method 2); water flow path and waterproof casing detailed.<br>• <b>Attachment / Detachment Mechanism (4 marks):</b> Shows non-destructive mounting system: heavy-duty clamp around board rail, fin-box slide-and-click locking tab, or heavy-duty velcro/suction strap; securely holds sensor during paddling and easily releases when deflating without puncturing PVC.<br><br><b>Issue 2 Breakdown (8 marks):</b><br>• <b>Circuit Diagram (4 marks):</b> Power supply (+5V, 0V) connected to GENIE-14; sensor output routed to input pin (e.g. Analogue A0 for voltage, or Digital D1 for pulse counting); 5 outputs (Q0–Q4) connected to 5 LEDs of bar graph with correct forward polarity and individual protective current-limiting resistors (e.g. $330\\,\\Omega$).<br>• <b>Program Flowchart (4 marks):</b> Start block; reads sensor input; sequential comparison against rising threshold variables (`sensor > 10`, `sensor > 20`, `sensor > 30`, `sensor > 40`, `sensor > 50`); activates corresponding incremental LED outputs (`LED 1 on`, `LED 1,2 on`, etc.); turns off upper LEDs as speed drops; infinite loop."
    },
    # Q5* [14m]
    {
        "id": f"{PID}-q5", "paper": PID, "question": "5*", "marks": 14, "page": 12,
        "topics": ["5.1"], "skills": ["design"],
        "summary": "Explain how enterprise can help drive development and commercialization of a new product such as the PB Speedometer.",
        "prompt": "As a new company, the developer of the PB Speedometer will require investment for further development and for getting the product onto the market.<br><br>Explain how <b>enterprise</b> can help drive the development of a new product such as the PB Speedometer. Your answer <b>must</b> make use of examples from your own studies. [*14]",
        "figures": [P + "rb-p8.jpg"],
        "image": P + "q5.jpg", "markscheme": P + "ms-5.jpg",
        "markscheme_text": "<b>Level 4 (12–14 marks):</b> Comprehensive understanding of enterprise driving development for both the PB Speedometer and at least two detailed case studies from own studies (e.g. Dyson, Raspberry Pi, Pebble, Kickstarter campaigns). Clear, developed narrative covering multiple enterprise models.<br><b>Level 3 (9–11 marks):</b> Good understanding referencing PB Speedometer and at least one case study.<br><b>Level 2 (5–8 marks):</b> Sufficient understanding but limited external examples.<br><b>Level 1 (1–4 marks):</b> Basic comments.<br><br><b>Enterprise Strategies to Evaluate:</b><br>• <b>Crowdfunding (Kickstarter/Indiegogo):</b> Pre-orders validate market demand before committing tooling CapEx; creates early community of enthusiast testers who provide UX feedback; raises non-dilutive capital without giving away equity.<br>• <b>Angel Investors & Venture Capital:</b> High-net-worth individuals provide capital injection in exchange for equity; brings industry connections, logistics scaling expertise, and supply chain mentorship (e.g. Dragons' Den model).<br>• <b>Commercial Partnerships / Joint Ventures:</b> Partnering with established paddle board manufacturers (e.g. Red Paddle Co) to bundle the speedometer with new boards or sell via existing retail distribution channels; co-branding reduces customer acquisition cost.<br>• <b>Government Enterprise Grants / Accelerators:</b> Innovation UK grants or regional incubator funds provide grant funding for marine tech R&D and intellectual property patent protection."
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
    "year": 2022,
    "level": "H404",
    "totalMarks": 70,
    "series": "Summer"
}

# Update or insert paper entry
d["papers"] = [p for p in d["papers"] if p["id"] != PID]
d["papers"].append(paper_entry)

# Filter out old partial 2022-summer-02 questions and append new authentic 7 questions
d["questions"] = [q for q in d["questions"] if q.get("paper") != PID] + questions_2022_02

with open(qpath, "w", encoding="utf-8") as f:
    json.dump(d, f, indent=2, ensure_ascii=False)

print(f"\n✓ Successfully registered {len(questions_2022_02)} questions totaling {sum(q['marks'] for q in questions_2022_02)} marks into questions.json!")
