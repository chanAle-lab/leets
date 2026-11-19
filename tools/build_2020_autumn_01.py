"""
Build and Ingest OCR H404/01 Autumn 2020 (Principles of Design Engineering)
Paper ID: 2020-autumn-01
Total Marks: 80 marks across 19 subquestions
"""
import os
import re
import json
import fitz
from PIL import Image

qp_path = r'C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded\media_1795097357720_416191c3.pdf'
ms_path = r'C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded\media_1795097352626_954663a3.pdf'
repo = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets'
out_dir = os.path.join(repo, 'img', '2020-autumn-01')
os.makedirs(out_dir, exist_ok=True)

qp = fitz.open(qp_path)
ms = fitz.open(ms_path)

zoom = 2.2
mat = fitz.Matrix(zoom, zoom)

def stitch(parts, out_name):
    imgs = [Image.open(p) for p in parts]
    w = max(im.width for im in imgs)
    h = sum(im.height for im in imgs)
    dst = Image.new('RGB', (w, h), (255, 255, 255))
    y = 0
    for im in imgs:
        dst.paste(im, (0, y))
        y += im.height
    dst.save(os.path.join(out_dir, out_name), quality=92)
    for p in parts:
        try: os.remove(p)
        except: pass

print("1. Cropping Resource Figures...")
fig_crops = {
    'fig-1-1.jpg': (2, fitz.Rect(45, 60, 555, 315)),
    'fig-1-2.jpg': (2, fitz.Rect(45, 315, 555, 765)),
    'fig-2-1.jpg': (8, fitz.Rect(45, 60, 555, 365)),
    'fig-2-2.jpg': (9, fitz.Rect(45, 60, 555, 355)),
    'fig-2-3.jpg': (10, fitz.Rect(45, 60, 555, 270)),
    'fig-4-1.jpg': (15, fitz.Rect(45, 60, 555, 470)),
    'fig-4-2.jpg': (16, fitz.Rect(45, 60, 555, 255)),
    'fig-4-3.jpg': (18, fitz.Rect(45, 60, 555, 260)),
    'fig-4-4.jpg': (19, fitz.Rect(45, 60, 555, 235)),
    'fig-4-5.jpg': (19, fitz.Rect(45, 235, 555, 775)),
}

for name, (pno, rect) in fig_crops.items():
    pix = qp[pno].get_pixmap(matrix=mat, clip=rect)
    pix.save(os.path.join(out_dir, name))
    print(f"  Figure {name}: {pix.width}x{pix.height}")

# Markscheme closed loop diagram
pix_diag = ms[7].get_pixmap(matrix=mat, clip=fitz.Rect(180, 280, 560, 495))
pix_diag.save(os.path.join(out_dir, 'ms-1bv-diagram.jpg'))

print("\n2. Cropping Question Cards (prompt and response space only)...")
q_crops = {
    'q1ai.jpg':   (1, fitz.Rect(45, 60, 555, 455)),
    'q1aii.jpg':  (1, fitz.Rect(45, 455, 555, 780)),
    'q1bi.jpg':   (3, fitz.Rect(45, 60, 555, 225)),
    'q1bii.jpg':  (3, fitz.Rect(45, 225, 555, 390)),
    'q1biii.jpg': (3, fitz.Rect(45, 390, 555, 775)),
    'q1biv.jpg':  (4, fitz.Rect(45, 60, 555, 435)),
    'q1bv.jpg':   (5, fitz.Rect(45, 60, 555, 775)),
    'q1bvi.jpg':  (6, fitz.Rect(45, 60, 555, 565)),
    'q2a.jpg':    (8, fitz.Rect(45, 365, 555, 775)),
    'q2bi.jpg':   (9, fitz.Rect(45, 355, 555, 645)),
    'q2bii.jpg':  (10, fitz.Rect(45, 270, 555, 775)),
    'q2biii.jpg': (11, fitz.Rect(45, 60, 555, 240)),
    'q2biv.jpg':  (11, fitz.Rect(45, 240, 555, 620)),
    'q3a.jpg':    (12, fitz.Rect(45, 60, 555, 400)),
    'q3b.jpg':    (13, fitz.Rect(45, 60, 555, 620)),
    'q4ai.jpg':   (16, fitz.Rect(45, 255, 555, 520)),
    'q4aii.jpg':  (16, fitz.Rect(45, 520, 555, 775)),
    'q4bi.jpg':   (17, fitz.Rect(45, 60, 555, 775)),
    'q4bii.jpg':  (18, fitz.Rect(45, 260, 555, 715)),
    'q4biii.jpg': (18, fitz.Rect(45, 715, 555, 775)),
    'q4c.jpg':    (20, fitz.Rect(45, 60, 555, 660)),
    'q4di.jpg':   (21, fitz.Rect(45, 60, 555, 145)),
    'q4dii.jpg':  (21, fitz.Rect(45, 145, 555, 410)),
}

for name, (pno, rect) in q_crops.items():
    pix = qp[pno].get_pixmap(matrix=mat, clip=rect)
    pix.save(os.path.join(out_dir, name))
    print(f"  Question {name}: {pix.width}x{pix.height}")

