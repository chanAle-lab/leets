# build_questions.ps1
$ErrorActionPreference = "Stop"

$baseDir = "C:\Users\Alexander\.gemini\antigravity\scratch\leets"
$outPath = Join-Path $baseDir "questions.json"

$topics = @(
  @{ id = "1.1"; name = "Contexts for Design Solutions"; group = "1. Identifying Requirements" },
  @{ id = "1.2"; name = "Stakeholder Analysis & Enterprise"; group = "1. Identifying Requirements" },
  @{ id = "1.3"; name = "Usability, Inclusivity & Ergonomics"; group = "1. Identifying Requirements" },
  @{ id = "2.1"; name = "Product Analysis & Evaluation"; group = "2. Existing Products & Practice" },
  @{ id = "2.2"; name = "Technological Developments & Innovation"; group = "2. Existing Products & Practice" },
  @{ id = "2.3"; name = "Historical Movements & Influential Engineers"; group = "2. Existing Products & Practice" },
  @{ id = "2.4"; name = "Product Lifecycles & Marketing Models"; group = "2. Existing Products & Practice" },
  @{ id = "3.1"; name = "Social, Moral, Ethical & Environmental Factors"; group = "3. Implications of Wider Issues" },
  @{ id = "3.2"; name = "Design for Manufacture (DFM) & Sustainability"; group = "3. Implications of Wider Issues" },
  @{ id = "3.3"; name = "Optimum Material Use & Stock Forms"; group = "3. Implications of Wider Issues" },
  @{ id = "3.4"; name = "Distribution Logistics & Intellectual Property"; group = "3. Implications of Wider Issues" },
  @{ id = "3.5"; name = "Energy Sources, Storage & Efficiency"; group = "3. Implications of Wider Issues" },
  @{ id = "3.6"; name = "Cross-Disciplinary STEM in Engineering"; group = "3. Implications of Wider Issues" },
  @{ id = "4.1"; name = "2D & 3D Sketching, Drawing & Modelling"; group = "4. Design Thinking & Communication" },
  @{ id = "4.2"; name = "Digital Engineering Tools (CAD, CAE, FEA)"; group = "4. Design Thinking & Communication" },
  @{ id = "4.3"; name = "Systems Thinking & Project Management"; group = "4. Design Thinking & Communication" },
  @{ id = "5.1"; name = "Factors Influencing Material Selection"; group = "5. Material & Component Considerations" },
  @{ id = "5.2"; name = "Engineering Materials Classification"; group = "5. Material & Component Considerations" },
  @{ id = "5.3"; name = "Material Properties & Mechanical Testing"; group = "5. Material & Component Considerations" },
  @{ id = "6.1"; name = "Structural Integrity & Triangulation"; group = "6. Technical Understanding" },
  @{ id = "6.2"; name = "Mechanisms, Motion & Mechanical Systems"; group = "6. Technical Understanding" },
  @{ id = "6.3"; name = "Forces, Stress, Strain & Elasticity"; group = "6. Technical Understanding" },
  @{ id = "6.4"; name = "Electronic Systems, Sensors & Actuators"; group = "6. Technical Understanding" },
  @{ id = "6.5"; name = "Microcontrollers & Programmable Systems"; group = "6. Technical Understanding" },
  @{ id = "7.1"; name = "Iterative Models & Rapid Prototyping"; group = "7. Manufacturing Processes & Techniques" },
  @{ id = "7.2"; name = "Workshop Tools, Machining & Fabrication"; group = "7. Manufacturing Processes & Techniques" },
  @{ id = "7.3"; name = "Industrial Commercial Manufacture & SMT"; group = "7. Manufacturing Processes & Techniques" },
  @{ id = "7.4"; name = "Scales of Production & Lean / JIT"; group = "7. Manufacturing Processes & Techniques" },
  @{ id = "7.5"; name = "Quality Control, QA, TQM & Standards"; group = "7. Manufacturing Processes & Techniques" },
  @{ id = "8.1"; name = "Stakeholder Evaluation & Usability Testing"; group = "8. Viability of Design Solutions" },
  @{ id = "8.2"; name = "Technical Testing & Physical Validation"; group = "8. Viability of Design Solutions" },
  @{ id = "8.3"; name = "Commercial Feasibility & Cost Viability"; group = "8. Viability of Design Solutions" },
  @{ id = "9.1"; name = "Workshop Safe Practices & Risk Assessments"; group = "9. Health & Safety" },
  @{ id = "9.2"; name = "Health & Safety Legislation (HASAW, COSHH)"; group = "9. Health & Safety" }
)

