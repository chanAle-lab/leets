# build_cheatsheets.ps1
$ErrorActionPreference = "Stop"

$baseDir = "C:\Users\Alexander\.gemini\antigravity\scratch\leets"
$cheatsDir = Join-Path $baseDir "cheatsheets"
if (-not (Test-Path $cheatsDir)) {
    New-Item -ItemType Directory -Path $cheatsDir -Force | Out-Null
}

$cheats = [ordered]@{}

function Add-Sheet {
    param(
        [string]$id,
        [string]$title,
        [string]$group,
        [string]$spec,
        [array]$sections
    )
    $cheats[$id] = [ordered]@{
        title = $title
        group = $group
        spec = $spec
        sections = $sections
    }
}

# 1.1
Add-Sheet "1.1" "Topic 1.1 · Contexts for Design Solutions" "1. Identifying Requirements" "Exploring contexts: environmental & surroundings, user requirements, economic & market considerations, product opportunities" @(
    @{
        heading = "Context Dependency & Operating Surroundings"
        points = @(
            "<b>Context dependency:</b> All design practice is context dependent. An engineered solution cannot be validated in isolation; it must satisfy the precise physical, social, and operational conditions of its intended deployment.",
            "<b>Environmental and surroundings analysis:</b> Investigating extreme ambient temperatures, humidity, UV radiation exposure, vibration spectra, airborne particulate ingress (IP rating), chemical exposure, and installation envelope.",
            "<b>Economic and market constraints:</b> Analysing purchasing power of target demographics, competitor unit pricing benchmarks, target BOM (Bill of Materials) cost ceilings, and commercial return on investment (ROI).",
            "<b>Product opportunities:</b> Identifying market gaps, underserved user niches, regulatory shifts (e.g. decarbonisation mandates), or technological readiness improvements that enable novel solutions."
        )
    },
    @{
        heading = "Primary Users & Stakeholder Ecosystem"
        points = @(
            "<b>Primary user:</b> The direct operator interacting with the product's controls and user interface on a routine operational basis.",
            "<b>Wider stakeholders:</b> Maintenance technicians, installation teams, safety certifiers, logistics handlers, and recycling facilities whose operational requirements shape product architecture.",
            "<b>Contextual inquiry:</b> Direct ethnographic observation and semi-structured interviews in the real operational environment to reveal tacit needs that users rarely express in surveys."
        )
    }
)

# 1.2
Add-Sheet "1.2" "Topic 1.2 · Stakeholder Analysis & Enterprise" "1. Identifying Requirements" "Stakeholder analysis, User-Centred Design (UCD), SWOT analysis, focus groups, market research, enterprise and routes to innovation" @(
    @{
        heading = "User-Centred Design (UCD) & Investigation Methods"
        points = @(
            "<b>User-Centred Design (UCD):</b> An iterative design philosophy (ISO 9241-210) placing the explicit needs, cognitive capabilities, and physical ergonomics of end-users at every development phase.",
            "<b>SWOT analysis:</b> Systematic matrix mapping internal Strengths and Weaknesses against external Opportunities and Threats to guide strategic design engineering decisions.",
            "<b>Focus groups & qualitative observation:</b> Structured interactive sessions evaluating concept prototypes, aesthetic styling, tactile switch resistance, and feedback clarity.",
            "<b>Market research & gap analysis:</b> Quantitative demographic surveys, TAM/SAM/SOM market sizing, and identifying price-performance voids in current competitor product lines."
        )
    },
    @{
        heading = "Enterprise & Routes to Innovation"
        points = @(
            "<b>Entrepreneurship:</b> The commercial initiative and risk management required to translate technical inventions into viable market solutions.",
            "<b>Commercial partnerships & licensing:</b> Teaming with established Tier-1 manufacturers or licensing patented IP for royalties to leverage existing supply chains and global distribution.",
            "<b>Venture capital & angel investment:</b> Early-stage equity funding to finance high capital expenditure tooling (e.g. injection moulds, stamping dies) and CE/UKCA regulatory compliance testing.",
            "<b>Crowdfunding models:</b> Pre-sales platforms (e.g. Kickstarter) used to validate consumer demand, establish early product evangelists, and fund initial production runs without diluting equity."
        )
    }
)

# 1.3
Add-Sheet "1.3" "Topic 1.3 · Usability, Inclusivity & Ergonomics" "1. Identifying Requirements" "Usability analysis, inclusive design, anthropometric data (5th, 50th, 95th percentiles), user comfort, control layouts, UI design" @(
    @{
        heading = "Anthropometrics & Percentile Design Rules"
        points = @(
            "<b>Anthropometry:</b> The measurement of physical dimensions, reach boundaries, biomechanical leverage, and strength capacities of human populations.",
            "<b>5th to 95th percentile envelope:</b> Standard engineering rule to accommodate at least 90% of the target user population.",
            "<b>Reach dimensions (5th percentile):</b> Operational reach, button distances, and shelf heights must be accessible to smaller users; designed according to the <b>5th percentile female</b> data.",
            "<b>Clearance dimensions (95th percentile):</b> Hand clearance, legroom, door apertures, and handle openings must fit larger users; designed according to the <b>95th percentile male</b> data.",
            "<b>Design for adjustability:</b> Incorporating mechanical sliders, telescopic linkages, or height adjustment mechanisms to comfortably span across the entire 5th to 95th percentile spectrum."
        )
    },
    @{
        heading = "Ergonomics & Human-Machine Interfaces (HMI)"
        points = @(
            "<b>Physical ergonomics:</b> Optimising grip diameters (power grip 30–45 mm; precision grip 8–15 mm), reducing repetitive strain injury (RSI) risks, and maintaining neutral wrist postures.",
            "<b>Cognitive ergonomics:</b> Minimising mental workload, preventing control confusion, intuitive layout mapping (e.g. clockwise rotation increases output), and sensory confirmation feedback within 100ms.",
            "<b>Inclusive design:</b> Creating accessible products that accommodate individuals with varying physical, sensory, or cognitive capabilities without requiring stigmatising adaptations (BS 8300 / Equality Act 2010)."
        )
    }
)

# 2.1
Add-Sheet "2.1" "Topic 2.1 · Product Analysis & Evaluation" "2. Existing Products & Practice" "Product analysis, disassembly, ACCESS FM, materials, construction methods, functionality, ergonomics, branding & commercial viability" @(
    @{
        heading = "Systematic Product Disassembly & Reverse Engineering"
        points = @(
            "<b>Product disassembly:</b> Methodical physical teardown of existing market products to analyse component count, mechanical sub-systems, fastening choices, and manufacturing workflows.",
            "<b>ACCESS FM evaluation:</b> Aesthetics, Cost, Customer, Environment, Size, Safety, Function, Material. Standard evaluative framework for rigorous product deconstruction.",
            "<b>Bill of Materials (BOM) analysis:</b> Cataloguing each discrete part, material type, net weight, standard fastener specifications (e.g. DIN 912 screws), and estimated unit production costs."
        )
    },
    @{
        heading = "Fitness for Purpose & Benchmarking"
        points = @(
            "<b>Fitness for purpose:</b> Objective engineering verification that a product meets all functional, environmental, and lifespan criteria specified in its design brief under operational duty cycles.",
            "<b>Branding and aesthetic identity:</b> Evaluating surface finishes, colourways, haptics, and brand coherence that drive consumer quality perception.",
            "<b>Enhancement opportunities:</b> Identifying structural fatigue vulnerabilities, excessive thermal buildup, redundant parts, or difficult assembly operations ripe for value-engineering redesign."
        )
    }
)

