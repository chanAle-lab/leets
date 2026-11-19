import json, os

questions_file = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets\questions.json'
quiz_file = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets\quiz_questions.json'

with open(questions_file, 'r', encoding='utf-8-sig') as f:
    db = json.load(f)

# Register paper in db['papers'] if not present
paper_id = '2019-summer-as-01'
existing_paper = next((p for p in db.get('papers', []) if p['id'] == paper_id), None)
if not existing_paper:
    db.setdefault('papers', []).append({
        "id": paper_id,
        "code": "H004/01",
        "unit": "Principles of Design Engineering (AS)",
        "year": 2019,
        "level": "H004",
        "totalMarks": 90,
        "series": "Summer"
    })

# Remove existing if any
db['questions'] = [q for q in db['questions'] if q['paper'] != paper_id]

as_questions = [
    {
        "id": f"{paper_id}-q1a",
        "paper": paper_id,
        "question": "1(a)",
        "marks": 2,
        "page": 2,
        "topics": ["2.1", "1.1"],
        "skills": ["design"],
        "summary": "Identify two design requirements taken into account when designing a domestic washing machine.",
        "prompt": "Fig. 1.1 shows a domestic washing machine that is used to clean clothes.<br><br>Identify <b>two</b> design requirements that would have been taken into account when designing the washing machine. [2]",
        "figures": ["img/2019-summer-as-01/fig-1-1.jpg"],
        "image": "img/2019-summer-as-01/q1a.jpg",
        "markscheme": "img/2019-summer-as-01/ms-1a.jpg",
        "markscheme_text": "<b>One mark for identifying each of two design requirements (max 2 marks):</b><br>• Size and ergonomics of controls / buttons (1)<br>• External dimensions / standard height to fit under kitchen worktops (600 mm width) (1)<br>• Drum load capacity / volume of clothes it can wash (1)<br>• Cycle duration and energy / water efficiency ratings (1)<br>• Manufacturing retail cost and material durability (1)<br>• Ease of maintenance and end-of-life recycling (1)"
    },
    {
        "id": f"{paper_id}-q1bi",
        "paper": paper_id,
        "question": "1(b)(i)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1"],
        "skills": ["technical"],
        "summary": "State two inputs that would be included in a system diagram for the washing machine.",
        "prompt": "State <b>two</b> inputs that would be included in a system diagram for the washing machine. [2]",
        "figures": [],
        "image": "img/2019-summer-as-01/q1bi.jpg",
        "markscheme": "img/2019-summer-as-01/ms-1bi.jpg",
        "markscheme_text": "<b>One mark for each of two valid inputs (max 2 marks):</b><br>• User push buttons / start button (1)<br>• Rotary program selector dial (1)<br>• Door safety interlock switch (1)<br>• Water level pressure sensor / water temperature thermistor (1)<br>• Touchscreen panel (1)"
    },
    {
        "id": f"{paper_id}-q1bii",
        "paper": paper_id,
        "question": "1(b)(ii)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1"],
        "skills": ["technical"],
        "summary": "State two outputs that would be included in a system diagram for the washing machine.",
        "prompt": "State <b>two</b> outputs that would be included in a system diagram for the washing machine. [2]",
        "figures": [],
        "image": "img/2019-summer-as-01/q1bii.jpg",
        "markscheme": "img/2019-summer-as-01/ms-1bii.jpg",
        "markscheme_text": "<b>One mark for each of two valid outputs (max 2 marks):</b><br>• Electric drum drive motor (1)<br>• Water heating element (1)<br>• Water inlet solenoid valve / drain pump (1)<br>• Digital screen interface / cycle timer countdown (1)<br>• Audible buzzer / chime signalling end of cycle (1)"
    },
    {
        "id": f"{paper_id}-q1ci",
        "paper": paper_id,
        "question": "1(c)(i)",
        "marks": 3,
        "page": 3,
        "topics": ["3.2"],
        "skills": ["technical"],
        "summary": "Identify and explain one reason why washing machines use a belt driven system.",
        "prompt": "A major part of a washing machine is the drum. Clothes are placed into the drum when they need to be washed. To spin the drum a belt driven system is often used such as the one shown in Fig. 1.2 below.<br><br>Identify and explain <b>one</b> reason why washing machines use this belt driven system. [3]",
        "figures": ["img/2019-summer-as-01/fig-1-2.jpg"],
        "image": "img/2019-summer-as-01/q1ci.jpg",
        "markscheme": "img/2019-summer-as-01/ms-1ci.jpg",
        "markscheme_text": "<b>One mark for identifying a reason, up to two further marks for explanation (max 3 marks):</b><br>• Speed reduction & torque multiplication: large pulley diameter ratio allows high-speed motor to produce the high torque required to tumble wet laundry (3)<br>• Vibration damping & motor protection: rubber belt flexes to absorb drum shock and out-of-balance loads during spin cycles; belt will slip if drum jams rather than burning out motor (3)<br>• Quiet operation: rubber V-belt runs significantly quieter than metal gears or chain drives (3)<br>• Maintenance: easily accessible and cost-effective to replace when worn (3)"
    },
    {
        "id": f"{paper_id}-q1cii",
        "paper": paper_id,
        "question": "1(c)(ii)",
        "marks": 4,
        "page": 4,
        "topics": ["3.2", "1.2"],
        "skills": ["maths", "technical"],
        "summary": "Calculate drum speed in rev/min if motor rotates at 45 rev/s with Ø350mm drum and Ø50mm motor pulleys.",
        "prompt": "Fig. 1.3 shows the diameters of the drum and motor pulleys (drum pulley \\(\\varnothing 350\\text{ mm}\\), motor pulley \\(\\varnothing 50\\text{ mm}\\)).<br><br>Calculate the drum speed if the motor is rotating at \\(45\\text{ rev/s}\\). Give your answer in rev/min to 1 decimal place. Show your working. [4]",
        "figures": ["img/2019-summer-as-01/fig-1-3.jpg"],
        "image": "img/2019-summer-as-01/q1cii.jpg",
        "markscheme": "img/2019-summer-as-01/ms-1cii.jpg",
        "markscheme_text": "<b>Award four marks as follows:</b><br>• Motor speed conversion to rpm: \\(45 \\times 60 = 2700\\text{ rev/min}\\) (1)<br>• Velocity ratio (driven/driver): \\(\\frac{350}{50} = 7\\) (1)<br>• Output speed formula: \\(\\frac{\\text{Motor rpm}}{\\text{VR}} = \\frac{2700}{7}\\) (1)<br>• Drum speed calculation: \\(385.7\\text{ rev/min}\\) (to 1 d.p.) (1)"
    },
    {
        "id": f"{paper_id}-q1di",
        "paper": paper_id,
        "question": "1(d)(i)",
        "marks": 5,
        "page": 5,
        "topics": ["4.1", "4.3"],
        "skills": ["technical", "design"],
        "summary": "Name a suitable metal for the washing machine drum and explain two reasons why it is suitable.",
        "prompt": "Fig. 1.4 shows the drum of the washing machine.<br><br>Name a suitable metal which the drum could be manufactured from and explain <b>two</b> reasons why this metal is suitable. [5]",
        "figures": ["img/2019-summer-as-01/fig-1-4.jpg"],
        "image": "img/2019-summer-as-01/q1di.jpg",
        "markscheme": "img/2019-summer-as-01/ms-1di.jpg",
        "markscheme_text": "<b>Award five marks as follows:</b><br>• 1 mark for naming metal: Stainless steel (or galvanised steel / aluminium) (1)<br>• Up to 2 marks for Reason 1: High corrosion resistance to detergent, bleach, and hot water; chromium oxide passive layer prevents rusting (2)<br>• Up to 2 marks for Reason 2: High tensile strength and stiffness; withstanding high centrifugal forces during 1400+ rpm spin cycles without distorting (2)<br>• <i>(Alternative: Good ductility allowing sheet metal piercing and roll-forming)</i>"
    },
    {
        "id": f"{paper_id}-q1dii",
        "paper": paper_id,
        "question": "1(d)(ii)",
        "marks": 6,
        "page": 6,
        "topics": ["5.1"],
        "skills": ["practical", "technical"],
        "summary": "Use annotated sketches/notes to show how the drum would be manufactured in a batch of 5000.",
        "prompt": "Use annotated sketches and/or notes to show how the drum in Fig. 1.4 would be manufactured in a batch of 5000.<br><br>Your response must make reference to the:<br>• sequence of stages involved in manufacturing the drum;<br>• joining methods needed;<br>• tools and equipment required. [6]",
        "figures": ["img/2019-summer-as-01/fig-1-4.jpg"],
        "image": "img/2019-summer-as-01/q1dii.jpg",
        "markscheme": "img/2019-summer-as-01/ms-1dii.jpg",
        "markscheme_text": "<b>Level 3 (5-6 marks):</b> Thorough understanding of industrial batch manufacture of the drum with accurate technical terms and complete end-to-end process sequence.<br><b>Level 2 (3-4 marks):</b> Sound understanding of major stages with reasonable technical vocabulary.<br><b>Level 1 (1-2 marks):</b> Basic descriptive knowledge with notable gaps.<br><br><b>Indicative Content:</b><br>1. Blanking & Piercing: CNC punching or laser cutting of flat stainless sheet; perforating drainage holes and embossing paddles.<br>2. Rolling: 3-roll sheet metal bender forms cylindrical drum wall.<br>3. Joining: Longitudinal seam welding (TIG/laser) or lock seaming.<br>4. Back Plate Pressing: Hydraulic deep drawing press forms circular rear dish.<br>5. Flanging & Seaming: Circular seam roller / spot welder joins cylinder to rear flange.<br>6. Paddles: Internal plastic agitation fins injection moulded and clipped/screwed in place."
    },
    {
        "id": f"{paper_id}-q2ai",
        "paper": paper_id,
        "question": "2(a)(i)",
        "marks": 2,
        "page": 7,
        "topics": ["1.2", "3.2"],
        "skills": ["maths"],
        "summary": "Convert 150 kg to Newtons (N) stating the formula used.",
        "prompt": "Fig. 2.1 shows an example of a bicycle for hire designed to support a maximum weight of \\(150\\text{ kg}\\).<br><br>Convert \\(150\\text{ kg}\\) to Newtons (N) stating the formula used. [2]",
        "figures": ["img/2019-summer-as-01/fig-2-1.jpg"],
        "image": "img/2019-summer-as-01/q2ai.jpg",
        "markscheme": "img/2019-summer-as-01/ms-2ai.jpg",
        "markscheme_text": "<b>Award two marks as follows:</b><br>• Formula: \\(\\text{Force} = \\text{mass} \\times \\text{acceleration (gravity)}\\) or \\(W = mg\\) (1)<br>• Calculation: \\(150 \\times 9.8 = 1470\\text{ N}\\) (allow \\(150 \\times 9.81 = 1471.5\\text{ N}\\) or \\(150 \\times 10 = 1500\\text{ N}\\)) (1)"
    },
    {
        "id": f"{paper_id}-q2aii",
        "paper": paper_id,
        "question": "2(a)(ii)",
        "marks": 2,
        "page": 8,
        "topics": ["1.2"],
        "skills": ["maths"],
        "summary": "Calculate the shaded cross-sectional area of the hollow seat post tube in m² to 3 sig figs.",
        "prompt": "Fig. 2.2 shows a cross-section of the hollow cylindrical tube that forms the seat post. The tube has a wall thickness of \\(2\\text{ mm}\\) and an outside diameter of \\(50\\text{ mm}\\).<br><br>Calculate the shaded cross-sectional area of the hollow cylindrical tube in \\(\\text{m}^2\\) to 3 significant figures. Show your working.<br><br>\\(\\text{Area of a circle } A = \\pi r^2\\) [2]",
        "figures": ["img/2019-summer-as-01/fig-2-2.jpg"],
        "image": "img/2019-summer-as-01/q2aii.jpg",
        "markscheme": "img/2019-summer-as-01/ms-2aii.jpg",
        "markscheme_text": "<b>Award two marks as follows:</b><br>• Radii identification: \\(r_{\\text{out}} = 25\\text{ mm} = 0.025\\text{ m}\\), \\(r_{\\text{in}} = 25 - 2 = 23\\text{ mm} = 0.023\\text{ m}\\) (1)<br>• Area formula & calculation: \\(A = \\pi(0.025^2 - 0.023^2) = \\pi(6.25 \\times 10^{-4} - 5.29 \\times 10^{-4}) = 3.016 \\times 10^{-4}\\text{ m}^2\\) (1)"
    },
    {
        "id": f"{paper_id}-q2aiii",
        "paper": paper_id,
        "question": "2(a)(iii)",
        "marks": 3,
        "page": 8,
        "topics": ["1.2", "4.1"],
        "skills": ["maths", "technical"],
        "summary": "Calculate the stress in the seat post in MPa when loaded to the maximum weight of 150 kg.",
        "prompt": "Calculate the stress in the seat post in MPa when loaded to the maximum weight of \\(150\\text{ kg}\\). Show your working. [3]",
        "figures": ["img/2019-summer-as-01/fig-2-2.jpg"],
        "image": "img/2019-summer-as-01/q2aiii.jpg",
        "markscheme": "img/2019-summer-as-01/ms-2aiii.jpg",
        "markscheme_text": "<b>Award three marks as follows:</b><br>• Stress formula: \\(\\text{Stress} = \\frac{\\text{Force}}{\\text{Area}}\\) (1)<br>• Substitution: \\(\\text{Stress} = \\frac{1470\\text{ N}}{3.016 \\times 10^{-4}\\text{ m}^2} = 4874005\\text{ Pa}\\) (1)<br>• Conversion to MPa: \\(4.87\\text{ MPa}\\) (allow \\(4.97\\text{ MPa}\\) if using \\(g=10\\)) (1)"
    },
    {
        "id": f"{paper_id}-q2b",
        "paper": paper_id,
        "question": "2(b)",
        "marks": 5,
        "page": 9,
        "topics": ["1.2", "4.1"],
        "skills": ["maths", "technical"],
        "summary": "Calculate Young's Modulus in GPa if seat post length is 60 cm and compresses by 0.04 mm.",
        "prompt": "The length of the seat post is \\(60\\text{ cm}\\). When a person weighing \\(150\\text{ kg}\\) sits on the bicycle the length of the seat post compresses by \\(0.04\\text{ mm}\\). Calculate the Young's Modulus of the material of the seat post in GPa. Show your working. [5]",
        "figures": [],
        "image": "img/2019-summer-as-01/q2b.jpg",
        "markscheme": "img/2019-summer-as-01/ms-2b.jpg",
        "markscheme_text": "<b>Award five marks as follows:</b><br>• Formula: \\(\\text{YM} = \\frac{\\text{stress}}{\\text{strain}}\\) (1)<br>• Strain formula: \\(\\text{Strain} = \\frac{\\text{extension}}{\\text{original length}}\\) (1)<br>• Strain calculation: \\(\\frac{0.04 \\times 10^{-3}\\text{ m}}{0.60\\text{ m}} = 6.67 \\times 10^{-5}\\) (1)<br>• Young's modulus application: \\(\\frac{4.87 \\times 10^6\\text{ Pa}}{6.67 \\times 10^{-5}}\\) (1)<br>• Final answer in GPa: \\(73\\text{ GPa}\\) (allow 73 to 75 GPa) (1)"
    },
    {
        "id": f"{paper_id}-q2c",
        "paper": paper_id,
        "question": "2(c)",
        "marks": 3,
        "page": 9,
        "topics": ["1.2", "2.3"],
        "skills": ["maths"],
        "summary": "Calculate how many days it takes to cover the £1400 annual bicycle cost based on hire data.",
        "prompt": "Bicycles can be hired multiple times in one day. The cost to the individual is £2 for every 30 minutes a bicycle is hired. Each bicycle costs the bicycle hire company £1400 per year.<br><br>Calculate how many days it takes to cover the £1400 cost of a bicycle if the bicycle is, on average, hired by 16 different people a day and ¾ of their journeys are completed within 30 minutes and the rest within one hour. Show your working. [3]",
        "figures": [],
        "image": "img/2019-summer-as-01/q2c.jpg",
        "markscheme": "img/2019-summer-as-01/ms-2c.jpg",
        "markscheme_text": "<b>Award three marks as follows:</b><br>• Breakdown of journeys: \\(16 \\times 0.75 = 12\\text{ people}\\) for \\(\\le 30\\text{ min}\\) (£2 each); remaining \\(4\\text{ people}\\) for 1 hour (£4 each) (1)<br>• Daily revenue: \\((12 \\times 2) + (4 \\times 4) = 24 + 16 = \\pounds 40\\text{ per day}\\) (1)<br>• Number of days: \\(\\frac{\\pounds 1400}{\\pounds 40} = 35\\text{ days}\\) (1)"
    },
    {
        "id": f"{paper_id}-q3a",
        "paper": paper_id,
        "question": "3(a)",
        "marks": 3,
        "page": 10,
        "topics": ["1.2", "3.2"],
        "skills": ["maths"],
        "summary": "Calculate the support length x in metres to 2 decimal places using trigonometry.",
        "prompt": "Fig. 3.1 shows a street light with a light sensor on the top which is used to illuminate pavements and roads at night.<br><br>Additional support (x) is added to the street light structure as shown in Fig. 3.2 below.<br><br>Using the information in Fig. 3.2 (vertical span \\(2.7\\text{ m}\\), angle \\(30^\\circ\\)), calculate the length \\(x\\) in metres (m) to 2 decimal places. Show your working. [3]",
        "figures": ["img/2019-summer-as-01/fig-3-1.jpg", "img/2019-summer-as-01/fig-3-2.jpg"],
        "image": "img/2019-summer-as-01/q3a.jpg",
        "markscheme": "img/2019-summer-as-01/ms-3a.jpg",
        "markscheme_text": "<b>Award three marks as follows:</b><br>• Trigonometry formula identification: \\(\\cos(30^\\circ) = \\frac{\\text{Adjacent}}{\\text{Hypotenuse}} = \\frac{2.7}{x}\\) (1)<br>• Rearranging for \\(x\\): \\(x = \\frac{2.7}{\\cos(30^\\circ)}\\) (1)<br>• Calculation: \\(x = \\frac{2.7}{0.8660} = 3.12\\text{ m}\\) (1)"
    },
    {
        "id": f"{paper_id}-q3b",
        "paper": paper_id,
        "question": "3(b)",
        "marks": 6,
        "page": 11,
        "topics": ["3.3"],
        "skills": ["technical"],
        "summary": "Describe how the street light circuit operates referring to inputs, processes, and outputs.",
        "prompt": "A student was asked to design a circuit to be used in the street light. Fig. 3.3 shows the circuit that was designed.<br><br>Describe how the circuit shown in Fig. 3.3 operates.<br><br>Make reference to inputs, processes and outputs in your response. [6]",
        "figures": ["img/2019-summer-as-01/fig-3-3.jpg"],
        "image": "img/2019-summer-as-01/q3b.jpg",
        "markscheme": "img/2019-summer-as-01/ms-3b.jpg",
        "markscheme_text": "<b>Up to 6 marks for structured description of circuit operation:</b><br>• Input: LDR resistance increases in darkness, raising the potential divider output voltage at the transistor base (2)<br>• Process: Darlington pair transistors conduct, energising the electromagnetic relay coil; flyback diode protects transistors from back-EMF spikes (2)<br>• Output: Relay contacts close, completing the 24V secondary circuit to illuminate the 3 LEDs protected by current-limiting resistor R2 (2)<br>• <i>(Note: Cap at 4/6 if terms input, process, and output are not explicitly used)</i>"
    },
    {
        "id": f"{paper_id}-q3ci",
        "paper": paper_id,
        "question": "3(c)(i)",
        "marks": 4,
        "page": 12,
        "topics": ["3.3"],
        "skills": ["technical", "design"],
        "summary": "Draw a flowchart for a microcontroller to turn on LED when dark and off when light in a closed loop.",
        "prompt": "The student wanted to redesign the circuit in Fig. 3.3 using a microcontroller. The student chose to use only one 3vdc LED as the output in the circuit which is shown in Fig. 3.4 below.<br><br>Draw a flowchart to show how the microcontroller could turn on the LED when it is dark and then off when it is light. Your solution needs to be a closed loop system so that the student can test it multiple times without resetting the system. [4]",
        "figures": ["img/2019-summer-as-01/fig-3-4.jpg", "img/2019-summer-as-01/ms-3ci-flowchart.jpg"],
        "image": "img/2019-summer-as-01/q3ci.jpg",
        "markscheme": "img/2019-summer-as-01/ms-3ci.jpg",
        "markscheme_text": "<b>Award four marks as follows:</b><br>• Correct start/terminator and process box shapes (1)<br>• Correct decision diamond labelled 'Is it dark?' / threshold check (1)<br>• Action branches: 'Yes' -> 'Turn ON LED', 'No' -> 'Turn OFF LED' (1)<br>• Closed loop loopback routing to re-check continuously without stopping (1)"
    },
    {
        "id": f"{paper_id}-q3cii",
        "paper": paper_id,
        "question": "3(c)(ii)",
        "marks": 2,
        "page": 13,
        "topics": ["3.3", "1.2"],
        "skills": ["maths", "technical"],
        "summary": "Calculate the resistance of the LDR in ohms when output voltage is 3.75 V.",
        "prompt": "Using the potential divider formula and the student workings shown in Fig. 3.5, calculate the resistance of the LDR labelled in Fig. 3.4 in ohms (Ω) when the output voltage is 3.75 volts. Show your working.<br><br>\\(V_{\\text{out}} = V_{\\text{in}} \\times \\frac{R_2}{R_1 + R_2}\\)<br>\\(V_{\\text{in}} = 4.5\\text{ V}\\), \\(R_2 = 10\\text{ k}\\Omega\\), \\(V_{\\text{out}} = 3.75\\text{ V}\\) [2]",
        "figures": ["img/2019-summer-as-01/fig-3-5.jpg"],
        "image": "img/2019-summer-as-01/q3cii.jpg",
        "markscheme": "img/2019-summer-as-01/ms-3cii.jpg",
        "markscheme_text": "<b>Award two marks as follows:</b><br>• Rearranging formula: \\(R_1 = \\frac{(V_{\\text{in}} \\times R_2) - (R_2 \\times V_{\\text{out}})}{V_{\\text{out}}} = \\frac{(4.5 \\times 10000) - (10000 \\times 3.75)}{3.75}\\) (1)<br>• Calculation: \\(R_1 = \\frac{45000 - 37500}{3.75} = \\frac{7500}{3.75} = 2000\\ \\Omega\\) (1)"
    },
    {
        "id": f"{paper_id}-q4ai",
        "paper": paper_id,
        "question": "4(a)(i)",
        "marks": 2,
        "page": 14,
        "topics": ["3.3"],
        "skills": ["technical"],
        "summary": "Identify and explain why a servo motor is better than a DC motor for controlling aircraft control surfaces.",
        "prompt": "Fig. 4.1 shows an example of a model aircraft and a remote control which an operator can use to fly and move the aircraft in the air.<br><br>When the model aircraft is in the air the operator can control the moving parts allowing the model aircraft to move left/right and up/down. The moving parts are often controlled by servo motors.<br><br>Identify and explain <b>one</b> reason why a servo motor is better than a DC motor for controlling the moving parts of the model aircraft. [2]",
        "figures": ["img/2019-summer-as-01/fig-4-1.jpg"],
        "image": "img/2019-summer-as-01/q4ai.jpg",
        "markscheme": "img/2019-summer-as-01/ms-4ai.jpg",
        "markscheme_text": "<b>Award two marks (1 mark for identifying reason, 1 mark for context):</b><br>• Precise angular position control: servos rotate to exact angles (e.g. 0° to 180°) corresponding to transmitter joystick position, holding control surfaces firmly against aerodynamic wind forces (2)<br>• Built-in closed loop feedback: internal potentiometer and gearing eliminate need for external limit switches or complex encoder software (2)"
    },
    {
        "id": f"{paper_id}-q4aii",
        "paper": paper_id,
        "question": "4(a)(ii)",
        "marks": 5,
        "page": 15,
        "topics": ["3.3"],
        "skills": ["technical", "design"],
        "summary": "Draw a circuit diagram showing how a potentiometer controls a servo motor using a programmable controller.",
        "prompt": "Fig. 4.2 shows a servo motor and a potentiometer (variable resistor) which could be used as part of the control system for the moving parts of the model aircraft.<br><br>Draw a circuit diagram to show how the potentiometer could control the servo motor using a programmable controller. [5]",
        "figures": ["img/2019-summer-as-01/fig-4-2.jpg", "img/2019-summer-as-01/ms-4aii-circuit.jpg"],
        "image": "img/2019-summer-as-01/q4aii.jpg",
        "markscheme": "img/2019-summer-as-01/ms-4aii.jpg",
        "markscheme_text": "<b>Award five marks as follows:</b><br>• 1 mark: Potentiometer connected across power rails with wiper to ADC input pin of microcontroller (1)<br>• 1 mark: Servo motor connected to PWM output pin and power/ground rails (1)<br>• 1 mark: Correct connections to programmable microcontroller (PIC) (1)<br>• 1 mark: Correct circuit symbols used throughout (1)<br>• 1 mark: Suitable power supply indicated (e.g. 5V battery) (1)"
    },
    {
        "id": f"{paper_id}-q4b",
        "paper": paper_id,
        "question": "4(b)*",
        "marks": 8,
        "page": 16,
        "topics": ["1.1", "2.3"],
        "skills": ["design"],
        "summary": "Discuss the ethical and environmental issues related to outsourcing manufacturing to China.",
        "prompt": "The model aircraft shown in Fig. 4.1 is designed and sold in the UK by a British company. It outsources the manufacture of the model aircraft to a Chinese company.<br><br>Discuss the ethical and environmental issues related to this partnership. [8]",
        "figures": ["img/2019-summer-as-01/fig-4-1.jpg"],
        "image": "img/2019-summer-as-01/q4b.jpg",
        "markscheme": "img/2019-summer-as-01/ms-4b.jpg",
        "markscheme_text": "<b>Level 3 (6-8 marks):</b> Thorough, balanced discussion covering both ethical and environmental issues from UK company and Chinese manufacturer perspectives.<br><b>Level 2 (3-5 marks):</b> Sound discussion of ethical and/or environmental issues with some relevant points.<br><b>Level 1 (1-2 marks):</b> Basic descriptive knowledge with minimal evaluation.<br><br><b>Indicative Content:</b><br>• Ethical (UK): Avoids heavy capital investment in UK factories; however, risks loss of domestic skilled manufacturing jobs and IP vulnerability.<br>• Ethical (China): Creates local employment and economic growth; but risks worker exploitation if labour standards, hours, and pay are not strictly audited.<br>• Environmental: Long-distance air/sea freight from China generates huge carbon footprints; manufacturing in regions with fossil-heavy energy grids increases embedded lifecycle emissions; potential circumvention of strict European environmental waste laws."
    },
    {
        "id": f"{paper_id}-q4ci",
        "paper": paper_id,
        "question": "4(c)(i)",
        "marks": 3,
        "page": 17,
        "topics": ["3.3"],
        "skills": ["technical"],
        "summary": "Describe how the speed of a DC motor can be controlled so an operator can change aircraft speed.",
        "prompt": "The propeller on the model aircraft in Fig. 4.1 is connected to a DC motor.<br><br>Describe how the speed of a DC motor can be controlled so the operator can easily change the speed of the model aircraft. [3]",
        "figures": ["img/2019-summer-as-01/fig-4-1.jpg"],
        "image": "img/2019-summer-as-01/q4ci.jpg",
        "markscheme": "img/2019-summer-as-01/ms-4ci.jpg",
        "markscheme_text": "<b>Up to three marks for describing DC motor speed control (max 3 marks):</b><br>• Pulse Width Modulation (PWM): rapid electronic switching of motor voltage on and off (1)<br>• Duty cycle variation: altering the ratio of 'on-time' to 'off-time' changes the average voltage supplied to the windings without reducing peak torque (1)<br>• Throttle interface: electronic speed controller (ESC) receives throttle command from transmitter to vary pulse width instantly (1)"
    },
    {
        "id": f"{paper_id}-q4cii",
        "paper": paper_id,
        "question": "4(c)(ii)",
        "marks": 6,
        "page": 18,
        "topics": ["3.2", "5.1"],
        "skills": ["technical", "design"],
        "summary": "Show using annotated sketches/notes how the propeller can be securely attached to the M8 threaded motor shaft.",
        "prompt": "Fig. 4.3 shows a DC motor and a propeller which can be used together to provide thrust for any model aircraft. Fig. 4.4 shows a sketch of these components drawn in 2D (motor shaft M8 threaded, propeller holes \\(\\varnothing 3\\text{ mm}\\) unthreaded).<br><br>Use annotated sketches and/or notes to show how the propeller can be attached to the DC motor. The motor and the propeller cannot be modified in anyway, i.e. drilling, cutting or bending.<br><br>Your response must show:<br>• how the movement from the DC motor will be transmitted to the propeller;<br>• how the attachment(s) will allow the propeller to move securely. The attachment(s) should also be able to be removed easily;<br>• the material(s)/component(s) to be used. [6]",
        "figures": ["img/2019-summer-as-01/fig-4-3.jpg", "img/2019-summer-as-01/fig-4-4.jpg", "img/2019-summer-as-01/ms-4cii-propeller.jpg"],
        "image": "img/2019-summer-as-01/q4cii.jpg",
        "markscheme": "img/2019-summer-as-01/ms-4cii.jpg",
        "markscheme_text": "<b>Level 3 (5-6 marks):</b> High detail covering all 3 bullet points. Clear annotated sketches showing intermediate adapter flange, M8 threaded bore, M3 fastening bolts, and anti-vibration locking nuts.<br><b>Level 2 (3-4 marks):</b> Sound solution covering at least two bullet points.<br><b>Level 1 (1-2 marks):</b> Basic solution with limited detail or unclear sketches.<br><br><b>Technical Details:</b><br>• Adapter Hub / Flange: CNC machined aluminium boss with internal M8 thread to screw onto motor shaft.<br>• Drive Transmission: Pitch circle of threaded M3 holes in the adapter flange aligning with the 6x Ø3mm unthreaded propeller holes.<br>• Security & Removal: M3 high-tensile steel cap head screws with nylon-locking nuts or spring washers; grub screw onto shaft flat to prevent spin-off under motor braking."
    },
    {
        "id": f"{paper_id}-q5a",
        "paper": paper_id,
        "question": "5(a)*",
        "marks": 8,
        "page": 20,
        "topics": ["1.1", "2.3"],
        "skills": ["design"],
        "summary": "Discuss relative advantages of using renewable and non-renewable energy sources for isolated UK islands.",
        "prompt": "Discuss the relative advantages of using renewable and non-renewable energy sources to meet the energy requirements of communities on isolated islands in the UK. [8]",
        "figures": [],
        "image": "img/2019-summer-as-01/q5a.jpg",
        "markscheme": "img/2019-summer-as-01/ms-5a.jpg",
        "markscheme_text": "<b>Level 3 (6-8 marks):</b> Thorough, balanced discussion weighing the merits of both renewable and non-renewable sources in the isolated island context. Clear line of reasoning.<br><b>Level 2 (3-5 marks):</b> Sound understanding covering advantages of both or one in depth.<br><b>Level 1 (1-2 marks):</b> Basic descriptive knowledge with little appreciation of island constraints.<br><br><b>Indicative Content:</b><br>• Renewable (Wind, Tidal/Wave, Solar PV): Abundant natural island wind/marine energy; zero greenhouse emissions; autonomous energy security without reliance on costly mainland fuel deliveries by tanker.<br>• Non-renewable (Diesel generators, gas): High energy density and on-demand baseload reliability regardless of weather; low initial capital installation cost; vital emergency backup when renewable output drops."
    },
    {
        "id": f"{paper_id}-q5b",
        "paper": paper_id,
        "question": "5(b)",
        "marks": 4,
        "page": 21,
        "topics": ["1.1", "2.3"],
        "skills": ["design"],
        "summary": "State two measures an island Government could put in place to tackle waste plastic, justifying each.",
        "prompt": "Waste plastic materials and products are a serious issue. State <b>two</b> measures that the Government of a small island could put in place to tackle this problem. Justify each of your responses. [4]",
        "figures": [],
        "image": "img/2019-summer-as-01/q5b.jpg",
        "markscheme": "img/2019-summer-as-01/ms-5b.jpg",
        "markscheme_text": "<b>Award up to 2 marks for each of two measures (1 mark for measure, 1 mark for justification) (max 4 marks):</b><br>• Plastic tax / Levy on single-use packaging: Discourages import and consumption of non-essential plastics, incentivising consumers and retailers to adopt reusable alternatives (2)<br>• Deposit return scheme (DRS): Provides financial incentive for residents and tourists to return bottles for recycling, drastically reducing beach and roadside litter (2)<br>• Ban on specific single-use plastics: Outlawing plastic straws/cutlery/carrier bags immediately eliminates high-volume litter streams (2)<br>• Island recycling infrastructure / pyrolysis plant: Establishes local mechanical recycling or conversion of plastic into fuel, reducing prohibitive costs of shipping plastic waste back to the mainland (2)"
    }
]

