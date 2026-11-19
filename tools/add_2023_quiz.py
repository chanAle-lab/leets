import json, os

repo = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets'
qpath = os.path.join(repo, "quiz_questions.json")

with open(qpath, "r", encoding="utf-8") as f:
    quizzes = json.load(f)

# Filter out any existing 2023 quiz questions if present
quizzes = [q for q in quizzes if not q["id"].startswith("quiz-2023-")]

new_quizzes = [
    {
        "id": "quiz-2023-s01-q1",
        "question": "Why is a flyback diode placed anti-parallel across a DC motor when switched by a MOSFET?",
        "choices": [
            "To dissipate inductive kickback voltage (back EMF) and prevent avalanche breakdown of the MOSFET",
            "To boost the motor starting torque during initial acceleration",
            "To convert AC motor noise into a regulated DC power supply",
            "To act as a current-limiting resistor when the motor stalls"
        ],
        "correctIndex": 0,
        "explanation": "When an inductive coil like a motor winding is rapidly switched off, collapsing magnetic flux induces a large reverse voltage spike (back EMF). A flyback diode provides a safe conduction loop to circulate and dissipate this energy.",
        "topic": "6"
    },
    {
        "id": "quiz-2023-s01-q2",
        "question": "Why is Pulse Width Modulation (PWM) significantly more energy-efficient for DC motor speed control than a variable resistor?",
        "choices": [
            "The switching transistor operates fully ON (near zero resistance) or fully OFF (zero current), minimizing thermal dissipation ($P = I^2 R \\approx 0$)",
            "PWM steps up the supply voltage so less current is required from the power source",
            "PWM cancels mechanical friction inside the motor bearings",
            "A variable resistor increases battery capacity during motor braking"
        ],
        "correctIndex": 0,
        "explanation": "A variable resistor controls speed by dropping voltage and dissipating power as pure waste heat ($P = I^2 R$). PWM switches the motor rapidly between fully on and fully off, achieving variable average power with negligible internal transistor heat loss.",
        "topic": "6"
    },
    {
        "id": "quiz-2023-s01-q3",
        "question": "How do quadrature incremental rotary encoders detect both rotational speed and direction?",
        "choices": [
            "Two square-wave channel signals are offset by 90° phase shift; the leading channel indicates direction while pulse frequency indicates speed",
            "Channel A measures velocity while Channel B measures magnetic compass heading",
            "Channel A provides an analogue voltage and Channel B provides a digital clock",
            "The encoder changes internal resistance depending on clockwise or anticlockwise torque"
        ],
        "correctIndex": 0,
        "explanation": "In a quadrature encoder, channels A and B are mechanically phased 90° apart. When rotated clockwise, channel A transitions before B; when rotated anticlockwise, channel B leads. The frequency of transitions reflects rotational speed.",
        "topic": "6"
    },
    {
        "id": "quiz-2023-s01-q4",
        "question": "In a worm gear drive with a single-start worm screw meshing with a 60-tooth worm wheel, what is the gear ratio and mechanical property?",
        "choices": [
            "60:1 gear reduction ratio, providing large torque multiplication and resistance to back-driving",
            "1:60 ratio, multiplying output speed sixty-fold",
            "30:1 ratio, operating with high mechanical back-drivability",
            "120:1 ratio, doubling torque only when driven in reverse"
        ],
        "correctIndex": 0,
        "explanation": "A single-start worm advances the gear by one tooth per revolution. For a 60-tooth wheel, 60 worm rotations produce 1 wheel rotation (60:1 reduction), which naturally locks against reverse back-driving.",
        "topic": "5"
    },
    {
        "id": "quiz-2023-s02-q1",
        "question": "If the aperture diameter of a conical rain gauge funnel is doubled while rainfall rate remains constant, by what factor does the volume of collected rainwater increase?",
        "choices": [
            "4 times (quadrupled)",
            "2 times (doubled)",
            "8 times (octupled)",
            "Remains unchanged"
        ],
        "correctIndex": 0,
        "explanation": "Catchment volume is directly proportional to aperture area $A = \\pi r^2 = \\frac{\\pi D^2}{4}$. Doubling the diameter multiplies the area and catchment volume by $2^2 = 4$.",
        "topic": "3"
    },
    {
        "id": "quiz-2023-s02-q2",
        "question": "Why are ceramic decoupling capacitors (e.g. 100 nF) placed across the V+ and 0V supply pins close to radio transmitter modules?",
        "choices": [
            "To filter high-frequency switching noise and supply transient surge currents during RF transmission",
            "To store sufficient power to run the transmitter for several hours without a battery",
            "To adjust the transmission carrier frequency to match antenna length",
            "To convert analogue sensor inputs into serial digital packets"
        ],
        "correctIndex": 0,
        "explanation": "RF transmitters draw sudden burst currents when pulsing signals into the antenna. Local decoupling capacitors provide low-impedance instantaneous current and bypass high-frequency electrical noise to 0V ground, preventing microcontroller resets.",
        "topic": "6"
    }
]

quizzes.extend(new_quizzes)

with open(qpath, "w", encoding="utf-8") as f:
    json.dump(quizzes, f, indent=2, ensure_ascii=False)

print(f"Successfully added {len(new_quizzes)} revision quiz questions! Total quiz questions: {len(quizzes)}")
