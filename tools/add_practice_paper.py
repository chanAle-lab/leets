# add_practice_paper.py
import json

new_paper = {
    'id': '2018-practice-01',
    'code': 'H404/01',
    'unit': 'Principles of Design Engineering',
    'year': 2018,
    'level': 'H404',
    'totalMarks': 80,
    'series': 'Practice Set 1'
}

new_questions = [
    # Question 1
    {
        'id': '2018-practice-01-q1a',
        'paper': '2018-practice-01',
        'question': '1(a)',
        'marks': 2,
        'page': 2,
        'topics': ['1.1', '2.2'],
        'skills': ['design'],
        'summary': 'Identify two reasons why using a handheld gimbal with mobile phones has recently increased in popularity.',
        'prompt': 'Fig. 1.1 shows a mobile phone in a handheld gimbal, a device that uses a set of motors and sensors to keep the phone steady, so that smooth video shots can be recorded.<br><br>Identify <b>two</b> reasons why using a handheld gimbal with mobile phones has recently increased in popularity. [2]',
        'figures': ['img/2018-practice-01/fig-1-1.jpg'],
        'image': 'img/2018-practice-01/q1a.jpg',
        'markscheme': 'img/2018-practice-01/ms-1a.jpg',
        'markscheme_text': '<b>One mark for identifying each of two reasons why using a handheld gimbal with mobile phones has recently increased in popularity (max 2 marks):</b><br>• Social media increasingly encourages people to post personal videos (1)<br>• The cost of gimbals is steadily reducing (1)<br>• The improving technology is making gimbals lighter and more portable (1)<br>• Users like the quality of the videos that can be shot (1)<br>• Any other valid suggestion.'
    },
    {
        'id': '2018-practice-01-q1b',
        'paper': '2018-practice-01',
        'question': '1(b)',
        'marks': 3,
        'page': 2,
        'topics': ['1.2', '8.3'],
        'skills': ['design'],
        'summary': 'Identify three issues a design engineering company would investigate before investing in developing a new handheld gimbal.',
        'prompt': 'A design engineering company is considering whether to invest in developing a new handheld gimbal for use with mobile phones.<br><br>Identify <b>three</b> issues the company would need to investigate before deciding whether to proceed. [3]',
        'figures': ['img/2018-practice-01/fig-1-1.jpg'],
        'image': 'img/2018-practice-01/q1b.jpg',
        'markscheme': 'img/2018-practice-01/ms-1b.jpg',
        'markscheme_text': '<b>One mark for identifying each of three issues the company would need to investigate before deciding whether to proceed (max 3 marks):</b><br>• Analysis of the environment in which the product may be used (1)<br>• User requirements / stakeholder needs (1)<br>• Types and sizes of phones / cameras (1)<br>• Economic / market considerations (1)<br>• Existing product / SWOT analysis (1)<br>• Ways of raising capital (1)<br>• Technology available – motors / batteries etc. (1)<br>• Any other valid suggestion.'
    },
    {
        'id': '2018-practice-01-q1ci',
        'paper': '2018-practice-01',
        'question': '1(c)(i)',
        'marks': 6,
        'page': 3,
        'topics': ['6.4', '6.5'],
        'skills': ['technical', 'design'],
        'summary': 'Discuss possible limitations when using the 3-axis handheld gimbal control system.',
        'prompt': 'Fig. 1.2a shows an annotated diagram of the handheld gimbal control system (camera, handle, yaw motor, roll motor, pitch motor). Three motors are used to stabilise the camera in the three axes of pitch, roll and yaw as shown in Fig. 1.2b.<br><br>Sensors are located at specific points around the handheld gimbal. When the sensors detect movement of the camera in each of the three axes, the motors counteract that motion almost instantly. The system is controlled by a microcontroller.<br><br>The handheld gimbal can remove most, but not all, of the unwanted motion caused by the movements of the user’s hand.<br><br>Discuss possible limitations when using the handheld gimbal control system. [6]',
        'figures': ['img/2018-practice-01/fig-1-2.jpg'],
        'image': 'img/2018-practice-01/q1ci.jpg',
        'markscheme': 'img/2018-practice-01/ms-1ci.jpg',
        'markscheme_text': '<b>Level 3 (5–6 marks):</b> Clear understanding of the handheld gimbal control system. Thorough discussion explaining a number of limitations from multiple perspectives.<br><b>Level 2 (3–4 marks):</b> Reasonable understanding. Sound discussion explaining limitations resulting from system use.<br><b>Level 1 (1–2 marks):</b> Basic descriptive knowledge with little appreciation of limitations.<br><br><b>Indicative content:</b><br>• Control system may not be fast enough to respond to rapid hand movements, especially in filming faster motion.<br>• High-frequency vibration may be too fast for the system to respond to.<br>• Processing speed of microcontroller may be too slow to react to sudden movements, resulting in missed movements and erratic responses.<br>• Inertia of the mechanical system will slow down response time.<br>• Limited motor torque will slow response time and limit allowable size/weight of camera unit.<br>• Motors may not rotate full 360° (mechanical end stops limit travel).<br>• Non-rotational movements (linear translation along X, Y, or Z axis) will not be cancelled out.<br>• Total weight of phone mount, motors, and batteries causes fatigue for user.<br>• Any other valid suggestion.'
    },
    {
        'id': '2018-practice-01-q1cii',
        'paper': '2018-practice-01',
        'question': '1(c)(ii)',
        'marks': 3,
        'page': 4,
        'topics': ['6.4', '3.6'],
        'skills': ['maths', 'technical'],
        'summary': 'Calculate the angle through which the gimbal tilted based on potentiometer voltage change.',
        'prompt': 'Fig. 1.3 shows a prototype system for sensing the angle of tilt of an object. It consists of a pendulum, freely pivoted on a potentiometer (a variable resistor). Data for the potentiometer is given below:<br>• Full rotation angle: 300°<br>• Track resistance: 10 kΩ<br><br>The potentiometer is connected in the circuit shown in Fig. 1.4 (powered by 5 V DC across the 10 kΩ track).<br>When the gimbal is held horizontal to the ground, the potentiometer output voltage (V_out) is 2.50 V.<br>When the gimbal is tilted the V_out rises to 2.70 V.<br><br>Calculate the angle through which the gimbal has tilted. Show your working. [3]',
        'figures': ['img/2018-practice-01/fig-1-3.jpg', 'img/2018-practice-01/fig-1-4.jpg'],
        'image': 'img/2018-practice-01/q1cii.jpg',
        'markscheme': 'img/2018-practice-01/ms-1cii.jpg',
        'markscheme_text': '<b>Award 3 marks as follows:</b><br>• Increase in V_out: 2.70 V – 2.50 V = <b>0.20 V</b> (1 mark)<br>• Sensitivity / Volt per degree: 5 V / 300° = <b>0.0167 V/degree</b> (to 3 s.f.) (1 mark)<br>• Angle turned = 0.20 V / (5 / 300) = <b>12°</b> (Allow 11.9° to 12.1°) (1 mark)<br><i>(If correct answer 12° is given without working out shown, award full marks. ECF applies.)</i>'
    },
    {
        'id': '2018-practice-01-q1ciii',
        'paper': '2018-practice-01',
        'question': '1(c)(iii)',
        'marks': 2,
        'page': 5,
        'topics': ['6.4', '3.5'],
        'skills': ['technical'],
        'summary': 'Explain one reason why the sensor specification is suitable for use on the handheld gimbal.',
        'prompt': 'Data for the actual sensor used on the handheld gimbal is given below:<br>• Power supply: 1.8 to 3.6 V<br>• Power consumption: &lt; 1 mW<br>• Sensitivity: 0.005g<br><br>Explain <b>one</b> reason why this sensor is suitable for use on the handheld gimbal. [2]',
        'image': 'img/2018-practice-01/q1ciii.jpg',
        'markscheme': 'img/2018-practice-01/ms-1ciii.jpg',
        'markscheme_text': '<b>One mark for analysing the data in the table to identify a reason; one mark for explaining why it is suitable on the gimbal (2 marks):</b><br>• <b>Wide power supply range (1.8–3.6 V) (1):</b> will suit a variety of single-cell or multi-cell battery packs without needing complex voltage regulation (1).<br>• <b>Low power consumption (&lt; 1 mW) (1):</b> ensures the battery will last a long time during extended handheld filming sessions (1).<br>• <b>High sensitivity (0.005g) (1):</b> enables minute hand tremors and slight vibrations to be detected quickly and corrected (1).'
    },
    {
        'id': '2018-practice-01-q1di',
        'paper': '2018-practice-01',
        'question': '1(d)(i)',
        'marks': 2,
        'page': 5,
        'topics': ['5.2', '6.4'],
        'skills': ['technical'],
        'summary': 'Explain one reason why modern materials such as rare earth magnets are used in electric motors.',
        'prompt': 'Electric motors as used in the handheld gimbal often make use of modern materials such as rare earth magnets.<br><br>Explain <b>one</b> reason why modern materials are used in electric motors. [2]',
        'image': 'img/2018-practice-01/q1di.jpg',
        'markscheme': 'img/2018-practice-01/ms-1di.jpg',
        'markscheme_text': '<b>Up to 2 marks for explaining why modern materials are used in electric motors:</b><br>• Modern materials such as rare earth magnets have a very strong magnetic field / high flux density (1). This enables the motor to produce a high torque / be very compact and lightweight / be very powerful for its size (1).<br>• High-performance alloys enable the rotor to be lightweight (1), allowing the rotor to spin at higher speeds and respond rapidly with low rotational inertia (1).<br><i>(Do not accept smart material-based answers.)</i>'
    },
    {
        'id': '2018-practice-01-q1dii',
        'paper': '2018-practice-01',
        'question': '1(d)(ii)',
        'marks': 2,
        'page': 5,
        'topics': ['6.4', '6.2'],
        'skills': ['technical'],
        'summary': 'State one type of motor suitable for use in the handheld gimbal and explain why it would be used.',
        'prompt': 'State <b>one</b> type of motor that would be suitable for use in the handheld gimbal and explain why it would be used. [2]',
        'image': 'img/2018-practice-01/q1dii.jpg',
        'markscheme': 'img/2018-practice-01/ms-1dii.jpg',
        'markscheme_text': '<b>One mark for identifying a suitable motor; one mark for explaining why it would be suitable (2 marks):</b><br>• <b>Brushless DC motor (BLDC) (1):</b> High torque-to-weight ratio, high efficiency, can hold fine angular positions smoothly without brush friction, and very quiet in operation (1).<br>• <b>Servo motor (1):</b> Rotates to a given commanded angular position then holds, provides fast response and high closed-loop torque (1).<br>• <b>Stepper motor (1):</b> Rotates through precise discrete step angles per pulse, provides high holding torque without slip (1).'
    },
    {
        'id': '2018-practice-01-q1diii',
        'paper': '2018-practice-01',
        'question': '1(d)(iii)',
        'marks': 4,
        'page': 6,
        'topics': ['6.4', '6.5'],
        'skills': ['technical', 'practical'],
        'summary': 'Explain using sketches and/or notes how the motor identified in part (ii) could be controlled.',
        'prompt': 'Explain, using sketches and/or notes, how the motor you identified in part (ii) could be controlled.<br><br>You should:<br>• identify the signals required for the motor to operate correctly;<br>• explain how these signals affect the direction, speed and position of the motor. [4]',
        'figures': ['img/2018-practice-01/ms-1diii-diagram.jpg'],
        'image': 'img/2018-practice-01/q1diii.jpg',
        'markscheme': 'img/2018-practice-01/ms-1diii.jpg',
        'markscheme_text': '<b>Award 4 marks as follows:</b><br>• <b>Signals required (1 mark):</b> Identifies connection wires and control signal (e.g. Servo: 3 wires — Red +V, Black 0V, White PWM pulse signal; Brushless/Stepper: multi-phase driver connections).<br>• <b>Direction of motor (1 mark):</b> Explains how signals affect direction (e.g. Servo: pulse width compared to center 1.5ms pulse determines clockwise/counter-clockwise travel; Brushless/Stepper: sequence of phase excitation determines forward or reverse direction).<br>• <b>Speed of motor (1 mark):</b> Explains how signals affect speed (e.g. Servo: rate of pulse width change / gearing; Brushless/Stepper: pulse frequency / commutation switching rate controls rotational velocity).<br>• <b>Position of motor (1 mark):</b> Explains how signals affect position (e.g. Servo: duty cycle pulse width 1.0ms–2.0ms maps proportionally to 0°–180° angular position; Stepper: total number of step pulses determines final angular displacement).'
    },

    # Question 2
    {
        'id': '2018-practice-01-q2a',
        'paper': '2018-practice-01',
        'question': '2(a)',
        'marks': 3,
        'page': 7,
        'topics': ['4.1'],
        'skills': ['technical', 'design'],
        'summary': 'Draw on a 10mm grid an accurate 2D elevation of an isometric part with hidden detail lines.',
        'prompt': 'Fig. 2.1 shows a 3-dimensional isometric projection of a part (overall dimensions 60 mm × 60 mm × 40 mm with 20 mm uprights, a 10 mm thick baseplate, and a Ø20 mm hole centred in the baseplate).<br><br>Draw, on a 10 mm grid, an accurate 2-dimensional elevation of the part from direction <b>A</b>. Indicate any hidden lines. [3]',
        'figures': ['img/2018-practice-01/fig-2-1.jpg', 'img/2018-practice-01/ms-2a-diagram.jpg'],
        'image': 'img/2018-practice-01/q2a.jpg',
        'markscheme': 'img/2018-practice-01/ms-2a.jpg',
        'markscheme_text': '<b>Award 3 marks as follows:</b><br>• One mark for analysing Fig. 2.1 to correctly outline the U-shape (1 mark).<br>• One mark for correct dimensions on grid paper (60 mm wide, 40 mm high uprights, 20 mm wide upright columns, 10 mm high baseplate) (1 mark).<br>• One mark for correct hidden detail lines representing the Ø20 mm hole and baseplate recess (dashed lines) (1 mark).'
    },
    {
        'id': '2018-practice-01-q2b',
        'paper': '2018-practice-01',
        'question': '2(b)',
        'marks': 3,
        'page': 8,
        'topics': ['6.1', '3.6'],
        'skills': ['maths', 'technical'],
        'summary': 'Calculate the horizontal spread length S of a camera tripod leg using trigonometry.',
        'prompt': 'Fig. 2.2a shows one leg of a camera tripod. Fig. 2.2b shows the right-angled triangle formed by one leg of the tripod (hypotenuse leg length = 385 mm, apex angle = 27°, base side = S).<br><br>Using the information from Fig. 2.2b, calculate the length of <b>S</b> correct to the nearest mm. Show your working. [3]',
        'figures': ['img/2018-practice-01/fig-2-2.jpg'],
        'image': 'img/2018-practice-01/q2b.jpg',
        'markscheme': 'img/2018-practice-01/ms-2b.jpg',
        'markscheme_text': '<b>Award 3 marks as follows:</b><br>• Apply trigonometry formula: sin(27°) = S / 385 (1 mark)<br>• Manipulate formula: S = 385 × sin(27°) = 174.79 mm (1 mark)<br>• Round answer to nearest mm: S = <b>175 mm</b> (1 mark)<br><i>(Full marks if correct answer 175 mm is given without working. Working must be shown for partial credit.)</i>'
    },
    {
        'id': '2018-practice-01-q2ci',
        'paper': '2018-practice-01',
        'question': '2(c)(i)',
        'marks': 2,
        'page': 9,
        'topics': ['6.2', '6.3'],
        'skills': ['maths', 'technical'],
        'summary': 'Calculate the tensile force F exerted on a bicycle brake cable from a 25 N lever force.',
        'prompt': 'Fig. 2.3 shows a bicycle brake lever. The rider exerts a 25 N force at an 85 mm lever distance from the fulcrum. The brake cable is attached at 40 mm from the fulcrum.<br><br>Using the information from Fig. 2.3, calculate the tensile force <b>F</b> exerted on the cable when the rider exerts a 25 N force at the end of the brake lever. Show your working. [2]',
        'figures': ['img/2018-practice-01/fig-2-3.jpg'],
        'image': 'img/2018-practice-01/q2ci.jpg',
        'markscheme': 'img/2018-practice-01/ms-2ci.jpg',
        'markscheme_text': '<b>Award 2 marks as follows:</b><br>• Lever arm ratio / Principle of Moments: 85 mm / 40 mm = 2.125 (or 25 × 85 = F × 40) (1 mark)<br>• Tensile force F = 25 N × 2.125 = <b>53.125 N</b> (or <b>53.1 N</b>) (1 mark)<br><i>(Full marks if correct answer is given without working out. ECF applies.)</i>'
    },
    {
        'id': '2018-practice-01-q2cii',
        'paper': '2018-practice-01',
        'question': '2(c)(ii)',
        'marks': 3,
        'page': 10,
        'topics': ['6.3', '5.3'],
        'skills': ['maths', 'technical'],
        'summary': 'Calculate the cross-sectional area of a 1.6 mm diameter stainless steel wire in m².',
        'prompt': 'The cable is made from stainless steel. It has an unstretched length of 1500 mm and a diameter of 1.6 mm.<br><br>Calculate the cross sectional area of the wire in m² to 3 significant figures. Show your working.<br>Area of a circle = πr² [3]',
        'image': 'img/2018-practice-01/q2cii.jpg',
        'markscheme': 'img/2018-practice-01/ms-2cii.jpg',
        'markscheme_text': '<b>Award 3 marks as follows:</b><br>• Radius r = 1.6 mm / 2 = 0.8 mm (1 mark)<br>• Convert mm into m: 0.8 mm = 0.0008 m = 8.0 × 10⁻⁴ m (1 mark)<br>• Area A = π × (0.0008)² = <b>2.01 × 10⁻⁶ m²</b> (to 3 s.f.) (1 mark)<br><i>(Full marks if correct answer is given without working out. ECF applies.)</i>'
    },
    {
        'id': '2018-practice-01-q2ciii',
        'paper': '2018-practice-01',
        'question': '2(c)(iii)',
        'marks': 3,
        'page': 10,
        'topics': ['6.3'],
        'skills': ['maths', 'technical'],
        'summary': 'Calculate tensile stress in the wire in Pa (N/m²) under a tensile force of 300 N.',
        'prompt': 'Calculate the stress in the wire in Pa (N·m⁻²) when a tensile force of 300 N is applied to the end of the cable. Show your working. [3]',
        'image': 'img/2018-practice-01/q2ciii.jpg',
        'markscheme': 'img/2018-practice-01/ms-2ciii.jpg',
        'markscheme_text': '<b>Award 3 marks as follows:</b><br>• Formula: Stress σ = Force / Cross-sectional Area (1 mark)<br>• Substitution: Stress = 300 N / 2.01 × 10⁻⁶ m² (1 mark)<br>• Stress = <b>1.49 × 10⁸ Pa (N·m⁻²)</b> or <b>149 MPa</b> (also accept 149,253,731 Pa) (1 mark)<br><i>(Full marks if correct answer is given without working out. ECF applies.)</i>'
    },
    {
        'id': '2018-practice-01-q2civ',
        'paper': '2018-practice-01',
        'question': '2(c)(iv)',
        'marks': 3,
        'page': 10,
        'topics': ['6.3'],
        'skills': ['maths', 'technical'],
        'summary': 'Calculate the extension of the stainless steel cable in mm using Young\'s modulus.',
        'prompt': 'Calculate the extension of the cable in mm to 3 significant figures. Show your working.<br>Young’s modulus of stainless steel = 180 GPa [3]',
        'image': 'img/2018-practice-01/q2civ.jpg',
        'markscheme': 'img/2018-practice-01/ms-2civ.jpg',
        'markscheme_text': '<b>Award 3 marks as follows:</b><br>• Young\'s Modulus equation: E = Stress / Strain ⇒ 180 × 10⁹ = 149 × 10⁶ / Strain (1 mark)<br>• Calculate Strain: ε = 149 × 10⁶ / 180 × 10⁹ = 0.000828 (or 8.28 × 10⁻⁴) (1 mark)<br>• Calculate Extension: ΔL = Strain × Original length = 0.000828 × 1500 mm = <b>1.24 mm</b> (to 3 s.f.) (1 mark)<br><i>(Full marks if correct answer is given without working out. ECF applies.)</i>'
    },
    {
        'id': '2018-practice-01-q2di',
        'paper': '2018-practice-01',
        'question': '2(d)(i)',
        'marks': 2,
        'page': 11,
        'topics': ['1.3'],
        'skills': ['maths', 'design'],
        'summary': 'Calculate the percentage of ladder users with a body mass above 90 kg from a histogram.',
        'prompt': 'A ladder manufacturer carried out a survey on the body masses of 30 users. A histogram of the results is shown in Fig. 2.4.<br><br>Calculate the percentage of users in the survey who had a body mass above 90 kg. Show your working. [2]',
        'figures': ['img/2018-practice-01/fig-2-4.jpg'],
        'image': 'img/2018-practice-01/q2di.jpg',
        'markscheme': 'img/2018-practice-01/ms-2di.jpg',
        'markscheme_text': '<b>Award 2 marks as follows:</b><br>• Users above 90 kg: 2 (in 90–95 kg bin) + 1 (in 95–100 kg bin) = <b>3 users</b> (1 mark)<br>• Percentage: (3 / 30) × 100 = <b>10%</b> (1 mark)<br><i>(Full marks if correct answer 10% is given without working out.)</i>'
    },
    {
        'id': '2018-practice-01-q2dii',
        'paper': '2018-practice-01',
        'question': '2(d)(ii)',
        'marks': 2,
        'page': 11,
        'topics': ['1.3'],
        'skills': ['maths', 'design'],
        'summary': 'Show that the 50th percentile body mass of the ladder user sample is less than 84 kg.',
        'prompt': 'Anthropometric data for the UK population states that the 50th percentile body mass is 84 kg.<br><br>Show that the 50th percentile mass of the sample in Fig. 2.4 is less than 84 kg. [2]',
        'figures': ['img/2018-practice-01/fig-2-4.jpg'],
        'image': 'img/2018-practice-01/q2dii.jpg',
        'markscheme': 'img/2018-practice-01/ms-2dii.jpg',
        'markscheme_text': '<b>Award 2 marks as follows:</b><br>• Understand that the 50th centile is the median value, which is the 15th / 16th value in the dataset of 30 users (1 mark).<br>• Cumulative count: 2 + 4 + 5 = 11 (up to 75 kg); + 6 = 17 (up to 80 kg). The median value is in the <b>75–80 kg</b> class, which is strictly less than 84 kg (1 mark).'
    },

    # Question 3
    {
        'id': '2018-practice-01-q3ai',
        'paper': '2018-practice-01',
        'question': '3(a)(i)',
        'marks': 2,
        'page': 12,
        'topics': ['3.1'],
        'skills': ['design'],
        'summary': 'Describe how a social footprint is created by the manufacture of a product.',
        'prompt': 'Designers and manufacturers should consider the social footprint and the ecological footprint of any materials they use.<br><br>Describe how a social footprint is created by the manufacture of a product. [2]',
        'image': 'img/2018-practice-01/q3ai.jpg',
        'markscheme': 'img/2018-practice-01/ms-3ai.jpg',
        'markscheme_text': '<b>Up to 2 marks for describing how a social footprint is created by product manufacture (macro or micro level):</b><br>• Mining chemicals or raw materials to make batteries and electronics can scar the landscape and impact local communities (1).<br>• Building factories to manufacture the product can alter the local environment and community infrastructure (1).<br>• Creating factory employment stimulates the local economy, skills base, and job market (1).<br>• Working conditions, worker safety, health standards, and fair wages across global supply chains (1).'
    },
    {
        'id': '2018-practice-01-q3aii',
        'paper': '2018-practice-01',
        'question': '3(a)(ii)',
        'marks': 4,
        'page': 12,
        'topics': ['3.1', '3.2'],
        'skills': ['design', 'technical'],
        'summary': 'Describe the ecological footprint that results when using timber in products.',
        'prompt': 'Describe the ecological footprint that results when using timber in products. [4]',
        'image': 'img/2018-practice-01/q3aii.jpg',
        'markscheme': 'img/2018-practice-01/ms-3aii.jpg',
        'markscheme_text': '<b>Up to 4 marks for describing the ecological footprint of using timber in products:</b><br>• Timber is a natural material requiring extensive forest land to cultivate; while tree growth absorbs carbon dioxide (nearly carbon neutral), fossil energy is required to fell, kiln dry, process, and transport timber to market (1).<br>• Softwoods (e.g. pine, spruce) grow significantly faster than hardwoods (e.g. oak, beech), producing a smaller ecological footprint in construction and furniture (1).<br>• Waste sawdust and offcuts created during milling are utilized for biomass fuel or manufactured boards like MDF and chipboard (1).<br>• Risk of deforestation, habitat destruction, and biodiversity loss if timber is not certified by sustainable forestry bodies (e.g. FSC / PEFC) (1).'
    },
    {
        'id': '2018-practice-01-q3b',
        'paper': '2018-practice-01',
        'question': '3(b)*',
        'marks': 8,
        'page': 13,
        'topics': ['2.4', '3.1', '3.2'],
        'skills': ['design', 'technical'],
        'summary': 'Extended response: Discuss how a Life Cycle Assessment (LCA) would be carried out on a domestic refrigerator.',
        'prompt': 'Discuss how a lifecycle assessment (LCA) would be carried out on a domestic refrigerator.<br><br>Make reference to the following stages of the product’s life in your answer:<br>• manufacture;<br>• use;<br>• end of life. [*8]',
        'image': 'img/2018-practice-01/q3b.jpg',
        'markscheme': 'img/2018-practice-01/ms-3b.jpg',
        'markscheme_text': '<b>Level 3 (6–8 marks):</b> Clear understanding of LCA. Thorough, well-structured discussion covering manufacture, use, and end-of-life stages for a refrigerator with relevant examples and clear reasoning.<br><b>Level 2 (3–5 marks):</b> Reasonable understanding. Sound discussion covering multiple LCA stages for a refrigerator with some structure.<br><b>Level 1 (1–2 marks):</b> Basic generic knowledge of LCA with little direct application.<br><br><b>Indicative content:</b><br>• <b>Manufacture:</b> Sourcing metals (sheet steel body, copper motor windings, aluminium cooling coils) and polymers (injection moulded ABS liners, polyurethane foam insulation). Toxic refrigerant gasses manufacture. Embodied energy in steel pressing, thermoforming liners, PCB assembly, and factory running energy.<br>• <b>Use:</b> Continuous 24/7 power draw over 10–15 year lifespan. Energy efficiency rating, improved vacuum/foam thermal insulation to lower compressor duty cycle.<br>• <b>End of Life:</b> Safe extraction and recycling of refrigerant gas (avoiding greenhouse/ozone depletion). Magnetic sorting and recycling of steel casing and copper coils. Difficulty recycling mixed insulation foam. RoHS directive compliance reducing hazardous substances.<br>• <b>Transport:</b> Embodied transport carbon moving bulky products from overseas manufacturing hubs.'
    },

    # Question 4
    {
        'id': '2018-practice-01-q4a',
        'paper': '2018-practice-01',
        'question': '4(a)',
        'marks': 1,
        'page': 14,
        'topics': ['6.1', '7.3'],
        'skills': ['technical'],
        'summary': 'State one reason why the side panels of a washing machine are manufactured with indentations.',
        'prompt': 'Fig. 4.1 shows a domestic washing machine.<br><br>The side panels of the washing machine shown in Fig. 4.1 are manufactured from a sheet metal with indentations.<br><br>State <b>one</b> reason why the side panels have been manufactured in this way. [1]',
        'figures': ['img/2018-practice-01/fig-4-1.jpg'],
        'image': 'img/2018-practice-01/q4a.jpg',
        'markscheme': 'img/2018-practice-01/ms-4a.jpg',
        'markscheme_text': '<b>One mark for identifying a reason why the side panels are manufactured in this way (1 mark):</b><br>• Adds structural rigidity / stiffness to the thin sheet steel panels without adding extra material or weight (1).<br>• Dampens vibration and acoustic drum noise during high-speed spinning (1).<br>• Adds aesthetic styling to the sides of the machine (1).<br>• Aids moving and lifting the appliance by providing grip indentations (1).'
    },
    {
        'id': '2018-practice-01-q4bi',
        'paper': '2018-practice-01',
        'question': '4(b)(i)',
        'marks': 3,
        'page': 15,
        'topics': ['6.2'],
        'skills': ['technical'],
        'summary': 'Identify three reasons why a belt and pulley drive system is used in a washing machine.',
        'prompt': 'Fig. 4.2 shows the belt and pulley drive system between the motor and the washing machine drum (motor pulley diameter 32 mm, drum pulley diameter 384 mm).<br><br>Identify <b>three</b> reasons why a belt and pulley drive system would be used in the washing machine. [3]',
        'figures': ['img/2018-practice-01/fig-4-2.jpg'],
        'image': 'img/2018-practice-01/q4bi.jpg',
        'markscheme': 'img/2018-practice-01/ms-4bi.jpg',
        'markscheme_text': '<b>One mark for identifying each of three reasons why a belt and pulley drive system is used (max 3 marks):</b><br>• Allows for a large reduction in rotational speed from high-speed motor to drum (1).<br>• Allows a substantial increase in mechanical torque to turn heavy wet laundry (1).<br>• Allows motor to sit compactly beneath the drum, reducing machine depth (1).<br>• Allows for a small amount of elastic flexing / shock absorption between motor and drum shafts (1).<br>• Quiet in operation compared to gear trains or chain drives (1).<br><i>(No credit for \'allows slipping\' or \'transfers drive from motor to drum\'.)</i>'
    },
    {
        'id': '2018-practice-01-q4bii',
        'paper': '2018-practice-01',
        'question': '4(b)(ii)',
        'marks': 2,
        'page': 15,
        'topics': ['6.2'],
        'skills': ['maths', 'technical'],
        'summary': 'Calculate the rotational speed of the motor when the washing machine drum spins at 1600 rpm.',
        'prompt': 'The maximum rotational drum speed is 1600 rpm. The motor pulley has a diameter of 32 mm and the drum pulley has a diameter of 384 mm.<br><br>Calculate the rotational speed of the motor when the drum is spinning at maximum speed. Show your working. [2]',
        'figures': ['img/2018-practice-01/fig-4-2.jpg'],
        'image': 'img/2018-practice-01/q4bii.jpg',
        'markscheme': 'img/2018-practice-01/ms-4bii.jpg',
        'markscheme_text': '<b>Award 2 marks as follows:</b><br>• Pulley ratio (Gear Ratio) = 384 mm / 32 mm = <b>12</b> (1 mark)<br>• Motor rotational speed = 12 × 1600 rpm = <b>19,200 rpm</b> (1 mark)<br><i>(Full marks if correct answer 19,200 rpm is given without working out. ECF applies.)</i>'
    },
    {
        'id': '2018-practice-01-q4biii',
        'paper': '2018-practice-01',
        'question': '4(b)(iii)',
        'marks': 3,
        'page': 16,
        'topics': ['6.4', '6.5'],
        'skills': ['technical'],
        'summary': 'Describe how a closed loop control system regulates the rotational speed of a washing machine drum.',
        'prompt': 'Describe how a closed loop control system is used to regulate the rotational speed of the washing machine drum. [3]',
        'image': 'img/2018-practice-01/q4biii.jpg',
        'markscheme': 'img/2018-practice-01/ms-4biii.jpg',
        'markscheme_text': '<b>Up to 3 marks for describing closed loop drum speed regulation:</b><br>• <b>Sensing:</b> The signal from an input transducer (e.g. slotted optical opto-switch, tachogenerator, or Hall effect sensor) measures drum/motor rotational speed (1).<br>• <b>Feedback comparison:</b> The measured speed signal is fed back to the microcontroller/controller and compared against the target programmed cycle speed (1).<br>• <b>Actuation error correction:</b> The controller adjusts the electrical drive power (e.g. PWM duty cycle or triac phase angle) to minimize the error difference between feedback speed and setpoint speed (1).'
    },
    {
        'id': '2018-practice-01-q4c',
        'paper': '2018-practice-01',
        'question': '4(c)',
        'marks': 4,
        'page': 16,
        'topics': ['1.3', '6.4'],
        'skills': ['design', 'technical'],
        'summary': 'Explain two ways in which a graphical display enhances the user interface on a washing machine compared to simple LEDs.',
        'prompt': 'User interfaces on early washing machines used simple LED indicators, but many modern washing machines feature graphical displays.<br><br>Explain <b>two</b> ways in which a graphical display enhances the user interface on the washing machine. [4]',
        'image': 'img/2018-practice-01/q4c.jpg',
        'markscheme': 'img/2018-practice-01/ms-4c.jpg',
        'markscheme_text': '<b>Award up to 4 marks (1 mark for identifying a way, 1 mark for explaining why in context, for each of two ways):</b><br>• <b>Rich visual & alphanumeric feedback:</b> Can display more than basic lights, such as exact remaining cycle time, wash temperature, spin speed, and animated tutorials/error diagnostics (1+1).<br>• <b>Universal international symbols:</b> Can display intuitive icons and multi-lingual text menus, allowing the appliance to be sold globally without redesigning physical control fascia panels (1+1).<br>• <b>Ergonomics and intuitive navigation:</b> Graphical layouts and icons are clearer to comprehend than cryptic blinking LEDs, reducing human operational errors (1+1).<br>• <b>Touchscreen / soft keys:</b> Touchscreens reduce physical push buttons, creating a flush, hygienic surface that is easy to wipe clean with a premium luxury aesthetic (1+1).'
    },
    {
        'id': '2018-practice-01-q4d',
        'paper': '2018-practice-01',
        'question': '4(d)*',
        'marks': 8,
        'page': 17,
        'topics': ['5.3', '7.5', '8.2'],
        'skills': ['technical', 'practical'],
        'summary': 'Extended response: Discuss how destructive and non-destructive testing methods assess a washing machine\'s suitability for purpose.',
        'prompt': 'Discuss how the washing machine manufacturer would use destructive and non-destructive testing methods to assess the machine’s suitability for purpose. [*8]',
        'image': 'img/2018-practice-01/q4d.jpg',
        'markscheme': 'img/2018-practice-01/ms-4d.jpg',
        'markscheme_text': '<b>Level 3 (6–8 marks):</b> Clear understanding of destructive and non-destructive testing. Thorough discussion explaining how both testing methods judge fitness for purpose across multiple perspectives.<br><b>Level 2 (3–5 marks):</b> Reasonable understanding of testing methods. Sound discussion explaining how destructive and/or non-destructive tests assess fitness for purpose.<br><b>Level 1 (1–2 marks):</b> Basic generic knowledge of testing with little application.<br><br><b>Indicative content:</b><br>• <b>Destructive tests (testing to failure):</b><br>  - Robotic cyclic door opening/slamming until latch failure.<br>  - Drive belt tensile fatigue pull test until snapping.<br>  - Accelerated life / time-to-failure continuous running tests.<br>  - Overload tests with excess heavy laundry and unbalanced weight distribution.<br>  - Thermal overheat and heater dry-run fire safety tests.<br>  - Electrical overvoltage/spike insulation breakdown tests.<br>• <b>Non-destructive tests (NDT / QA verification):</b><br>  - Water pressure leak testing of pumps, valves, and drum seals.<br>  - PAT testing (earth bonding continuity and insulation resistance).<br>  - Failsafe cut-out testing (e.g. door interlock preventing opening during spin).<br>  - Dynamic drum balancing sensor and accelerometer calibration.<br>  - Automated PCB diagnostic test bench and firmware verification.<br>  - Acoustic noise level measurements (dB meter) during 1600 rpm spin.'
    }
]

def main():
    qpath = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets\questions.json'
    with open(qpath, 'r', encoding='utf-8-sig') as f:
        d = json.load(f)

    # Add paper
    paper_ids = [p['id'] for p in d['papers']]
    if new_paper['id'] not in paper_ids:
        d['papers'].append(new_paper)

    # Filter out existing with same IDs if any, then append
    existing_ids = set(q['id'] for q in new_questions)
    d['questions'] = [q for q in d['questions'] if q['id'] not in existing_ids] + new_questions

    with open(qpath, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)

    np = len(d['papers'])
    nq = len(d['questions'])
    print(f'Successfully updated questions.json! Total papers: {np}, Total questions: {nq}')

if __name__ == '__main__':
    main()