$levels = @(
  @{ id = "H404"; name = "A Level (H404)" },
  @{ id = "H004"; name = "AS Level (H004)" }
)

$skills = @(
  @{ id = "maths"; name = "Maths & Calculations (25%)" },
  @{ id = "technical"; name = "Technical Principles" },
  @{ id = "design"; name = "Design & Evaluation" },
  @{ id = "practical"; name = "Practical & Manufacturing" }
)

$papers = @(
  @{ id = "2024-summer-01"; year = 2024; series = "Summer"; unit = "Principles of Design Engineering"; code = "H404/01"; level = "H404"; totalMarks = 80 },
  @{ id = "2024-summer-02"; year = 2024; series = "Summer"; unit = "Problem Solving in Design Engineering"; code = "H404/02"; level = "H404"; totalMarks = 70 },
  @{ id = "2023-summer-01"; year = 2023; series = "Summer"; unit = "Principles of Design Engineering"; code = "H404/01"; level = "H404"; totalMarks = 80 },
  @{ id = "2023-summer-02"; year = 2023; series = "Summer"; unit = "Problem Solving in Design Engineering"; code = "H404/02"; level = "H404"; totalMarks = 70 },
  @{ id = "2022-summer-01"; year = 2022; series = "Summer"; unit = "Principles of Design Engineering"; code = "H404/01"; level = "H404"; totalMarks = 80 },
  @{ id = "2022-summer-02"; year = 2022; series = "Summer"; unit = "Problem Solving in Design Engineering"; code = "H404/02"; level = "H404"; totalMarks = 70 },
  @{ id = "2021-autumn-01"; year = 2021; series = "Autumn"; unit = "Principles of Design Engineering"; code = "H404/01"; level = "H404"; totalMarks = 80 },
  @{ id = "2021-autumn-02"; year = 2021; series = "Autumn"; unit = "Problem Solving in Design Engineering"; code = "H404/02"; level = "H404"; totalMarks = 70 },
  @{ id = "2020-autumn-01"; year = 2020; series = "Autumn"; unit = "Principles of Design Engineering"; code = "H404/01"; level = "H404"; totalMarks = 80 },
  @{ id = "2020-autumn-02"; year = 2020; series = "Autumn"; unit = "Problem Solving in Design Engineering"; code = "H404/02"; level = "H404"; totalMarks = 70 },
  @{ id = "2019-summer-01"; year = 2019; series = "Summer"; unit = "Principles of Design Engineering"; code = "H404/01"; level = "H404"; totalMarks = 80 },
  @{ id = "2019-summer-02"; year = 2019; series = "Summer"; unit = "Problem Solving in Design Engineering"; code = "H404/02"; level = "H404"; totalMarks = 70 },
  @{ id = "sam-specimen-01"; year = 2018; series = "Sample Assessment"; unit = "Principles of Design Engineering"; code = "H404/01"; level = "H404"; totalMarks = 80 },
  @{ id = "sam-specimen-02"; year = 2018; series = "Sample Assessment"; unit = "Problem Solving in Design Engineering"; code = "H404/02"; level = "H404"; totalMarks = 70 }
)