# 2.2
Add-Sheet "2.2" "Topic 2.2 · Technological Developments & Innovation" "2. Existing Products & Practice" "Emerging technologies, blue sky innovation vs incremental innovation, disruptive technologies, smart systems, Industry 4.0" @(
    @{
        heading = "Innovation Types & Technology Lifecycles"
        points = @(
            "<b>Incremental innovation:</b> Successive, low-risk refinements to existing products (e.g. shaving 5% component weight, increasing battery energy density by 3%, firmware updates).",
            "<b>Disruptive / Blue sky innovation:</b> Radically novel technology that displaces entrenched markets or creates entirely new industries (e.g. solid-state batteries, generative AI-driven design, electric vehicle skateboards).",
            "<b>Technology Readiness Levels (TRL):</b> NASA/EU scale from TRL 1 (basic principles observed) to TRL 9 (proven in full operational commercial environment)."
        )
    },
    @{
        heading = "Emerging Engineering Technologies"
        points = @(
            "<b>Additive metal manufacturing (DMLS):</b> Direct Metal Laser Sintering enabling complex generative internal cooling channels impossible via subtractive milling.",
            "<b>Internet of Things (IoT) edge computing:</b> Integrating low-power sensors and microcontrollers with cloud connectivity for real-time predictive maintenance telemetry.",
            "<b>Advanced composites & meta-materials:</b> Tailored carbon-nanotube matrices and auxetic structures exhibiting negative Poisson's ratio for ultra-high impact absorption."
        )
    }
)

# 2.3
Add-Sheet "2.3" "Topic 2.3 · Historical Movements & Influential Engineers" "2. Existing Products & Practice" "Design movements (Arts & Crafts, Bauhaus, Modernism, Postmodernism/Memphis), influential figures (Rams, Dyson, Brunel), social & environmental legacy" @(
    @{
        heading = "Major Design & Engineering Movements"
        points = @(
            "<b>Arts & Crafts (1880–1920):</b> William Morris; emphasis on handcrafted integrity, honest use of natural materials, and moral rejection of dehumanising industrial mass manufacture.",
            "<b>Bauhaus (1919–1933):</b> Walter Gropius; 'Form follows function', bridging art with industrial manufacturing, geometric purity, tubular steel, glass, and modular architecture.",
            "<b>Modernism & International Style:</b> Mies van der Rohe ('Less is more'); structural steel, reinforced concrete, clean unadorned surfaces, standardization.",
            "<b>Memphis Group (1981–1988):</b> Ettore Sottsass; colourful rebellion against cold functionalism, combining geometric whimsy, patterned laminates, and provocative postmodern aesthetics."
        )
    },
    @{
        heading = "Influential Design Engineers & Philosophy"
        points = @(
            "<b>Dieter Rams:</b> Chief design officer at Braun; 'Good design is as little design as possible'. Established the iconic 10 Principles of Good Design emphasizing utility, honesty, unobtrusiveness, and longevity.",
            "<b>Sir James Dyson:</b> Cyclonic air separation technology; executed 5,127 functional prototypes to eliminate vacuum bags, embodying persistence through empirical test rigs.",
            "<b>Isambard Kingdom Brunel:</b> Victorian engineering giant; pioneered screw-propelled iron steamships (SS Great Britain) and audacious suspension bridges, calculating structural limits with innovative ironwork."
        )
    }
)

# 2.4
Add-Sheet "2.4" "Topic 2.4 · Product Lifecycles & Marketing Models" "2. Existing Products & Practice" "Product life cycle stages (introduction, growth, maturity, decline), lifecycle extension strategies, digital marketing & social media models" @(
    @{
        heading = "Product Life Cycle (PLC) Dynamics"
        points = @(
            "<b>Introduction phase:</b> High development & tooling cost amortization, low sales volume, negative cash flow; requires targeted marketing to innovators.",
            "<b>Growth phase:</b> Rapid market adoption, unit production costs drop via manufacturing economies of scale, distribution channels expand.",
            "<b>Maturity phase:</b> Peak sales, market saturation, intense competitor price pressure; cash generation peaks and funds subsequent R&D pipelines.",
            "<b>Decline phase:</b> Falling sales due to technological obsolescence or shifting consumer habits; leads to product discontinuation or harvest strategy."
        )
    },
    @{
        heading = "Extension Strategies & Digital Models"
        points = @(
            "<b>Lifecycle extension strategies:</b> Re-engineering aesthetic facelifts, software feature upgrades, entering emerging geographic markets, or re-targeting alternative commercial applications.",
            "<b>Direct-to-Consumer (D2C) & viral models:</b> Bypassing traditional retail margins through digital channels, influencer unboxings, and community crowdfunding feedback."
        )
    }
)

# 3.1
Add-Sheet "3.1" "Topic 3.1 · Social, Moral, Ethical & Environmental Factors" "3. Implications of Wider Issues" "Life Cycle Assessment (LCA), carbon footprint, resource depletion, planned obsolescence, consumer buying trends, RoHS & WEEE directives" @(
    @{
        heading = "Life Cycle Assessment (LCA) & Environmental Footprint"
        points = @(
            "<b>Life Cycle Assessment (LCA):</b> Standardized ISO 14040 methodology evaluating total environmental impact across 5 phases: 1. Raw Material Extraction -> 2. Material Processing -> 3. Manufacture -> 4. Operational Use -> 5. End of Life (EOL).",
            "<b>Embodied energy:</b> The cumulative non-renewable primary energy consumed from mining and refining raw materials to finished assembly.",
            "<b>Carbon footprint:</b> Total equivalent carbon dioxide ($CO_2e$) emissions generated across the entire product lifecycle.",
            "<b>Circular economy:</b> Regenerative industrial framework replacing linear 'take-make-dispose' with closed-loop biological and technical nutrient loops (Ellen MacArthur Foundation)."
        )
    },
    @{
        heading = "Planned Obsolescence & Statutory Directives"
        points = @(
            "<b>Planned obsolescence types:</b> Technological (incompatible communication ports/software), functional (glued-in batteries, artificial component wear limits), and psychological (stylistic dating).",
            "<b>RoHS Directive:</b> Restriction of Hazardous Substances; strictly restricts hazardous materials in electronic products (Lead Pb, Mercury Hg, Cadmium Cd, Hexavalent Chromium Cr(VI), PBB, PBDE).",
            "<b>WEEE Directive:</b> Waste Electrical and Electronic Equipment; legally mandates OEM take-back, treatment, and recycling of post-consumer electronic waste."
        )
    }
)

# 3.2
Add-Sheet "3.2" "Topic 3.2 · Design for Manufacture (DFM) & Sustainability" "3. Implications of Wider Issues" "DFM principles, part count reduction, modularity, repairability, Ethical Trading Initiative (ETI), eco-materials, upcycling" @(
    @{
        heading = "Design for Manufacture and Assembly (DFMA)"
        points = @(
            "<b>Part count minimisation:</b> Integrating multiple functional features (e.g. snap fits, bearing mounts, wire clips) into unified injection mouldings or die castings.",
            "<b>Poka-Yoke (Mistake proofing):</b> Asymmetric locator pins, keyed plugs, and polarized connectors making incorrect manual assembly physically impossible.",
            "<b>Top-down unidirectional assembly:</b> Designing parts to stack vertically in the Z-axis, eliminating tool reorientation and accelerating robotic assembly.",
            "<b>Standardisation:</b> Restricting hardware to single screw sizes (e.g. M3 Torx throughout), eliminating tool changes during workshop and factory assembly.",
            "<b>Design for Disassembly (DFD):</b> Using threaded or snap fasteners rather than irreversible chemical adhesives or sonic welds to facilitate maintenance and component recycling."
        )
    },
    @{
        heading = "Ethical Trade & Sustainable Materials"
        points = @(
            "<b>Ethical Trading Initiative (ETI):</b> Global code requiring fair living wages, freely chosen employment, safe working conditions, reasonable hours, and zero child labour in supply chains.",
            "<b>Eco-materials:</b> Certified sustainable timber (FSC/PEFC), bio-based resins, recycled rPET/rHDPE polymers, and solvent-free waterborne powder coatings.",
            "<b>Upcycling:</b> Repurposing manufacturing scrap or discarded products into higher-value engineered products without energy-intensive melting or re-refining."
        )
    }
)

