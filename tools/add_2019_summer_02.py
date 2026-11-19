import json
import os

qpath = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets\questions.json'
quiz_path = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets\quiz_questions.json'

with open(qpath, 'r', encoding='utf-8') as f:
    d = json.load(f)

# 1. Ensure paper metadata is correct in papers list
paper_entry = {
    'id': '2019-summer-02',
    'code': 'H404/02',
    'unit': 'Problem Solving in Design Engineering',
    'year': 2019,
    'level': 'H404',
    'totalMarks': 70,
    'series': 'Summer'
}

paper_exists = False
for idx, p in enumerate(d['papers']):
    if p['id'] == '2019-summer-02':
        d['papers'][idx] = paper_entry
        paper_exists = True
        break
if not paper_exists:
    d['papers'].append(paper_entry)

# 2. Authentic OCR June 2019 H404/02 Questions (70 Marks Total)
new_questions = [
    # Question 1* (14 marks)
    {
        'id': '2019-summer-02-q1',
        'paper': '2019-summer-02',
        'question': '1*',
        'marks': 14,
        'page': 2,
        'topics': ['1.1', '2.1', '3.1'],
        'skills': ['design'],
        'summary': 'Discuss design engineering considerations for developing a new groundwater pump for a remote rural village.',
        'prompt': 'Water scarcity is a major concern for parts of the developing world. The World Health Organisation (WHO) is one organisation that is helping by fitting water pumps to extract groundwater in those rural areas worst affected.<br><br>Discuss the issues that a design engineer would need to consider when developing a new water pump for use in a remote rural village.<br><br><i>Refer to information on pages 2, 3 and 4 of the Resource Booklet.</i> [*14]',
        'figures': [
            'img/2019-summer-02/fig-1.jpg',
            'img/2019-summer-02/fig-2.jpg',
            'img/2019-summer-02/fig-3.jpg'
        ],
        'image': 'img/2019-summer-02/q1.jpg',
        'markscheme': 'img/2019-summer-02/ms-1.jpg',
        'markscheme_text': '<b>Level 4 (11–14 marks):</b> Comprehensive discussion of a wide range (at least 3) of issues a design engineer must consider when developing a new water pump for a remote village. Effectively exemplifies points using Resource Booklet data. Well-constructed, logically structured narrative with supported evaluative comments.<br><b>Level 3 (7–10 marks):</b> Good critical discussion covering at least 2 issues with mostly effective use of Resource Booklet evidence.<br><b>Level 2 (4–6 marks):</b> Sufficient understanding covering at least 2 issues with basic structure.<br><b>Level 1 (1–3 marks):</b> Limited discussion; basic isolated points without evaluation.<br><br><b>Indicative Content:</b><br>• <b>Operating Environment & Climate:</b> Arid equatorial conditions with extreme high temperatures (up to 41°C) and tropical monsoons where surface runoff rapidly evaporates or is contaminated; must be installable on unprepared waste land or shared communal ground.<br>• <b>Location & Transport Distance:</b> Wells often located between multiple villages to share drilling and setup costs; requires villagers (primarily women and young children) to walk miles carrying water, increasing exhaustion, school absence, loss of economic productivity, and vulnerability to violence.<br>• <b>Water Source Quality & Geology:</b> Deep groundwater (>10m) is naturally filtered through soil layers against surface pathogens/faeces, but may contain dissolved heavy metals or bacteria from leaking septic systems; requires regular testing which rural areas lack financial and technical resources to perform.<br>• <b>Materials & Manufacturing:</b> Cast alloy main body provides high corrosion resistance and long operational lifespan in harsh outdoor weather; minimal moving parts to simplify sand/die casting and machining; balance between initial material cost and ruggedness.<br>• <b>Maintenance & Supply Chain:</b> Moving parts need periodic lubrication; rubber/nitrile piston seals wear out over time; seals and lubricants must be cheap and easily sourced locally without prolonged shipping delays causing well shutdown.<br>• <b>Ergonomics & Human Factors:</b> Handle height, fulcrum pivot distance, and effort required to operate the lever arm (India MkIII has 650 mm handle vs 150 mm lever arm) must suit the anthropometrics and physical strength of women and children who collect the majority of water.'
    },

    # Question 2 (6 marks)
    {
        'id': '2019-summer-02-q2',
        'paper': '2019-summer-02',
        'question': '2',
        'marks': 6,
        'page': 4,
        'topics': ['6.1', '6.2'],
        'skills': ['maths', 'technical'],
        'summary': 'Calculate the number of complete pump handle cycles required to fill a 20-litre container with water.',
        'prompt': 'The WHO supplies the India MkIII hand-operated water pump shown in Fig. 3 of the Resource Booklet. It also donates the DP4b water containers shown in Fig. 10 of the Resource Booklet to villagers to transport fresh water. Each water container holds 20 litres of water.<br><br>Using the information on page 5 of the Resource Booklet, calculate how many <b>complete cycles</b> of the pump handle will be required to fill <b>one 20 litre container</b> with water. Show your working.<br><br>The formula for calculating the volume of a cylinder is $V = \\pi r^2 h$. [6]',
        'figures': [
            'img/2019-summer-02/fig-3.jpg',
            'img/2019-summer-02/fig-4.jpg',
            'img/2019-summer-02/fig-5.jpg',
            'img/2019-summer-02/fig-10.jpg'
        ],
        'image': 'img/2019-summer-02/q2.jpg',
        'markscheme': 'img/2019-summer-02/ms-2.jpg',
        'markscheme_text': '<b>Full Credit Method (accounting for Piston Rod volume, max 6 marks):</b><br>• Cylinder dimensions from Fig. 5: Diameter $d = 100\\text{ mm} \\implies r = 50\\text{ mm} = 0.05\\text{ m}$; Stroke $h = 300\\text{ mm} = 0.3\\text{ m}$.<br>• Piston rod dimensions: Diameter $D = 38\\text{ mm} \\implies R = 19\\text{ mm} = 0.019\\text{ m}$.<br>• Gross cylinder volume: $V_{\\text{cyl}} = \\pi r^2 h = \\pi \\times (0.05)^2 \\times 0.3 = 0.002356\\text{ m}^3 = 2356\\text{ cm}^3 = 2.356\\text{ L}$ (or $2.365\\text{ L}$ using truncated values).<br>• Piston rod displaced volume: $V_{\\text{rod}} = \\pi R^2 h = \\pi \\times (0.019)^2 \\times 0.3 = 0.000340\\text{ m}^3 = 340\\text{ cm}^3 = 0.34\\text{ L}$ (or $0.30\\text{ L}$).<br>• Net water displaced per stroke: $V_{\\text{net}} = V_{\\text{cyl}} - V_{\\text{rod}} = 2.365 - 0.30 = 2.065\\text{ L}$ (or $2.1\\text{ L}$).<br>• Number of cycles required: $\\text{Cycles} = 20 / 2.065 \\approx 9.68$ (or $20 / 2.1 = 9.52$).<br>• Round up to complete cycles: <b>10 complete cycles</b>.<br><br><b>Alternative Method (ignoring Piston Rod, max 4 marks):</b><br>• $V = 2.365\\text{ L} \\implies \\text{Cycles} = 20 / 2.365 = 8.45 \\implies$ <b>9 complete cycles</b>.'
    },

    # Question 3 (6 marks)
    {
        'id': '2019-summer-02-q3',
        'paper': '2019-summer-02',
        'question': '3',
        'marks': 6,
        'page': 5,
        'topics': ['4.1', '4.2'],
        'skills': ['maths', 'technical'],
        'summary': 'Calculate the minimum number of RB500 photovoltaic panels required to produce 1890 kWh annual energy output.',
        'prompt': 'A design team is investigating whether the use of a solar-powered water pump would be more of a viable solution.<br><br>It is looking into the use of the RB500 photovoltaic panels shown in Fig. 6 of the Resource Booklet. A number of these panels could be used together in a photovoltaic array to provide the required energy output.<br><br>It has been determined that an annual energy output of <b>1890 kilowatt-hours (kWh)</b> is required for the pump to work efficiently.<br><br>Calculate the minimum number of photovoltaic panels of the type shown that would be required to produce the energy output needed for the water pump.<br><br>Use the equation below and information on page 6 of the Resource Booklet. Show your working.<br><br>$$E = A \\times r \\times H \\times PR$$<br>Where:<br>• $E$ = annual energy output from photovoltaic array (kWh)<br>• $A$ = total photovoltaic array area (m²)<br>• $r$ = photovoltaic panel yield<br>• $H$ = annual average solar irradiation (kWh m⁻²)<br>• $PR$ = performance ratio, coefficient of losses. [6]',
        'figures': [
            'img/2019-summer-02/fig-6.jpg'
        ],
        'image': 'img/2019-summer-02/q3.jpg',
        'markscheme': 'img/2019-summer-02/ms-3.jpg',
        'markscheme_text': '<b>Mark Scheme Steps (6 marks):</b><br>1. Rearrange formula in terms of $A$: $A = \\frac{E}{r \\times H \\times PR}$ [1 mark]<br>2. Extract correct data from Resource Booklet (page 6):<br>   - $r = 0.15$<br>   - $PR = 0.75$<br>   - $H = 2100\\text{ kWh m}^{-2}$ [2 marks]<br>3. Substitute values and calculate total area $A$:<br>   $$A = \\frac{1890}{0.15 \\times 2100 \\times 0.75} = \\frac{1890}{236.25} = 8.0\\text{ m}^2\\text{ [1 mark]}$$<br>4. Calculate surface area of single RB500 panel:<br>   $$\\text{Area} = 1.0\\text{ m} \\times 0.5\\text{ m} = 0.5\\text{ m}^2\\text{ [1 mark]}$$<br>5. Divide total array area by single panel area:<br>   $$\\text{Panels} = \\frac{8\\text{ m}^2}{0.5\\text{ m}^2} = \\mathbf{16\\text{ panels}}\\text{ [1 mark]}$$'
    },

    # Question 4 (14 marks)
    {
        'id': '2019-summer-02-q4',
        'paper': '2019-summer-02',
        'question': '4',
        'marks': 14,
        'page': 6,
        'topics': ['1.1', '2.1', '4.1'],
        'skills': ['design'],
        'summary': 'Critically evaluate the use of photovoltaic panels for powering water pumps in water-scarce areas, considering stakeholders and users.',
        'prompt': 'Due to the large initial cost of developing a solar-powered water pump, the WHO is reluctant to commission the design work without further research.<br><br>Critically evaluate the use of photovoltaic panels for powering water pumps in areas affected by water scarcity. Your response should consider the needs of <b>stakeholders</b> and <b>users</b> of the system.<br><br><i>Refer to the information on pages 2, 3 and 6 of the Resource Booklet.</i> [*14]',
        'figures': [
            'img/2019-summer-02/fig-1.jpg',
            'img/2019-summer-02/fig-2.jpg',
            'img/2019-summer-02/fig-6.jpg'
        ],
        'image': 'img/2019-summer-02/q4.jpg',
        'markscheme': 'img/2019-summer-02/ms-4.jpg',
        'markscheme_text': '<b>Level 4 (11–14 marks):</b> Comprehensive critical evaluation considering positive and negative impacts of solar-powered water pumps in water-scarce communities. Analysis consistently and appropriately aligned with both stakeholder and user needs, fully exemplified using Resource Booklet data. Clear, logically structured narrative.<br><b>Level 3 (7–10 marks):</b> Good critical evaluation with balanced stakeholder/user perspectives.<br><b>Level 2 (4–6 marks):</b> Sufficient understanding with basic points.<br><b>Level 1 (1–3 marks):</b> Limited description without evaluation.<br><br><b>Indicative Content:</b><br>• <b>Stakeholder Considerations (WHO, NGOs, Government, Donors, Maintenance Teams):</b><br>  - High initial capital outlay for 16 PV panels, inverters, motor controllers, and structural mounting arrays compared to inexpensive manual hand pumps.<br>  - Installation requires specialized electrical and mechanical engineers rather than local village labour.<br>  - Maintenance: While PV cells have no moving parts, dust, sand, and bird droppings rapidly degrade panel yield in arid zones, requiring regular cleaning; electronics/inverters can fail under extreme heat (up to 41°C).<br>  - Security risks: High-value solar panels and copper wiring are prone to theft and vandalism; necessitates fencing, locking fasteners, or community guarding.<br>  - Energy storage / multi-use potential: Excess electricity generated during peak midday solar irradiance can be stored in batteries or used to power community lighting, refrigeration for medicine, or phone charging.<br>  - Need for manual backup: If electrical components fail or during extended monsoon overcast periods, a manual hand-pump mechanism must remain operational.<br>• <b>User Considerations (Villagers, Women, Children):</b><br>  - Greatly reduces physical labour: Eliminates hours of strenuous manual pumping, preventing exhaustion and musculoskeletal injury.<br>  - Faster water delivery: Motorized pumping fills 20L containers rapidly, drastically shortening queues at the well.<br>  - Social & educational benefits: Frees young girls and women from daily water collection chores, enabling girls to attend school and women to pursue trade/farming.<br>  - Operational education: Villagers must be trained to operate taps and valves responsibly, avoiding leaving taps running and wasting depleted groundwater reserves.<br>  - Sunlight limitations: Pumping is restricted to daytime hours (average 7 hours daily sunlight) unless expensive battery storage is incorporated.'
    },

    # Question 5 (16 marks)
    {
        'id': '2019-summer-02-q5',
        'paper': '2019-summer-02',
        'question': '5',
        'marks': 16,
        'page': 8,
        'topics': ['6.1', '6.2', '6.3', '6.5'],
        'skills': ['technical', 'practical', 'maths'],
        'summary': 'Technical design solutions: PICAXE solar-tracking microcontroller flowchart/code (Issue 1) and a 32:1 compound spur gear train (Issue 2).',
        'prompt': 'A decision has been made to proceed with the design of the solar-powered water pump.<br>The design team has been given two immediate issues to overcome.<br><br><b>Issue 1</b><br>The efficiency of the photovoltaic array will vary throughout the day depending on the position of the sun in the sky. In order to improve the efficiency it has been suggested that the photovoltaic array should move so that it always faces the sun.<br>A system has been designed to do this which uses a motor, connected through a gearbox, to move the array. The system is controlled by a PICAXE microcontroller. Page 7 of the Resource Booklet explains the operation of the system.<br><b>A program flowchart or code with annotation is required for the PICAXE microcontroller so that the photovoltaic array will move to follow the sun across the sky.</b><br><br><b>Issue 2</b><br>Spur gears need to be used for the gearbox to move the photovoltaic array.<br>A gear ratio of <b>32:1</b> is required.<br>Due to the remote area it is working in, the design team has a limited selection of spur gears available shown on page 7 of the Resource Booklet.<br><b>A gear system is required using only the available spur gears that would produce the required gear ratio.</b><br><br>Use sketches and/or notes to determine suitable technical solutions that overcome the two issues identified. All of the information you need is on page 7 of the Resource Booklet. [16]',
        'figures': [
            'img/2019-summer-02/fig-7.jpg',
            'img/2019-summer-02/fig-8.jpg',
            'img/2019-summer-02/fig-9.jpg',
            'img/2019-summer-02/ms-5-flowcode.jpg',
            'img/2019-summer-02/ms-5-gear-train.jpg'
        ],
        'image': 'img/2019-summer-02/q5.jpg',
        'markscheme': 'img/2019-summer-02/ms-5.jpg',
        'markscheme_text': '<b>Issue 1 (8 marks) – Microcontroller Flowchart / Code:</b><br>• Identification of inputs: Two LDR potential dividers connected to analogue ADC inputs C.0 and C.2.<br>• Reading ADC values: Use of `readadc c.0, varA` and `readadc c.2, varB` (or `readadc c.0, LDR1` / `readadc c.2, LDR2`).<br>• Comparison logic:<br>  - If $LDR_1 = LDR_2$ (balanced light): Hold motor (`Low B.0`, `Low B.1`).<br>  - If $LDR_1 < LDR_2$: Turn motor Clockwise (`High B.0`, `Low B.1`).<br>  - If $LDR_1 > LDR_2$: Turn motor Counter-Clockwise (`Low B.0`, `High B.1`).<br>• Motor driver control: Correct dual output pins (B.0 and B.1) driving L293D H-bridge IC.<br>• Program loop: Unconditional jump (`goto main`) ensuring continuous closed-loop sun tracking.<br><br><b>Issue 2 (8 marks) – 32:1 Gearbox Design:</b><br>• Gear ratio formula: $\\text{Gear Ratio} = \\frac{\\text{Product of Driven Teeth}}{\\text{Product of Driver Teeth}} = 32:1$.<br>• Identification that a <b>compound gear train</b> is required because a single pair ratio of 32:1 would require a 5-tooth pinion ($160 / 32 = 5$), which does not exist in stock.<br>• Factoring 32 into two stages: $32 = 8 \\times 4$ (or $4 \\times 8$).<br>• Available gears in inventory: 160t (2), 80t (3), 40t (2), 20t (3).<br>• Stage 1 (4:1 reduction): Driver 20t meshing with Driven 80t ($80 / 20 = 4:1$).<br>• Stage 2 (8:1 reduction): The 80t gear shares a common shaft with a second 20t driver pinion, which meshes with a 160t driven gear on the array output shaft ($160 / 20 = 8:1$).<br>• Total Compound Ratio: $\\frac{80 \\times 160}{20 \\times 20} = 4 \\times 8 = \\mathbf{32:1}$.<br>• Inventory check: Uses two 20t gears (3 in stock), one 80t gear (3 in stock), and one 160t gear (2 in stock).<br>• Annotated schematic showing input motor shaft, intermediate compound shaft, output turntable shaft, and gear tooth counts.'
    },

    # Question 6* (14 marks)
    {
        'id': '2019-summer-02-q6',
        'paper': '2019-summer-02',
        'question': '6*',
        'marks': 14,
        'page': 12,
        'topics': ['1.1', '1.2', '2.1', '3.1'],
        'skills': ['design', 'technical'],
        'summary': 'Critically evaluate the DLR-90 industrial trolley for transporting 20L water containers and suggest design improvements.',
        'prompt': 'During the course of a day the average family will require two containers of water of the type shown in Fig. 10 of the Resource Booklet. Traditionally, these are collected by the women and children of the families and are sometimes carried over large distances.<br><br>The WHO is working with a company that specialises in producing heavy-duty trollies for industrial applications. The company has proposed a trolley design shown in Fig. 11 of the Resource Booklet that could be used by families to transport water from the water source to their homes.<br><br>Critically evaluate the design of the trolley in Fig. 11 of the Resource Booklet making suggestions for improvement for the task specified. [*14]',
        'figures': [
            'img/2019-summer-02/fig-10.jpg',
            'img/2019-summer-02/fig-11.jpg'
        ],
        'image': 'img/2019-summer-02/q6.jpg',
        'markscheme': 'img/2019-summer-02/ms-6.jpg',
        'markscheme_text': '<b>Level 4 (11–14 marks):</b> Comprehensive evaluation of the DLR-90 industrial trolley design with detailed, justified recommendations for improvement. Product analysis consistently aligned with the task of carrying two 20L water containers across remote rural terrain by women and children. Information in Resource Booklet fully exploited. Logically structured narrative.<br><b>Level 3 (7–10 marks):</b> Good evaluation covering trolley materials, wheels, bed dimensions, and weight with several practical improvements.<br><b>Level 2 (4–6 marks):</b> Sufficient evaluation with basic points.<br><b>Level 1 (1–3 marks):</b> Limited descriptive comments without evaluation.<br><br><b>Indicative Content:</b><br>• <b>Evaluation of Existing DLR-90 Trolley:</b><br>  - Load Capacity: 90 kg max load is well suited for two 20L containers ($2 \\times 20\\text{ kg} = 40\\text{ kg} + 10\\text{ kg trolley} = 50\\text{ kg}$ total load, safety factor ~1.8).<br>  - Materials: Aluminium frame is lightweight and rust-free, but costly to produce and difficult to weld in rural villages; steel axle is robust but prone to corrosion in wet conditions and requires grease-packed sealed bearings.<br>  - Wheel & Tyre Limitations: 150 mm diameter wheels are far too small for uneven, rutted dirt roads, mud, and sand; solid rubber tyres provide zero shock absorption, causing extreme jarring, spill risk, and operator fatigue.<br>  - Carrying Bed Size: $380 \\times 250\\text{ mm}$ bed is smaller in depth than the container base ($280 \\times 280\\text{ mm}$), causing container overhang and tipping. The bed is too narrow to place two containers side-by-side ($2 \\times 280 = 560\\text{ mm} > 380\\text{ mm}$), forcing vertical stacking which elevates the centre of gravity and causes rollover on slopes.<br>  - ABS bed material is brittle under sharp impact on rocks.<br>• <b>Recommended Design Improvements:</b><br>  - Wheel Overhaul: Fit large diameter (300–400 mm) pneumatic or puncture-proof micro-cellular / airless tyres with wider tread to roll easily over rough terrain and soft sand.<br>  - Bed Redesign: Widen and lengthen the carrying platform (at least $600 \\times 300\\text{ mm}$) to support two containers side-by-side with a low centre of gravity; add raised perimeter retaining lips, tie-down bungee straps, or a quick-release wire cage.<br>  - Material & Chassis: Fabricate frame from tubular mild steel with galvanized or epoxy powder coating for lower cost, higher impact toughness, and easy repair by local blacksmiths.<br>  - Ergonomic Handle: Ergonomic twin-loop push/pull handle with soft rubber grips; ensure telescoping adjustment mechanism has sealed detent pins to prevent grit/sand jamming.'
    }
]