total_as_m = sum(q['marks'] for q in as_questions)
print(f'H004/01 Questions: {len(as_questions)}, Total marks: {total_as_m}')
assert total_as_m == 90, f'Expected 90 marks, got {total_as_m}'

db['questions'].extend(as_questions)

with open(questions_file, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print('Successfully added H004/01 questions to questions.json!')

# Add Quiz questions
with open(quiz_file, 'r', encoding='utf-8-sig') as f:
    quiz_data = json.load(f)

new_quizzes = [
    {
        "id": "quiz-2019-as-pulley-ratio",
        "topic": "3.2",
        "question": "In a belt-driven pulley system, if a motor pulley has a diameter of 50 mm and the driven drum pulley is 350 mm, what is the velocity ratio?",
        "options": [
            "7 : 1 (reduction)",
            "1 : 7 (speed increase)",
            "14 : 1",
            "3.5 : 1"
        ],
        "answer": 0,
        "explanation": "Velocity ratio is Driven Diameter / Driver Diameter = 350 / 50 = 7. The drum rotates at 1/7th the speed of the motor."
    },
    {
        "id": "quiz-2019-as-youngs-modulus",
        "topic": "4.1",
        "question": "What is the standard engineering unit for Young's Modulus of elasticity (E)?",
        "options": [
            "GPa (or N/m² / Pa)",
            "N m",
            "J / kg",
            "Dimensionless ratio"
        ],
        "answer": 0,
        "explanation": "Young's Modulus is stress / strain. Since strain is dimensionless, E has units of pressure / stress: Pa (Pascals), typically expressed in GPa for metals."
    },
    {
        "id": "quiz-2019-as-flyback-diode",
        "topic": "3.3",
        "question": "Why is a diode connected in reverse-parallel across an electromagnetic relay coil in transistor driver circuits?",
        "options": [
            "To suppress high-voltage back-EMF spikes when the relay switches off",
            "To rectify AC supply voltage into pure DC",
            "To increase the current gain of the transistor",
            "To indicate with light when the coil is energised"
        ],
        "answer": 0,
        "explanation": "When an inductor's current is abruptly cut off, the collapsing magnetic field induces a large reverse back-EMF spike that can destroy the driver transistor. A flyback diode safely clamps this spike."
    },
    {
        "id": "quiz-2019-as-pwm-speed",
        "topic": "3.3",
        "question": "How does Pulse Width Modulation (PWM) control the speed of a DC electric motor efficiently?",
        "options": [
            "By varying the duty cycle (ratio of ON to OFF time) at a fixed frequency",
            "By inserting variable power resistors in series with the motor",
            "By altering the chemical composition of the motor brushes",
            "By converting the DC supply into variable three-phase AC"
        ],
        "answer": 0,
        "explanation": "PWM rapidly switches the full supply voltage ON and OFF; varying the pulse duty cycle adjusts the average voltage and rotational speed while keeping low power losses in the switching transistor."
    }
]

existing_quiz_ids = {q['id'] for q in quiz_data}
for qz in new_quizzes:
    if qz['id'] not in existing_quiz_ids:
        quiz_data.append(qz)

with open(quiz_file, 'w', encoding='utf-8') as f:
    json.dump(quiz_data, f, indent=2, ensure_ascii=False)

print('Successfully added quiz questions to quiz_questions.json!')
