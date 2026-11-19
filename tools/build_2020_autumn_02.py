"""
Build OCR H404/02 Problem Solving in Design Engineering - November 2020 (paper id 2020-autumn-02).
QP and RB are scanned (image-only) PDFs, so crop rectangles were measured from rendered pages.

Standards applied (see tools/INGESTION_GUIDE.md):
  * q.image   -> question prompt + 1-2 answer lines (or final answer line) + mark [X]
  * q.figures -> preamble + Resource Booklet figures
  * q.markscheme -> stitched mark scheme rows (blank table space auto-trimmed)
"""
import os, json
import numpy as np
from PIL import Image
try:
    import pymupdf as fitz
except ImportError:
    import fitz

UP = r'C:\Users\Alexander\.gemini\antigravity\brain\35e24780-11e3-4c7b-9712-4e87202bc9ef\.user_uploaded'
QP = os.path.join(UP, 'media_1795103629618_9725bcc2.pdf')
RB = os.path.join(UP, 'media_1795103629654_1d68d5a2.pdf')
MS = os.path.join(UP, 'media_1795103634304_08b9b4ad.pdf')

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PID = '2020-autumn-02'
OUT = os.path.join(REPO, 'img', PID)
os.makedirs(OUT, exist_ok=True)

qp, rb, ms = fitz.open(QP), fitz.open(RB), fitz.open(MS)
ZOOM = 2.0


def render(doc, page, y0, y1, x0=40, x1=555):
    pix = doc[page - 1].get_pixmap(clip=fitz.Rect(x0, y0, x1, y1), matrix=fitz.Matrix(ZOOM, ZOOM))
    return Image.frombytes('RGB', (pix.width, pix.height), pix.samples)


def autotrim_bottom(im, pad=16, thresh=40):
    """Remove trailing rows that only contain table vertical rules / whitespace."""
    a = np.asarray(im.convert('L'))
    dark = (a < 160).sum(axis=1)
    # ignore full-width horizontal table rules (e.g. the bottom border)
    rows = np.where((dark > thresh) & (dark < 0.6 * im.width))[0]
    if len(rows) == 0:
        return im
    last = min(im.height, rows[-1] + pad)
    if last >= im.height - 4:
        return im
    out = im.crop((0, 0, im.width, last)).copy()
    # close the table with a thin rule
    from PIL import ImageDraw
    ImageDraw.Draw(out).line([(6, last - 2), (im.width - 6, last - 2)], fill=(120, 120, 120), width=2)
    return out


def stitch(parts, name):
    w = max(p.width for p in parts)
    h = sum(p.height for p in parts)
    out = Image.new('RGB', (w, h), 'white')
    y = 0
    for p in parts:
        out.paste(p, (0, y))
        y += p.height
    out.save(os.path.join(OUT, name), quality=90)
    print(f'  {name:16s} {out.size}')


# ---------------- Question prompt cards ----------------
print('Question cards:')
stitch([render(qp, 2, 140, 298)], 'q1.jpg')
stitch([render(qp, 4, 62, 272)], 'q2.jpg')
stitch([render(qp, 6, 62, 545)], 'q3.jpg')
stitch([render(qp, 11, 166, 222), render(qp, 11, 728, 766)], 'q4a.jpg')
stitch([render(qp, 12, 62, 130), render(qp, 12, 588, 625)], 'q4b.jpg')
stitch([render(qp, 13, 62, 208), render(qp, 13, 682, 770)], 'q4c.jpg')
stitch([render(qp, 14, 62, 246)], 'q5.jpg')