# 3.3
Add-Sheet "3.3" "Topic 3.3 · Optimum Material Use & Stock Forms" "3. Implications of Wider Issues" "Material optimization, 2D nesting & tessellation, standard stock forms, raw material costing, scrap reduction" @(
    @{
        heading = "Nesting, Tessellation & Scrap Minimisation"
        points = @(
            "<b>2D Nesting algorithms:</b> CAD/CAM software mathematically optimizing part orientation and layout on standard sheet stock to maximize material yield.",
            "<b>Tessellation:</b> Geometrically interlocking identical profiles with common cutting edges, eliminating skeleton scrap and reducing laser/plasma cutting distance.",
            "<b>Scrap percentage formula:</b> $\\text{Scrap \\%} = \\frac{\\text{Total Raw Stock Area} - \\text{Total Useful Part Area}}{\\text{Total Raw Stock Area}} \\times 100\\%$."
        )
    },
    @{
        heading = "Standard Commercial Stock Forms"
        points = @(
            "<b>Stock forms:</b> Round bar, square bar, hexagonal bar, angle (L-section), channel (U-section), box section (SHS/RHS), I-beam, flat bar, tube, sheet and plate.",
            "<b>Cost advantages of standard stock:</b> Eliminates bespoke extrusion die setup costs, ensures immediate off-the-shelf availability, and guarantees certified mechanical properties."
        )
    }
)

# 3.4
Add-Sheet "3.4" "Topic 3.4 · Distribution Logistics & Intellectual Property" "3. Implications of Wider Issues" "Distribution logistics, packaging optimization, Intellectual Property: patents, registered designs, trademarks, copyright, design rights" @(
    @{
        heading = "Freight Logistics & Packaging Engineering"
        points = @(
            "<b>Volumetric cargo efficiency:</b> Sizing primary and secondary packaging to interlock without overhang on standard EUR pallets (1200 × 800 mm) or ISO containers (20ft / 40ft).",
            "<b>Transport modes & emissions:</b> Maritime shipping (lowest $CO_2$ per tonne-km) vs rail, road freight, and air freight (highest carbon emissions and cost per kg).",
            "<b>Sustainable packaging:</b> Corrugated single/double wall board (high compressive crush strength, biodegradable) replacing expanded polystyrene (EPS) with moulded pulp or mushroom mycelium."
        )
    },
    @{
        heading = "Intellectual Property (IP) Law"
        points = @(
            "<b>Patents:</b> Grants up to <b>20 years</b> legal monopoly over novel technical inventions, mechanical movements, or industrial processes. Must possess novelty, inventive step, and industrial applicability.",
            "<b>Registered Designs:</b> Protects aesthetic visual appearance, shape, contours, and decorative ornamentation for up to <b>25 years</b> (renewed every 5 years).",
            "<b>Trademarks:</b> Protects distinctive brand names, logos, symbols, and slogans indefinitely, subject to 10-year renewal fees.",
            "<b>Copyright:</b> Automatic legal protection for original technical drawings, schematics, source code, and user manuals (author's life + 70 years).",
            "<b>Unregistered Design Rights:</b> Protects 3D functional shape automatically in the UK for 10 years from first commercial sale (or 15 years from creation)."
        )
    }
)

# 3.5
Add-Sheet "3.5" "Topic 3.5 · Energy Sources, Storage & Efficiency" "3. Implications of Wider Issues" "Primary energy sources, battery chemistries (Li-ion, LiFePO4, NiMH), supercapacitors, power transmission, efficiency calculations" @(
    @{
        heading = "Energy Storage Technologies"
        points = @(
            "<b>Lithium-ion (NMC):</b> High specific energy density (~250 Wh/kg), nominal 3.7V per cell, high energy-to-weight; requires Battery Management System (BMS) for thermal runaway prevention.",
            "<b>Lithium Iron Phosphate (LiFePO4 / LFP):</b> Extremely stable chemistry, high thermal runaway ceiling, >3000 charge cycles, 3.2V nominal; ideal for stationary energy and robust EVs.",
            "<b>Supercapacitors:</b> Electrostatic double-layer storage; ultra-rapid charge/discharge, virtually unlimited cycle life, low specific energy; handles regenerative braking burst loads."
        )
    },
    @{
        heading = "Energy Transmission & Efficiency"
        points = @(
            "<b>Energy efficiency formula:</b> $\\text{Efficiency } \\eta = \\frac{\\text{Useful Output Power / Energy}}{\\text{Total Input Power / Energy}} \\times 100\\%$.",
            "<b>I^2R transmission loss:</b> Electrical conductor resistive power loss scales with the square of current ($P_{loss} = I^2 R$). High-voltage transmission reduces current and cuts transmission heat losses.",
            "<b>Energy harvesting:</b> Piezoelectric vibration harvesting, Peltier-Seebeck thermoelectric generators, and micro photovoltaic cells powering autonomous low-energy IoT nodes."
        )
    }
)

# 3.6
Add-Sheet "3.6" "Topic 3.6 · Cross-Disciplinary STEM in Engineering" "3. Implications of Wider Issues" "Applying mathematics, physics, and materials science to engineering decisions, interpreting technical datasheets and curves" @(
    @{
        heading = "STEM Integration & Datasheet Analysis"
        points = @(
            "<b>Applied mathematics in engineering:</b> Trigonometric vector resolution for truss analysis, calculus for dynamic rate of change, and statistics for manufacturing quality control.",
            "<b>Physics principles:</b> Conservation of energy, Newton's laws of motion, Faraday's law of induction, thermodynamics of heat transfer (conduction, convection, radiation).",
            "<b>Interpreting technical datasheets:</b> Deriving maximum continuous drain current ($I_D$), thermal junction-to-ambient resistance ($\\theta_{JA}$), and stress-strain curves to ensure components operate within their Safe Operating Area (SOA)."
        )
    }
)

# 4.1
Add-Sheet "4.1" "Topic 4.1 · 2D & 3D Sketching, Drawing & Modelling" "4. Design Thinking & Communication" "Sketching, 3rd angle orthographic projection (BS 8888), section views, isometric, circuit & system block diagrams, flowcharts" @(
    @{
        heading = "BS 8888 Engineering Drawing Standards"
        points = @(
            "<b>Third Angle Orthographic Projection:</b> Universal standard engineering drawing layout: Plan view positioned directly above Front elevation; End elevation positioned on the side viewed.",
            "<b>Line conventions (BS 8888):</b> Continuous thick (visible edges), Continuous thin (dimension, leader, and projection lines), Dashed thin (hidden details), Chain thin (centre lines, axes of symmetry).",
            "<b>Sectional views:</b> Hatched at 45° to reveal interior bores and chambers. Standard rule: webs, ribs, shafts, bolts, nuts, and pins are <b>never hatched</b> in longitudinal section.",
            "<b>Dimensioning conventions:</b> Dimensions placed above horizontal dimension lines or to the left of vertical lines; arrowheads sharp and filled; leader lines never crossing dimension lines."
        )
    },
    @{
        heading = "System Visualisations & Schematic Diagrams"
        points = @(
            "<b>System block diagrams:</b> High-level signal flow decomposition: Input Sensor -> Conditioning Circuit -> Microcontroller Process -> Driver Stage -> Mechanical Actuator.",
            "<b>Circuit schematics:</b> Standardized electronic component symbols (resistors, NPN/MOSFET transistors, diodes, capacitors) showing logical electrical connectivity.",
            "<b>Flowcharts:</b> Program logic flow; Terminals (oval), Operations/Processes (rectangle), Input/Output (parallelogram), Decisions/Conditionals (diamond)."
        )
    }
)