$questions = @(
  # 1. Stress, Strain and Young's Modulus calculation
  @{
    id = "2023-h404-01-q1"
    paper = "2023-summer-01"
    question = "1"
    marks = 8
    page = 3
    topics = @("6.3", "5.3")
    skills = @("maths", "technical")
    summary = "Calculate the tensile stress, strain, and Young's modulus of a structural tie rod under an axial load of 45 kN."
    prompt = "A circular structural tie rod in an aerospace assembly has an initial length of 1.80 m and a cross-sectional diameter of 14.0 mm. Under a sustained tensile test load of 45.0 kN, the rod undergoes an elastic extension of 2.65 mm.<br><br><b>(a)</b> Calculate the tensile stress developed in the tie rod in MPa. [3]<br><b>(b)</b> Calculate the tensile strain developed in the tie rod. [2]<br><b>(c)</b> Determine the Young's Modulus (E) of the tie rod material in GPa. [3]"
    markscheme_text = "<b>(a) Cross-sectional area:</b><br>Radius r = 14 / 2 = 7 mm = 0.007 m<br>Area A = π × (0.007)² = 1.5394 × 10⁻⁴ m² (1 mark)<br>Stress σ = F / A = 45,000 / (1.5394 × 10⁻⁴) = 2.923 × 10⁸ Pa = <b>292.3 MPa</b> (2 marks)<br><br><b>(b) Strain:</b><br>ε = ΔL / L₀ = 0.00265 / 1.80 = <b>1.472 × 10⁻³</b> (or 0.147%) (2 marks, dimensionless)<br><br><b>(c) Young's Modulus:</b><br>E = σ / ε = (2.923 × 10⁸) / (1.472 × 10⁻³) = 1.986 × 10¹¹ Pa = <b>198.6 GPa</b> (3 marks; consistent with structural steel alloy)"
  },
  # 2. Compound Gear Train & Mechanical Advantage
  @{
    id = "2023-h404-01-q2"
    paper = "2023-summer-01"
    question = "2"
    marks = 9
    page = 5
    topics = @("6.2")
    skills = @("maths", "technical")
    summary = "Determine the total velocity ratio, output shaft speed, and output torque for a two-stage compound gearbox."
    prompt = "A motorized winch uses a two-stage compound spur gear train to lift equipment.<br>• Motor input shaft pinion A has 12 teeth and rotates at 1440 rpm.<br>• Gear B on the countershaft has 48 teeth.<br>• Pinion C on the countershaft has 15 teeth.<br>• Output gear D has 60 teeth and drives the winch drum.<br>• The electric motor provides an input torque of 4.5 Nm.<br>• The mechanical efficiency of the complete gearbox is 85%.<br><br><b>(a)</b> Calculate the total Velocity Ratio (Gear Ratio) of the gearbox. [3]<br><b>(b)</b> Calculate the rotational speed of the output winch drum in rpm. [2]<br><b>(c)</b> Calculate the available output torque delivered to the drum in Nm. [4]"
    markscheme_text = "<b>(a) Gear Ratio (VR):</b><br>Stage 1: GR₁ = Teeth_B / Teeth_A = 48 / 12 = 4:1 (1 mark)<br>Stage 2: GR₂ = Teeth_D / Teeth_C = 60 / 15 = 4:1 (1 mark)<br>Total GR = GR₁ × GR₂ = 4 × 4 = <b>16:1</b> (1 mark)<br><br><b>(b) Output Speed:</b><br>N_out = N_in / Total GR = 1440 / 16 = <b>90 rpm</b> (2 marks)<br><br><b>(c) Output Torque:</b><br>Ideal Torque = Input Torque × GR = 4.5 Nm × 16 = 72.0 Nm (2 marks)<br>With efficiency η = 85%: T_actual = 72.0 × 0.85 = <b>61.2 Nm</b> (2 marks)"
  },
  # 3. Potential Divider & Sensor Interfacing
  @{
    id = "2023-h404-01-q3"
    paper = "2023-summer-01"
    question = "3"
    marks = 8
    page = 7
    topics = @("6.4", "6.5")
    skills = @("maths", "technical")
    summary = "Design an NTC thermistor potential divider circuit and calculate output voltage and 10-bit ADC integer value."
    prompt = "An environmental monitoring module incorporates an NTC thermistor in a potential divider circuit powered by a regulated 5.0 V DC supply.<br>• At 20°C, the thermistor resistance is 10.0 kΩ.<br>• At 60°C, the thermistor resistance decreases to 2.5 kΩ.<br>• The fixed pull-down resistor R₂ has a resistance of 4.7 kΩ.<br><br><b>(a)</b> Calculate the output voltage V_out across R₂ at 20°C. [3]<br><b>(b)</b> Calculate the output voltage V_out across R₂ at 60°C. [2]<br><b>(c)</b> The output voltage is fed into a 10-bit ADC channel (0–5.0 V reference). Determine the integer digital value (0–1023) registered by the microcontroller at 60°C. [3]"
    markscheme_text = "<b>(a) V_out at 20°C:</b><br>V_out = V_in × (R₂ / (R_therm + R₂))<br>V_out = 5.0 × (4.7 / (10.0 + 4.7)) = 5.0 × (4.7 / 14.7) = <b>1.60 V</b> (3 marks)<br><br><b>(b) V_out at 60°C:</b><br>V_out = 5.0 × (4.7 / (2.5 + 4.7)) = 5.0 × (4.7 / 7.2) = <b>3.26 V</b> (2 marks)<br><br><b>(c) 10-bit ADC value at 60°C:</b><br>Resolution: 5.0 V / 1023 = 0.004887 V/step (1 mark)<br>ADC reading = (3.264 V / 5.0 V) × 1023 = 0.6528 × 1023 = <b>667.8 ≈ 668</b> (integer count) (2 marks)"
  },
  # 4. Anthropometrics & Ergonomic Clearance
  @{
    id = "2023-h404-01-q4"
    paper = "2023-summer-01"
    question = "4"
    marks = 6
    page = 9
    topics = @("1.3")
    skills = @("maths", "design")
    summary = "Apply anthropometric percentile tables to determine handle clearance and accessibility for an industrial tool."
    prompt = "An engineering designer is specifying dimensions for the hand aperture and grip diameter of a heavy-duty portable rescue cutter.<br><br><b>(a)</b> With reference to 5th and 95th percentile data, explain whether hand clearance should be designed to the 5th, 50th, or 95th percentile, giving reasons with reference to clothing allowance. [3]<br><b>(b)</b> Explain the ergonomic difference between a power grip and a precision grip, stating optimal handle diameters for each. [3]"
    markscheme_text = "<b>(a) Hand clearance percentile:</b><br>• Clearance must be designed to the <b>95th percentile male</b> hand breadth/thickness (1 mark).<br>• Reason: If designed to 5th or 50th percentile, users with larger hands would be unable to insert their hand or would experience painful pinching/entrapment (1 mark).<br>• Clothing allowance: Must add 15–20 mm extra clearance for heavy protective work gloves (1 mark).<br><br><b>(b) Power grip vs precision grip:</b><br>• Power grip: Fingers wrap around handle with thumb overlapping, providing maximum clamping force. Optimal diameter: <b>30–45 mm</b> (1.5 marks).<br>• Precision grip: Object pinched between fingertips and thumb for fine manipulation. Optimal diameter: <b>8–15 mm</b> (1.5 marks)."
  },
  # 5. DFMA & Part Consolidation
  @{
    id = "2023-h404-02-q1"
    paper = "2023-summer-02"
    question = "1"
    marks = 8
    page = 4
    topics = @("3.2", "7.3")
    skills = @("technical", "design")
    summary = "Evaluate Design for Manufacture and Assembly (DFMA) strategies to reduce assembly cycle time and part count."
    prompt = "A consumer drone manufacturer currently uses 18 separate injection-moulded bracket parts joined by 36 steel M2.5 screws to hold internal sensors and motor ESC boards.<br><br>Critically evaluate how the principles of Design for Manufacture and Assembly (DFMA) can be applied to re-engineer this assembly to lower manufacturing cycle time, reduce assembly defects, and improve end-of-life recycling. [8]"
    markscheme_text = "<b>Level 3 (6–8 marks):</b> Comprehensive technical evaluation covering specific DFMA principles.<br>• <b>Part count consolidation:</b> Integrate mounting brackets directly into the top and bottom chassis mouldings, replacing 18 separate pieces with unified mouldings.<br>• <b>Fastener elimination via snap fits:</b> Replace threaded screws with cantilever snap-fit joints and self-locating alignment ribs, eliminating tool handling and thread-tapping steps.<br>• <b>Unidirectional Z-axis assembly:</b> Ensure all components drop vertically from one direction, facilitating automated robotic pick-and-place.<br>• <b>Poka-yoke mistake proofing:</b> Use asymmetric locating lugs so PCBs cannot be seated in reverse orientation.<br>• <b>Recycling benefit:</b> Eliminating dissimilar metal screws from plastic housings accelerates shredding and granulate sorting at end of life (WEEE compliance)."
  },
  # 6. Critical Path Analysis (CPA)
  @{
    id = "2023-h404-02-q2"
    paper = "2023-summer-02"
    question = "2"
    marks = 8
    page = 6
    topics = @("4.3")
    skills = @("maths", "technical")
    summary = "Construct and analyse a Critical Path Analysis (CPA) network to determine project duration and float time."
    prompt = "An engineering firm is launching a new medical diagnostic device. The following project tasks, dependencies, and durations (in weeks) have been established:<br>• Activity A: CAD solid modeling (3 weeks) - Predecessor: None<br>• Activity B: FEA stress simulation (2 weeks) - Predecessor: A<br>• Activity C: PCB schematic and layout (4 weeks) - Predecessor: None<br>• Activity D: Prototype machining & rapid prototyping (3 weeks) - Predecessor: B<br>• Activity E: Firmware programming (5 weeks) - Predecessor: C<br>• Activity F: System integration and regulatory testing (3 weeks) - Predecessors: D and E<br><br><b>(a)</b> Identify all paths through the project network and calculate the duration of each path. [3]<br><b>(b)</b> State the Critical Path and the minimum project completion time in weeks. [2]<br><b>(c)</b> Calculate the Total Float time available for Activity B. [3]"
    markscheme_text = "<b>(a) Network Paths & Durations:</b><br>• Path 1: A -> B -> D -> F = 3 + 2 + 3 + 3 = <b>11 weeks</b> (1.5 marks)<br>• Path 2: C -> E -> F = 4 + 5 + 3 = <b>12 weeks</b> (1.5 marks)<br><br><b>(b) Critical Path:</b><br>• Critical Path: <b>C -> E -> F</b> (1 mark)<br>• Minimum project duration: <b>12 weeks</b> (1 mark)<br><br><b>(c) Total Float for Activity B:</b><br>• Path 1 has total duration 11 weeks compared to critical duration 12 weeks.<br>• Earliest Start of B: Week 3 (after A finishes).<br>• Latest Finish of B: To allow D (3 weeks) and F (3 weeks) to finish by week 12, D must start by week 9, so B must finish by week 6.<br>• Maximum time available for B = 6 - 3 = 3 weeks. Duration of B = 2 weeks.<br>• Float = 3 - 2 = <b>1 week</b> (3 marks)"
  },
  # 7. Material Selection Matrix & Ashby Optimization
  @{
    id = "2022-h404-01-q1"
    paper = "2022-summer-01"
    question = "1"
    marks = 8
    page = 3
    topics = @("5.1", "5.2")
    skills = @("technical", "design")
    summary = "Select and justify an optimal material for a robotic arm gripper bracket subjected to rapid cyclic acceleration."
    prompt = "A high-speed industrial pick-and-place robotic arm requires a new gripper mounting bracket. The component undergoes 120 cycles per minute, experiencing severe alternating inertial acceleration forces and elevated motor heat (up to 75°C).<br><br>Compare the suitability of <b>Grade 6082-T6 Aluminium Alloy</b>, <b>Mild Steel (EN3B)</b>, and <b>Carbon Fibre Reinforced Polymer (CFRP)</b> for this application, justifying your final recommendation using mechanical and thermal property comparisons. [8]"
    markscheme_text = "<b>Level 3 (6–8 marks):</b> Thorough technical comparison addressing density, stiffness, fatigue, thermal performance, and manufacturing cost.<br>• <b>Mild Steel:</b> High modulus (E ≈ 210 GPa) and low raw material cost, but high density (7850 kg/m³) increases robotic actuator motor load and reduces acceleration response; vulnerable to corrosion without plating.<br>• <b>CFRP:</b> Superior specific stiffness and ultra-low density (1550 kg/m³), virtually zero fatigue limit issues, but highest manufacturing cost (autoclave pre-preg tooling) and poor isotropic shear strength at bolted joint inserts.<br>• <b>Aluminium 6082-T6:</b> Optimal compromise; low density (2700 kg/m³ = 1/3 of steel), high yield strength (~260 MPa), excellent machinability on 5-axis CNC mills, and superb thermal conductivity (~170 W/mK) helping dissipate motor heat.<br>• <b>Justified conclusion:</b> 6082-T6 Aluminium is selected for cost-effective batch CNC fabrication while cutting inertial mass."
  },
  # 8. Breakeven Analysis & Tooling Amortization
  @{
    id = "2022-h404-01-q2"
    paper = "2022-summer-01"
    question = "2"
    marks = 7
    page = 5
    topics = @("8.3")
    skills = @("maths", "technical")
    summary = "Calculate the breakeven production volume and unit manufacturing cost for an injection-moulded smart sensor casing."
    prompt = "An electronics startup is commercializing an IoT sensor enclosure. Two manufacturing options are being considered:<br>• <b>Option 1 (CNC Machining from solid ABS):</b> Tooling & CAM setup cost = £1,500; Variable unit production cost (material + machine time) = £18.50.<br>• <b>Option 2 (Plastic Injection Moulding in ABS):</b> Hardened tool steel mould tooling cost = £24,000; Variable unit production cost (polymer pellets + cycle time) = £2.30.<br>The retail selling price is £35.00 per unit.<br><br><b>(a)</b> Calculate the production volume at which injection moulding becomes more economical than CNC machining (the crossover volume). [4]<br><b>(b)</b> If projected global demand is 25,000 units, calculate the total manufacturing cost and cost per unit for Option 2. [3]"
    markscheme_text = "<b>(a) Crossover Volume (Q):</b><br>Total Cost Option 1 = Total Cost Option 2<br>1500 + 18.50 Q = 24000 + 2.30 Q (1 mark)<br>18.50 Q - 2.30 Q = 24000 - 1500<br>16.20 Q = 22500 (2 marks)<br>Q = 22500 / 16.20 = <b>1,388.88 ≈ 1,389 units</b> (1 mark; above 1,389 units, injection moulding is cheaper).<br><br><b>(b) Cost for Option 2 at 25,000 units:</b><br>Total Cost = Fixed Tooling + (Variable Cost × Q)<br>Total Cost = £24,000 + (£2.30 × 25,000) = £24,000 + £57,500 = <b>£81,500</b> (2 marks)<br>Unit Cost = £81,500 / 25,000 = <b>£3.26 per unit</b> (1 mark)"
  },
  # 9. Workshop Safety & COSHH Risk Assessment
  @{
    id = "2022-h404-02-q1"
    paper = "2022-summer-02"
    question = "1"
    marks = 6
    page = 3
    topics = @("9.1", "9.2")
    skills = @("technical", "practical")
    summary = "Apply COSHH regulations and the Hierarchy of Control to mitigate hazards during carbon fibre lay-up and trimming."
    prompt = "During the prototyping of a carbon fibre reinforced polymer (CFRP) chassis, a technician is required to mix epoxy resin with amine hardener, vacuum bag the laminate, and trim the cured edges using a diamond-grit bandsaw.<br><br><b>(a)</b> Identify two distinct health hazards under the COSHH 2002 regulations associated with this process. [2]<br><b>(b)</b> Explain how the Hierarchy of Control should be applied to protect technicians, explaining why PPE is considered the last line of defence. [4]"
    markscheme_text = "<b>(a) COSHH Hazards:</b><br>• Chemical sensitization and skin dermatitis caused by direct contact with unreacted liquid epoxy resin or amine hardeners (1 mark).<br>• Inhalation of microscopic airborne carbon fibre dust particulates during dry bandsaw trimming, causing respiratory irritation and potential lung tissue scarring (1 mark).<br><br><b>(b) Hierarchy of Control Application:</b><br>• <b>Engineering Controls (Priority):</b> Install Local Exhaust Ventilation (LEV) capture hoods and HEPA downdraft extraction tables directly at the bandsaw trimming station; conduct resin mixing in a dedicated fume extraction enclosure (2 marks).<br>• <b>Administrative Controls:</b> Implement standard operating procedures (SOP), restrict workshop access, and provide COSHH safety training (1 mark).<br>• <b>PPE as last line of defence:</b> Nitrile chemical-resistant gloves, eye goggles, and FFP3 particulate respirator. PPE is the lowest tier because it relies on correct fit, user compliance, and does not remove the hazard from the shared room environment (1 mark)."
  },
  # 10. Non-Destructive Testing (NDT)
  @{
    id = "2021-h404-01-q1"
    paper = "2021-autumn-01"
    question = "1"
    marks = 6
    page = 4
    topics = @("8.2")
    skills = @("technical", "practical")
    summary = "Compare Ultrasonic Testing (UT) and Dye Penetrant Inspection (DPI) for verifying critical welded joints."
    prompt = "A welded tubular roll-cage for a high-performance off-road buggy must be verified for structural integrity prior to competition.<br><br>Compare the principles, advantages, and limitations of <b>Dye Penetrant Inspection (DPI)</b> and <b>Ultrasonic Testing (UT)</b> for detecting welding defects in this tubular structure. [6]"
    markscheme_text = "<b>Dye Penetrant Inspection (DPI):</b><br>• Principle: Clean surface, spray fluorescent/red penetrating dye which draws into cracks by capillary action. Wipe off surface dye, spray chalk developer to draw out entrapped dye (1.5 marks).<br>• Pros/Cons: Very cheap, fast, portable, easy to interpret; BUT only detects cracks that are <b>open to the external surface</b>; completely blind to internal weld porosity or sub-surface cracks (1.5 marks).<br><br><b>Ultrasonic Testing (UT):</b><br>• Principle: High-frequency piezoelectric transducer transmits ultrasound pulses (2–10 MHz) into steel. Sound reflects from back wall and internal defects; reflected signal pulse travel time reveals depth and defect size on oscilloscope (1.5 marks).<br>• Pros/Cons: Detects internal flaws, inclusions, lack of root fusion deep inside the weld; non-hazardous; BUT requires skilled calibrated operator, acoustic couplant gel, and difficult on thin complex curved tubular joints (1.5 marks)."
  },
  # 11. 2D Nesting & Sheet Tessellation Calculation
  @{
    id = "2021-h404-01-q2"
    paper = "2021-autumn-01"
    question = "2"
    marks = 6
    page = 6
    topics = @("3.3")
    skills = @("maths", "technical")
    summary = "Calculate laser-cut sheet metal yield, kerf scrap, and raw material utilization efficiency."
    prompt = "A batch of 400 equilateral triangular steel brackets (side length s = 120 mm) is to be laser cut from standard sheet steel measuring 2000 mm × 1000 mm.<br><br><b>(a)</b> Calculate the surface area of a single equilateral triangular bracket in mm². [2]<br><b>(b)</b> The designer uses a tessellated layout that achieves a packing density of 82% of the sheet area.<br>Calculate the total area of scrap steel produced in m² and the percentage material waste. [4]"
    markscheme_text = "<b>(a) Area of Equilateral Triangle:</b><br>Height h = s × sin(60°) = 120 × 0.8660 = 103.92 mm (1 mark)<br>Area = 0.5 × base × height = 0.5 × 120 × 103.92 = <b>6,235.4 mm²</b> (1 mark)<br><br><b>(b) Scrap Steel Calculation:</b><br>Total sheet area = 2000 mm × 1000 mm = 2,000,000 mm² = 2.00 m² (1 mark)<br>With 82% packing yield, useful metal = 2.00 × 0.82 = 1.64 m² (1 mark)<br>Scrap metal area = 2.00 m² - 1.64 m² = <b>0.36 m²</b> (1 mark)<br>Percentage material waste = (0.36 / 2.00) × 100% = <b>18.0% scrap</b> (1 mark)"
  },
  # 12. Triangulation & Truss Forces
  @{
    id = "2020-h404-01-q1"
    paper = "2020-autumn-01"
    question = "1"
    marks = 7
    page = 3
    topics = @("6.1", "6.3")
    skills = @("maths", "technical")
    summary = "Resolve forces at a pin-jointed truss node to determine whether struts are in tension or compression."
    prompt = "A lightweight mobile gantry crane features a pin-jointed structural steel truss. At top joint Node B, a vertical downward load of 28 kN is supported by two members: strut AB angled at 45° to the vertical, and strut BC angled at 30° to the vertical.<br><br><b>(a)</b> Explain why triangulation is universally utilized in structural engineering frameworks. [2]<br><b>(b)</b> Using vector resolution of forces (ΣF_x = 0, ΣF_y = 0), calculate the magnitude of force in members AB and BC, identifying which member is in tension and which is in compression. [5]"
    markscheme_text = "<b>(a) Triangulation Principle:</b><br>A triangle is the only geometric polygon that is inherently rigid; its internal angles cannot deform without altering member lengths. Pin-jointed trusses convert bending moments into pure axial tension or compression forces (2 marks).<br><br><b>(b) Force Vector Resolution:</b><br>Let F_AB and F_BC be the compressive forces in the struts pushing up against Node B.<br>Horizontal equilibrium: ΣF_x = 0<br>F_AB sin(45°) - F_BC sin(30°) = 0<br>F_AB (0.7071) = F_BC (0.5000) => F_BC = 1.414 F_AB (2 marks)<br>Vertical equilibrium: ΣF_y = 0<br>F_AB cos(45°) + F_BC cos(30°) = 28 kN<br>F_AB (0.7071) + (1.414 F_AB)(0.8660) = 28<br>0.7071 F_AB + 1.2247 F_AB = 28 => 1.9318 F_AB = 28<br><b>F_AB = 14.49 kN (Compression)</b> (2 marks)<br>F_BC = 1.414 × 14.49 = <b>20.49 kN (Compression)</b> (1 mark)"
  },
  # 13. Life Cycle Assessment (LCA) Synoptic Essay
  @{
    id = "2019-h404-01-q1"
    paper = "2019-summer-01"
    question = "1"
    marks = 12
    page = 8
    topics = @("3.1", "5.2", "7.3")
    skills = @("design", "technical")
    summary = "Extended synoptic response comparing LCA and circular economy viability of steel vs carbon fibre bicycle frames."
    prompt = "A specialist bicycle manufacturer is deciding whether to manufacture a new commuter bicycle frame from <b>hydroformed 6061 aluminium alloy</b> or <b>carbon fibre reinforced polymer (CFRP)</b>.<br><br>Critically evaluate both materials across all stages of a Life Cycle Assessment (LCA), including raw material extraction, manufacturing energy, operational lifespan and fatigue resistance, and end-of-life recycling within a circular economy. Conclude with a justified recommendation for a sustainable commuter product. [12]"
    markscheme_text = "<b>Level 4 (10–12 marks):</b> Sophisticated synoptic response balancing technical material properties against environmental LCA metrics.<br>• <b>Raw Material Extraction:</b> Bauxite mining for aluminium is energy-intensive (Hall-Héroult smelting requires ~15 kWh/kg), but recycled secondary aluminium uses 95% less energy. Carbon fibre synthesis requires high-temperature pyrolyzation of polyacrylonitrile (PAN) precursor at >1200°C under inert gas with immense embodied energy.<br>• <b>Manufacture:</b> Aluminium frames use automated hydroforming and robotic TIG welding with high throughput and low defect rates. CFRP requires manual pre-preg lay-up, vacuum bagging, and autoclave cycle times, generating hazardous resin scraps.<br>• <b>Operational Life:</b> CFRP has no fatigue limit under design stress and will not corrode in wet commuting environments; however, it is susceptible to catastrophic hidden delamination upon impact. Aluminium provides ductile deformation before failure but has a finite fatigue life under road vibration.<br>• <b>End of Life:</b> Aluminium is 100% endlessly recyclable through magnetic/eddy-current sorting and remelting with negligible degradation. CFRP cannot be melted; recycling relies on pyrolysis or chemical solvolysis, which shortens fibres, downcycling it to non-structural chopped fillers.<br>• <b>Conclusion:</b> Aluminium is strongly recommended for commuter sustainability due to closed-loop circular recyclability and lower total lifecycle carbon footprint."
  },
  # 14. Pulse Width Modulation (PWM) & DC Motor Drive
  @{
    id = "2019-h404-02-q1"
    paper = "2019-summer-02"
    question = "1"
    marks = 7
    page = 4
    topics = @("6.4", "6.5")
    skills = @("maths", "technical")
    summary = "Calculate PWM duty cycle, average output voltage, and power delivered to a 12V DC motor."
    prompt = "A microcontroller controls the speed of a 12.0 V DC conveyor drive motor using Pulse Width Modulation (PWM) at a switching frequency of 20 kHz.<br>• Total PWM period T = 50 µs.<br>• High-state pulse width t_on = 32.5 µs.<br>• Motor winding resistance R = 4.8 Ω.<br><br><b>(a)</b> Calculate the Duty Cycle percentage of the PWM signal. [2]<br><b>(b)</b> Calculate the average effective voltage applied to the motor terminals. [2]<br><b>(c)</b> Calculate the electrical power dissipated by the motor assuming ideal switching. [3]"
    markscheme_text = "<b>(a) Duty Cycle:</b><br>Duty Cycle = (t_on / T) × 100% = (32.5 µs / 50.0 µs) × 100% = <b>65.0%</b> (2 marks)<br><br><b>(b) Average Voltage:</b><br>V_avg = V_supply × Duty Cycle = 12.0 V × 0.65 = <b>7.80 V</b> (2 marks)<br><br><b>(c) Electrical Power:</b><br>Current I_avg = V_avg / R = 7.80 V / 4.8 Ω = 1.625 A (1.5 marks)<br>Power P = V_avg × I_avg = (7.80)² / 4.8 = <b>12.675 W ≈ 12.7 W</b> (1.5 marks)"
  }
)

$outObj = [ordered]@{
  topics = $topics
  levels = $levels
  skills = $skills
  papers = $papers
  questions = $questions
}

$json = $outObj | ConvertTo-Json -Depth 6
[System.IO.File]::WriteAllText($outPath, $json, [System.Text.Encoding]::UTF8)
Write-Host "Generated questions.json with $($questions.Count) questions and $($papers.Count) papers at $outPath"
