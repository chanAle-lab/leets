import json, os

questions_file = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets\questions.json'
quiz_file = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets\quiz_questions.json'

with open(questions_file, 'r', encoding='utf-8-sig') as f:
    db = json.load(f)

# Remove any existing dummy questions for 2019-summer-01
db['questions'] = [q for q in db['questions'] if q['paper'] != '2019-summer-01']

new_questions = [
    {
        "id": "2019-summer-01-q1a",
        "paper": "2019-summer-01",
        "question": "1(a)",
        "marks": 3,
        "page": 2,
        "topics": ["2.1", "1.1"],
        "skills": ["design", "technical"],
        "summary": "Identify three ways in which the manufacturer of the home lift can ensure safe operation by its users.",
        "prompt": "Fig. 1.1 shows an electrically-powered home lift. The first image shows the lift on the ground floor. The second image shows the lift on the upper floor.<br><br>Identify <b>three</b> ways in which the manufacturer of the home lift can ensure the safe operation of the lift by its users. [3]",
        "figures": ["img/2019-summer-01/fig-1-1.jpg"],
        "image": "img/2019-summer-01/q1a.jpg",
        "markscheme": "img/2019-summer-01/ms-1a.jpg",
        "markscheme_text": "<b>One mark for identifying each of three ways in which the manufacturer can ensure safe operation (max 3 marks):</b><br>• Provide safety warning labels (e.g. maximum load 2 people / 350 kg) (1)<br>• Door interlock mechanism to prevent lift moving if door is open (1)<br>• Overweight load sensor and audible alarm (1)<br>• Key lock or PIN pad to prevent children operating the lift unsupervised (1)<br>• Battery backup system to lower carriage safely in case of power failure (1)<br>• Emergency stop button / alarm button to summon assistance (1)<br>• Sensitive safety edges on car underside to stop motor if an obstruction is met (1)"
    },
    {
        "id": "2019-summer-01-q1bi",
        "paper": "2019-summer-01",
        "question": "1(b)(i)",
        "marks": 3,
        "page": 3,
        "topics": ["3.2", "1.2"],
        "skills": ["maths", "technical"],
        "summary": "Calculate the time in seconds for the lift to rise 2800 mm at a speed of 0.08 m/s.",
        "prompt": "The home lift in Fig. 1.1 uses a screw thread and nut mechanism in which the nut is attached to the lift and rotated through a double chain drive by an electric motor. The screw thread is held in position and does not move. Fig. 1.2 shows the mechanism.<br><br>The lift moves at a speed of \\(0.08\\text{ m s}^{-1}\\).<br><br>Calculate the time taken in seconds (s) for the lift to rise between floors which are \\(2800\\text{ mm}\\) apart. Show your working. [3]",
        "figures": ["img/2019-summer-01/fig-1-2.jpg"],
        "image": "img/2019-summer-01/q1bi.jpg",
        "markscheme": "img/2019-summer-01/ms-1bi.jpg",
        "markscheme_text": "<b>Award three marks as follows:</b><br>• Rearranging speed formula: \\(\\text{Time} = \\frac{\\text{distance}}{\\text{speed}}\\) (1)<br>• Converting distance units: \\(2800\\text{ mm} = 2.8\\text{ m}\\) (1)<br>• Calculating time: \\(\\text{Time} = \\frac{2.8}{0.08} = 35\\text{ s}\\) (1)"
    },
    {
        "id": "2019-summer-01-q1bii",
        "paper": "2019-summer-01",
        "question": "1(b)(ii)",
        "marks": 3,
        "page": 3,
        "topics": ["3.2", "1.2"],
        "skills": ["maths", "technical"],
        "summary": "Calculate the required motor rotational speed in rpm for the nut to climb the thread at 0.08 m/s.",
        "prompt": "Analysing the data in Fig. 1.2 (screw thread \\(8\\text{ mm}\\) pitch, motor sprockets \\(20\\) teeth, nut sprockets \\(30\\) teeth), calculate the motor rotational speed required in revolutions per minute (rpm) to cause the nut to climb up the thread at a speed of \\(0.08\\text{ m s}^{-1}\\). Show your working. [3]",
        "figures": ["img/2019-summer-01/fig-1-2.jpg"],
        "image": "img/2019-summer-01/q1bii.jpg",
        "markscheme": "img/2019-summer-01/ms-1bii.jpg",
        "markscheme_text": "<b>Award three marks as follows:</b><br>• In 1 second, nut linear travel \\(= 0.08\\text{ m} = 80\\text{ mm}\\). Nut rev/s \\(= \\frac{80\\text{ mm}}{8\\text{ mm pitch}} = 10\\text{ rev/s}\\) (1)<br>• Sprocket gear ratio \\(= \\frac{\\text{driven}}{\\text{driver}} = \\frac{30}{20} = 1.5\\). Motor rev/s \\(= 10 \\times 1.5 = 15\\text{ rev/s}\\) (1)<br>• Convert to rpm: \\(15 \\times 60 = 900\\text{ rpm}\\) (1)<br><i>(OR: Nut rpm \\(= 10 \\times 60 = 600\\text{ rpm}\\); Motor rpm \\(= 600 \\times 1.5 = 900\\text{ rpm}\\))</i>"
    },
    {
        "id": "2019-summer-01-q1biii",
        "paper": "2019-summer-01",
        "question": "1(b)(iii)",
        "marks": 2,
        "page": 4,
        "topics": ["3.2"],
        "skills": ["technical"],
        "summary": "Give two reasons why a double chain drive is used in this home lift application.",
        "prompt": "Give <b>two</b> reasons why a double chain drive is used in this application. [2]",
        "figures": ["img/2019-summer-01/fig-1-2.jpg"],
        "image": "img/2019-summer-01/q1biii.jpg",
        "markscheme": "img/2019-summer-01/ms-1biii.jpg",
        "markscheme_text": "<b>One mark for each of two valid reasons (max 2 marks):</b><br>• Redundancy / safety: if one chain breaks, the second chain continues to hold and drive the carriage, preventing system failure (1)<br>• Load distribution: splitting the drive torque across two chains halves the tension in each link (1)<br>• Compactness: allows two narrower chains instead of one bulky single chain, reducing required motor enclosure depth (1)<br>• Positive non-slip drive: roller chains cannot slip under peak starting inertia unlike friction belt drives (1)"
    },
    {
        "id": "2019-summer-01-q1biv",
        "paper": "2019-summer-01",
        "question": "1(b)(iv)",
        "marks": 3,
        "page": 4,
        "topics": ["3.2", "1.2"],
        "skills": ["maths", "technical"],
        "summary": "Calculate the power required in watts to raise a 350 kg lift at 0.08 m/s.",
        "prompt": "The maximum total mass of the lift and occupants is \\(350\\text{ kg}\\).<br><br>Calculate the power required in watts (W) to raise the \\(350\\text{ kg}\\) lift at a velocity of \\(0.08\\text{ m s}^{-1}\\). Show your working.<br><br>\\(\\text{gravitational potential energy} = mgh\\)<br>\\(\\text{power} = \\frac{E}{t}\\)<br>\\(\\text{gravitational field strength, } g = 9.81\\text{ N kg}^{-1}\\) [3]",
        "figures": [],
        "image": "img/2019-summer-01/q1biv.jpg",
        "markscheme": "img/2019-summer-01/ms-1biv.jpg",
        "markscheme_text": "<b>Award three marks as follows:</b><br>• Method 1: In \\(t = 1\\text{ s}\\), lift rises \\(h = 0.08\\text{ m}\\) (1)<br>  \\(E = mgh = 350 \\times 9.81 \\times 0.08 = 274.68\\text{ J}\\) (1)<br>  \\(P = \\frac{E}{t} = \\frac{274.68}{1} = 274.68\\text{ W}\\) (allow \\(275\\text{ W}\\)) (1)<br>• Method 2: \\(F = mg = 350 \\times 9.81 = 3433.5\\text{ N}\\) (1)<br>  \\(P = F \\times v = 3433.5 \\times 0.08 = 274.68\\text{ W}\\) (2)"
    },
    {
        "id": "2019-summer-01-q1bv",
        "paper": "2019-summer-01",
        "question": "1(b)(v)",
        "marks": 4,
        "page": 4,
        "topics": ["3.2"],
        "skills": ["technical", "design"],
        "summary": "Explain one advantage and one disadvantage of using a screw thread and nut mechanism in a lift.",
        "prompt": "Conventional lifts usually use a cable mechanism with an electric motor located at the top of the lift shaft.<br><br>Explain <b>one</b> advantage and <b>one</b> disadvantage of using a screw thread and nut mechanism in a lift. [4]",
        "figures": [],
        "image": "img/2019-summer-01/q1bv.jpg",
        "markscheme": "img/2019-summer-01/ms-1bv.jpg",
        "markscheme_text": "<b>Up to 2 marks for explaining an advantage (1 mark for point, 1 mark for application context):</b><br>• Self-locking: the high friction inherent in screw threads prevents back-driving, meaning the carriage cannot free-fall even if motor power or brakes fail (2)<br>• No overhead motor room: the mechanism mounts behind or underneath the car, eliminating the need for rooftop machinery housings (2)<br>• No cable stretch: leadscrew drive maintains precise floor levelling over years without cable stretch adjustment (2)<br><br><b>Up to 2 marks for explaining a disadvantage:</b><br>• Low efficiency / speed: substantial sliding friction between nut and thread requires more motor energy and limits ascent speed (2)<br>• High maintenance lubrication: screw thread requires regular grease maintenance to prevent excessive friction, wear, and noise (2)<br>• Limited travel height: long screws are susceptible to buckling and whipping at high rotation, limiting maximum floor heights (2)"
    },
    {
        "id": "2019-summer-01-q1c",
        "paper": "2019-summer-01",
        "question": "1(c)",
        "marks": 8,
        "page": 5,
        "topics": ["2.1", "2.3"],
        "skills": ["design"],
        "summary": "Discuss, using examples, the significance of good user interface design in engineered products.",
        "prompt": "Discuss, using examples, the significance of good user interface design in engineered products. [8]",
        "figures": [],
        "image": "img/2019-summer-01/q1c.jpg",
        "markscheme": "img/2019-summer-01/ms-1c.jpg",
        "markscheme_text": "<b>Level 3 (6-8 marks):</b> Clear, thorough understanding of UI significance in engineered products (i.e. good UI simplifies complex interactions). Well-structured line of reasoning with relevant, substantiated physical and software UI examples.<br><b>Level 2 (3-5 marks):</b> Sound understanding of UI significance, recognising what UI accomplishes in specific products, with some structure.<br><b>Level 1 (1-2 marks):</b> Basic descriptive knowledge with limited examples or evaluation.<br><br><b>Indicative Content:</b><br>• Physical UI: Button sizing, grouping, tactile feedback, color-coding (e.g. red emergency stop), anthropometric sizing for diverse users.<br>• Software UI: Menu hierarchy, clear visual feedback, confirmation dialogs for critical actions, high contrast displays.<br>• Usability & Safety: Preventing operator error in safety-critical devices (medical equipment, vehicles); reducing cognitive workload; intuitive operation without dense training manuals.<br>• Commercial impact: Enhanced brand reputation, user satisfaction, and reduced customer support costs."
    },
    {
        "id": "2019-summer-01-q2a",
        "paper": "2019-summer-01",
        "question": "2(a)",
        "marks": 3,
        "page": 6,
        "topics": ["1.2"],
        "skills": ["maths"],
        "summary": "Calculate the maximum straight part length which can be shipped in a 305 x 215 x 100 mm box.",
        "prompt": "A manufacturer wishes to ship items in the cardboard box shown in Fig. 2.1. The cardboard box is a cuboid shape.<br><br>The box has internal dimensions of \\(305 \\times 215 \\times 100\\text{ mm}\\).<br><br>Calculate the maximum straight part length which can be shipped in this cardboard box. Give your answer in mm to 1 decimal place and show your working. [3]",
        "figures": ["img/2019-summer-01/fig-2-1.jpg"],
        "image": "img/2019-summer-01/q2a.jpg",
        "markscheme": "img/2019-summer-01/ms-2a.jpg",
        "markscheme_text": "<b>Award three marks as follows:</b><br>• Base diagonal: \\(D_1^2 = 305^2 + 215^2 = 93025 + 46225 = 139250\\text{ mm}^2\\) (1)<br>• 3D Space diagonal: \\(D_2^2 = D_1^2 + 100^2 = 139250 + 10000 = 149250\\text{ mm}^2\\) (1)<br>• Maximum straight length: \\(D_2 = \\sqrt{149250} = 386.3\\text{ mm}\\) (1)"
    },
    {
        "id": "2019-summer-01-q2bi",
        "paper": "2019-summer-01",
        "question": "2(b)(i)",
        "marks": 1,
        "page": 7,
        "topics": ["4.1"],
        "skills": ["technical", "practical"],
        "summary": "Name an instrument which could be used to measure the diameter of the brass part to a precision of 0.02 mm.",
        "prompt": "Fig. 2.2 shows an orthographic (two-dimensional) diagram of a part manufactured from brass. Dimensions are given in mm.<br><br>Name an instrument which could be used to measure the diameter of the part shown in Fig. 2.2 to a precision of \\(0.02\\text{ mm}\\). [1]",
        "figures": ["img/2019-summer-01/fig-2-2.jpg"],
        "image": "img/2019-summer-01/q2bi.jpg",
        "markscheme": "img/2019-summer-01/ms-2bi.jpg",
        "markscheme_text": "<b>One mark for naming a suitable precision instrument (1 mark):</b><br>• Vernier caliper (1)<br>• Digital caliper / Electronic caliper (1)<br>• Micrometer (1)"
    },
    {
        "id": "2019-summer-01-q2bii",
        "paper": "2019-summer-01",
        "question": "2(b)(ii)",
        "marks": 5,
        "page": 7,
        "topics": ["1.2", "4.1"],
        "skills": ["maths", "technical"],
        "summary": "Calculate the mass in grams of the turned brass part (cylinder plus cone).",
        "prompt": "Calculate the mass in grams (g) of the part shown in Fig. 2.2. Give your answer to 1 decimal place and show your working.<br><br>\\(\\text{Area of a circle} = \\frac{\\pi d^2}{4}\\)<br>\\(\\text{Volume of a cone} = \\frac{1}{3} \\times \\text{base area} \\times \\text{height}\\)<br>\\(\\text{Density of brass} = 8.73\\text{ g cm}^{-3}\\) [5]",
        "figures": ["img/2019-summer-01/fig-2-2.jpg"],
        "image": "img/2019-summer-01/q2bii.jpg",
        "markscheme": "img/2019-summer-01/ms-2bii.jpg",
        "markscheme_text": "<b>Award five marks as follows:</b><br>• Cone volume: \\(V_{\\text{cone}} = \\frac{1}{3} \\times \\frac{\\pi \\times 26^2}{4} \\times 20 = 3539.53\\text{ mm}^3\\) (1)<br>• Cylinder volume: \\(V_{\\text{cyl}} = \\frac{\\pi \\times 26^2}{4} \\times 15 = 7963.94\\text{ mm}^3\\) (1)<br>• Total volume: \\(V = 7963.94 + 3539.53 = 11503.47\\text{ mm}^3\\) (1)<br>• Volume conversion to cm³: \\(\\frac{11503.47}{1000} = 11.5035\\text{ cm}^3\\) (1)<br>• Mass calculation: \\(\\text{Mass} = 11.5035 \\times 8.73 = 100.425\\text{ g} = 100.4\\text{ g}\\) (1)"
    },
    {
        "id": "2019-summer-01-q2biii",
        "paper": "2019-summer-01",
        "question": "2(b)(iii)",
        "marks": 2,
        "page": 8,
        "topics": ["5.1", "1.2"],
        "skills": ["maths", "technical"],
        "summary": "Calculate the volume in mm³ of waste brass generated when turning the part from bar stock.",
        "prompt": "The part in Fig. 2.2 is to be turned on a centre lathe from a cylindrical brass bar with diameter \\(30\\text{ mm}\\) and length \\(35\\text{ mm}\\).<br><br>Calculate the volume in \\(\\text{mm}^3\\) of the waste brass generated. Give your answer to 1 decimal place and show your working. [2]",
        "figures": ["img/2019-summer-01/fig-2-2.jpg"],
        "image": "img/2019-summer-01/q2biii.jpg",
        "markscheme": "img/2019-summer-01/ms-2biii.jpg",
        "markscheme_text": "<b>Award two marks as follows:</b><br>• Original bar volume: \\(V_{\\text{bar}} = \\frac{\\pi \\times 30^2}{4} \\times 35 = 24740.04\\text{ mm}^3\\) (1)<br>• Waste volume \\(= V_{\\text{bar}} - V_{\\text{part}} = 24740.04 - 11503.47 = 13236.5\\text{ mm}^3\\) (1) (allow ECF from 2(b)(ii))"
    },
    {
        "id": "2019-summer-01-q2biv",
        "paper": "2019-summer-01",
        "question": "2(b)(iv)",
        "marks": 2,
        "page": 8,
        "topics": ["1.2", "4.1"],
        "skills": ["maths", "technical"],
        "summary": "Calculate the minimum allowable diameter for 26.00 mm with a tolerance of ±2%.",
        "prompt": "The diameter of the part must be \\(26.00\\text{ mm}\\) with a tolerance of \\(\\pm 2\\%\\).<br><br>Calculate the <b>minimum</b> allowable diameter in mm of the part. Show your working. [2]",
        "figures": ["img/2019-summer-01/fig-2-2.jpg"],
        "image": "img/2019-summer-01/q2biv.jpg",
        "markscheme": "img/2019-summer-01/ms-2biv.jpg",
        "markscheme_text": "<b>Award two marks as follows:</b><br>• Tolerance calculation: \\(26.00 \\times 0.02 = 0.52\\text{ mm}\\) (1)<br>• Minimum diameter: \\(26.00 - 0.52 = 25.48\\text{ mm}\\) (1)"
    },
    {
        "id": "2019-summer-01-q2c",
        "paper": "2019-summer-01",
        "question": "2(c)",
        "marks": 2,
        "page": 9,
        "topics": ["1.2"],
        "skills": ["maths"],
        "summary": "Calculate the initial velocity for a tennis ball to reach 2.5 m vertically using v² = u² + 2as.",
        "prompt": "A machine is being developed to help tennis players practise their serve. The machine projects a tennis ball vertically to a height, \\(s\\), of \\(2.5\\text{ m}\\).<br><br>Use the formula, \\(v^2 = u^2 + 2as\\), to calculate the initial velocity, \\(u\\), at which the ball needs to leave the machine so that it just reaches the required height of \\(2.5\\text{ m}\\). Give your answer in \\(\\text{m s}^{-1}\\) and show your working.<br><br>Acceleration, \\(a\\), due to gravity in this situation is \\(-9.81\\text{ m s}^{-2}\\) [2]",
        "figures": [],
        "image": "img/2019-summer-01/q2c.jpg",
        "markscheme": "img/2019-summer-01/ms-2c.jpg",
        "markscheme_text": "<b>Award two marks as follows:</b><br>• Stating that final vertical velocity at peak height is zero: \\(v = 0\\) (1)<br>• Substituting and solving: \\(0 = u^2 + 2(-9.81)(2.5) \\implies u^2 = 49.05 \\implies u = \\sqrt{49.05} = 7.0\\text{ m s}^{-1}\\) (1)"
    },
    {
        "id": "2019-summer-01-q3a",
        "paper": "2019-summer-01",
        "question": "3(a)",
        "marks": 8,
        "page": 10,
        "topics": ["1.1", "2.3"],
        "skills": ["design", "technical"],
        "summary": "Discuss the implications to manufacturers of producing BSI Kitemark approved products.",
        "prompt": "To certify that products conform to a standard set by the British Standards Institute (BSI), many products carry the BSI Kitemark® shown in Fig. 3.<br><br>Discuss the implications to manufacturers of producing Kitemark® approved products. [8]",
        "figures": ["img/2019-summer-01/fig-3.jpg"],
        "image": "img/2019-summer-01/q3a.jpg",
        "markscheme": "img/2019-summer-01/ms-3a.jpg",
        "markscheme_text": "<b>Level 3 (6-8 marks):</b> Thorough, balanced discussion of the implications to manufacturers of producing Kitemark approved products, examining both benefits and drawbacks/costs.<br><b>Level 2 (3-5 marks):</b> Sound understanding with reasonable discussion covering one or two key implications.<br><b>Level 1 (1-2 marks):</b> Basic descriptive knowledge of kitemarked products without evaluating implications for the manufacturer.<br><br><b>Indicative Content:</b><br>• Commercial advantages: Differentiates products in competitive markets; builds consumer trust; commands higher price points; unlocks commercial tenders requiring compliance.<br>• Legal & Risk benefits: Demonstrates due diligence, reducing liability risk and customer litigation in product liability claims.<br>• Financial costs: High cost of purchasing BSI standard documents; annual fees for licensing the mark; recurring costs for third-party auditing and sample batch destructive testing.<br>• Manufacturing & Design impacts: Limits design flexibility to prescribed standard geometries; necessitates stringent quality control (SPC) and traceable calibration on the production line."
    },
    {
        "id": "2019-summer-01-q3bi",
        "paper": "2019-summer-01",
        "question": "3(b)(i)",
        "marks": 2,
        "page": 11,
        "topics": ["2.3"],
        "skills": ["design"],
        "summary": "Explain what is meant by 'enterprise' in the context of designing.",
        "prompt": "Explain what is meant by ‘enterprise’ in the context of designing. [2]",
        "figures": [],
        "image": "img/2019-summer-01/q3bi.jpg",
        "markscheme": "img/2019-summer-01/ms-3bi.jpg",
        "markscheme_text": "<b>Award two marks as follows:</b><br>• One mark for understanding enterprise: bold decision making, initiative, willingness to take calculated commercial/financial risks (1)<br>• One mark for explaining in design context: capturing innovative opportunities, breaking new ground, creating commercial ventures from design ideas (1)"
    },
    {
        "id": "2019-summer-01-q3bii",
        "paper": "2019-summer-01",
        "question": "3(b)(ii)",
        "marks": 4,
        "page": 11,
        "topics": ["2.3"],
        "skills": ["design"],
        "summary": "Describe two ways in which enterprise can help drive the development of new product ideas.",
        "prompt": "Describe <b>two</b> ways in which enterprise can help drive the development of new product ideas. [4]",
        "figures": [],
        "image": "img/2019-summer-01/q3bii.jpg",
        "markscheme": "img/2019-summer-01/ms-3bii.jpg",
        "markscheme_text": "<b>Award up to 2 marks for each of two described ways (1 mark for mechanism, 1 mark for justification) (max 4 marks):</b><br>• Venture capital / Angel investment: Attracting external investors willing to fund speculative prototype development in exchange for equity (2)<br>• Crowdfunding platforms: Testing market viability directly with early adopters who pre-fund production tooling (2)<br>• Strategic commercial partnerships: Forging alliances with established manufacturers to access manufacturing technology and distribution channels (2)<br>• Open innovation and IP sharing: Collaborating with outside technology specialists to integrate advanced sensors or microcontrollers (2)"
    },
    {
        "id": "2019-summer-01-q4a",
        "paper": "2019-summer-01",
        "question": "4(a)",
        "marks": 2,
        "page": 12,
        "topics": ["3.3", "1.1"],
        "skills": ["technical"],
        "summary": "Identify two issues associated with providing power to the robotic lawnmower charging station.",
        "prompt": "Fig. 4.1 shows a robotic lawnmower.<br><br>A 12 V battery is used to power the robotic lawnmower. The robotic lawnmower returns to a charging station placed at the edge of the lawn to recharge its battery. The charging station requires a source of power.<br><br>Identify <b>two</b> issues associated with providing power to the charging station. [2]",
        "figures": ["img/2019-summer-01/fig-4-1.jpg"],
        "image": "img/2019-summer-01/q4a.jpg",
        "markscheme": "img/2019-summer-01/ms-4a.jpg",
        "markscheme_text": "<b>One mark for identifying each of two valid issues (max 2 marks):</b><br>• Weatherproofing: The charging station and power supply must be IP-rated against rain, humidity, and temperature extremes (1)<br>• Power cable safety: Cable running across the garden risks being cut by the lawnmower blade or damaged by animals/foot traffic (1)<br>• Distance to mains outlet: Lawns are often distant from external wall sockets, requiring long low-voltage DC cable runs (1)<br>• Safety regulations: Outdoor electrical supplies require RCD (Residual Current Device) protection to prevent electric shocks (1)"
    },
    {
        "id": "2019-summer-01-q4bi",
        "paper": "2019-summer-01",
        "question": "4(b)(i)",
        "marks": 2,
        "page": 13,
        "topics": ["4.2", "5.1"],
        "skills": ["technical", "design"],
        "summary": "Describe how rigidity of the polymer part in Fig. 4.2a and 4.2b is achieved through effective design.",
        "prompt": "The case of the robotic lawnmower is made from a thermo softening polymer.<br><br>Fig. 4.2a and Fig. 4.2b show two views of a typical thermo softening polymer part from a similar garden product.<br><br>Describe how the rigidity of the thermo softening polymer part in Fig. 4.2a and Fig. 4.2b is achieved through effective designing. [2]",
        "figures": ["img/2019-summer-01/fig-4-2.jpg"],
        "image": "img/2019-summer-01/q4bi.jpg",
        "markscheme": "img/2019-summer-01/ms-4bi.jpg",
        "markscheme_text": "<b>Award two marks as follows:</b><br>• 1 mark for identifying reinforcing ribs / webs molded into the internal structure (1)<br>• 1 mark for explaining that ribs increase the second moment of area, provide structural triangulation, and prevent deflection without increasing overall wall thickness (1)"
    },
    {
        "id": "2019-summer-01-q4bii",
        "paper": "2019-summer-01",
        "question": "4(b)(ii)",
        "marks": 2,
        "page": 13,
        "topics": ["5.1"],
        "skills": ["technical", "practical"],
        "summary": "State the manufacturing method for the polymer part and identify one piece of evidence from the images.",
        "prompt": "State the industrial method used to manufacture the thermo softening polymer part and identify <b>one</b> piece of evidence from either Fig. 4.2a or Fig. 4.2b that leads you to this conclusion. [2]",
        "figures": ["img/2019-summer-01/fig-4-2.jpg"],
        "image": "img/2019-summer-01/q4bii.jpg",
        "markscheme": "img/2019-summer-01/ms-4bii.jpg",
        "markscheme_text": "<b>Award two marks as follows:</b><br>• 1 mark for stating: Injection moulding (1)<br>• 1 mark for identifying evidence: Circular ejector pin witness marks; thin uniform wall sections; complex integrated 3D ribs and bosses; embossed cavity date/material identification stamp (1)"
    },
    {
        "id": "2019-summer-01-q4biii",
        "paper": "2019-summer-01",
        "question": "4(b)(iii)",
        "marks": 2,
        "page": 14,
        "topics": ["1.1", "4.2"],
        "skills": ["technical"],
        "summary": "Explain one reason why a plastic manufacturer marks the product with >PP<.",
        "prompt": "The >PP< marking that is visible on the surface of the product in Fig. 4.2b identifies the type of thermo softening polymer that has been used.<br><br>Explain <b>one</b> reason why a plastic manufacturer marks the type of plastic used on their product in this way. [2]",
        "figures": ["img/2019-summer-01/fig-4-2b.jpg"],
        "image": "img/2019-summer-01/q4biii.jpg",
        "markscheme": "img/2019-summer-01/ms-4biii.jpg",
        "markscheme_text": "<b>Award up to 2 marks (1 mark for reason, 1 mark for significance) (max 2 marks):</b><br>• Material identification for recycling: Visually identical polymers have different melt flow indices and cannot be blended; marking enables optical or manual sorting at recycling plants (2)<br>• Environmental legislation compliance: Satisfies End-of-Life Vehicles / WEEE directives requiring material traceability to keep plastics out of landfills (2)"
    },
    {
        "id": "2019-summer-01-q4c",
        "paper": "2019-summer-01",
        "question": "4(c)",
        "marks": 4,
        "page": 14,
        "topics": ["3.3"],
        "skills": ["technical"],
        "summary": "Compare the use of DC motors and stepper motors for driving the wheels of a robotic lawnmower.",
        "prompt": "Compare the use of DC motors and stepper motors for driving the wheels of a robotic lawnmower. [4]",
        "figures": [],
        "image": "img/2019-summer-01/q4c.jpg",
        "markscheme": "img/2019-summer-01/ms-4c.jpg",
        "markscheme_text": "<b>Award up to 4 marks (2 marks for DC motors, 2 marks for stepper motors, linked to lawnmower function):</b><br>• DC Motors: High continuous operating torque and efficiency to navigate inclines/rough grass; easy speed regulation using PWM; requires rotary encoders to track distance travelled (2)<br>• Stepper Motors: Delivers precise angular rotation allowing dead-reckoning navigation without encoders; high holding torque; however, draws constant current even when stalled (draining battery), has low high-speed torque, and requires more expensive stepper driver chips (2)"
    },
    {
        "id": "2019-summer-01-q4d",
        "paper": "2019-summer-01",
        "question": "4(d)",
        "marks": 4,
        "page": 15,
        "topics": ["3.1"],
        "skills": ["technical", "design"],
        "summary": "Complete the system diagram for the robotic lawnmower including inputs, microcontroller, and outputs.",
        "prompt": "The robotic lawnmower is controlled by an electronic system with a number of sensors, user-operated controls and outputs. The robotic lawnmower function is described below:<br>• The user sets the lawnmower to operate at a set time every day using buttons and a display.<br>• At the set time, the lawnmower automatically undocks from its charging station, starts its grass-cutting blade and begins to move across the lawn.<br>• A cable, buried around the edge of the lawn, carries an electronic signal which the lawnmower detects and uses to avoid running off the edge of the lawn.<br>• Proximity sensors on the lawnmower detect the presence of obstacles in the lawnmower's path so that they can be avoided.<br>• The lawnmower monitors its battery voltage and if the voltage falls below a set level the lawnmower returns to its charging station.<br><br>Use this function description to complete the system diagram for the robotic lawnmower. [4]",
        "figures": ["img/2019-summer-01/ms-4d-system-diagram.jpg"],
        "image": "img/2019-summer-01/q4d.jpg",
        "markscheme": "img/2019-summer-01/ms-4d.jpg",
        "markscheme_text": "<b>Award four marks as follows:</b><br>• Two marks for identifying two input subsystems: Edge-of-lawn cable detector, Proximity sensor, Battery voltage monitor (2)<br>• Two marks for identifying two output subsystems: Left drive motor, Right drive motor, Grass-cutting blade motor, Display (2)<br>• <i>(Deduct 1 mark if signal flow arrows or block diagram conventions are missing)</i>"
    },
    {
        "id": "2019-summer-01-q4ei",
        "paper": "2019-summer-01",
        "question": "4(e)(i)",
        "marks": 3,
        "page": 16,
        "topics": ["3.3", "1.2"],
        "skills": ["maths", "technical"],
        "summary": "Calculate the voltage at point VA when the battery voltage is 10.5 V in the potential divider.",
        "prompt": "Fig. 4.3 shows a circuit diagram for the part of the robotic lawnmower which monitors the battery voltage.<br><br>The lithium ion battery produces a nominal voltage of \\(11.1\\text{ V}\\). When the battery voltage drops to \\(10.5\\text{ V}\\) an alert is generated within the microcontroller code and the robotic lawnmower returns to its charging station.<br><br>Calculate the voltage (V) at point \\(V_A\\) in Fig. 4.3 when the battery voltage is \\(10.5\\text{ V}\\). Give your answer to 2 decimal places and show your working. [3]",
        "figures": ["img/2019-summer-01/fig-4-3.jpg"],
        "image": "img/2019-summer-01/q4ei.jpg",
        "markscheme": "img/2019-summer-01/ms-4ei.jpg",
        "markscheme_text": "<b>Award three marks as follows:</b><br>• Potential divider formula / Ohm's law: \\(V_A = V_{\\text{in}} \\times \\frac{R_2}{R_1 + R_2}\\) (1)<br>• Substitution: \\(V_A = 10.5 \\times \\frac{1.8}{3.9 + 1.8} = 10.5 \\times \\frac{1.8}{5.7}\\) (1)<br>• Calculation: \\(V_A = 3.3158\\text{ V} = 3.32\\text{ V}\\) (to 2 d.p.) (1)"
    },
    {
        "id": "2019-summer-01-q4eii",
        "paper": "2019-summer-01",
        "question": "4(e)(ii)",
        "marks": 3,
        "page": 17,
        "topics": ["3.3", "1.2"],
        "skills": ["maths", "technical"],
        "summary": "Calculate the 10-bit ADC value produced when the input voltage VA is 3.32 V.",
        "prompt": "Voltage \\(V_A\\) in Fig. 4.3 is fed into an analogue to digital converter (ADC) pin on the microcontroller. The ADC produces a full-scale value of 1023 when the analogue input is \\(5.0\\text{ V}\\).<br><br>Calculate the ADC value produced when the input voltage \\(V_A\\) is at the value you calculated in part (e)(i) (\\(3.32\\text{ V}\\)). Give your answer as a rounded-down integer and show your working. [3]",
        "figures": ["img/2019-summer-01/fig-4-3.jpg"],
        "image": "img/2019-summer-01/q4eii.jpg",
        "markscheme": "img/2019-summer-01/ms-4eii.jpg",
        "markscheme_text": "<b>Award three marks as follows:</b><br>• Voltage fraction: \\(\\frac{3.32}{5.0} = 0.664\\) (1)<br>• ADC scaling: \\(0.664 \\times 1023 = 679.272\\) (1)<br>• Rounded-down integer: \\(\\text{ADC output} = 679\\) (1)"
    },
    {
        "id": "2019-summer-01-q4eiii",
        "paper": "2019-summer-01",
        "question": "4(e)(iii)",
        "marks": 3,
        "page": 18,
        "topics": ["3.3"],
        "skills": ["technical", "design"],
        "summary": "Draw a flowchart of the robotic lawnmower subroutine to check battery voltage and generate an alert.",
        "prompt": "Draw a flowchart of the robotic lawnmower subroutine to check the battery voltage and generate an alert if the battery voltage falls below \\(10.5\\text{ V}\\) (ADC value \\(< 679\\)). [3]",
        "figures": ["img/2019-summer-01/ms-4eiii-flowchart.jpg"],
        "image": "img/2019-summer-01/q4eiii.jpg",
        "markscheme": "img/2019-summer-01/ms-4eiii.jpg",
        "markscheme_text": "<b>Award three marks as follows:</b><br>• Correct input symbol (parallelogram) to read battery voltage ADC value (1)<br>• Correct decision symbol (diamond) checking 'Is ADC < 679?' (1)<br>• Correct process branch: 'Yes' triggers 'Generate an alert' and both branches cleanly route to End Subroutine (1)"
    }
]