# Remove existing 2019-summer-02 questions and replace with new authentic list
d['questions'] = [q for q in d['questions'] if q.get('paper') != '2019-summer-02'] + new_questions

with open(qpath, 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2, ensure_ascii=False)

print(f"Successfully updated questions.json! Ingested {len(new_questions)} questions totaling {sum(q['marks'] for q in new_questions)} marks.")

# 3. Add Quiz Questions
quiz_items = [
    {
        'id': 'quiz-2019-s02-q1',
        'question': 'How many complete cycles of the India MkIII hand pump handle are required to fill one 20-litre container with water (accounting for piston rod displacement)?',
        'choices': ['7 cycles', '8 cycles', '10 cycles', '14 cycles'],
        'correctIndex': 2,
        'explanation': 'Gross cylinder volume is 2.365 L and piston rod displacement is 0.30 L, leaving a net delivery of ~2.065 L per stroke. 20 L / 2.065 L = 9.68 strokes, which rounds up to 10 complete cycles.',
        'topic': '6'
    },
    {
        'id': 'quiz-2019-s02-q2',
        'question': 'Using the solar equation E = A × r × H × PR, how many 1000 × 500 mm photovoltaic panels (r = 0.15, PR = 0.75, H = 2100 kWh/m²) are required to produce 1890 kWh annually?',
        'choices': ['8 panels', '12 panels', '16 panels', '24 panels'],
        'correctIndex': 2,
        'explanation': 'Required array area A = 1890 / (0.15 × 2100 × 0.75) = 8.0 m². Each 1000 × 500 mm panel has an area of 0.5 m². Total panels = 8.0 / 0.5 = 16 panels.',
        'topic': '4'
    },
    {
        'id': 'quiz-2019-s02-q3',
        'question': 'Which compound gear arrangement produces a 32:1 gear reduction using available spur gears (20t, 80t, 160t)?',
        'choices': [
            '(80t / 20t) × (160t / 20t)',
            '(160t / 40t) × (80t / 40t)',
            '(160t / 20t) × (40t / 20t)',
            '(160t / 80t) × (80t / 20t)'
        ],
        'correctIndex': 0,
        'explanation': '(80t / 20t) gives a 4:1 reduction and (160t / 20t) gives an 8:1 reduction. Compounding them yields 4 × 8 = 32:1.',
        'topic': '6'
    },
    {
        'id': 'quiz-2019-s02-q4',
        'question': 'What is the primary operational defect of the DLR-90 industrial trolley when transporting 20L water containers across rural dirt terrain?',
        'choices': [
            'Max load capacity is exceeded by the containers',
            '150 mm solid wheels cause excessive jarring and bed is too narrow for two containers side-by-side',
            'Aluminium frame is too heavy for women and children',
            'Telescopic handle cannot adjust to adult human height'
        ],
        'correctIndex': 1,
        'explanation': 'Small 150 mm solid wheels struggle in mud and sand with zero shock absorption, and the 380 mm wide bed forces vertical stacking which raises the centre of gravity dangerously.',
        'topic': '1'
    }
]

if os.path.exists(quiz_path):
    with open(quiz_path, 'r', encoding='utf-8') as f:
        quiz_data = json.load(f)
    quiz_ids = set(q['id'] for q in quiz_items)
    quiz_data = [q for q in quiz_data if q['id'] not in quiz_ids] + quiz_items
    with open(quiz_path, 'w', encoding='utf-8') as f:
        json.dump(quiz_data, f, indent=2, ensure_ascii=False)
    print(f"Updated quiz_questions.json with {len(quiz_items)} new questions. Total: {len(quiz_data)}")