# ---------------- Resources ----------------
print('Resources:')
stitch([render(rb, 2, 58, 792)], 'rb-p2.jpg')
stitch([render(rb, 3, 56, 382)], 'rb-p3.jpg')
stitch([render(rb, 4, 58, 420)], 'fig-3.jpg')
stitch([render(rb, 4, 428, 615)], 'fig-4.jpg')
stitch([render(rb, 4, 616, 799)], 'fig-5.jpg')
stitch([render(rb, 5, 58, 266)], 'fig-6.jpg')
stitch([render(rb, 5, 272, 456)], 'fig-7.jpg')
stitch([render(rb, 5, 466, 644)], 'fig-8.jpg')
stitch([render(rb, 6, 58, 366)], 'rb-p6.jpg')
# Q4 preamble (question paper) stacked above Fig. 9a / 9b
stitch([render(qp, 11, 62, 165), render(rb, 6, 368, 748)], 'fig-9.jpg')
stitch([render(rb, 7, 58, 207)], 'fig-9c.jpg')
stitch([render(rb, 7, 214, 402)], 'fig-10.jpg')

# ---------------- Mark schemes (landscape pages) ----------------
print('Mark schemes:')


def msr(page, y0=49, y1=549):
    return autotrim_bottom(render(ms, page, y0, y1, 36, 826))


stitch([msr(4), msr(5, 49, 362)], 'ms-1.jpg')
stitch([render(ms, 5, 514, 549, 36, 826), msr(6), msr(7), msr(8)], 'ms-2.jpg')
stitch([msr(9), msr(10), render(ms, 11, 49, 120, 36, 826)], 'ms-3.jpg')
stitch([msr(12)], 'ms-4a.jpg')
stitch([msr(13)], 'ms-4b.jpg')
stitch([msr(14)], 'ms-4c.jpg')
stitch([msr(15), msr(16), msr(17, 49, 358)], 'ms-5.jpg')

# ---------------- questions.json ----------------
P = f'img/{PID}/'
LEVELS_14 = ('<b>Level 4 (11–14 marks):</b> Comprehensive discussion/evaluation, information in the RB used effectively to fully exemplify points, well-developed and logically structured line of reasoning.<br>'
             '<b>Level 3 (7–10 marks):</b> Good discussion; RB used for the most part effectively, one or two opportunities missed.<br>'
             '<b>Level 2 (4–6 marks):</b> Sufficient discussion; RB used to exemplify some points, limited structure.<br>'
             '<b>Level 1 (1–3 marks):</b> Limited discussion; simplistic use of RB, basic and unstructured.<br><br>')