# 4.2
Add-Sheet "4.2" "Topic 4.2 · Digital Engineering Tools (CAD, CAE, FEA)" "4. Design Thinking & Communication" "Parametric 3D CAD solid modelling, assembly mates, CAE simulation, Finite Element Analysis (FEA), CFD, digital twins" @(
    @{
        heading = "Parametric CAD & Assembly Modeling"
        points = @(
            "<b>Parametric solid modelling:</b> Feature-based tree modeling (Extrude, Revolve, Sweep, Loft, Cut, Fillet) where dimensions drive geometry; altering a root sketch dynamically propagates across drawings and assemblies.",
            "<b>Kinematic assembly mates:</b> Coincident, concentric, parallel, tangent, and gear mechanical mates allowing digital verification of range of motion and collision detection.",
            "<b>DFM digital validation:</b> Draft angle inspection to ensure plastic injection mould release; wall thickness analysis to eliminate sink marks and internal voids."
        )
    },
    @{
        heading = "CAE, Finite Element Analysis (FEA) & Simulation"
        points = @(
            "<b>Finite Element Analysis (FEA):</b> Discretising continuous solid models into a mesh of finite elements (tetrahedral/hexahedral) to calculate displacement and von Mises stress tensors under mechanical loads.",
            "<b>Stress concentration factors ($K_t$):</b> Detecting severe stress concentrations at sharp internal corners, keyways, and bolt holes; mitigated by adding generous transition fillets.",
            "<b>Computational Fluid Dynamics (CFD):</b> Simulating airflow velocity vectors, boundary layer separation, aerodynamic drag ($C_d$), and thermal convective heat dissipation across heatsinks."
        )
    }
)

# 4.3
Add-Sheet "4.3" "Topic 4.3 · Systems Thinking & Project Management" "4. Design Thinking & Communication" "Systems thinking, iterative loop (explore-create-evaluate), UI/Data/Process design, Critical Path Analysis (CPA), Agile/Scrum, Six Sigma" @(
    @{
        heading = "Systems Thinking & Sub-System Design"
        points = @(
            "<b>Systems thinking:</b> Holistic analysis focusing on interrelationships and feedback loops between constituent mechanical, electronic, and software sub-assemblies.",
            "<b>Three engineering sub-tasks:</b> 1. <b>User-Interface Design</b> (tactile feel, display ergonomics), 2. <b>Data Design</b> (signal protocols, memory budgets, bus bandwidth), 3. <b>Process Design</b> (state machines, loop timings).",
            "<b>Closed-loop vs open-loop:</b> Open-loop performs actions blindly without monitoring output (e.g. basic timer switch); closed-loop measures output via sensors and feeds back error signal to dynamically adjust actuators."
        )
    },
    @{
        heading = "Project Management & Quality Frameworks"
        points = @(
            "<b>Critical Path Analysis (CPA):</b> Network diagram calculation of Earliest Start Time (EST) and Latest Finish Time (LFT). The <b>Critical Path</b> is the sequence of dependent activities with zero float; any delay on this path delays the final delivery date.",
            "<b>Agile & Scrum:</b> Flexible development methodology organizing engineering teams into short 2–4 week sprints, daily stand-up meetings, and continuous prototype testing with stakeholders.",
            "<b>Six Sigma (DMAIC):</b> Define, Measure, Analyse, Improve, Control. Statistical management methodology striving for fewer than 3.4 defective parts per million opportunities ($99.99966\\%$ yield)."
        )
    }
)

# 5.1
Add-Sheet "5.1" "Topic 5.1 · Factors Influencing Material Selection" "5. Material & Component Considerations" "Selection criteria: functional performance, mechanical properties, cost, availability, machinability, environmental & ethical footprint" @(
    @{
        heading = "Engineering Material Selection Factors"
        points = @(
            "<b>Functional requirements:</b> Mechanical load capacity, fatigue strength, operating temperature envelope, thermal expansion coefficient (CTE), corrosion resistance, electrical conductivity or dielectric breakdown.",
            "<b>Economic viability:</b> Balancing raw material cost per kg against machining speed, tooling amortisation, and scrap rate. (e.g. Aluminium costs more than steel per kg but machines 3x faster, reducing labour cost).",
            "<b>Ashby charts:</b> Material selection charts plotting property trade-offs (e.g. Young's Modulus vs Density $E/\\rho$, or Strength vs Cost $\\sigma/\\text{Cost}$) to identify optimal material candidates for minimum weight beams."
        )
    }
)

# 5.2
Add-Sheet "5.2" "Topic 5.2 · Engineering Materials Classification" "5. Material & Component Considerations" "Ferrous, non-ferrous, alloys, thermosoftening & thermosetting polymers, timber & boards, geotextiles, composites, smart & modern materials" @(
    @{
        heading = "Metals & Engineering Alloys"
        points = @(
            "<b>Mild Steel:</b> Ferrous; 0.15–0.30% Carbon. Ductile, highly weldable, tough; structural beams, car chassis, universal steel sections.",
            "<b>High Carbon Steel / Tool Steel:</b> Ferrous; 0.60–1.40% Carbon. Very hard, can be hardened and tempered; cutting blades, drill bits, stamping dies.",
            "<b>Cast Iron:</b> Ferrous; 2.0–4.0% Carbon. High compressive strength, brittle, superb vibration dampening; machine beds, engine blocks.",
            "<b>Aluminium:</b> Non-ferrous; low density ($\\rho \\approx 2700 \\text{ kg/m}^3$), natural oxide passivation layer resists corrosion, high thermal/electrical conductivity; aircraft skins, heatsinks.",
            "<b>Brass:</b> Copper-Zinc alloy (typically 70/30 or 60/40); low friction coefficient, acoustic resonance, corrosion resistant; valves, bearings, electrical pin connectors."
        )
    },
    @{
        heading = "Polymers (Thermosoftening & Thermosetting)"
        points = @(
            "<b>ABS (Acrylonitrile Butadiene Styrene):</b> Thermosoftening; copolymer combining chemical resistance (A), impact toughness (B), and structural rigidity (S); injection-moulded tool housings, 3D printing, consumer electronics.",
            "<b>HIPS (High Impact Polystyrene):</b> Thermosoftening; lightweight, rigid, easily thermoformed and vacuum formed; internal refrigerator liners, packaging.",
            "<b>Polypropylene (PP):</b> Thermosoftening; exceptional fatigue resistance to repeated flexing; integral living hinges, chemical containers.",
            "<b>Epoxy Resin:</b> Thermosetting; highly crosslinked polymer matrix, exceptional adhesive strength, chemical resistance, electrical insulator; composite matrix (CFRP), PCB FR4 substrate.",
            "<b>Polyester Resin:</b> Thermosetting; cured with MEKP catalyst; matrix for Glass-Reinforced Plastic (GRP), boat hulls, fairings."
        )
    },
    @{
        heading = "Composites, Smart & Modern Materials"
        points = @(
            "<b>CFRP (Carbon Fibre Reinforced Polymer):</b> Continuous high-tensile carbon fibres embedded in rigid epoxy resin matrix; exceptional strength-to-weight ratio and stiffness; aerospace spars, Formula 1 chassis.",
            "<b>GRP (Glass Reinforced Plastic):</b> Woven or chopped glass fibres in polyester/epoxy matrix; lightweight, non-conductive, corrosion resistant; architectural cladding, marine hulls.",
            "<b>Shape Memory Alloys (SMA - Nitinol):</b> Nickel-Titanium alloy that returns to a memorized shape upon heating past its martensite-to-austenite transition temperature; medical arterial stents, robotic micro-actuators.",
            "<b>Modern Super-alloys & Graphene:</b> Inconel (nickel-chromium superalloy maintaining extreme strength at >1000°C in jet turbine blades); Graphene (single 2D layer of carbon atoms arranged in hexagonal lattice, tensile strength >130 GPa, ballistic thermal conductivity)."
        )
    }
)

