# add_practice_paper_02.py
import json

new_paper = {
    'id': '2018-practice-02',
    'code': 'H404/02',
    'unit': 'Problem Solving in Design Engineering',
    'year': 2018,
    'level': 'H404',
    'totalMarks': 70,
    'series': 'Practice Set 1'
}

new_questions = [
    # Question 1*
    {
        'id': '2018-practice-02-q1',
        'paper': '2018-practice-02',
        'question': '1*',
        'marks': 14,
        'page': 2,
        'topics': ['3.1', '1.1', '2.2'],
        'skills': ['design'],
        'summary': 'Critically examine the social, moral and ethical considerations of supplying developing countries with 3D-printed prosthetic limbs.',
        'prompt': 'Every year, thousands of people across the world are born without limbs, or lose a limb through accidents. In any society this can be life changing but in the developing world it can have devastating effects across the community.<br><br>Charities are looking into the effects of supplying these developing communities with the ability to produce 3D-printed prosthetic limbs to improve the quality of life of those affected.<br><br>Critically examine the <b>social, moral and ethical</b> considerations of developing countries being given access to the use of 3D printing for the production of prosthetic limbs for those affected in their communities.<br><br><i>Refer to information on pages 2 and 3 of the Resource Booklet.</i> [*14]',
        'figures': [
            'img/2018-practice-02/fig-1.jpg',
            'img/2018-practice-02/fig-2.jpg',
            'img/2018-practice-02/fig-3.jpg'
        ],
        'image': 'img/2018-practice-02/q1.jpg',
        'markscheme': 'img/2018-practice-02/ms-1.jpg',
        'markscheme_text': '<b>Level 4 (12–14 marks):</b> Comprehensive understanding of social, moral, and ethical implications of 3D printing prosthetics in developing countries. All three areas considered with both positive and negative perspectives. Well-developed, logically structured argument using Resource Booklet data and design knowledge.<br><b>Level 3 (9–11 marks):</b> Good understanding of social/moral/ethical implications. At least two areas considered with balanced views.<br><b>Level 2 (5–8 marks):</b> Sufficient understanding covering at least one area with some structure.<br><b>Level 1 (1–4 marks):</b> Limited descriptive knowledge without evaluation.<br><br><b>Indicative Content:</b><br>• <b>Social Implications:</b> Restores mobility and dignity; allows individuals to walk without crutches, freeing their hands to carry water/food and perform productive work; reduces community dependency; reintegration into social activities and sports (e.g. wheelchair/prosthetic basketball); risk of social stigma or being ostracised if aesthetic appearance is strange or culturally unaccepted.<br>• <b>Moral Implications:</b> Moral duty to alleviate suffering and restore human potential; designer responsibility for biomechanical safety, structural durability, and avoiding stump skin ulceration/infection; managing expectations when simple mechanical prosthetics cannot match biological limb dexterity.<br>• <b>Ethical Implications:</b> Resource allocation and equity (who decides which amputees receive prosthetics in impoverished refugee camps?); cost and long-term funding (£2800 printer vs £20 per limb); lifespan and replacement protocols as child amputees grow; provision of physiotherapist rehabilitation and clinical follow-up; intellectual property of open-source CAD prosthetics vs medical certification standards.'
    },

    # Question 2
    {
        'id': '2018-practice-02-q2',
        'paper': '2018-practice-02',
        'question': '2',
        'marks': 14,
        'page': 4,
        'topics': ['5.1', '5.2', '7.1', '7.3'],
        'skills': ['technical', 'practical'],
        'summary': 'Propose an alternative manufacturing process, thermoplastic material, and finishing techniques for an individual upper limb socket.',
        'prompt': 'Page 2 of the Resource Booklet explains how a prosthetic specialist produces a positive model of a patient’s affected limb. This positive model is then used to create the socket of the prosthetic leg shown in Fig. 1 of the Resource Booklet.<br><br>Other than 3D printing, explain using sketches and/or notes a suitable manufacturing process which could be used to make the upper limb socket for an individual as shown in Fig. 1 of the Resource Booklet.<br><br>In your response you must include:<br>• <b>technical details of methods of manufacture</b>;<br>• <b>appropriate materials and their properties</b>;<br>• <b>manufacturing processes to appropriately finish the socket</b>. [14]',
        'figures': [
            'img/2018-practice-02/fig-1.jpg',
            'img/2018-practice-02/ms-2-diagram.jpg'
        ],
        'image': 'img/2018-practice-02/q2.jpg',
        'markscheme': 'img/2018-practice-02/ms-2.jpg',
        'markscheme_text': '<b>Level 4 (11–14 marks):</b> Excellent, end-to-end account of the manufacturing process for an upper limb socket covering all three bullet points. Naming a suitable thermoplastic (e.g. Polypropylene, Polyethylene, Polyurethane, ABS, HIPS) with property justification for custom one-off production. Clear annotated sketches and notes.<br><b>Level 3 (7–10 marks):</b> Good account covering at least two bullet points with clear material and process choices.<br><b>Level 2 (4–6 marks):</b> Sufficient account with basic material identification but limited one-off production justification.<br><b>Level 1 (1–3 marks):</b> Basic account with knowledge gaps.<br><br><b>Indicative Content:</b><br>• <b>Manufacturing Methods:</b><br>  - <i>Vacuum Forming / Drape Thermoforming:</i> Highly suited for custom one-off manufacture over the plaster/vermiculite positive limb cast. A sheet of thermoplastic is clamped, heated by infrared ceramic heaters until pliable/rubbery, draped over the positive mould, and vacuum suction draws the sheet into intimate contact. Low tooling cost and quick cycle time.<br>  - <i>Thermoplastic Dip/Press Moulding:</i> Alternatively, heated sheet pulled and seamed around mould.<br>  - <i>(If Injection Moulding is chosen):</i> Must explain machine operation (hopper, reciprocating screw, heater bands, molten injection under pressure), but candidate must address that high tooling cost is normally unsuitable for one-off bespoke items unless modular cavity inserts are utilized.<br>• <b>Materials & Properties:</b><br>  - <i>Polypropylene (PP):</i> High fatigue resistance (living hinge property), low density, ductile, excellent chemical resistance, thermoforms easily over plaster positive.<br>  - <i>Polyurethane (PU) / TPU:</i> Flexible, tear-resistant, resilient cushioning, skin-compatible, provides comfortable pressure distribution.<br>  - <i>High-Density Polyethylene (HDPE):</i> Tough, lightweight, moisture resistant, easily trimmed.<br>• <b>Finishing Processes:</b><br>  - Trimming excess flash and flashing lines with oscillating cast cutter / bandsaw.<br>  - Deburring and beveling socket rim edges with a rotary burr/flap wheel to prevent skin chaffing.<br>  - Flaming or solvent polishing perimeter edges to create smooth, hygienic radius.<br>  - Adding closed-cell foam liner (Plastazote) and adjustable hook-and-loop (Velcro) suspension straps.'
    },

    # Question 3(a)
    {
        'id': '2018-practice-02-q3a',
        'paper': '2018-practice-02',
        'question': '3(a)',
        'marks': 3,
        'page': 6,
        'topics': ['6.1', '3.6'],
        'skills': ['maths', 'technical'],
        'summary': 'Calculate angle C formed between the tie and the forearm in the prosthetic arm force diagram.',
        'prompt': 'Engineers have been working on a 3D-printed prosthetic arm which is easy to manufacture and simple to use. The design is shown in Fig. 4 of the Resource Booklet. It has a loose elbow joint which is held at a fixed 90° angle by a tie attached between the upper arm and the forearm. Fig. 5 shows a force diagram for the 3D-printed prosthetic arm.<br><br>In Fig. 5, the tie is anchored at a height of 120 mm above the elbow joint on the upper arm, and attached to the forearm at a distance of 70 mm from the elbow joint.<br><br>Calculate the angle <b>C</b> in Fig. 5 formed between the tie and the forearm. Show your working. [3]',
        'figures': [
            'img/2018-practice-02/fig-4.jpg',
            'img/2018-practice-02/fig-5.jpg'
        ],
        'image': 'img/2018-practice-02/q3a.jpg',
        'markscheme': 'img/2018-practice-02/ms-3a.jpg',
        'markscheme_text': '<b>Award 3 marks as follows:</b><br>• Correct trigonometry formula: tan(C) = Opposite / Adjacent ⇒ C = tan⁻¹(Opp / Adj) (1 mark)<br>• Correct substitution: C = tan⁻¹(120 / 70) = tan⁻¹(1.714) (1 mark)<br>• Calculate angle C: C = <b>59.68°</b> (Accept rounded answers to <b>60°</b> or <b>59.7°</b>) (1 mark)<br><i>(Full marks if correct answer is given without working. ECF applies.)</i>'
    },

    # Question 3(b)
    {
        'id': '2018-practice-02-q3b',
        'paper': '2018-practice-02',
        'question': '3(b)',
        'marks': 3,
        'page': 6,
        'topics': ['6.1', '3.6'],
        'skills': ['maths', 'technical'],
        'summary': 'Calculate the length of the support tie to the nearest mm using trigonometry or Pythagoras.',
        'prompt': 'Calculate the length of the tie in Fig. 5 to the nearest mm. Show your working. [3]',
        'figures': [
            'img/2018-practice-02/fig-4.jpg',
            'img/2018-practice-02/fig-5.jpg'
        ],
        'image': 'img/2018-practice-02/q3b.jpg',
        'markscheme': 'img/2018-practice-02/ms-3b.jpg',
        'markscheme_text': '<b>Award 3 marks as follows:</b><br>• Method 1 (Trigonometry):<br>  y = Opposite / sin(C) = 120 / sin(59.68°) = 120 / 0.8632 = <b>139 mm</b> (3 marks)<br>• Method 2 (Pythagoras theorem):<br>  y² = 120² + 70² = 14,400 + 4,900 = 19,300 (1 mark)<br>  y = √19,300 = 138.92 mm (1 mark)<br>  Rounding to nearest mm: y = <b>139 mm</b> (1 mark)<br><i>(Full marks if correct answer 139 mm is given without working out. ECF applies.)</i>'
    },

    # Question 3(c)
    {
        'id': '2018-practice-02-q3c',
        'paper': '2018-practice-02',
        'question': '3(c)',
        'marks': 6,
        'page': 7,
        'topics': ['6.2', '6.3'],
        'skills': ['maths', 'technical'],
        'summary': 'Calculate the tensile force F in the tie under maximum hand load considering moments about the elbow joint.',
        'prompt': 'Fig. 5 of the Resource Booklet shows a force diagram for the 3D-printed prosthetic arm.<br><br>Using the product information from Fig. 6 in the Resource Booklet:<br>• Mass of lower arm = 2 kg (acting at center of gravity distance 115 mm from elbow)<br>• Maximum recommended load held in hand = 9 kg (acting at distance 70 + 160 = 230 mm from elbow)<br>• Tie attached at 70 mm from elbow at angle C = 59.68°<br>• Gravitational field strength g = 9.81 N·kg⁻¹<br><br>Calculate the tensile force (<b>F</b>) in the tie when the maximum recommended load is being held in the hand.<br>You will find it useful to consider the moments acting about the elbow joint. Show your working. [6]',
        'figures': [
            'img/2018-practice-02/fig-5.jpg',
            'img/2018-practice-02/fig-6.jpg'
        ],
        'image': 'img/2018-practice-02/q3c.jpg',
        'markscheme': 'img/2018-practice-02/ms-3c.jpg',
        'markscheme_text': '<b>Award 6 marks as follows:</b><br>• Hand load force L: 9 kg × 9.81 = <b>88.29 N</b> (1 mark)<br>• Arm weight force W: 2 kg × 9.81 = <b>19.62 N</b> (1 mark)<br>• Anticlockwise moments about elbow joint:<br>  M_ACW = (L × 230 mm) + (W × 115 mm) = (88.29 × 230) + (19.62 × 115) = 20,306.7 + 2,256.3 = <b>22,563 N·mm</b> (1 mark)<br>• Clockwise moment about elbow joint from tie force F:<br>  Perpendicular component of F = F sin(C)<br>  M_CW = F sin(59.68°) × 70 mm (1 mark)<br>• Equate moments in equilibrium (ΣM = 0):<br>  22,563 = F × sin(59.68°) × 70 (1 mark)<br>  F = 22,563 / (0.8632 × 70) = 22,563 / 60.426 = <b>373.4 N</b> (allow <b>373 N to 374 N</b>) (1 mark)<br><i>(Full marks if correct answer in range 373–374 N is given without working. ECF applies.)</i>'
    },

    # Question 4
    {
        'id': '2018-practice-02-q4',
        'paper': '2018-practice-02',
        'question': '4',
        'marks': 14,
        'page': 8,
        'topics': ['6.2', '6.4', '6.5', '5.1'],
        'skills': ['technical', 'design'],
        'summary': 'Design mechanical and electronic solutions for the Endo-wrist forceps: 3:1 linear-to-oscillating amplification and forceps rotation.',
        'prompt': 'The design engineers have been challenged to further develop the Endo-wrist described on page 5 of the Resource Booklet. They have identified that the current movement of the Endo-wrist does not sufficiently fulfil the movements of a surgeon’s hand and wrist, specifically when the Endo-wrist is being used with a forceps attachment as shown in Fig. 10 of the Resource Booklet.<br><br>Use sketches and/or notes to determine suitable technical solutions that overcome the following problems identified by the design engineers:<br><br><b>Problem 1:</b> Opening and closing of forceps using the existing linear actuator (converting 5 mm linear stroke into 15 mm oscillating jaw tip opening — a 3:1 movement amplification).<br><b>Problem 2:</b> Rotation of forceps (providing controllable continuous or bidirectional rotation of the forceps assembly).<br><br>In your response you must include details that demonstrate:<br>• appropriate mechanical function;<br>• appropriate electronic control systems;<br>• materials and components to be used. [14]',
        'figures': [
            'img/2018-practice-02/fig-8.jpg',
            'img/2018-practice-02/fig-9.jpg',
            'img/2018-practice-02/fig-10.jpg',
            'img/2018-practice-02/ms-4-diagram.jpg'
        ],
        'image': 'img/2018-practice-02/q4.jpg',
        'markscheme': 'img/2018-practice-02/ms-4.jpg',
        'markscheme_text': '<b>Level 4 (11–14 marks):</b> Candidate designs a suitable system producing the required motion for BOTH problems, covering all three bullet points. Excellent understanding of medical tool kinematics, explicit 3:1 amplification calculations/dimensions (5 mm stroke to 15 mm tip opening), clear annotated sketches, actuator selection, and biocompatible sterilizable materials.<br><b>Level 3 (7–10 marks):</b> Suitable system solving both problems with clear sketches and notes, but minor gaps in dimensions or amplification calculations.<br><b>Level 2 (4–6 marks):</b> Solves one problem or omits 3:1 amplification.<br><b>Level 1 (1–3 marks):</b> Basic ideas with missing kinematics or unfeasible mechanics.<br><br><b>Indicative Content:</b><br>• <b>Problem 1 (Forceps Jaw Motion & 3:1 Amplification):</b><br>  - Conversion of linear actuator stroke (5 mm) to jaw tip oscillation (15 mm opening).<br>  - Linkage mechanism: Scissor linkage, bell-crank lever, or toggle mechanism with pivot lever arm ratio of 3:1 (e.g. input arm 10 mm from pivot to actuator clevis, output jaw arm 30 mm from pivot to tip).<br>  - Plain miniature ceramic/PTFE sleeve bearings to minimize friction and prevent biological fluid contamination.<br>  - Biocompatible materials: Surgical grade stainless steel (316L) or titanium alloy (Ti-6Al-4V) suitable for autoclave steam sterilization or gamma irradiation.<br>• <b>Problem 2 (Forceps Rotation & Transducer Control):</b><br>  - Miniature rotational actuator: Brushless DC micromotor or stepper motor fitted with planetary reduction gearbox, mounted concentrically within the surgical shaft.<br>  - Electronic control: Microcontroller receives rotary encoder input from surgeon\'s master console joystick/wheel; drives motor via H-bridge PWM motor driver (or microstepping driver for discrete angular positioning).<br>  - Slip ring or flexible spiral ribbon cable to transmit signals through rotating joint without wire entanglement.<br>  - Speed and position feedback: Closed-loop Hall-effect sensors or magnetic absolute encoder to guarantee sub-millimeter surgical accuracy and torque limiting.'
    },

    # Question 5*
    {
        'id': '2018-practice-02-q5',
        'paper': '2018-practice-02',
        'question': '5*',
        'marks': 16,
        'page': 10,
        'topics': ['2.2', '4.2', '7.1', '7.3'],
        'skills': ['design', 'technical'],
        'summary': 'Extended synoptic evaluation: How technological advancements have assisted design engineers to progress medical science.',
        'prompt': 'Advancements in medical technology are one of the pioneering areas of design engineering.<br><br>Critically evaluate how technological advancements have assisted design engineers in the design and development of products to progress medical science.<br><br>You may refer to any of the products outlined in the Resource Booklet and also other products with which you are familiar. [*16]',
        'figures': [
            'img/2018-practice-02/fig-2.jpg',
            'img/2018-practice-02/fig-7.jpg',
            'img/2018-practice-02/fig-9.jpg'
        ],
        'image': 'img/2018-practice-02/q5.jpg',
        'markscheme': 'img/2018-practice-02/ms-5.jpg',
        'markscheme_text': '<b>Level 4 (13–16 marks):</b> Comprehensive synoptic evaluation of how technological advancements have assisted design engineers to progress medical science. Seamlessly synthesizes evidence from the Resource Booklet (3D-printed limbs, da Vinci surgical robotics, Endo-wrist) with wider engineering knowledge (CAD/CAM, FEA, CT/MRI scan slicing, bio-materials, VR/AR surgical training). Flawlessly structured, logical argument with clear evidence.<br><b>Level 3 (9–12 marks):</b> Good understanding connecting technological advances to medical product development with substantiated examples.<br><b>Level 2 (5–8 marks):</b> Sufficient understanding covering technological points with basic structure.<br><b>Level 1 (1–4 marks):</b> Descriptive summary with limited evaluation.<br><br><b>Indicative Content:</b><br>• <b>Rapid Prototyping & Additive Manufacturing:</b><br>  - Evolution from SLA, SLS to direct metal laser sintering (DMLS/SLM) of titanium bone implants.<br>  - Patient-specific customization: Converting 3D CT/MRI DICOM scans directly into STL surface meshes to 3D print bespoke cranial plates, hearing aids, dental bridges, and burn-victim skin scaffolds.<br>  - Rapid turnaround and drastic cost reduction (£2800 printer yielding £20 prosthetic limbs vs traditional £1000s plaster casting in developing countries).<br>• <b>Digital Engineering Tools (CAD, CAE, FEA, AR/VR):</b><br>  - Parametric 3D solid modelling and kinematic simulation of miniature robotic linkages before physical fabrication.<br>  - Finite Element Analysis (FEA) to verify stress distribution in artificial joint replacements, eliminating failure points.<br>  - Augmented Reality (AR) and 3D immersive simulator consoles for surgeons to practice complex incisions without risking patient safety.<br>• <b>Robotic Surgery & Tele-operation:</b><br>  - da Vinci system: 3D HD stereoscopic magnification, tremor filtration, and motion scaling (converting 5 cm surgeon hand motion into 5 mm surgical tip displacement).<br>  - Miniaturization: 1 cm diameter instruments reducing incision size (minimally invasive keyhole surgery), dramatically decreasing tissue trauma, hospital stay, infection risk, and recovery time.<br>• <b>Smart Materials & Micro-electronics:</b><br>  - High-precision micro-actuators, piezoelectric ultrasonic scalpels, wireless real-time endoscopic cameras, and bio-inert polymers.'
    }
]

def main():
    qpath = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets\questions.json'
    with open(qpath, 'r', encoding='utf-8') as f:
        d = json.load(f)

    # Add or update paper entry
    paper_ids = [p['id'] for p in d['papers']]
    if new_paper['id'] not in paper_ids:
        d['papers'].append(new_paper)
    else:
        for idx, p in enumerate(d['papers']):
            if p['id'] == new_paper['id']:
                d['papers'][idx] = new_paper

    # Remove existing with same ID if any, then append
    existing_ids = set(q['id'] for q in new_questions)
    d['questions'] = [q for q in d['questions'] if q['id'] not in existing_ids] + new_questions

    with open(qpath, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)

    np = len(d['papers'])
    nq = len(d['questions'])
    print(f'Successfully updated questions.json! Total papers: {np}, Total questions: {nq}')

if __name__ == '__main__':
    main()