questions = [
    {
        'id': f'{PID}-q1', 'paper': PID, 'question': '1', 'marks': 14, 'page': 2,
        'topics': ['1.1', '5.1'], 'skills': ['design'],
        'summary': 'Discuss the social, economic and marketing issues considered when designing a piece of fitness equipment.',
        'prompt': 'Personal fitness is a growing market, led by trends which are affected by social, economic and marketing issues. It is important that companies who manufacture exercise equipment are able to monitor and predict these trends as they happen.<br><br>Discuss the <b>social, economic and marketing</b> issues that would be considered when designing a piece of fitness equipment.<br><br><i>Refer to information on pages 2 and 3 of the Resource Booklet.</i> [14]',
        'figures': [P + 'rb-p2.jpg', P + 'rb-p3.jpg'],
        'image': P + 'q1.jpg', 'markscheme': P + 'ms-1.jpg',
        'markscheme_text': LEVELS_14 + '<b>Indicative content:</b><br>'
            '• <b>Social:</b> increased self-confidence, self-esteem and emotional health; interaction with others (classes, social cycle groups, over-65 sessions); performing better at work.<br>'
            '• <b>Economic:</b> fitness trends drive sales and gym memberships; timing of release (sales peak every January); better fitness saves NHS money (obesity cost £5.1bn in 2006/7; £9.27bn on mental health 2016/17); healthier workforce needs less sick leave.<br>'
            '• <b>Marketing:</b> designing the right equipment for the right trend at the right time; target age range (e.g. over-65s, home-gym users); market size and disposable income (UK industry worth £5bn, 1 in 7 people with gym membership); end fitness goals of the group; product lifespan informing material choice.'
    },
    {
        'id': f'{PID}-q2', 'paper': PID, 'question': '2*', 'marks': 14, 'page': 4,
        'topics': ['1.1', '6.3', '3.1'], 'skills': ['design', 'technical'],
        'summary': 'Critically evaluate the issues a designer must consider when developing a kinetic-energy device-charging system for a gym rowing machine.',
        'prompt': 'A manufacturer of exercise equipment has approached its design team with a concept to make its products more appealing to the gym user.<br><br>It has proposed that a charging system is installed on its rowing machines so that the user is able to charge their mobile electronic devices by making use of the rowing machine\u2019s kinetic energy.<br><br>The rowing machine is the Rowmatic-1 shown on page 4 of the Resource Booklet.<br><br>Critically evaluate the issues a designer would need to consider when developing a charging system for a rowing machine used in a gym.<br><br><i>Refer to information on pages 4 and 5 of the Resource Booklet.</i> [*14]',
        'figures': [P + 'fig-3.jpg', P + 'fig-4.jpg', P + 'fig-5.jpg', P + 'fig-6.jpg', P + 'fig-8.jpg'],
        'image': P + 'q2.jpg', 'markscheme': P + 'ms-2.jpg',
        'markscheme_text': LEVELS_14 + '<b>Indicative content:</b><br>'
            '• Size of the unit – gym floor space is at a premium.<br>'
            '• Charging capability: range of devices; different voltage/current requirements (Fig. 4 battery capacities 100–3800 mAh); connectors (Lightning, USB-C, Micro USB, wireless) – supplied cables or user\u2019s own; charge time.<br>'
            '• User experience – will driving the alternator increase effort at each resistance level?<br>'
            '• Materials – e.g. a justified polymer casing suited to a busy, sweaty gym environment.<br>'
            '• Drive connection to the existing flywheel – pulleys, gears, chain and sprocket.<br>'
            '• Maintenance – cleaning, replacing damaged cables / USB ports.<br>'
            '• Safety – trailing cables as trip hazards; accessible voltage/current; no interference or electric shock to the user.<br>'
            '• Varying fitness levels affect output – current limiter or battery buffer for constant safe output.<br>'
            '• A method of holding the device securely while rowing.'
    },
    {
        'id': f'{PID}-q3', 'paper': PID, 'question': '3', 'marks': 16, 'page': 6,
        'topics': ['6.1', '6.4', '6.5'], 'skills': ['technical', 'maths'],
        'summary': 'Design a pulley drive from the flywheel to the TB-401/10 generator for 3 A charging, and an electronic system that switches off the output below 1000 rpm.',
        'prompt': 'The designers of the rowing machine charging system described in Question 2 wish to develop a working prototype. A TB-401/10 generator (page 5 of the RB) converts the rower\u2019s kinetic energy into electrical power. The average user produces 600 rpm at the flywheel. The prototype must <b>charge the iPhone with the specification in Fig. 8</b>.<br><br><b>Issue 1:</b> A drive system is required to transfer the rotary motion from the flywheel to the generator at an appropriate speed.<br><br><b>Issue 2:</b> Mobile devices require a 5 V output; the generator maintains 5 V only if its pulley rotates at a minimum of 1000 rpm. An annotated system diagram is required, describing an electronic system to monitor the speed of the generator pulley and to switch off the electrical output if the speed drops below 1000 rpm. Appropriate sensor(s) and output device(s) must be identified.<br><br>Use sketches and/or notes. All information is on pages 4 and 5 of the Resource Booklet. [16]',
        'figures': [P + 'fig-3.jpg', P + 'fig-6.jpg', P + 'fig-7.jpg', P + 'fig-8.jpg'],
        'image': P + 'q3.jpg', 'markscheme': P + 'ms-3.jpg',
        'markscheme_text': '<b>Level 4 (13–16):</b> Both solutions comprehensive and well developed; end-to-end process clear. <b>Level 3 (9–12):</b> Both covered, one may be underdeveloped. <b>Level 2 (5–8):</b> Both may be underdeveloped. <b>Level 1 (1–4):</b> Basic. (Max 8 marks per issue.)<br><br>'
            '<b>Issue 1 – drive system:</b><br>'
            '• Required current (Fig. 8) = 3 A → Fig. 7 gives a generator speed of ≈1500 rpm (allow 1400–1600).<br>'
            '• Velocity ratio: $\\frac{600}{1500} = 0.4$ (or $\\frac{1500}{600} = 2.5$).<br>'
            '• $\\frac{\\text{driven } (50\\text{ mm})}{\\text{driver}} = 0.4 \\Rightarrow$ driver pulley on flywheel $= \\frac{50}{0.4} = \\mathbf{125\\text{ mm}}$.<br>'
            '• Workable drive detail: pulley and belt, attaching driver pulley to the flywheel, belt tensioning, ribbed belt to reduce slip, generator mounting (gears / friction wheel / chain and sprocket also allowed).<br><br>'
            '<b>Issue 2 – speed-monitoring system:</b><br>'
            '• Sensor: slotted opto-switch with slotted disc on the pulley (or gear-tooth sensor, reed switch, microswitch, quadrature encoder).<br>'
            '• Signal: a stream of pulses whose frequency is proportional to speed.<br>'
            '• Process: microcontroller measures the time interval between pulses.<br>'
            '• Output: relay or MOSFET switching the charging current.<br>'
            '• Logic: if interval is shorter than the 1000 rpm threshold, output high → relay on → charging current flows; otherwise relay off. Add a short delay to stop rapid switching around 1000 rpm.'
    },
    {
        'id': f'{PID}-q4a', 'paper': PID, 'question': '4(a)', 'marks': 3, 'page': 11,
        'topics': ['6.2'], 'skills': ['maths'],
        'summary': 'Use Pythagoras to calculate the extended length of the Bike-ease pneumatic cylinder.',
        'prompt': 'Calculate the <b>extended length</b> (to the nearest mm) of the pneumatic cylinder shown in Fig. 9a. Show your working.<br><br><i>Use the data in Fig. 9a and Fig. 9c of the Resource Booklet.</i> [3]',
        'figures': [P + 'fig-9.jpg', P + 'fig-9c.jpg'],
        'image': P + 'q4a.jpg', 'markscheme': P + 'ms-4a.jpg',
        'markscheme_text': '• Vertical height $= a + d = 100 + 200 = 300\\text{ mm}$ (1)<br>'
            '• $L = \\sqrt{300^2 + 750^2}$ (1)<br>'
            '• Extended length $= \\mathbf{808\\text{ mm}}$ (1)<br>'
            'Correct answer without working = full marks; allow ECF and other methods (e.g. trigonometry).'
    },
    {
        'id': f'{PID}-q4b', 'paper': PID, 'question': '4(b)', 'marks': 4, 'page': 12,
        'topics': ['6.2'], 'skills': ['maths'],
        'summary': 'Use trigonometry to find the horizontal distance H moved by the bicycle clamp as the rack is raised.',
        'prompt': 'Calculate the horizontal distance labelled H on Fig. 9a (to the nearest mm), through which the bicycle clamp moves as the Bike-ease roof-mounted bicycle rack is raised. Show your working.<br><br><i>Use the data in Fig. 9a, Fig. 9b and Fig. 9c of the Resource Booklet.</i> [4]',
        'figures': [P + 'fig-9.jpg', P + 'fig-9c.jpg'],
        'image': P + 'q4b.jpg', 'markscheme': P + 'ms-4b.jpg',
        'markscheme_text': '• $\\sin\\theta = \\frac{d}{L_2}$ (1)<br>'
            '• $\\theta = \\sin^{-1}\\left(\\frac{200}{300}\\right) = 41.8^\\circ$ (1)<br>'
            '• $\\cos(41.8^\\circ) = \\frac{H}{L_1 + L_2}$ (1)<br>'
            '• $H = \\cos(41.8^\\circ) \\times (340 + 300) = \\mathbf{477\\text{ mm}}$ (1)<br>'
            'Allow ECF and other appropriate methods; sketches of triangles may be drawn.'
    },
    {
        'id': f'{PID}-q4c', 'paper': PID, 'question': '4(c)', 'marks': 7, 'page': 13,
        'topics': ['6.2'], 'skills': ['maths', 'technical'],
        'summary': 'Select a pneumatic cylinder (A–D) giving an 1100 N instroke force at 0.6 N/mm², accounting for extended length and piston rod area.',
        'prompt': 'The pneumatic cylinder shown in Fig. 9a needs to exert a minimum instroke force of 1100 N to begin lifting the bicycle into the vertical position. Compressed air at a pressure of 0.6 N mm⁻² is being used in this system.<br><br>The list of pneumatic cylinders available is shown in Fig. 10 on page 7 of the Resource Booklet (A to D).<br><br>Determine by calculation which pneumatic cylinder would be suitable for this design. Show your working. Justify your answer. [7]',
        'figures': [P + 'fig-9.jpg', P + 'fig-10.jpg'],
        'image': P + 'q4c.jpg', 'markscheme': P + 'ms-4c.jpg',
        'markscheme_text': '• Eliminate A (650 mm) and C (750 mm) – maximum extended length below the 808 mm required from 4(a) (1)<br>'
            '• $A = \\frac{F}{P}$ (1)<br>'
            '• Minimum area $= \\frac{1100}{0.6} = 1833.3\\text{ mm}^2$ (1)<br>'
            '• B: $A = \\frac{\\pi}{4}(50^2 - 20^2) = 1649\\text{ mm}^2$ – too small (2; only 1 if rod ignored, giving 1963 mm²)<br>'
            '• D: $A = \\frac{\\pi}{4}(80^2 - 25^2) = 4536\\text{ mm}^2$ (1)<br>'
            '• <b>Cylinder D</b> – sufficient length and instroke area to generate the required force (1)<br>'
            'Allow ECF (ignoring rod area leads to B). No marks for guessing D without reasoning.'
    },
    {
        'id': f'{PID}-q5', 'paper': PID, 'question': '5*', 'marks': 12, 'page': 14,
        'topics': ['1.2', '4.2', '5.1'], 'skills': ['design'],
        'summary': 'Discuss the advantages of digital design tools during development and market introduction of the Bike-ease roof-mounted bicycle rack.',
        'prompt': 'This question refers to the development and introduction to market of the Bike-ease roof-mounted bicycle rack shown on page 6 of the Resource Booklet.<br><br>During the development and introduction to market, design engineers will use a variety of digital design tools.<br><br>Discuss the <b>advantages</b> to design engineers of using digital design tools during the development and introduction to market of a product such as the Bike-ease roof-mounted bicycle rack.<br><br><i>Refer to information on page 6 of the Resource Booklet.</i> [*12]',
        'figures': [P + 'rb-p6.jpg', P + 'fig-9.jpg'],
        'image': P + 'q5.jpg', 'markscheme': P + 'ms-5.jpg',
        'markscheme_text': '<b>Level 4 (10–12):</b> Comprehensive discussion of advantages during development and introduction, directly linked to the bike rack. <b>Level 3 (7–9):</b> Good. <b>Level 2 (4–6):</b> Sufficient. <b>Level 1 (1–3):</b> Limited. No credit for listing tools without linking to advantages and the roof rack.<br><br>'
            '<b>Development:</b><br>'
            '• Stakeholder research – online questionnaires, video-conference focus groups, spreadsheets, social media and online groups (wider reach, lower cost, easy collation).<br>'
            '• CAD concepts – quick, high-quality representations, easy modification before prototyping.<br>'
            '• Photo-realistic renders – communicate the concept to investors and prototype builders.<br>'
            '• CAE – stress analysis of components and simulation of the pneumatic system; right material without over-engineering.<br>'
            '• Modelling of the roof attachment system to fit many car types before physical prototyping.<br>'
            '• CAM – fast transfer to manufacture, consistent quality (e.g. welding).<br>'
            '• Communication – sharing files between teams/international manufacturers, faster turnaround.<br><br>'
            '<b>Introduction to market:</b> social-media advertising to cycling communities; graphics packages for presentations, posters and adverts.'
    },
]