# 5.3
Add-Sheet "5.3" "Topic 5.3 · Material Properties & Mechanical Testing" "5. Material & Component Considerations" "Tensile strength, hardness, toughness, ductility, malleability, stiffness, thermal/electrical conductivity, standardized testing methods" @(
    @{
        heading = "Mechanical Properties Definitions"
        points = @(
            "<b>Tensile Strength (UTS):</b> Maximum tensile stress a material withstands before necking and fracture occur ($\\sigma_u = F_{max}/A_0$).",
            "<b>Hardness:</b> Resistance of a material's surface to mechanical penetration, abrasion, scratching, and indentation.",
            "<b>Toughness:</b> Ability of a material to absorb kinetic impact energy without catastrophic brittle fracture (total area under stress-strain curve).",
            "<b>Ductility:</b> Capacity of a material to undergo extensive plastic deformation in tension (drawn into wire) without rupture.",
            "<b>Malleability:</b> Capacity of a material to deform plastically under compressive force (hammering, rolling into sheets) without cracking.",
            "<b>Stiffness:</b> Ability to resist elastic deflection under applied load, measured by Young's Modulus ($E = \\sigma / \\epsilon$)."
        )
    },
    @{
        heading = "Standardised Mechanical Testing"
        points = @(
            "<b>Tensile testing (Tensometer):</b> Pulling a standard dogbone test piece at constant strain rate to record force-extension data and calculate $\\sigma$, $\\epsilon$, $E$, yield point, and UTS.",
            "<b>Hardness testing methods:</b> Rockwell (measures depth of indentation under major load using diamond cone), Vickers (diamond pyramid leaving square indent measured microscopically), Brinell (hardened steel ball indent).",
            "<b>Impact testing (Charpy & Izod):</b> Standard notched specimen struck by a swinging pendulum; potential energy absorbed during fracture measured in Joules on calibrated scale."
        )
    }
)

# 6.1
Add-Sheet "6.1" "Topic 6.1 · Structural Integrity & Triangulation" "6. Technical Understanding" "Structural reinforcement, triangulation, gusset plates, ribbing, load paths, second moment of area, monocoque vs space-frame" @(
    @{
        heading = "Structural Reinforcement & Rigidity"
        points = @(
            "<b>Triangulation principle:</b> Triangles cannot be distorted without physically changing the length of one of their member struts; transforms complex bending forces into pure axial tension or compression.",
            "<b>Structural ribs and web stiffeners:</b> Thin perpendicular ribs integrated into injection mouldings and castings multiply the second moment of area ($I$) and section modulus ($Z$), increasing bending stiffness by up to 10x with minimal material addition.",
            "<b>Gusset plates:</b> Welded or bolted triangular reinforcement plates securing column-to-beam joints to disperse concentrated bending moments over broader weld perimeters.",
            "<b>Monocoque vs space-frame:</b> Monocoque relies on a continuous structural skin (stressed skin) to absorb dynamic torsional and shear loads (e.g. aircraft fuselages); space-frame utilizes a three-dimensional triangulated skeletal truss."
        )
    }
)

# 6.2
Add-Sheet "6.2" "Topic 6.2 · Mechanisms, Motion & Mechanical Systems" "6. Technical Understanding" "Types of motion, gear trains (compound, worm, epicyclic), cams & followers, linkages, screws, pulleys, MA, VR, efficiency" @(
    @{
        heading = "Kinematics & Motion Conversion"
        points = @(
            "<b>Four motion regimes:</b> Rotary (continuous 360° circular), Linear (continuous straight-line single direction), Reciprocating (repetitive back-and-forth linear), Oscillating (repetitive back-and-forth arc around fixed pivot).",
            "<b>Rack and pinion:</b> Transforms rotary motion into precise linear motion (or vice-versa; CNC machine beds, automotive steering racks).",
            "<b>Cams and followers:</b> Shaped cam plate (eccentric, pear, snail) rotates to impart programmed displacement to follower (knife-edge, roller, flat-faced); characterized by Dwell, Rise, and Fall phases.",
            "<b>Mechanical linkages:</b> Bell crank (redirects linear force through 90° angle), Four-bar linkage (crank-rocker, double-crank), Pantograph (parallel motion scaling)."
        )
    },
    @{
        heading = "Gear Calculations & Mechanical Advantage"
        points = @(
            "<b>Gear Ratio / Velocity Ratio:</b> $\\text{GR} = \\frac{\\text{Teeth on Driven (Output)}}{\\text{Teeth on Driver (Input)}} = \\frac{\\omega_{in}}{\\omega_{out}} = \\frac{N_{in}}{N_{out}}$.",
            "<b>Compound gear train:</b> Intermediate shafts bearing two rigidly keyed gears; total ratio is the product of individual gear stages: $\\text{GR}_{total} = \\text{GR}_1 \\times \\text{GR}_2 \\times \\dots$",
            "<b>Worm and worm wheel:</b> Achieves huge single-stage reduction (e.g. 50:1) with non-intersecting shafts at 90°; inherently self-locking, preventing output back-driving.",
            "<b>Epicyclic (Planetary) gearing:</b> Coaxial high-torque system comprising Sun gear, Planet gears on a Planet Carrier, and Annulus (ring gear); compact form factor for automatic transmissions.",
            "<b>Mechanical Advantage (MA):</b> $\\text{MA} = \\frac{\\text{Load (Output Force)}}{\\text{Effort (Input Force)}}$.",
            "<b>Velocity Ratio (VR):</b> $\\text{VR} = \\frac{\\text{Distance moved by Effort}}{\\text{Distance moved by Load}}$.",
            "<b>Efficiency:</b> $\\text{Efficiency } \\eta = \\frac{\\text{MA}}{\\text{VR}} \\times 100\\%$. Due to friction and inertia, $\\text{MA} < \\text{VR}$ and $\\eta < 100\\%$."
        )
    }
)

