# LEETS · OCR A-Level Design Engineering (H404)

> Minimalist revision portal, technical past paper bank, formula sheet, interactive practice flashcards, and syllabus cheatsheets for **OCR A-Level Design and Technology: Design Engineering (H404)**.

Sister platform to [SENOTS](https://github.com/chanAle-lab/senots) (Geology), redesigned from the ground up for engineering principles, technical calculations, mechanics, electronics, and materials.

---

## ⚡ Features

1. **Specification Matrix (Topics View):**
   - Full breakdown of all 9 specification strands and 34 subtopics in OCR H404 Design Engineering.
   - Colour-coded topics with mark distributions and question counts.
   - Direct cross-filtering into the question bank.

2. **Past Paper Question Bank:**
   - Real-time search with instant filtering (`/` keyboard shortcut).
   - Filter by Component (`H404/01 Principles` vs `H404/02 Problem Solving`), Topic (1.1 to 9.2), Exam Year, Marks (2+, 4+, 6+, 8+), and Mathematical Skills (25% calculation requirement).
   - Side-by-side split screen view with official mark schemes and model calculations.
   - Progress tracking with LocalStorage persistence (Mastered marks tracker, Bookmarks, and Needs Work).

3. **Active Recall Practice (Flashcards Mode):**
   - 219+ targeted engineering flashcards covering every subtopic.
   - Keyboard shortcuts: `Space` to reveal, `1` Needs Review, `2` Mastered, `←` / `→` Navigate, `S` Star card.
   - Topic-specific filtering and deck shuffling.

4. **Technical Cheatsheets:**
   - 34 dedicated cheatsheet guides covering the complete syllabus.
   - Exact mathematical equations from Appendices 5c & 5d (Young's Modulus, Stress/Strain, Hooke's Law, Torque, SUVAT, Potential Dividers, ADC Resolution, Gear Ratios).
   - One-click launch from cheatsheet directly into matching flashcards.

5. **Quick-Access Formulae Sheet:**
   - Instant header modal displaying all mandatory mathematical and scientific recall formulae required for OCR H404 exams.

---

## 📚 Specification Coverage (OCR H404)

| Strand | Name | Focus |
|---|---|---|
| **Topic 1** | Identifying Requirements | Context analysis, user-centred design (UCD), stakeholder personas, anthropometrics (5th/50th/95th percentiles), ergonomics. |
| **Topic 2** | Existing Products & Practice | Product disassembly, ACCESS FM, technological innovations, historical movements (Bauhaus, Memphis, Rams), product life cycles (PLC). |
| **Topic 3** | Implications of Wider Issues | Life Cycle Assessment (LCA), circular economy, DFMA, material optimization/nesting, logistics, IP law (patents, registered designs). |
| **Topic 4** | Design Thinking & Communication | BS 8888 3rd angle orthographic drawing, section views, parametric CAD, CAE, Finite Element Analysis (FEA), Critical Path Analysis (CPA), Scrum. |
| **Topic 5** | Material & Component Considerations | Ferrous/non-ferrous metals, alloys, thermoforming/thermosetting polymers, composites (CFRP/GRP), smart materials (SMA/Nitinol), mechanical testing. |
| **Topic 6** | Technical Understanding | Triangulation, mechanisms & compound gears, stress/strain/Young's modulus, Ohm's law, potential dividers, microcontrollers, ADC, PWM. |
| **Topic 7** | Manufacturing Processes & Techniques | Rapid prototyping, lathe turning, milling, welding/brazing, injection moulding, die casting, SMT electronics assembly, Lean/JIT, QC/QA, ISO 9001. |
| **Topic 8** | Viability of Design Solutions | Stakeholder usability trials, destructive vs Non-Destructive Testing (NDT: dye penetrant, ultrasonic, X-ray), tooling amortization, breakeven analysis. |
| **Topic 9** | Health & Safety | Workshop risk assessments, hierarchy of hazard control, machine interlocks, HASAW 1974, COSHH 2002 regulations, PPE regulations. |

---

## 🔐 Passcode Access

The portal includes a minimalist authentication gate. Accepted passcodes include:
- `engineering`
- `leets`
- `steel`
- `h404`

---

## 📁 Adding Past Paper Images in the Future

Paper images can be placed into the `img/<paper-id>/` directory:
- `q<number>.jpg` - Question paper crop
- `fig-<name>.jpg` - Resource figures or data sheets
- `ms-q<number>.jpg` - Official mark scheme crop

The application automatically displays high-resolution images when present, with automatic fallback to formatted text prompts and calculations.

---

## 🚀 Live Site
Deployable via GitHub Pages: [https://chanale-lab.github.io/leets/](https://chanale-lab.github.io/leets/)
