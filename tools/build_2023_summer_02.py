"""
Build OCR H404/02 Problem Solving in Design Engineering - June 2023 (paper id 2023-summer-02).
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
QP_PATH = os.path.join(BASE_UP, "media_1795110317476_4679c2e5.pdf")
RB_PATH = os.path.join(BASE_UP, "media_1795110317484_8fb96ae2.pdf")
MS_PATH = os.path.join(BASE_UP, "media_1795110317466_c1794bb1.pdf")

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PID = "2023-summer-02"
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
# RB p2-3: Climate Change stimulus
stitch_vert([
    crop_area(rb, 2, 50, 780),
    crop_area(rb, 3, 50, 780)
], "rb-climate-change.jpg")

# RB p4: PWS Sensor & Remote display units
stitch_vert([crop_area(rb, 4, 50, 780)], "rb-pws-units.jpg")

# RB p5: Rain sensor funnel Fig. 5
stitch_vert([crop_area(rb, 5, 50, 390)], "rb-rain-funnel.jpg")

# RB p5: Pressure sensor Fig. 6
stitch_vert([crop_area(rb, 5, 390, 790)], "rb-pressure-sensor.jpg")

# RB p6: Mounting solutions & mild steel tubes (Fig. 7 & 8)
stitch_vert([crop_area(rb, 6, 50, 795)], "rb-mounting-tubes.jpg")

# RB p7: Wind speed sensor Fig. 9
stitch_vert([crop_area(rb, 7, 50, 530)], "rb-wind-sensor.jpg")

# RB p8-9: PICAXE 14M2 & Radio circuits (Fig. 10 & 11)
stitch_vert([
    crop_area(rb, 8, 50, 650),
    crop_area(rb, 9, 50, 560)
], "rb-electronics-radio.jpg")

# Exemplars from MS:
# MS p21: Monopole stand design exemplar sketch
stitch_vert([crop_area(ms, 21, 50, 560, x0=100, x1=740)], "ms-4-monopole-sketch.jpg")

# MS p22: Slotted opto-switch diagram
stitch_vert([crop_area(ms, 22, 335, 435, x0=100, x1=580)], "ms-5-opto-sensor.jpg")

# MS p23: Epicyclic gear diagram
stitch_vert([crop_area(ms, 23, 185, 370, x0=100, x1=580)], "ms-5-epicyclic-gear.jpg")

# MS p25: Student sketch for Issue 1
stitch_vert([crop_area(ms, 25, 50, 560, x0=80, x1=740)], "ms-5-wind-sketch.jpg")

# MS p26: Circuit diagram exemplar for Issue 2
stitch_vert([crop_area(ms, 26, 290, 550, x0=90, x1=580)], "ms-5-circuit-diagram.jpg")

# MS p28: Flowchart Example 1
stitch_vert([crop_area(ms, 28, 50, 560, x0=100, x1=740)], "ms-5-flowchart-ex1.jpg")

# MS p29: Flowchart Example 2
stitch_vert([crop_area(ms, 29, 50, 560, x0=100, x1=740)], "ms-5-flowchart-ex2.jpg")


print("\n--- 2. Cropping Question Prompt Cards ---")
# q1.jpg
stitch_vert([
    crop_area(qp, 2, 85, 215),
    crop_area(qp, 2, 215, 255),
    crop_area(qp, 3, 745, 785)
], "q1.jpg")

# q2.jpg
stitch_vert([
    crop_area(qp, 4, 85, 245),
    crop_area(qp, 4, 245, 285),
    crop_area(qp, 5, 745, 785)
], "q2.jpg")

# q3ai.jpg
stitch_vert([
    crop_area(qp, 6, 60, 180),
    crop_area(qp, 6, 735, 775)
], "q3ai.jpg")

# q3aii.jpg
stitch_vert([
    crop_area(qp, 7, 60, 330),
    crop_area(qp, 7, 735, 775)
], "q3aii.jpg")

# q3bi.jpg
stitch_vert([
    crop_area(qp, 8, 60, 135),
    crop_area(qp, 8, 135, 160)
], "q3bi.jpg")

# q3bii.jpg
stitch_vert([
    crop_area(qp, 8, 165, 255),
    crop_area(qp, 8, 325, 360)
], "q3bii.jpg")

# q4.jpg
stitch_vert([
    crop_area(qp, 9, 60, 290)
], "q4.jpg")

# q5.jpg
stitch_vert([
    crop_area(qp, 12, 60, 595)
], "q5.jpg")


print("\n--- 3. Cropping Mark Schemes ---")
# ms-1.jpg
stitch_vert([
    crop_area(ms, 8, 125, 545, x0=45, x1=790),
    crop_area(ms, 9, 70, 545, x0=45, x1=790),
    crop_area(ms, 10, 60, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 11, 60, 480, x0=45, x1=790))
], "ms-1.jpg")

# ms-2.jpg
stitch_vert([
    crop_area(ms, 12, 65, 545, x0=45, x1=790),
    crop_area(ms, 13, 65, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 14, 65, 480, x0=45, x1=790))
], "ms-2.jpg")

# ms-3ai.jpg
stitch_vert([
    crop_area(ms, 15, 65, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 16, 65, 205, x0=45, x1=790))
], "ms-3ai.jpg")

# ms-3aii.jpg
stitch_vert([
    autotrim_table(crop_area(ms, 16, 205, 545, x0=45, x1=790))
], "ms-3aii.jpg")

# ms-3bi.jpg
stitch_vert([
    autotrim_table(crop_area(ms, 17, 65, 210, x0=45, x1=790))
], "ms-3bi.jpg")

# ms-3bii.jpg
stitch_vert([
    autotrim_table(crop_area(ms, 17, 210, 480, x0=45, x1=790))
], "ms-3bii.jpg")

# ms-4.jpg
stitch_vert([
    crop_area(ms, 18, 65, 545, x0=45, x1=790),
    crop_area(ms, 19, 65, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 20, 65, 300, x0=45, x1=790))
], "ms-4.jpg")

# ms-5.jpg
stitch_vert([
    crop_area(ms, 22, 65, 545, x0=45, x1=790),
    crop_area(ms, 23, 65, 545, x0=45, x1=790),
    crop_area(ms, 24, 65, 545, x0=45, x1=790),
    crop_area(ms, 26, 65, 545, x0=45, x1=790),
    autotrim_table(crop_area(ms, 27, 65, 545, x0=45, x1=790))
], "ms-5.jpg")


print("\n--- 4. Assembling Questions JSON Entry for 2023-summer-02 ---")

new_questions = [
    {
        "id": "2023-h404-02-q1",
        "paper": PID,
        "question_number": "1*",
        "marks": 12,
        "topic": "Climate Change & Environmental Impacts",
        "question": "Climate change is affecting all parts of the world. Failing to control it could have devastating impacts across the globe. Critically examine the ways in which climate change and the methods to control it, affect global communities. Refer to information on pages 2–3 of the Resource Booklet and also information from your own studies.",
        "image": f"img/{PID}/q1.jpg",
        "figures": [f"img/{PID}/rb-climate-change.jpg"],
        "markscheme": f"img/{PID}/ms-1.jpg",
        "markscheme_text": "**Level of Response (12 marks):**\n\n- **Level 4 (10–12 marks):** Comprehensive, critically evaluative examination of climate change impacts on global communities balanced against the socio-economic and technological consequences of mitigation methods.\n- **Level 3 (7–9 marks):** Detailed examination exploring both impacts and mitigation strategies across diverse global contexts.\n- **Level 2 (4–6 marks):** Sound discussion identifying some climate effects and control measures.\n- **Level 1 (1–3 marks):** Basic points on weather changes or global warming.\n\n**Indicative Content:**\n- **Direct Impacts of Climate Change:**\n  - Rising temperatures cause melting polar ice sheets, sea-level rise, coastal flooding, displacement of low-lying island communities (climate refugees).\n  - Extreme weather events: severe droughts causing crop failure, famine, food price spikes; intensified hurricanes destroying infrastructure.\n  - Disproportionate impact: Top 10 emitting countries produce 68% of emissions, whereas the bottom 100 produce only 3% but face the worst existential risks.\n- **Methods to Control Climate Change & Community Impacts:**\n  - Transitioning to renewables (wind, solar, nuclear) requires huge initial capital expenditure and grid reconfiguration, impacting energy costs.\n  - Transitioning from fossil fuel vehicles to electric vehicles (EVs) requires mining rare earth metals (lithium, cobalt) with localized ecological and ethical costs.\n  - Agricultural reforms (reducing livestock methane emissions, reforesting cleared land) impact rural farming livelihoods, requiring balanced food security policies."
    },
    {
        "id": "2023-h404-02-q2",
        "paper": PID,
        "question_number": "2*",
        "marks": 14,
        "topic": "Design for Manufacture & IoT Hardware",
        "question": "Weather Watch (WW) is using the funding it has received to manufacture its Pro Weather Station (PWS). Discuss the factors that a design engineer would need to consider when manufacturing the PWS sensor unit and the remote display unit. Refer to information on page 4 of the Resource Booklet.",
        "image": f"img/{PID}/q2.jpg",
        "figures": [f"img/{PID}/rb-pws-units.jpg"],
        "markscheme": f"img/{PID}/ms-2.jpg",
        "markscheme_text": "**Level of Response (14 marks):**\n\n- **Level 4 (11–14 marks):** Comprehensive discussion addressing all design engineering factors (materials, manufacturing methods, power supply, wireless telemetry, weatherproofing, and batch production of 100,000 units).\n- **Level 3 (7–10 marks):** Thorough discussion addressing multiple relevant manufacturing and operational factors.\n- **Level 2 (4–6 marks):** Competent discussion with some specific manufacturing details.\n- **Level 1 (1–3 marks):** Basic awareness of materials and manufacturing.\n\n**Key Indicative Content:**\n- **Materials Selection:**\n  - Outdoor sensor housing: UV-stabilised ABS or ASA polymer for high impact strength, UV-degradation resistance, and thermal stability (-35°C to +60°C).\n  - Internal hardware/fasteners: Marine-grade stainless steel (316) or brass to avoid galvanic corrosion and rust in wet outdoor environments.\n  - Indoor display unit: Recycled ABS/HIPS or PMMA (acrylic) for modern, clean aesthetic appeal.\n- **Manufacturing Methods (Batch 100,000 units):**\n  - High-pressure injection moulding with multi-cavity hardened steel tooling for cost-effective, high-tolerance mass production of housings.\n  - Automated Surface Mount Technology (SMT) for rapid, defect-free printed circuit board (PCB) assembly.\n  - Ingress Protection (IP65/IP66) sealing using co-moulded elastomer gaskets (TPE) or ultrasonic welding.\n- **Power Source & Wireless Data Transmission:**\n  - Sensor unit: Solar panel with rechargeable Li-ion / supercapacitor buffer, or ultra-low-power sleep modes with long-life lithium primary cells.\n  - Display unit: USB mains adapter with coin-cell backup for real-time clock retention.\n  - Wireless telemetry: 433 MHz / 868 MHz ISM radio frequency link for robust long-range penetration through domestic brick walls with low power consumption."
    },
    {
        "id": "2023-h404-02-q3ai",
        "paper": PID,
        "question_number": "3(a)(i)",
        "marks": 6,
        "topic": "Frustum Geometry & Conical Volumetrics",
        "question": "Use the information in Fig. 5 of the Resource Booklet to calculate the total internal volume of the funnel (both sections). Give your answer in cm3 to 2 decimal places. Show your working. Volume of a cone = 1/3 pi r^2 h.",
        "image": f"img/{PID}/q3ai.jpg",
        "figures": [f"img/{PID}/rb-rain-funnel.jpg"],
        "markscheme": f"img/{PID}/ms-3ai.jpg",
        "markscheme_text": "**Six marks total:**\n\n1. Identify conical dimensions and radii:  \n   $$R_1 = \\frac{110\\text{ mm}}{2} = 55\\text{ mm} = 5.5\\text{ cm} \\quad [1]$$\n   $$R_2 = \\frac{20\\text{ mm}}{2} = 10\\text{ mm} = 1.0\\text{ cm}$$\n   $$\\text{Height of conical section } h = 49\\text{ mm} = 4.9\\text{ cm}$$\n\n2. Calculate full apex height \\(H\\) of cone by similar triangles:  \n   $$\\frac{H}{55} = \\frac{H - 49}{10} \\implies 10H = 55H - 2695 \\implies 45H = 2695 \\implies H = 59.889\\text{ mm} = 5.989\\text{ cm} \\quad [1]$$\n\n3. Calculate volume of large cone:  \n   $$V_{\\text{large}} = \\frac{1}{3}\\pi R_1^2 H = \\frac{1}{3}\\pi (5.5)^2 (5.989) = 189.72\\text{ cm}^3 \\quad [1]$$\n\n4. Calculate volume of small cut-off cone:  \n   $$h_2 = 59.889 - 49 = 10.889\\text{ mm} = 1.089\\text{ cm}$$\n   $$V_{\\text{small}} = \\frac{1}{3}\\pi R_2^2 h_2 = \\frac{1}{3}\\pi (1.0)^2 (1.089) = 1.14\\text{ cm}^3 \\quad [1]$$\n\n5. Volume of conical frustum:  \n   $$V_{\\text{frustum}} = 189.72 - 1.14 = 188.58\\text{ cm}^3 \\quad (\\text{or via frustum formula: } 188.92\\text{ cm}^3) \\quad [1]$$\n\n6. Add cylindrical volume and give total:  \n   $$V_{\\text{total}} = 188.92 + 4.7 = \\mathbf{193.6\\text{ cm}^3} \\quad (\\text{accept } 193.28\\text{ cm}^3 - 193.62\\text{ cm}^3) \\quad [1]$$"
    },
    {
        "id": "2023-h404-02-q3aii",
        "paper": PID,
        "question_number": "3(a)(ii)",
        "marks": 3,
        "topic": "Volumetric Flow & Collection Rates",
        "question": "During a period of rain, the rain falls steadily at a rate of 0.2 cm3 per cm2 per hour. Calculate the time it takes for the rain to fill just the cylindrical section of the funnel. Give your answer in minutes to 1 decimal place. Show your working.",
        "image": f"img/{PID}/q3aii.jpg",
        "figures": [f"img/{PID}/rb-rain-funnel.jpg"],
        "markscheme": f"img/{PID}/ms-3aii.jpg",
        "markscheme_text": "**Three marks total:**\n\n1. Calculate top catchment area of funnel:  \n   $$r = 5.5\\text{ cm}$$\n   $$\\text{Area } A = \\pi r^2 = \\pi (5.5)^2 = 95.033\\text{ cm}^2 \\quad [1]$$\n\n2. Calculate rainfall volume collection rate per hour:  \n   $$\\text{Rate} = 0.2\\text{ cm}^3/(\\text{cm}^2\\cdot\\text{hr}) \\times 95.033\\text{ cm}^2 = 19.007\\text{ cm}^3/\\text{hr} \\quad [1]$$\n\n3. Calculate time to collect 4.7 cm3 in minutes:  \n   $$\\text{Time} = \\frac{4.7\\text{ cm}^3}{19.007\\text{ cm}^3/\\text{hr}} = 0.24728\\text{ hours}$$\n   $$\\text{Time in minutes} = 0.24728 \\times 60 = 14.837\\text{ minutes} \\approx \\mathbf{14.8\\text{ minutes}} \\quad [1]$$"
    },
    {
        "id": "2023-h404-02-q3bi",
        "paper": PID,
        "question_number": "3(b)(i)",
        "marks": 1,
        "topic": "Sensor Characterisation & Calibration Graphs",
        "question": "Use data from Fig. 6 of the Resource Booklet to determine the value of the output voltage from the BP135 sensor when the air pressure is 100 kPa.",
        "image": f"img/{PID}/q3bi.jpg",
        "figures": [f"img/{PID}/rb-pressure-sensor.jpg"],
        "markscheme": f"img/{PID}/ms-3bi.jpg",
        "markscheme_text": "**One mark:**\n- Reading from the calibration graph in Fig. 6 at 100 kPa:  \n  $$\\mathbf{V_{\\text{out}} = 3.3\\text{ V}} \\quad (\\text{accept } 3.2\\text{ V} - 3.4\\text{ V})$$"
    },
    {
        "id": "2023-h404-02-q3bii",
        "paper": PID,
        "question_number": "3(b)(ii)",
        "marks": 2,
        "topic": "ADC Resolution & Pressure Sensitivity",
        "question": "The output from the BP135 sensor is fed into the analogue input of a microcontroller. The smallest change of input voltage that the microcontroller can detect is 5 mV. Use the information in Fig. 6 of the Resource Booklet to calculate the smallest change in air pressure that can be detected by the microcontroller. Give your answer in kPa to 3 decimal places. Show your working.",
        "image": f"img/{PID}/q3bii.jpg",
        "figures": [f"img/{PID}/rb-pressure-sensor.jpg"],
        "markscheme": f"img/{PID}/ms-3bii.jpg",
        "markscheme_text": "**Two marks total:**\n\n1. Identify sensor output sensitivity from specification table:  \n   $$\\text{Sensitivity} = 40\\text{ mV/kPa} \\quad [1]$$\n\n2. Calculate smallest detectable air pressure change:  \n   $$\\Delta P = \\frac{5\\text{ mV}}{40\\text{ mV/kPa}} = \\mathbf{0.125\\text{ kPa}} \\quad [1]$$"
    },
    {
        "id": "2023-h404-02-q4",
        "paper": PID,
        "question_number": "4",
        "marks": 16,
        "topic": "Monopole Structural Design & Flatpack Engineering",
        "question": "WW requires 100 000 PWS sensor unit mounting solutions that will be flatpacked for transportation in a 1.5 m long cardboard tube. Use sketches and/or notes to outline a suitable monopole design for the mounting solution. For the monopole you must only select mild steel tubes from Fig. 8 of the Resource Booklet. In your answer you must consider the design requirements as listed on page 6 of the Resource Booklet: • mild steel tube sizes chosen for the monopole • specialist parts and assembly methods used • methods to ensure the monopole is freestanding and can withstand high winds. Refer to all of the information on page 6 of the Resource Booklet.",
        "image": f"img/{PID}/q4.jpg",
        "figures": [f"img/{PID}/rb-mounting-tubes.jpg", f"img/{PID}/ms-4-monopole-sketch.jpg"],
        "markscheme": f"img/{PID}/ms-4.jpg",
        "markscheme_text": "**Level of Response (16 marks):**\n\n- **Level 4 (13–16 marks):** Comprehensive, fully engineered monopole design satisfying all constraints: correct mild steel tube selection from Fig. 8, robust tool-free jointing, effective freestanding base / ground anchoring, sensor mounting flange, and corrosion protection.\n- **Level 3 (9–12 marks):** Clear monopole design addressing assembly, packaging, and stability.\n- **Level 2 (5–8 marks):** Competent design with some omissions.\n- **Level 1 (1–4 marks):** Basic sketch or incomplete mounting proposal.\n\n**Key Engineering Elements:**\n- **Tube Selection & Telescoping / Sleeve Joint:**\n  - Select two 1.5 m tubes from Fig. 8 that fit closely (e.g. Tube B outer $\\varnothing 28.6$ mm / inner $\\varnothing 25.4$ mm and Tube A outer $\\varnothing 25.4$ mm; or Tube C outer $\\varnothing 31.8$ mm and Tube B outer $\\varnothing 28.6$ mm).\n  - Tool-free assembly: Push-button spring clip (snap button) that clicks into pre-drilled holes, or quick-release cam collar/bayonet pin mechanism.\n- **Sensor Mounting:**\n  - Welded or pre-fitted top mounting flange/bracket with thumbscrew clamp to securely retain the 150×200×200 mm PWS unit.\n- **Freestanding Stability in High Winds:**\n  - Three high-tensile steel guy wires with turnbuckles/carabiners attached to a collar midway/top and staked into soil with heavy-duty metal tent pegs; OR a folding tripod base / cross-foot with ground spikes or heavy ballast weights.\n- **Packaging & Protective Finish:**\n  - Disassembled sections (2 × 1.5 m tubes + guy wires + pegs) easily fit within the 1.5 m shipping tube.\n  - Hot-dip galvanised or exterior architectural polyester powder coating to withstand outdoor weathering and prevent corrosion."
    },
    {
        "id": "2023-h404-02-q5",
        "paper": PID,
        "question_number": "5",
        "marks": 16,
        "topic": "Embedded Telemetry & Anemometer Instrumentation",
        "question": "WW wants to explore the feasibility of adding a wind speed sensor to the PWS. The design engineers have to solve the following two issues: Issue 1: The sensor must produce output electrical signals which could be processed by a PICAXE 14M2 microcontroller. Use sketches and/or notes to further develop the wind speed sensor shown in Fig. 9 of the Resource Booklet. Issue 2: Draw a circuit diagram to show how the wind sensor electronic components and the radio transmitter components connect to the PICAXE 14M2, and draw a program flowchart that indicates how rotation speed is monitored and data transmitted. Refer to pages 7–9 of the Resource Booklet.",
        "image": f"img/{PID}/q5.jpg",
        "figures": [
            f"img/{PID}/rb-wind-sensor.jpg",
            f"img/{PID}/rb-electronics-radio.jpg",
            f"img/{PID}/ms-5-opto-sensor.jpg",
            f"img/{PID}/ms-5-circuit-diagram.jpg",
            f"img/{PID}/ms-5-flowchart-ex1.jpg"
        ],
        "markscheme": f"img/{PID}/ms-5.jpg",
        "markscheme_text": "**16 marks total (8 marks for Issue 1 + 8 marks for Issue 2):**\n\n**Issue 1: Mechanical & Sensor Development (8 marks):**\n- **Rotation & Bearing Support:** Low-friction stainless steel / ceramic ball bearings housed inside the fixed base to allow free rotation of the vertical rod with minimal wind resistance.\n- **Sensing Component Selection:**\n  - *Option A:* Slotted optical switch (phototransistor + IR LED) with a slotted encoder disc mounted on the rotating rod.\n  - *Option B:* Hall effect magnetic sensor or reed switch actuated by a small neodymium magnet embedded in the rotating hub.\n- **Signal Description:** Digital pulses whose frequency is directly proportional to rotational velocity (wind speed).\n\n**Issue 2: Circuit Diagram & Program Flowchart (8 marks):**\n- **Circuit Diagram:**\n  - PICAXE 14M2 powered from +V (Pin 1) and 0V (Pin 14).\n  - Sensor output connected to digital input pin (e.g. C.3) with appropriate pull-up/pull-down resistor.\n  - Serial Data Out (pin B.0 / Sout) connected to NKM2401 Serial Data In (pin 2).\n  - NKM2401 module interfaced with A434 radio transmitter, including 10 kΩ pull-down resistor and 100 nF decoupling capacitors across supply rails.\n- **Program Flowchart:**\n  - Start $\\to$ Initialize pulse counter variable $= 0$.\n  - Start a fixed timer loop (e.g. 1.0 second or use hardware `count` command).\n  - Increment pulse counter on each rising edge from sensor input.\n  - When timer elapses, compute wind speed: $\\text{speed} = \\text{pulses} \\times \\text{calibration factor}$.\n  - Transmit data string via `serout` command to radio transmitter.\n  - Reset counter and repeat monitoring loop."
    }
]

print(f"Total new questions: {len(new_questions)}")
tot_m = sum(q['marks'] for q in new_questions)
print(f"Total marks for 2023-summer-02: {tot_m}/70 marks")
assert tot_m == 70, f"Marks mismatch: expected 70, got {tot_m}"

# Update questions.json
qpath = os.path.join(REPO, "questions.json")
with open(qpath, "r", encoding="utf-8") as f:
    db = json.load(f)

# Filter out old placeholders for 2023-summer-02
db["questions"] = [q for q in db["questions"] if q.get("paper") != PID]
db["questions"].extend(new_questions)

with open(qpath, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Successfully saved {len(new_questions)} questions into questions.json for {PID}!")