# 6.3
Add-Sheet "6.3" "Topic 6.3 · Forces, Stress, Strain & Elasticity" "6. Technical Understanding" "Static & dynamic forces, stress (F/A), strain (ΔL/L), Young's Modulus (E), Hooke's Law (F=kx), torque, SUVAT, modes of failure" @(
    @{
        heading = "Stress, Strain & Elasticity Formulae (Recall Required)"
        points = @(
            "<b>Tensile / Compressive Stress ($\\sigma$):</b> $\\sigma = \\frac{F}{A}$ where $F$ is applied force in Newtons (N) and $A$ is original cross-sectional area in $\\text{m}^2$. Unit: Pascals ($\\text{Pa} = \\text{N/m}^2$, $1 \\text{ MPa} = 1 \\text{ N/mm}^2$).",
            "<b>Tensile Strain ($\\epsilon$):</b> $\\epsilon = \\frac{\\Delta L}{L_0}$ where $\\Delta L$ is change in length (extension) and $L_0$ is original length. Dimensionless ratio (often expressed as a percentage).",
            "<b>Young's Modulus of Elasticity ($E$):</b> $E = \\frac{\\text{Stress}}{\\text{Strain}} = \\frac{\\sigma}{\\epsilon} = \\frac{F \\cdot L_0}{A \\cdot \\Delta L}$. Unit: $\\text{Pa}$ or $\\text{GPa}$ ($1 \\text{ GPa} = 10^9 \\text{ Pa}$). Constant gradient of linear elastic region of stress-strain curve.",
            "<b>Hooke's Law:</b> $F = k \\cdot \\Delta x$ where $k$ is spring constant / stiffness in $\\text{N/m}$ and $\\Delta x$ is extension in metres.",
            "<b>Torque (Turning moment):</b> $\\text{Torque } T = F \\cdot d$ where $F$ is applied perpendicular force and $d$ is radial distance to pivot. Unit: $\\text{N}\\cdot\\text{m}$."
        )
    },
    @{
        heading = "SUVAT Equations & Modes of Mechanical Failure"
        points = @(
            "<b>SUVAT Equations of Motion:</b> $v = u + at$; $s = ut + \\frac{1}{2}at^2$; $v^2 = u^2 + 2as$; $s = \\frac{(u + v)t}{2}$.",
            "<b>Resolving Force Vectors:</b> Horizontal component $F_x = F \\cos\\theta$; Vertical component $F_y = F \\sin\\theta$.",
            "<b>Factor of Safety (FoS):</b> $\\text{FoS} = \\frac{\\text{Yield Strength or UTS}}{\\text{Allowable Working Stress}}$. Ensures structural integrity under unexpected peak overloads.",
            "<b>Modes of failure:</b> Elastic buckling (Euler buckling in slender compression struts), fatigue failure (cyclic alternating stress causing microscopic crack propagation), creep (gradual deformation under constant load at elevated temperatures)."
        )
    }
)

# 6.4
Add-Sheet "6.4" "Topic 6.4 · Electronic Systems, Sensors & Actuators" "6. Technical Understanding" "Ohm's law, electrical power, potential dividers, passive components, sensors, MOSFET switching, flyback diodes, wireless protocols" @(
    @{
        heading = "Ohm's Law, Power & Potential Dividers"
        points = @(
            "<b>Ohm's Law:</b> $V = I \\cdot R$; Potential difference (Volts) = Current (Amperes) × Resistance (Ohms).",
            "<b>Electrical Power:</b> $P = V \\cdot I = I^2 R = \\frac{V^2}{R}$ [Watts, W].",
            "<b>Potential Divider Equation:</b> $V_{out} = V_{in} \\cdot \\frac{R_2}{R_1 + R_2}$. Fundamental circuit to convert sensor resistance changes into readable voltage signals.",
            "<b>Resistor network rules:</b> Series: $R_T = R_1 + R_2 + \\dots$; Parallel: $\\frac{1}{R_T} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\dots$"
        )
    },
    @{
        heading = "Sensors, Semiconductor Switching & Actuators"
        points = @(
            "<b>Sensors:</b> LDR (light-dependent resistor; resistance falls with light intensity), NTC Thermistor (negative temperature coefficient; resistance drops as temperature rises), Piezoelectric sensor, Hall effect (magnetic proximity).",
            "<b>MOSFET as high-current electronic switch:</b> N-channel MOSFET turns fully ON when Gate-Source voltage exceeds threshold ($V_{GS} > V_{th}$). Minimal gate current; ultra-low $R_{DS(on)}$ eliminates resistive heat losses in motor control.",
            "<b>Flyback protection diode:</b> Placed in reverse parallel across inductive loads (motors, solenoids, relays) to clamp dangerous back-EMF voltage spikes generated during switch-off.",
            "<b>Actuators:</b> Brushed DC motors (continuous rotary motion, speed controlled by PWM), Servo motors (closed-loop angular positioning 0–180°), Stepper motors (discrete digital step angles for CNC positioning)."
        )
    }
)

# 6.5
Add-Sheet "6.5" "Topic 6.5 · Microcontrollers & Programmable Systems" "6. Technical Understanding" "Microcontroller architecture, ADC conversion, PWM duty cycle, embedded coding, flowcharts, closed-loop PID control" @(
    @{
        heading = "Microcontrollers & Signal Conditioning"
        points = @(
            "<b>Microcontroller architecture:</b> Integrated IC housing CPU, Flash ROM (program memory), RAM (volatile variables), EEPROM, Timers, ADC, and GPIO pins (e.g. PIC, ATmega, ARM Cortex).",
            "<b>Analogue-to-Digital Conversion (ADC):</b> Samples continuous analogue input voltages (0–5V) into discrete digital integers. A 10-bit ADC provides $2^{10} = 1024$ quantization levels ($0 \\to 1023$); voltage step size $= \\frac{5\\text{V}}{1023} \\approx 4.88\\text{ mV}$.",
            "<b>Pulse Width Modulation (PWM):</b> Varying the ratio of on-time to off-time in a high-frequency square wave (Duty Cycle $\\% = \\frac{t_{on}}{t_{period}} \\times 100\\%$) to smoothly vary average power delivery to DC motors and heaters."
        )
    },
    @{
        heading = "Control Logic & Closed-Loop Feedback"
        points = @(
            "<b>Closed-loop feedback control:</b> Continuously measures system output via sensors, subtracts output from desired target setpoint to derive error ($e = \\text{Setpoint} - \\text{Sensor Feedback}$), and applies correction.",
            "<b>PID controller components:</b> Proportional (responds to current error magnitude), Integral (accumulates historical steady-state error), Derivative (anticipates future error rate of change).",
            "<b>Flowchart programming conventions:</b> Explicit decision diamonds checking sensor threshold limits, branch logic, loops, and digital pin writes."
        )
    }
)

# 7.1
Add-Sheet "7.1" "Topic 7.1 · Iterative Models & Rapid Prototyping" "7. Manufacturing Processes & Techniques" "Iterative prototyping, low-fidelity sketch models, test rigs, 3D printing (FDM, SLA), laser cutting, virtual simulation" @(
    @{
        heading = "Iterative Physical & Digital Modelling"
        points = @(
            "<b>Low-fidelity sketch modelling:</b> Rapid construction using corrugated cardboard, Styrofoam, and wire to test volumetric proportions, visual ergonomics, and spatial clearance in hours.",
            "<b>Functional test rigs (breadboard / bread-rig):</b> Building isolated sub-system test benches (e.g. laser-cut acrylic gearboxes with microcontrollers) to validate physical kinematic forces before tooling.",
            "<b>Additive rapid prototyping (FDM / SLA):</b> Fused Deposition Modelling (FDM) extrudes molten thermoplastic filaments (PLA, ABS, PETG) layer-by-layer; Stereolithography (SLA) cures liquid photopolymer resin with UV lasers for ultra-smooth optical precision."
        )
    }
)