print("\n3. Cropping Mark Schemes...")
single_ms = {
    'ms-1ai.jpg':   (4, fitz.Rect(40, 95, 800, 375)),
    'ms-1aii.jpg':  (4, fitz.Rect(40, 370, 800, 565)),
    'ms-1bi.jpg':   (5, fitz.Rect(40, 180, 800, 480)),
    'ms-1bii.jpg':  (5, fitz.Rect(40, 475, 800, 565)),
    'ms-1biii.jpg': (6, fitz.Rect(40, 95, 800, 565)),
    'ms-1biv.jpg':  (7, fitz.Rect(40, 95, 800, 420)),
    'ms-2a.jpg':    (11, fitz.Rect(40, 95, 800, 360)),
    'ms-2bi.jpg':   (11, fitz.Rect(40, 355, 800, 565)),
    'ms-2bii.jpg':  (12, fitz.Rect(40, 95, 800, 420)),
    'ms-2biii.jpg': (12, fitz.Rect(40, 415, 800, 565)),
    'ms-3a.jpg':    (15, fitz.Rect(40, 95, 800, 350)),
    'ms-4ai.jpg':   (18, fitz.Rect(40, 95, 800, 320)),
    'ms-4aii.jpg':  (18, fitz.Rect(40, 315, 800, 490)),
    'ms-4bii.jpg':  (19, fitz.Rect(40, 275, 800, 565)),
    'ms-4biii.jpg': (20, fitz.Rect(40, 95, 800, 160)),
    'ms-4c.jpg':    (20, fitz.Rect(40, 160, 800, 505)),
    'ms-4di.jpg':   (20, fitz.Rect(40, 505, 800, 565)),
}

for name, (pno, rect) in single_ms.items():
    pix = ms[pno].get_pixmap(matrix=mat, clip=rect)
    pix.save(os.path.join(out_dir, name))

# Multi-page mark schemes
# 1bv: p7 bottom + p8 top
p1 = os.path.join(out_dir, '_tmp_ms_1bv_1.jpg')
p2 = os.path.join(out_dir, '_tmp_ms_1bv_2.jpg')
ms[7].get_pixmap(matrix=mat, clip=fitz.Rect(40, 420, 800, 565)).save(p1)
ms[8].get_pixmap(matrix=mat, clip=fitz.Rect(40, 95, 800, 545)).save(p2)
stitch([p1, p2], 'ms-1bv.jpg')

# 1bvi: p9 + p10
p1 = os.path.join(out_dir, '_tmp_ms_1bvi_1.jpg')
p2 = os.path.join(out_dir, '_tmp_ms_1bvi_2.jpg')
ms[9].get_pixmap(matrix=mat, clip=fitz.Rect(40, 95, 800, 565)).save(p1)
ms[10].get_pixmap(matrix=mat, clip=fitz.Rect(40, 95, 800, 280)).save(p2)
stitch([p1, p2], 'ms-1bvi.jpg')

# 2biv: p13 + p14
p1 = os.path.join(out_dir, '_tmp_ms_2biv_1.jpg')
p2 = os.path.join(out_dir, '_tmp_ms_2biv_2.jpg')
ms[13].get_pixmap(matrix=mat, clip=fitz.Rect(40, 95, 800, 565)).save(p1)
ms[14].get_pixmap(matrix=mat, clip=fitz.Rect(40, 95, 800, 260)).save(p2)
stitch([p1, p2], 'ms-2biv.jpg')

# 3b: p15 + p16 + p17
p1 = os.path.join(out_dir, '_tmp_ms_3b_1.jpg')
p2 = os.path.join(out_dir, '_tmp_ms_3b_2.jpg')
p3 = os.path.join(out_dir, '_tmp_ms_3b_3.jpg')
ms[15].get_pixmap(matrix=mat, clip=fitz.Rect(40, 345, 800, 565)).save(p1)
ms[16].get_pixmap(matrix=mat, clip=fitz.Rect(40, 95, 800, 565)).save(p2)
ms[17].get_pixmap(matrix=mat, clip=fitz.Rect(40, 95, 800, 360)).save(p3)
stitch([p1, p2, p3], 'ms-3b.jpg')

# 4bi: p18 + p19
p1 = os.path.join(out_dir, '_tmp_ms_4bi_1.jpg')
p2 = os.path.join(out_dir, '_tmp_ms_4bi_2.jpg')
ms[18].get_pixmap(matrix=mat, clip=fitz.Rect(40, 490, 800, 565)).save(p1)
ms[19].get_pixmap(matrix=mat, clip=fitz.Rect(40, 95, 800, 275)).save(p2)
stitch([p1, p2], 'ms-4bi.jpg')

# 4dii: p21 + p22
p1 = os.path.join(out_dir, '_tmp_ms_4dii_1.jpg')
p2 = os.path.join(out_dir, '_tmp_ms_4dii_2.jpg')
ms[21].get_pixmap(matrix=mat, clip=fitz.Rect(40, 95, 800, 565)).save(p1)
ms[22].get_pixmap(matrix=mat, clip=fitz.Rect(40, 95, 800, 230)).save(p2)
stitch([p1, p2], 'ms-4dii.jpg')

print("All mark scheme images stitched and saved!")