# Verify marks
total_m = sum(q['marks'] for q in new_questions)
print(f'New questions count: {len(new_questions)}, Total marks: {total_m}')
assert total_m == 80, f'Expected 80 marks, got {total_m}'

db['questions'].extend(new_questions)

with open(questions_file, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print('Successfully saved questions.json!')

# Add Quiz questions
with open(quiz_file, 'r', encoding='utf-8-sig') as f:
    quiz_data = json.load(f)

new_quizzes = [
    {
        "id": "quiz-2019-p1-stress",
        "topic": "1.2",
        "question": "What is the formula used to calculate direct mechanical stress (σ) in a loaded component?",
        "options": [
            "Stress = Force / Cross-sectional Area",
            "Stress = Force × Distance",
            "Stress = Strain / Original Length",
            "Stress = Mass × Acceleration"
        ],
        "answer": 0,
        "explanation": "Direct stress is defined as force per unit cross-sectional area: σ = F / A (measured in N/m² or Pa)."
    },
    {
        "id": "quiz-2019-p1-plastic-marking",
        "topic": "4.2",
        "question": "What polymer is denoted by the resin identification symbol '>PP<' on a moulded plastic part?",
        "options": [
            "Polypropylene",
            "Polyethylene",
            "Polycarbonate",
            "Polystyrene"
        ],
        "answer": 0,
        "explanation": "PP stands for Polypropylene, a flexible, fatigue-resistant thermo softening polymer widely used in garden equipment and living hinges."
    },
    {
        "id": "quiz-2019-p1-vernier",
        "topic": "4.1",
        "question": "Which measuring tool is standardly designed to measure outer diameters to a precision of 0.02 mm?",
        "options": [
            "Vernier / Digital Caliper",
            "Steel Rule",
            "Dial Test Indicator (DTI)",
            "Feeler Gauge"
        ],
        "answer": 0,
        "explanation": "A standard vernier or digital caliper offers external jaw resolution down to 0.02 mm (or 0.01 mm for digital displays)."
    },
    {
        "id": "quiz-2019-p1-ribbing",
        "topic": "5.1",
        "question": "Why do engineers incorporate internal ribs and webs into thin-walled injection moulded casings?",
        "options": [
            "To increase structural rigidity without increasing wall thickness",
            "To speed up raw molten plastic flow into the mould cavity",
            "To act as internal conduit channels for electrical wiring",
            "To decrease thermal conductivity through the polymer"
        ],
        "answer": 0,
        "explanation": "Ribs increase the section modulus and second moment of area, delivering high torsional and bending stiffness while preventing sink marks that occur with thick walls."
    }
]

existing_quiz_ids = {q['id'] for q in quiz_data}
for qz in new_quizzes:
    if qz['id'] not in existing_quiz_ids:
        quiz_data.append(qz)

with open(quiz_file, 'w', encoding='utf-8') as f:
    json.dump(quiz_data, f, indent=2, ensure_ascii=False)

print('Successfully saved quiz_questions.json!')