qpath = os.path.join(REPO, 'questions.json')
with open(qpath, 'r', encoding='utf-8') as f:
    d = json.load(f)

paper = {'id': PID, 'code': 'H404/02', 'unit': 'Problem Solving in Design Engineering',
         'year': 2020, 'level': 'H404', 'totalMarks': 70, 'series': 'Autumn'}
d['papers'] = [p for p in d['papers'] if p['id'] != PID]
idx = next((i for i, p in enumerate(d['papers']) if p['id'] == '2020-autumn-01'), 0)
d['papers'].insert(idx, paper)
d['questions'] = [q for q in d['questions'] if q.get('paper') != PID] + questions

with open(qpath, 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2, ensure_ascii=False)
print(f'Registered {len(questions)} questions, {sum(q["marks"] for q in questions)} marks.')

# ---------------- quiz ----------------
quiz_path = os.path.join(REPO, 'quiz_questions.json')
quiz_items = [
    {'id': 'quiz-2020-a02-q1',
     'question': 'A 50 mm generator pulley must turn at 1500 rpm when the flywheel turns at 600 rpm. What diameter driver pulley is needed on the flywheel?',
     'choices': ['20 mm', '75 mm', '125 mm', '250 mm'], 'correctIndex': 2,
     'explanation': 'Velocity ratio = 600/1500 = 0.4, so driver = 50 / 0.4 = 125 mm.', 'topic': '6'},
    {'id': 'quiz-2020-a02-q2',
     'question': 'A pneumatic cylinder has a 300 mm vertical rise over a 750 mm horizontal run. What is its extended length to the nearest mm?',
     'choices': ['750 mm', '808 mm', '850 mm', '1050 mm'], 'correctIndex': 1,
     'explanation': '√(300² + 750²) = √652 500 ≈ 808 mm.', 'topic': '6'},
    {'id': 'quiz-2020-a02-q3',
     'question': 'Why must the piston rod area be subtracted when calculating the instroke force of a double-acting cylinder?',
     'choices': ['Air only acts on the annular area around the rod on the instroke', 'The rod increases air pressure', 'The rod adds friction equal to its area', 'It is only needed on the outstroke'],
     'correctIndex': 0,
     'explanation': 'On the instroke the rod occupies part of the piston face, so the effective area is π/4 (D² − d²).', 'topic': '6'},
    {'id': 'quiz-2020-a02-q4',
     'question': 'Which sensor arrangement best measures the rotational speed of a generator pulley for a microcontroller?',
     'choices': ['LDR and fixed resistor', 'Slotted opto-switch with a slotted disc', 'Thermistor on the bearing', 'Strain gauge on the belt'],
     'correctIndex': 1,
     'explanation': 'The slotted disc breaks the opto-switch beam, producing pulses whose interval the microcontroller can time.', 'topic': '6'},
]
if os.path.exists(quiz_path):
    with open(quiz_path, 'r', encoding='utf-8') as f:
        qd = json.load(f)
    ids = {q['id'] for q in quiz_items}
    qd = [q for q in qd if q['id'] not in ids] + quiz_items
    with open(quiz_path, 'w', encoding='utf-8') as f:
        json.dump(qd, f, indent=2, ensure_ascii=False)
    print(f'quiz_questions.json now has {len(qd)} items.')