print("\n4. Building JSON question entries...")
new_questions = [
    # Q1
    {
        "id": "2020-autumn-01-q1ai",
        "paper": "2020-autumn-01",
        "question": "1(a)(i)",
        "marks": 3,
        "page": 2,
        "topics": ["6.5", "1.1"],
        "skills": ["technical"],
        "summary": "State the meaning of smart object, network, and communication protocol in a smart home technology system.",
        "prompt": "Smart home technology is increasing in popularity and is being installed in homes throughout the world. A smart home technology system involves a number of <b>smart objects</b>, known as smart home devices, being connected through a <b>network</b> and controlled from a central hub. Smart objects include light bulbs, window blinds, security cameras, kettles and other household appliances. A number of different <b>communication protocols</b> have been developed for use in smart home technology systems.<br><br>State the meaning of the following terms in the context of a smart home technology system: smart object, network, communication protocol. [3]",
        "figures": [],
        "image": "img/2020-autumn-01/q1ai.jpg",
        "markscheme": "img/2020-autumn-01/ms-1ai.jpg",
        "markscheme_text": "<b>One mark for definition of each term (max 3 marks):</b><br>• <b>Smart object:</b> A physical object with embedded electronic sensors/microcontrollers/actuators which is equipped for two-way communication (1).<br>• <b>Network:</b> A series of devices (e.g. smart objects) connected together in such a way that they can communicate with each other and exchange data (1).<br>• <b>Communication protocol:</b> An agreed method of communication between the devices in a network which allows for successful data exchange and routing (1)."
    },
    {
        "id": "2020-autumn-01-q1aii",
        "paper": "2020-autumn-01",
        "question": "1(a)(ii)",
        "marks": 4,
        "page": 2,
        "topics": ["6.5", "1.2"],
        "skills": ["design", "technical"],
        "summary": "Describe two benefits to a designer or manufacturer of embedding a microcontroller into a simple kettle.",
        "prompt": "The latest generation of simple household products, such as kettles, often contain an embedded microcontroller.<br><br>Describe <b>two</b> benefits to a designer or manufacturer of embedding a microcontroller into a kettle. [4]",
        "figures": [],
        "image": "img/2020-autumn-01/q1aii.jpg",
        "markscheme": "img/2020-autumn-01/ms-1aii.jpg",
        "markscheme_text": "<b>Up to two marks for describing each of two benefits to a designer or manufacturer (max 4 marks):</b><br>• Can add enhanced functionality, e.g. a smart kettle (1), increasing attraction to potential buyers (1).<br>• Control circuit may be a commonly available standard subsystem (1), making it simple for a designer to integrate rather than designing a bespoke control system (1).<br>• Kettle can be networked (1), so can be controlled remotely or exchange info e.g. about energy usage (1).<br>• Increased reliability (1), prolonging the kettle's life (1).<br>• Can accurately sense water temperature (1), meaning reliable boiling and energy saving (1).<br>• Firmware can be upgraded (1), so development features can be added later (1)."
    },
    {
        "id": "2020-autumn-01-q1bi",
        "paper": "2020-autumn-01",
        "question": "1(b)(i)",
        "marks": 2,
        "page": 4,
        "topics": ["6.1", "1.2"],
        "skills": ["technical", "design"],
        "summary": "Explain one functional feature of a worm drive system that makes it useful in the roller-blind drive system.",
        "prompt": "Fig. 1.1 shows a roller-blind fitted to a window. Fig. 1.2 shows part of a prototype roller-blind mechanical drive system driven by a DC motor through a worm drive system.<br><br>Explain <b>one</b> functional feature of a worm drive system which makes it useful in the roller-blind mechanical drive system shown in Fig. 1.2. [2]",
        "figures": ["img/2020-autumn-01/fig-1-1.jpg", "img/2020-autumn-01/fig-1-2.jpg"],
        "image": "img/2020-autumn-01/q1bi.jpg",
        "markscheme": "img/2020-autumn-01/ms-1bi.jpg",
        "markscheme_text": "<b>Up to two marks for explaining one functional feature of a worm drive system in this context (max 2 marks):</b><br>• The input worm screw can drive the output wheel/gear but not vice-versa (1), which means that the blind cannot fall under its own weight when the motor is not running (1).<br>• A large gear ratio provides slow rotation and steady controlled movement of the blind (1), enabling the user to stop the blind at a desired position (1).<br>• A large gear ratio can be achieved in a single stage (1), allowing for a compact gearbox size (1).<br>• The mechanism is quiet in operation (1), which is beneficial in a home environment (1)."
    },
    {
        "id": "2020-autumn-01-q1bii",
        "paper": "2020-autumn-01",
        "question": "1(b)(ii)",
        "marks": 2,
        "page": 4,
        "topics": ["6.1", "6.2"],
        "skills": ["maths"],
        "summary": "Calculate the circumference of the 35 mm roller in Fig. 1.2 to the nearest mm.",
        "prompt": "Calculate the circumference of the roller in Fig. 1.2 to the nearest mm. Show your working. [2]",
        "figures": ["img/2020-autumn-01/fig-1-2.jpg"],
        "image": "img/2020-autumn-01/q1bii.jpg",
        "markscheme": "img/2020-autumn-01/ms-1bii.jpg",
        "markscheme_text": "<b>Award two marks as follows:</b><br>• Formula: \\(\\text{Circumference} = \\pi d\\) (or \\(2\\pi r\\)) (1)<br>• Calculation: \\(\\text{Circumference} = \\pi \\times 35 = 109.955\\dots = 110\\text{ mm}\\) (to nearest mm) (1)"
    },
    {
        "id": "2020-autumn-01-q1biii",
        "paper": "2020-autumn-01",
        "question": "1(b)(iii)",
        "marks": 4,
        "page": 4,
        "topics": ["6.1", "6.2"],
        "skills": ["maths", "technical"],
        "summary": "Calculate the required motor output speed in rpm to raise the blind 165 mm in 2 seconds with a 40-tooth worm gear.",
        "prompt": "It has been determined that, during operation, the roller-blind mechanical drive system should take 2 seconds to raise the blind a vertical distance of 165 mm.<br><br>Using information from Fig. 1.2 and your answer to part (b)(ii), calculate the required output speed of the DC motor in revolutions per minute (rpm). Show your working.<br><br>Assume that the diameter of the roller stays constant as the blind rises. [4]",
        "figures": ["img/2020-autumn-01/fig-1-2.jpg"],
        "image": "img/2020-autumn-01/q1biii.jpg",
        "markscheme": "img/2020-autumn-01/ms-1biii.jpg",
        "markscheme_text": "<b>Award four marks as follows:</b><br>• Revolutions of roller to raise blind \\(165\\text{ mm} = \\frac{\\text{distance}}{\\text{circumference}} = \\frac{165}{110} = 1.5\\text{ revs}\\) (1)<br>• Rotational speed of roller \\(= \\frac{1.5\\text{ revs}}{2\\text{ s}} = 0.75\\text{ rev s}^{-1}\\) (1)<br>• Worm gear ratio \\(= 40\\). Motor rotational speed \\(= 0.75 \\times 40 = 30\\text{ rev s}^{-1}\\) (1)<br>• Convert to rpm: \\(30 \\times 60 = 1800\\text{ rpm}\\) (1)"
    },
    {
        "id": "2020-autumn-01-q1biv",
        "paper": "2020-autumn-01",
        "question": "1(b)(iv)",
        "marks": 4,
        "page": 5,
        "topics": ["6.1", "6.2"],
        "skills": ["technical", "design"],
        "summary": "Explain two reasons why the speed of the roller-blind increases throughout the raising cycle.",
        "prompt": "During testing of the prototype system, a design engineer notices that the speed at which the blind rises does not stay constant but gradually increases throughout the raising cycle.<br><br>Study the roller-blind mechanical drive system in Fig. 1.2 and explain <b>two</b> reasons why the speed of the blind increases throughout the raising cycle. [4]",
        "figures": ["img/2020-autumn-01/fig-1-2.jpg"],
        "image": "img/2020-autumn-01/q1biv.jpg",
        "markscheme": "img/2020-autumn-01/ms-1biv.jpg",
        "markscheme_text": "<b>Up to two marks for explaining each of two reasons (max 4 marks):</b><br>• As the blind rises the roller effective diameter increases (1) due to the layers/thickness of the wound blind fabric (1).<br>• As the roller diameter increases, its effective circumference increases (1), so each revolution lifts more fabric per second (1).<br>• As the blind rises, there is less fabric weight hanging off the roller (1), meaning less gravitational load/torque on the motor, allowing it to spin faster (1).<br>• The motor must overcome initial static inertia of the system (1), so speed naturally accelerates after starting (1)."
    },
    {
        "id": "2020-autumn-01-q1bv",
        "paper": "2020-autumn-01",
        "question": "1(b)(v)",
        "marks": 4,
        "page": 6,
        "topics": ["6.5", "6.4"],
        "skills": ["technical", "design"],
        "summary": "Draw a closed loop control system diagram to maintain a constant lifting speed throughout the raising cycle.",
        "prompt": "In order to eliminate the problem observed in part (b)(iv), the designer decides to add a closed loop control system to ensure that the blind is raised and lowered at a constant speed.<br><br>Draw a system diagram to show how an electronic closed loop control system would maintain a constant lifting speed throughout the raising cycle.<br><br>Your system diagram <b>must</b> include a specific sensor component for the closed loop control system. You <b>must</b> also explain the principle of operation of the closed loop control system. [4]",
        "figures": ["img/2020-autumn-01/ms-1bv-diagram.jpg"],
        "image": "img/2020-autumn-01/q1bv.jpg",
        "markscheme": "img/2020-autumn-01/ms-1bv.jpg",
        "markscheme_text": "<b>Award four marks as follows:</b><br>• <b>Sensor (1 mark):</b> Slotted opto-sensor and slotted disk on roller / rotary encoder / reed switch and magnet / hall effect sensor.<br>• <b>System diagram (1 mark):</b> Clear block diagram showing speed sensor, microprocessor/controller, motor, and feedback loop.<br>• <b>Principle of operation (2 marks):</b> Speed signal from the sensor is compared against desired reference speed by the processor (1); motor drive/PWM is dynamically adjusted to match the target speed (1)."
    },
    {
        "id": "2020-autumn-01-q1bvi",
        "paper": "2020-autumn-01",
        "question": "1(b)(vi)",
        "marks": 6,
        "page": 7,
        "topics": ["1.1", "6.4", "1.2"],
        "skills": ["design", "technical"],
        "summary": "Discuss the technical challenges faced when developing wireless devices and identify potential solutions.",
        "prompt": "Stakeholders decide that they want the smart roller-blind to be a wireless device, with no cables or wires running to it, as this improves the aesthetics and simplifies installation in the home.<br><br>Discuss the technical challenges faced by design engineers when developing wireless devices such as the smart roller-blind and identify potential solutions which would be worth further investigation during the iterative designing process. [6]",
        "figures": ["img/2020-autumn-01/fig-1-1.jpg"],
        "image": "img/2020-autumn-01/q1bvi.jpg",
        "markscheme": "img/2020-autumn-01/ms-1bvi.jpg",
        "markscheme_text": "<b>Level 3 (5–6 marks):</b> Clear, thorough understanding of wireless challenges with well-developed discussion identifying challenges and justified iterative solutions.<br><b>Level 2 (3–4 marks):</b> Reasonable understanding with sound discussion of challenges and possible solutions.<br><b>Level 1 (1–2 marks):</b> Basic descriptive knowledge.<br><br><b>Indicative Content:</b><br>• <i>Power supply:</i> Battery pack required; needs removable rechargeable pack or low battery indicator.<br>• <i>Energy harvesting:</i> Solar cells mounted on the window side of the blind casing to trickle-charge batteries from daylight.<br>• <i>Wireless communication:</i> Protocol selection (WiFi, Zigbee, Bluetooth LE); interference and range limitations.<br>• <i>Two-way feedback:</i> Bi-directional telemetry allows status confirmation, fault diagnosis, and battery state reporting.<br>• <i>Packaging:</i> Balancing battery capacity against size of enclosure to maintain slimline aesthetic."
    },
    # Q2
    {
        "id": "2020-autumn-01-q2a",
        "paper": "2020-autumn-01",
        "question": "2(a)",
        "marks": 3,
        "page": 9,
        "topics": ["6.2", "4.1"],
        "skills": ["maths"],
        "summary": "Calculate length L of non-transparent tube required for a light sensor using similar triangles or trigonometry.",
        "prompt": "A light sensor is placed in a non-transparent tube so that it can only receive light from a specific light source.<br><br>Fig. 2.1 shows a two-dimensional side view of the tube which is \\(5\\text{ mm}\\) in diameter, placed perpendicular to the extended light source AB which is \\(100\\text{ mm}\\) wide.<br><br>The light sensor will be placed at point P which is a perpendicular distance of \\(4\\text{ m}\\) from the light source AB.<br><br>Calculate the length L of tube required for this application. Give your answer in mm. Show your working. [3]",
        "figures": ["img/2020-autumn-01/fig-2-1.jpg"],
        "image": "img/2020-autumn-01/q2a.jpg",
        "markscheme": "img/2020-autumn-01/ms-2a.jpg",
        "markscheme_text": "<b>Award three marks as follows:</b><br>• Convert units: \\(4\\text{ m} = 4000\\text{ mm}\\) (1)<br>• Similar triangles ratio: \\(\\frac{100}{4000} = \\frac{5}{L}\\) (1)<br>• Solve for L: \\(L = \\frac{4000 \\times 5}{100} = 200\\text{ mm}\\) (1)<br><i>(Can also be solved using trigonometry: \\(\\tan(\\theta) = \\frac{50}{4000}\\); \\(L = \\frac{2.5}{\\tan(\\theta)} = 200\\text{ mm}\\))</i>"
    },
    {
        "id": "2020-autumn-01-q2bi",
        "paper": "2020-autumn-01",
        "question": "2(b)(i)",
        "marks": 2,
        "page": 10,
        "topics": ["4.1", "6.2"],
        "skills": ["maths"],
        "summary": "Calculate the width W of the top face of the former with 30 mm corner radii.",
        "prompt": "A former is used to make sure that parts are formed or bent to the same shape. Fig. 2.2 shows a former, made from a rectangular block of MDF measuring \\(180\\text{ mm}\\) wide and \\(75\\text{ mm}\\) thick. The top corners are sanded to a radius (r) of \\(30\\text{ mm}\\).<br><br>Calculate the width W of the top face of the former in Fig. 2.2. Give your answer in mm. Show your working. [2]",
        "figures": ["img/2020-autumn-01/fig-2-2.jpg"],
        "image": "img/2020-autumn-01/q2bi.jpg",
        "markscheme": "img/2020-autumn-01/ms-2bi.jpg",
        "markscheme_text": "<b>Award two marks as follows:</b><br>• Subtracting 2 corner radii from total width: \\(W = 180 - 30 - 30\\) (1)<br>• Calculating answer: \\(W = 120\\text{ mm}\\) (1)"
    },
    {
        "id": "2020-autumn-01-q2bii",
        "paper": "2020-autumn-01",
        "question": "2(b)(ii)",
        "marks": 4,
        "page": 11,
        "topics": ["6.2", "4.1"],
        "skills": ["maths"],
        "summary": "Calculate the total outside length from corner P to corner Q of the laminated wooden part.",
        "prompt": "The former in Fig. 2.2 is used to construct the laminated wooden part shown in Fig. 2.3. Three laminated layers are used to construct the part. Each laminate layer is \\(5\\text{ mm}\\) thick.<br><br>Calculate the outside length from corner P to corner Q on the laminated wooden part, indicated by the dotted line in Fig. 2.3. Give your answer in mm. Show your working.<br><br>You should ignore the thickness of the adhesive used between each layer. [4]",
        "figures": ["img/2020-autumn-01/fig-2-2.jpg", "img/2020-autumn-01/fig-2-3.jpg"],
        "image": "img/2020-autumn-01/q2bii.jpg",
        "markscheme": "img/2020-autumn-01/ms-2bii.jpg",
        "markscheme_text": "<b>Award four marks as follows:</b><br>• Radius of outer curved surface: \\(r_{\\text{outer}} = 30 + (3 \\times 5) = 45\\text{ mm}\\) (1)<br>• Total arc length of the two 90° corners: \\(\\text{Arc} = 2 \\times \\left(\\frac{2\\pi r}{4}\\right) = \\pi \\times 45 = 141.37\\text{ mm}\\) (1)<br>• Height of vertical straight sides: \\(90 - 45 = 45\\text{ mm}\\) (each side) (1)<br>• Total outside length PQ: \\((2 \\times 45) + 120 + 141.37 = 351.4\\text{ mm}\\) (accept 350 to 351 mm) (1)"
    },
    {
        "id": "2020-autumn-01-q2biii",
        "paper": "2020-autumn-01",
        "question": "2(b)(iii)",
        "marks": 2,
        "page": 12,
        "topics": ["4.1", "5.1"],
        "skills": ["design", "practical"],
        "summary": "Explain why well-designed formers are not usually manufactured with vertical sides.",
        "prompt": "The former in Fig. 2.2 has vertical sides.<br><br>Explain why well-designed formers are <b>not</b> usually manufactured with vertical sides. [2]",
        "figures": ["img/2020-autumn-01/fig-2-2.jpg"],
        "image": "img/2020-autumn-01/q2biii.jpg",
        "markscheme": "img/2020-autumn-01/ms-2biii.jpg",
        "markscheme_text": "<b>Up to two marks for explaining why formers need draft angles (max 2 marks):</b><br>• The laminated part binds tightly to the former due to friction/clamping (1), preventing easy separation after curing (1).<br>• Tapered sides / a draft angle allow the formed part to release cleanly without damaging the surface (1)."
    },
    {
        "id": "2020-autumn-01-q2biv",
        "paper": "2020-autumn-01",
        "question": "2(b)(iv)",
        "marks": 5,
        "page": 12,
        "topics": ["3.1", "2.1"],
        "skills": ["design", "practical"],
        "summary": "Name an alternative material for manufacturing the former and evaluate functional performance and environmental considerations.",
        "prompt": "The former in Fig. 2.2 could be manufactured from an alternative material to MDF.<br><br>Name an alternative material which could be used to manufacture the former and explain the selection of material in terms of functional performance and environmental considerations. [5]",
        "figures": ["img/2020-autumn-01/fig-2-2.jpg"],
        "image": "img/2020-autumn-01/q2biv.jpg",
        "markscheme": "img/2020-autumn-01/ms-2biv.jpg",
        "markscheme_text": "<b>Award five marks as follows:</b><br>• <b>Named material (1 mark):</b> High-density polystyrene modelling foam / Pine (timber) / Plywood / Plaster of Paris / Aluminium tooling block.<br>• <b>Functional performance (up to 2 marks):</b> e.g. Polystyrene foam has fine closed-cell structure that can be easily sanded/shaped with hot-wire or abrasive tools without crumbling (1); retains sufficient compressive strength under clamping (1).<br>• <b>Environmental considerations (up to 2 marks):</b> e.g. Polystyrene is difficult to recycle but reusable over many moulding cycles, minimising waste (1); pine can be sourced from FSC certified sustainable forests and is biodegradable (1)."
    },
    # Q3
    {
        "id": "2020-autumn-01-q3a",
        "paper": "2020-autumn-01",
        "question": "3(a)",
        "marks": 4,
        "page": 13,
        "topics": ["1.2", "5.1"],
        "skills": ["design"],
        "summary": "Explain two ways in which an incremental innovation strategy can be beneficial to a product manufacturer.",
        "prompt": "As new technologies emerge, existing products can evolve through a process of incremental innovation.<br><br>Explain <b>two</b> ways in which an incremental innovation strategy can be beneficial to a product manufacturer. [4]",
        "figures": [],
        "image": "img/2020-autumn-01/q3a.jpg",
        "markscheme": "img/2020-autumn-01/ms-3a.jpg",
        "markscheme_text": "<b>Up to two marks for explaining each of two benefits (max 4 marks):</b><br>• Lower financial risk and reduced R&D expenditure (1) as small evolutionary improvements build on existing verified tooling and production lines (1).<br>• Sustains market interest and product lifecycle (1), releasing regular updates (e.g. annual smartphone refreshes) to drive repeat sales (1).<br>• Allows integration of newly matured components/features (1), maintaining competitiveness without needing radical system redesign (1).<br>• Production systems can evolve iteratively (1), minimising manufacturing downtime and quality defects (1)."
    },
    {
        "id": "2020-autumn-01-q3b",
        "paper": "2020-autumn-01",
        "question": "3(b)",
        "marks": 8,
        "page": 14,
        "topics": ["1.2", "5.2"],
        "skills": ["design"],
        "summary": "Discuss the ways in which the intellectual property (IP) of designers can be protected.",
        "prompt": "Discuss the ways in which the intellectual property (IP) of designers can be protected. [8]",
        "figures": [],
        "image": "img/2020-autumn-01/q3b.jpg",
        "markscheme": "img/2020-autumn-01/ms-3b.jpg",
        "markscheme_text": "<b>Level 3 (6–8 marks):</b> Clear, thorough understanding of IP legislation. Well-developed line of reasoning covering multiple IP mechanisms with specific examples.<br><b>Level 2 (3–5 marks):</b> Reasonable understanding of IP protection with sound explanation.<br><b>Level 1 (1–2 marks):</b> Basic descriptive knowledge.<br><br><b>Indicative Content:</b><br>• <b>Patents:</b> Protect functional/mechanical mechanisms and technical inventions for 20 years; must be novel, involve an inventive step, and be industrially applicable.<br>• <b>Registered Designs:</b> Protect the visual aesthetic, shape, contours, and physical appearance of a product for up to 25 years (renewed every 5 years).<br>• <b>Trademarks:</b> Protect brand identity, logos, brand names, and symbols through the IPO for 10 years (renewable indefinitely).<br>• <b>Copyright:</b> Automatic protection for original literary, software code, schematic diagrams, and artistic drawings (lasts for creator's life + 70 years).<br>• <b>Unregistered Design Rights:</b> Automatic protection for 3D shapes for 10–15 years."
    },
    # Q4
    {
        "id": "2020-autumn-01-q4ai",
        "paper": "2020-autumn-01",
        "question": "4(a)(i)",
        "marks": 2,
        "page": 17,
        "topics": ["6.3", "6.5"],
        "skills": ["maths", "technical"],
        "summary": "Determine the period of the sound signal waveform in Fig. 4.2 in ms.",
        "prompt": "Fig. 4.1 shows parts of a puzzle toy. Fig. 4.2 shows the sound signal waveform produced by the electronic pen.<br><br>Determine the period of the signal in Fig. 4.2. Give your answer in ms. Show your working. [2]",
        "figures": ["img/2020-autumn-01/fig-4-1.jpg", "img/2020-autumn-01/fig-4-2.jpg"],
        "image": "img/2020-autumn-01/q4ai.jpg",
        "markscheme": "img/2020-autumn-01/ms-4ai.jpg",
        "markscheme_text": "<b>Award two marks as follows:</b><br>• Reading on-time and off-time from graph: \\(\\text{On time} = 0.1\\text{ ms}\\), \\(\\text{Off time} = 0.3\\text{ ms}\\) (1)<br>• Calculating period: \\(\\text{Period} = 0.1 + 0.3 = 0.4\\text{ ms}\\) (1)"
    },
    {
        "id": "2020-autumn-01-q4aii",
        "paper": "2020-autumn-01",
        "question": "4(a)(ii)",
        "marks": 2,
        "page": 17,
        "topics": ["6.3", "6.5"],
        "skills": ["maths", "technical"],
        "summary": "Calculate the frequency in kHz of the signal in Fig. 4.2.",
        "prompt": "Calculate the frequency in kHz of the signal in Fig. 4.2. Show your working. [2]",
        "figures": ["img/2020-autumn-01/fig-4-2.jpg"],
        "image": "img/2020-autumn-01/q4aii.jpg",
        "markscheme": "img/2020-autumn-01/ms-4aii.jpg",
        "markscheme_text": "<b>Award two marks as follows:</b><br>• Recall formula: \\(f = \\frac{1}{T}\\) (1)<br>• Calculate frequency: \\(f = \\frac{1}{0.4\\text{ ms}} = \\frac{1}{0.0004\\text{ s}} = 2500\\text{ Hz} = 2.5\\text{ kHz}\\) (1)"
    },
    {
        "id": "2020-autumn-01-q4bi",
        "paper": "2020-autumn-01",
        "question": "4(b)(i)",
        "marks": 4,
        "page": 18,
        "topics": ["6.3", "3.2"],
        "skills": ["maths", "technical"],
        "summary": "Calculate resistance in kΩ between sensor probes on conductive ink using R = rho * d / (w * t).",
        "prompt": "When the sensor probes are touching a conductive ink disk the resistance (in \\(\\Omega\\)) between the probes is given by the formula:<br>\\[ R = \\rho \\frac{d}{wt} \\]<br>where \\(\\rho\\) = resistivity of conductive ink (\\(1.25\\ \\Omega\\text{ m}\\)), \\(d\\) = probe separation (\\(3\\text{ mm}\\)), \\(w\\) = width of probes (\\(5\\text{ mm}\\)), \\(t\\) = thickness of conductive ink film (\\(50\\ \\mu\\text{m}\\)).<br><br>Calculate the resistance in k\\(\\Omega\\) between the sensor probes when they are touching the conductive ink. Show your working. [4]",
        "figures": [],
        "image": "img/2020-autumn-01/q4bi.jpg",
        "markscheme": "img/2020-autumn-01/ms-4bi.jpg",
        "markscheme_text": "<b>Award four marks as follows:</b><br>• Converting \\(d\\) and \\(w\\) to metres: \\(d = 0.003\\text{ m}\\), \\(w = 0.005\\text{ m}\\) (1)<br>• Converting \\(t\\) to metres: \\(t = 50\\ \\mu\\text{m} = 50 \\times 10^{-6}\\text{ m} = 0.00005\\text{ m}\\) (1)<br>• Substituting and calculating \\(R\\):<br>\\[ R = 1.25 \\times \\frac{0.003}{0.005 \\times 50 \\times 10^{-6}} = \\frac{0.00375}{2.5 \\times 10^{-7}} = 15000\\ \\Omega \\] (1)<br>• Converting to k\\(\\Omega\\): \\(R = 15\\text{ k}\\Omega\\) (1)"
    },
    {
        "id": "2020-autumn-01-q4bii",
        "paper": "2020-autumn-01",
        "question": "4(b)(ii)",
        "marks": 3,
        "page": 19,
        "topics": ["6.3", "6.5"],
        "skills": ["maths", "technical"],
        "summary": "Calculate the minimum value of resistor R required in Fig. 4.3 for a 2V analogue threshold.",
        "prompt": "Fig. 4.3 shows the sensor circuit for the electronic pen. A minimum voltage of \\(2\\text{ V}\\) is required at the microcontroller analogue input A.0 in Fig. 4.3 when the sensor probes are touching a conductive ink disk.<br><br>Using your answer to part (b)(i), calculate the minimum value of resistor R required in Fig. 4.3. Give your answer in \\(\\Omega\\). Show your working. [3]",
        "figures": ["img/2020-autumn-01/fig-4-3.jpg"],
        "image": "img/2020-autumn-01/q4bii.jpg",
        "markscheme": "img/2020-autumn-01/ms-4bii.jpg",
        "markscheme_text": "<b>Award three marks as follows:</b><br>• Voltage across probes: \\(V_{\\text{probes}} = 3\\text{ V} - 2\\text{ V} = 1\\text{ V}\\) (1)<br>• Potential divider voltage-to-resistance ratio: \\(\\frac{V_{\\text{probes}}}{V_R} = \\frac{1}{2} = \\frac{R_{\\text{probes}}}{R}\\) (1)<br>• Solve for R: \\(R = 2 \\times R_{\\text{probes}} = 2 \\times 15\\text{ k}\\Omega = 30\\text{ k}\\Omega = 30000\\ \\Omega\\) (1)"
    },
    {
        "id": "2020-autumn-01-q4biii",
        "paper": "2020-autumn-01",
        "question": "4(b)(iii)",
        "marks": 1,
        "page": 19,
        "topics": ["6.3", "6.5"],
        "skills": ["technical"],
        "summary": "State the voltage at analogue input A.0 when probes touch non-conductive ink.",
        "prompt": "State, without calculation, the value of the voltage at the analogue input A.0 in Fig. 4.3 when the sensor probes are touching a non-conductive ink disk. [1]",
        "figures": ["img/2020-autumn-01/fig-4-3.jpg"],
        "image": "img/2020-autumn-01/q4biii.jpg",
        "markscheme": "img/2020-autumn-01/ms-4biii.jpg",
        "markscheme_text": "<b>Award one mark:</b><br>• \\(0\\text{ V}\\) (1) <i>(Since non-conductive ink has infinite resistance, no current flows through R, pulling A.0 down to 0V)</i>."
    },
    {
        "id": "2020-autumn-01-q4c",
        "paper": "2020-autumn-01",
        "question": "4(c)",
        "marks": 6,
        "page": 21,
        "topics": ["6.5"],
        "skills": ["technical"],
        "summary": "Evaluate the microcontroller flowchart in Fig. 4.5 against the functional specification and suggest corrections.",
        "prompt": "Fig. 4.4 gives information about the microcontroller input and output pins. Fig. 4.5 shows a prototype version of a flowchart program.<br><br>The functional specification of the electronic pen is described as follows:<br><i>When the electronic pen's sensor is touched onto a conductive ink disk, an LED is illuminated and a sound is produced for a period of 1.5 seconds. After this, if the pen is no longer touching the conductive ink disk, the LED turns off and the sound stops.</i><br><br>Evaluate the effectiveness of the flowchart in Fig. 4.5 against the functional specification. You need to suggest any changes to the flowchart to ensure that the specification is met. [6]",
        "figures": ["img/2020-autumn-01/fig-4-4.jpg", "img/2020-autumn-01/fig-4-5.jpg"],
        "image": "img/2020-autumn-01/q4c.jpg",
        "markscheme": "img/2020-autumn-01/ms-4c.jpg",
        "markscheme_text": "<b>Two marks for each identified problem and corresponding solution (max 6 marks):</b><br>• <b>Problem 1:</b> When result of 'A.0 > 2V?' is No, the program gets stuck in an infinite dead-end loop (1).<br>  <b>Solution 1:</b> The 'No' branch should loop back to 'Read ADC A.0' to continue polling (1).<br>• <b>Problem 2:</b> After turning LED on (High B.0), it is never turned off when the pen is removed (1).<br>  <b>Solution 2:</b> Insert 'Low B.0' after the sound loop exits when Y reaches the target (1).<br>• <b>Problem 3:</b> The sound loop count of \\(Y = 1600\\) does not give 1.5 seconds (each cycle is \\(0.1 + 0.3 = 0.4\\text{ ms}\\), giving only \\(1600 \\times 0.0004 = 0.64\\text{ s}\\)) (1).<br>  <b>Solution 3:</b> Set decision to \\(Y = \\frac{1.5}{0.0004} = 3750\\) (1)."
    },
    {
        "id": "2020-autumn-01-q4di",
        "paper": "2020-autumn-01",
        "question": "4(d)(i)",
        "marks": 1,
        "page": 22,
        "topics": ["3.2"],
        "skills": ["technical"],
        "summary": "Identify another smart material, apart from conductive ink, used to provide functionality in a product.",
        "prompt": "Identify another smart material, apart from conductive ink, that is used to provide functionality in a product. [1]",
        "figures": [],
        "image": "img/2020-autumn-01/q4di.jpg",
        "markscheme": "img/2020-autumn-01/ms-4di.jpg",
        "markscheme_text": "<b>Award one mark for identifying a smart material:</b><br>• Thermochromic pigment / sheet (1)<br>• Photochromic pigment (1)<br>• Electroluminescent material (1)<br>• Shape memory alloy (SMA / Nitinol) (1)<br>• Piezoelectric material (1)<br>• Electrochromic material / privacy glass (1)<br>• Shape memory polymer (1)<br><i>(Do NOT accept 'conductive ink' or 'smart ink')</i>."
    },
    {
        "id": "2020-autumn-01-q4dii",
        "paper": "2020-autumn-01",
        "question": "4(d)(ii)",
        "marks": 4,
        "page": 22,
        "topics": ["3.2", "1.1"],
        "skills": ["design", "technical"],
        "summary": "Describe, using an example of a product, how the properties of the identified smart material provide functionality.",
        "prompt": "Describe, using an example of a product, how the properties of the smart material you have identified in part (d)(i) provide functionality. [4]",
        "figures": [],
        "image": "img/2020-autumn-01/q4dii.jpg",
        "markscheme": "img/2020-autumn-01/ms-4dii.jpg",
        "markscheme_text": "<b>Up to four marks for describing how the properties provide functionality in a specific product:</b><br>• <i>Product identified (1 mark):</i> e.g. Baby feeding spoon / battery tester / privacy glass / aircraft window / medical stent.<br>• <i>Functional description (up to 3 marks):</i> e.g. Thermochromic pigment changes colour reversibly when passing through a transition temperature (1). In baby spoons, it alerts parents if food is dangerously hot without contaminating the food (1); in battery testers, electric current heats a tapered resistive track, revealing charge levels across the colour gradient (1)."
    }
]

print("Total questions defined:", len(new_questions))
print("Total marks across questions:", sum(q['marks'] for q in new_questions))

# Load existing database
with open(os.path.join(repo, 'questions.json'), 'r', encoding='utf-8') as f:
    db = json.load(f)

# Update paper metadata
paper_meta = {
    "id": "2020-autumn-01",
    "code": "H404/01",
    "unit": "Principles of Design Engineering",
    "year": 2020,
    "level": "H404",
    "totalMarks": 80,
    "series": "Autumn"
}

existing_papers = [p for p in db['papers'] if p['id'] != '2020-autumn-01']
existing_papers.append(paper_meta)
db['papers'] = sorted(existing_papers, key=lambda x: (x['year'], x['code']), reverse=True)

# Replace any old questions for 2020-autumn-01
db['questions'] = [q for q in db['questions'] if q.get('paper') != '2020-autumn-01']
db['questions'].extend(new_questions)

with open(os.path.join(repo, 'questions.json'), 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("\nSuccessfully updated questions.json!")