# 7.2
Add-Sheet "7.2" "Topic 7.2 · Workshop Tools, Machining & Fabrication" "7. Manufacturing Processes & Techniques" "Wasting (lathe turning, milling, drilling), joining (welding, brazing, soldering, fasteners), reforming (bending, vacuum forming), tolerances" @(
    @{
        heading = "Subtractive Machining (Wasting)"
        points = @(
            "<b>Centre lathe operations:</b> Cylindrical turning: facing off datum ends, parallel turning, taper turning, boring, knurling, and parting off. Work held in 3-jaw self-centring chuck or between centres.",
            "<b>Vertical milling machine:</b> Multi-tooth rotating cutter traversing workpiece in X, Y, and Z axes to create flat faces, steps, slots, pockets, and keyways.",
            "<b>Drilling & reaming:</b> Twist drill generates rough hole; machine reamer achieves exact dimensional diameter and mirror surface finish within ISO tolerance limits."
        )
    },
    @{
        heading = "Fabrication, Joining & Reforming"
        points = @(
            "<b>Welding:</b> Parent metals melted and fused with filler material. MIG (Metal Inert Gas; wire feed, argon shielding, fast structural steel); TIG (Tungsten Inert Gas; tungsten electrode, highest aesthetic quality on aluminium/stainless steel).",
            "<b>Brazing & Soldering:</b> Non-ferrous filler metal melted below parent metal melting points ($>450°\\text{C}$ for brazing; $<450°\\text{C}$ for electrical lead-free soldering).",
            "<b>Mechanical fasteners & locking:</b> ISO metric bolts (M3, M4, M5); Nyloc locking nuts and Belleville disc springs prevent fastener loosening under vibration.",
            "<b>Sheet metal folding:</b> Sheet metal folded along bend lines using workshop box-and-pan folder, accounting for bend allowance and neutral axis K-factor."
        )
    }
)

# 7.3
Add-Sheet "7.3" "Topic 7.3 · Industrial Commercial Manufacture & SMT" "7. Manufacturing Processes & Techniques" "Commercial polymer moulding (injection, blow, compression, thermoforming), metal casting (sand, die), stamping, SMT assembly" @(
    @{
        heading = "Commercial Polymer Moulding Methods"
        points = @(
            "<b>Injection moulding:</b> Molten polymer forced under extreme hydraulic pressure (up to 1500 bar) into hardened tool steel mould cavities. High tool cost (£15k–£100k+), ultra-fast cycle times (10–30s), complex geometries, integrated snap fits.",
            "<b>Blow moulding:</b> Molten hollow plastic parison extruded, clamped in mould, and inflated with compressed air; produces seamless bottles, containers, and fuel tanks.",
            "<b>Compression moulding:</b> Preheated thermosetting charge placed into open heated cavity, closed under hydraulic pressure; produces heat-resistant electrical plugs and melamine tableware."
        )
    },
    @{
        heading = "Industrial Metal Casting & Electronics SMT Assembly"
        points = @(
            "<b>High pressure die casting:</b> Molten aluminium or zinc alloy injected under high pressure into permanent steel dies; excellent surface finish, thin walls, tight dimensional tolerances.",
            "<b>Sand casting:</b> Molten metal poured into temporary sand moulds formed around patterns; low tooling cost, ideal for large engine blocks and low volume castings.",
            "<b>Surface Mount Technology (SMT) Assembly:</b> 1. Laser-cut stainless steel stencil applies solder paste onto PCB surface pads, 2. High-speed pick-and-place robot places surface-mount components, 3. Multi-zone reflow oven melts solder paste at ~217°C to form robust solder joints."
        )
    }
)

# 7.4
Add-Sheet "7.4" "Topic 7.4 · Scales of Production & Lean / JIT" "7. Manufacturing Processes & Techniques" "Production scales (one-off, batch, mass, continuous), cellular manufacturing, Lean manufacturing (7 wastes), Just-in-Time (JIT)" @(
    @{
        heading = "Scales of Manufacturing Production"
        points = @(
            "<b>One-off / bespoke production:</b> Highly customized single units manufactured by skilled artisans or specialist machinists; flexible, high unit cost, minimal tooling.",
            "<b>Batch production:</b> Pre-determined batch sizes using flexible machine setups and interchangeable jigs/fixtures; balances setup downtime against warehouse storage inventory.",
            "<b>Mass / High-volume production:</b> Dedicated automated assembly lines producing millions of standardized identical products; ultra-low unit cost, immense capital investment in dedicated tooling.",
            "<b>Continuous flow production:</b> 24/7 automated continuous processing of bulk materials (oil refining, steel blast furnaces, petrochemicals)."
        )
    },
    @{
        heading = "Lean Manufacturing & Just-In-Time (JIT)"
        points = @(
            "<b>Lean manufacturing:</b> Systematic elimination of the 7 wastes (TIMWOOD): Transport, Inventory, Motion, Waiting, Overproduction, Over-processing, Defects.",
            "<b>Just-In-Time (JIT):</b> Components and raw stock arrive at assembly lines exactly as needed; eliminates buffer warehouse inventory and minimizes tied-up working capital.",
            "<b>Cellular manufacturing:</b> U-shaped workstations manned by cross-trained technicians, minimizing part transport distance and optimizing operator workflow balance."
        )
    }
)

# 7.5
Add-Sheet "7.5" "Topic 7.5 · Quality Control, QA, TQM & Standards" "7. Manufacturing Processes & Techniques" "Quality Control (QC), Quality Assurance (QA), Total Quality Management (TQM), ISO 9001, BSI Kitemark, CE / UKCA compliance" @(
    @{
        heading = "QC vs QA & Total Quality Management"
        points = @(
            "<b>Quality Control (QC):</b> Reactive inspection of physical parts against engineering drawings and tolerances during and after production; defective items are rejected or reworked.",
            "<b>Quality Assurance (QA):</b> Proactive systemic management of processes, machine calibrations, and operator procedures to ensure defects cannot arise in the first place.",
            "<b>Total Quality Management (TQM):</b> Company-wide culture of continuous incremental improvement (Kaizen) where every employee is accountable for product excellence.",
            "<b>Statistical Process Control (SPC):</b> Control charts plotting critical part dimensions in real time; warns when tooling wear causes dimensions to drift before parts fall out of tolerance."
        )
    },
    @{
        heading = "Certification & Statutory Standards"
        points = @(
            "<b>ISO 9001:</b> International benchmark for Quality Management Systems; establishes documented procedures, calibrated inspection tooling, and regular audits.",
            "<b>BSI Kitemark:</b> Prestigious third-party certification from the British Standards Institution confirming independent testing and ongoing factory compliance.",
            "<b>CE and UKCA marking:</b> Mandatory conformity assessment marking declaring product adherence to all applicable safety, electromagnetic compatibility (EMC), and low-voltage directives."
        )
    }
)

# 8.1
Add-Sheet "8.1" "Topic 8.1 · Stakeholder Evaluation & Usability Testing" "8. Viability of Design Solutions" "Usability trials, quantitative metrics, stakeholder feedback, accessibility compliance, testing against design specification" @(
    @{
        heading = "Usability Trials & Stakeholder Verification"
        points = @(
            "<b>Structured usability trials:</b> Placing functional prototypes into the hands of target end-users to measure task completion duration, error frequency, and cognitive confusion.",
            "<b>Quantitative vs Qualitative data:</b> Quantitative metrics (seconds to complete action, clamping force applied in N, battery life in hours) vs qualitative observations (user comfort comments, intuitive grip feel).",
            "<b>Specification verification matrix:</b> Methodical check verifying every measurable requirement in the engineering technical specification against empirical prototype performance data."
        )
    }
)

# 8.2
Add-Sheet "8.2" "Topic 8.2 · Technical Testing & Physical Validation" "8. Viability of Design Solutions" "Destructive testing, Non-Destructive Testing (NDT: dye penetrant, ultrasonic, X-ray), environmental stress screening, FEA validation" @(
    @{
        heading = "Destructive vs Non-Destructive Testing (NDT)"
        points = @(
            "<b>Destructive testing:</b> Applying physical loads until catastrophic component failure occurs to determine ultimate mechanical limits: UTS tensile pull tests, burst pressure tests, drop impact tests.",
            "<b>Dye Penetrant Inspection (DPI):</b> NDT technique where fluorescent/red dye penetrates surface micro-cracks; developer draws dye out to highlight surface defects under white/UV light.",
            "<b>Ultrasonic Testing (UT):</b> High-frequency acoustic sound waves transmitted into solid components; reflected echo pulses detect internal sub-surface voids, inclusions, and delaminations.",
            "<b>X-Ray Radiography:</b> Penetrating ionizing radiation creates radiographic film images showing internal porosity in critical structural castings and welds."
        )
    }
)

