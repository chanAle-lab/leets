import json, os

QUIZ_PATH = r"C:\Users\Alexander\.gemini\antigravity\scratch\leets\quiz_questions.json"

with open(QUIZ_PATH, "r", encoding="utf-8") as f:
    quizzes = json.load(f)

new_quizzes = [
    {
        "id": "quiz-2024-s01-q1",
        "question": "In a compound gear train reducing shaft speed by a total velocity ratio of 9:1, how do the output speed and ideal output torque compare to the motor input?",
        "choices": [
            "Output speed is 1/9 of input speed, and output torque is 9 times input torque",
            "Output speed is 9 times input speed, and output torque is 1/9 of input torque",
            "Output speed and torque are both reduced by a factor of 9",
            "Output speed is 1/3 of input speed, and output torque is 3 times input torque"
        ],
        "correctIndex": 0,
        "explanation": "Mechanical power P = T * omega. In an ideal gear reduction where velocity ratio VR = omega_in / omega_out = 9:1, speed is reduced by 9x and torque is amplified by 9x.",
        "topic": "5"
    },
    {
        "id": "quiz-2024-s01-q2",
        "question": "When a heating element of resistance R is powered by a pulsed DC square wave with 40% duty cycle at constant voltage V, what is the average thermal power dissipated compared to continuous DC?",
        "choices": [
            "40% of continuous DC power (P_avg = 0.40 * V^2 / R)",
            "16% of continuous DC power (P_avg = 0.40^2 * V^2 / R)",
            "63.2% of continuous DC power due to thermal capacitance",
            "100% because peak voltage V is unchanged during ON pulses"
        ],
        "correctIndex": 0,
        "explanation": "Instantaneous power during the ON time is P_peak = V^2 / R, and 0 during OFF time. The average power over time period T is P_avg = (t_on / T) * P_peak = Duty Cycle * (V^2 / R) = 0.40 * (V^2 / R).",
        "topic": "6"
    },
    {
        "id": "quiz-2024-s01-q3",
        "question": "Which of the following best contrasts planned obsolescence with Total Quality Management (TQM)?",
        "choices": [
            "Planned obsolescence deliberately designs products with a limited lifespan to stimulate replacement sales, whereas TQM focuses on continuous improvement and zero defects to maximise quality and durability",
            "Planned obsolescence focuses on minimizing manufacturing scrap, whereas TQM designs products to fail predictably at the warranty boundary",
            "Planned obsolescence uses standardized metric fasteners, whereas TQM uses proprietary anti-tamper security screws",
            "Planned obsolescence is required by ISO 9001 quality audits, whereas TQM is optional commercial branding"
        ],
        "correctIndex": 0,
        "explanation": "Planned obsolescence limits functional lifespan to force repeat purchasing. In contrast, Total Quality Management (TQM) is an organization-wide philosophy pursuing Kaizen (continuous improvement), defect prevention, and robust long-term customer satisfaction.",
        "topic": "1"
    },
    {
        "id": "quiz-2024-s02-q1",
        "question": "A synthetic playground rope has cross-sectional area A = 1.13 x 10^-4 m^2 and tensile Young's modulus E = 480 MPa. When carrying a tensile force of 382.6 N over an effective length of 1.51 m, what is the resulting rope extension?",
        "choices": [
            "Approximately 10.7 mm",
            "Approximately 1.07 mm",
            "Approximately 34.2 mm",
            "Approximately 107 mm"
        ],
        "correctIndex": 0,
        "explanation": "Stress sigma = F / A = 382.6 / (1.13 x 10^-4) = 3.386 MPa. Strain epsilon = sigma / E = 3.386 / 480 = 0.007054. Extension delta L = epsilon * L0 = 0.007054 * 1510 mm = 10.65 mm (10.7 mm).",
        "topic": "4"
    },
    {
        "id": "quiz-2024-s02-q2",
        "question": "In an ambient light sensor circuit, an LDR is connected in a potential divider with a fixed resistor. In darkness, LDR resistance increases significantly (e.g. > 100 kOhm). If the LDR is connected between the sensing node and 0V (ground), what happens to the output voltage in darkness?",
        "choices": [
            "Output voltage rises towards supply voltage V+",
            "Output voltage falls close to 0V ground",
            "Output voltage oscillates at high frequency",
            "Output voltage remains locked at exactly V+ / 2"
        ],
        "correctIndex": 0,
        "explanation": "With the LDR between the sensing node and 0V and fixed resistor R connected to V+, V_out = V+ * (R_ldr / (R + R_ldr)). As darkness causes R_ldr to become very large (R_ldr >> R), V_out approaches V+.",
        "topic": "6"
    },
    {
        "id": "quiz-2024-s02-q3",
        "question": "A solenoid with a linear stroke of only 15 mm must actuate a locking bolt requiring a 45 mm stroke. Which lever configuration achieves this motion amplification?",
        "choices": [
            "Input applied at 1/3 distance from the pivot compared to the output pin (Velocity Ratio VR = 1/3, stroke ratio 1:3)",
            "Input applied at 3 times the distance from the pivot compared to the output pin (Mechanical Advantage = 3)",
            "A symmetrical 1:1 first-class lever with a compound gear reducer",
            "A rack and pinion mechanism with equal pitch circle diameter"
        ],
        "correctIndex": 0,
        "explanation": "To magnify movement from 15 mm to 45 mm (3x stroke amplification), the output arm must be 3 times longer than the input effort arm from the fulcrum. Velocity ratio VR = effort movement / load movement = 15 / 45 = 1/3.",
        "topic": "5"
    }
]

existing_ids = {q["id"] for q in quizzes}
added = 0
for q in new_quizzes:
    if q["id"] not in existing_ids:
        quizzes.append(q)
        added += 1

with open(QUIZ_PATH, "w", encoding="utf-8") as f:
    json.dump(quizzes, f, indent=2)

print(f"Added {added} new quiz questions. Total quizzes now: {len(quizzes)}")