# 8.3
Add-Sheet "8.3" "Topic 8.3 · Commercial Feasibility & Cost Viability" "8. Viability of Design Solutions" "Unit manufacturing cost calculation, tooling amortization, breakeven analysis, contribution margin, commercial risk analysis" @(
    @{
        heading = "Unit Cost Calculation & Breakeven Analysis"
        points = @(
            "<b>Unit Manufacturing Cost Formula:</b> $\\text{Unit Cost} = \\text{Direct Materials} + \\text{Direct Labour} + \\text{Overhead} + \\frac{\\text{Tooling \\& Development Cost}}{\\text{Total Production Volume}}$.",
            "<b>Tooling amortisation:</b> Distributing high upfront tooling costs (e.g. £50,000 for press dies) across unit volume; over 500,000 units tooling cost is £0.10/unit, while over 5,000 units it is £10.00/unit.",
            "<b>Breakeven Point (BEP):</b> $\\text{BEP (units)} = \\frac{\\text{Total Fixed Costs}}{\\text{Selling Price per Unit} - \\text{Variable Cost per Unit}}$.",
            "<b>Contribution Margin:</b> $\\text{Selling Price} - \\text{Variable Cost per Unit}$. The surplus generated per unit sold that contributes to paying off fixed overheads and generating net profit."
        )
    }
)

# 9.1
Add-Sheet "9.1" "Topic 9.1 · Workshop Safe Practices & Risk Assessments" "9. Health & Safety" "Risk assessment matrix (likelihood × severity), hazard identification, hierarchy of control, machine interlocks, emergency stops" @(
    @{
        heading = "Risk Assessment & Hazard Control"
        points = @(
            "<b>Hazard vs Risk:</b> A <b>hazard</b> is anything with intrinsic potential to cause harm (e.g. rotating lathe spindle, toxic solvent). A <b>risk</b> is the evaluated probability that harm occurs multiplied by its severity.",
            "<b>Risk Rating Formula:</b> $\\text{Risk Score} = \\text{Likelihood (1–5)} \\times \\text{Severity (1–5)}$. High scores require immediate implementation of higher-level engineering controls.",
            "<b>Hierarchy of Hazard Controls:</b> 1. <b>Elimination</b> (physically remove hazard), 2. <b>Substitution</b> (replace hazard with safer material), 3. <b>Engineering Controls</b> (interlocked guards, LEV local exhaust ventilation), 4. <b>Administrative Controls</b> (Standard Operating Procedures SOP, training, signage), 5. <b>PPE</b> (Personal Protective Equipment as last line of defence)."
        )
    },
    @{
        heading = "Machinery Safety & Interlocking"
        points = @(
            "<b>Machine guarding:</b> Fixed guards preventing operator reach into entrapment pinch points; interlocked physical guards that immediately break the electrical control circuit and brake the drive spindle when opened.",
            "<b>Emergency stop circuits (E-Stop):</b> Latching mushroom-head push buttons wired into hardwired safety relays; must fail-safe to a de-energized state and require manual reset before machine restarts."
        )
    }
)

# 9.2
Add-Sheet "9.2" "Topic 9.2 · Health & Safety Legislation (HASAW, COSHH)" "9. Health & Safety" "Health and Safety at Work Act 1974, COSHH 2002 regulations, PPE Regulations 1992, CE/UKCA marking, product liability & warranties" @(
    @{
        heading = "Statutory Health & Safety Legislation"
        points = @(
            "<b>Health and Safety at Work Act (HASAW) 1974:</b> Foundational UK statute placing a non-delegable legal duty on employers to ensure the health, safety, and welfare of employees and the public 'so far as is reasonably practicable'. Employees must take reasonable care of themselves and cooperate with safety protocols.",
            "<b>COSHH Regulations 2002:</b> Control of Substances Hazardous to Health; legally mandates comprehensive risk assessments, proper chemical storage in flame-proof bunded cabinets, Safety Data Sheets (SDS), and Local Exhaust Ventilation (LEV) testing for hazardous dusts, cutting fluids, and resin vapours.",
            "<b>PPE at Work Regulations 1992:</b> Mandates that employers must supply suitable, CE/UKCA-certified PPE (impact safety glasses EN 166, ear defenders EN 352, dust respirators, steel toe-cap footwear) free of charge wherever risks cannot be adequately controlled by engineering means."
        )
    },
    @{
        heading = "Product Safety Regulations & Consumer Warranties"
        points = @(
            "<b>General Product Safety Regulations (GPSR):</b> Prohibits placing any product on consumer markets that poses foreseeable safety hazards under reasonable usage or misuse.",
            "<b>Consumer Rights Act 2015:</b> Requires all engineered products sold to consumers to be of satisfactory quality, fit for purpose, and match manufacturer descriptions; backed by mandatory warranty redress."
        )
    }
)

# Convert to JSON
$json = $cheats | ConvertTo-Json -Depth 6
[System.IO.File]::WriteAllText((Join-Path $baseDir "cheatsheets.json"), $json, [System.Text.Encoding]::UTF8)
Write-Host "cheatsheets.json created successfully. Topics: $($cheats.Count)"

# Also write individual markdown files into cheatsheets/
foreach ($tid in $cheats.Keys) {
    $item = $cheats[$tid]
    $fileSlug = $tid.Replace(".", "_") + ".md"
    $mdPath = Join-Path $cheatsDir $fileSlug

    $mdLines = @(
        "# $($item.title)",
        "**Specification Strand:** $($item.group)",
        "**Syllabus Focus:** $($item.spec)",
        "",
        "---",
        ""
    )

    foreach ($sec in $item.sections) {
        $mdLines += "## $($sec.heading)"
        $mdLines += ""
        foreach ($pt in $sec.points) {
            # convert html b tags to markdown **
            $cleanPt = $pt -replace '<b>', '**' -replace '</b>', '**'
            $mdLines += "- $cleanPt"
        }
        $mdLines += ""
    }

    [System.IO.File]::WriteAllLines($mdPath, $mdLines, [System.Text.Encoding]::UTF8)
}

# Write a README.md inside cheatsheets
$csReadme = @(
    "# LEETS · OCR A-Level Design Engineering (H404) Cheatsheets",
    "",
    "This directory contains high-yield, technical revision cheatsheets covering all 34 topic strands of the OCR A-Level Design and Technology: Design Engineering (H404) specification.",
    "",
    "## Topic Strands",
    "- **1. Identifying Requirements** (1.1, 1.2, 1.3)",
    "- **2. Existing Products & Practice** (2.1, 2.2, 2.3, 2.4)",
    "- **3. Implications of Wider Issues** (3.1, 3.2, 3.3, 3.4, 3.5, 3.6)",
    "- **4. Design Thinking & Communication** (4.1, 4.2, 4.3)",
    "- **5. Material & Component Considerations** (5.1, 5.2, 5.3)",
    "- **6. Technical Understanding** (6.1, 6.2, 6.3, 6.4, 6.5)",
    "- **7. Manufacturing Processes & Techniques** (7.1, 7.2, 7.3, 7.4, 7.5)",
    "- **8. Viability of Design Solutions** (8.1, 8.2, 8.3)",
    "- **9. Health & Safety** (9.1, 9.2)"
)
[System.IO.File]::WriteAllLines((Join-Path $cheatsDir "README.md"), $csReadme, [System.Text.Encoding]::UTF8)

Write-Host "Markdown cheatsheet files written to $cheatsDir"

