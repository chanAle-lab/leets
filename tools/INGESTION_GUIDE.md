# LEETS Past Paper Ingestion Guide & Pipeline Reference

This guide details the streamlined pipeline for adding past papers to **LEETS**, formatted and arranged identically to **SENOTS**.

---

## 1. Supported Paper Formats

| Unit Code | Component Name | Total Marks | Structure | Stimulus Material |
|---|---|:---:|---|---|
| **H404/01** | Principles of Design Engineering | **80m** | 4 main questions with subparts (e.g. 1a, 1bi ... 4eiii) | Figures embedded directly in Question Paper |
| **H404/02** | Problem Solving in Design Engineering | **70m** | 5–6 extended design questions (e.g. Q1* [14m], Q2 [6m], Q3 [6m], Q4* [14m], Q5 [16m], Q6* [14m]) | Separate **Resource Booklet (RB)** with Figs. 1–11+ |
| **H004/01** | Principles of Design Engineering (AS) | **90m** | 5 main questions with subparts | Figures embedded directly in Question Paper |

---

## 2. Ingestion Pipeline Tool (`tools/ingest_paper.py`)

The pipeline CLI is located at [`tools/ingest_paper.py`](file:///C:/Users/Alexander/.gemini/antigravity/scratch/leets/tools/ingest_paper.py).

### Commands

* **Scan Latest Uploads & Identify Target:**
  ```powershell
  python tools/ingest_paper.py
  ```
  * Automatically scans for the most recent `.pdf` files.
  * Identifies QP, MS, and RB roles from document header signatures.
  * Extracts code, year, series, and creates the directory `img/<paper_id>/`.

* **Explicit File Ingestion:**
  ```powershell
  python tools/ingest_paper.py --qp <path_to_qp.pdf> --ms <path_to_ms.pdf> [--rb <path_to_rb.pdf>] [--push]
  ```

* **Verify Integrity Across All Ingested Papers:**
  ```powershell
  python tools/ingest_paper.py --verify-only
  ```
  * Checks exact mark totals against official targets (80m, 70m, 90m).
  * Validates that 100% of question cards, figures, and mark scheme images exist on disk without 404s.

---

## 3. Data Arrangement Standards (Matching SENOTS)

Every question in `questions.json` adheres to the clean visual format:

1. **Strict Question vs. Resource Separation (Template Standard):**
   * **Question Prompt Card (`q.image`):** Cropped strictly around the subpart prompt only (e.g., `(a) Identify three ways... [3]`, `(b)(i) The lift moves at... [3]`). Introductory context paragraphs and stimulus drawings are excluded from `q.image`.
   * **Resources Section (`q.figures`):** Contextual preambles and stimulus drawings/photos (e.g., `1 A home lift can be installed... Fig. 1.1 shows...` + photos) are isolated into `fig-*.jpg` and displayed under the collapsible **Resources** accordion (`<details class="details-clean"><summary>${figLabel(f)}</summary>`).
   * *Benefit:* Eliminates visual duplication, keeps the main question card concise and readable, and lets subparts (e.g., `(a)`, `(b)(i)`, `(b)(ii)`) cleanly share the same stimulus figure.
2. **Clean Visual Card:**
   * No raw HTML prompt boxes cluttering the card when `q.image` is present.
3. **Descriptive Figure Labels:**
   * Handled dynamically by `figLabel(f)` in `index.html`.
   * Formats filenames like `fig-1-1.jpg` into `Fig. 1.1`, `fig-3.jpg` into `Fig. 3`, and `ms-...` into `Exemplar Model Solution Diagram`.
4. **Streamlined Mark Schemes:**
   * `q.markscheme`: Stitched mark scheme image (`img/<paper-id>/ms-{num}.jpg`).
   * Rendered in `<details class="details-clean"><summary>Mark scheme</summary>...`.
5. **Side-by-Side Modal:**
   * Left pane: Question snippet + stacked resource figures.
   * Right pane: Mark scheme solution.
6. **PDF Export & Selection Dock:**
   * Checkboxes enable custom problem pack creation.
   * Floating dock displays total marks selected with an "Export PDF / Print" action.

---

## 4. Current Repository Ingestion Status

* **2020 Autumn H404/02** (Problem Solving): 7 questions · **70 / 70 marks** · Verified ✓
* **2020 Autumn H404/01** (Principles): 23 questions · **80 / 80 marks** · Verified ✓
* **2019 Summer H404/01** (Principles): 25 questions · **80 / 80 marks** · Verified ✓
* **2019 Summer H404/02** (Problem Solving): 6 questions · **70 / 70 marks** · Verified ✓
* **2019 Summer H004/01** (AS Principles): 23 questions · **90 / 90 marks** · Verified ✓
* **2018 Practice Set 1 H404/01** (Principles): 25 questions · **80 / 80 marks** · Verified ✓
* **2018 Practice Set 1 H404/02** (Problem Solving): 7 questions · **70 / 70 marks** · Verified ✓
* **Total Questions in Database:** **127**
* **Total Curriculum Marks:** **620 marks**

---

## 5. Notes for Scanned (image-only) PDFs

Some OCR papers (e.g. Nov 2020 QP + RB) are scanned, so `get_text()` returns nothing.

1. Render each page (zoom 1.1) and build contact sheets with a pt ruler to measure crop rectangles.
2. Write a per-paper build script (template: [`tools/build_2020_autumn_02.py`](file:///C:/Users/Alexander/.gemini/antigravity/scratch/leets/tools/build_2020_autumn_02.py)) that renders clips at zoom 2.
3. **Answer-space rule:** question cards keep the prompt + 1–2 answer lines (or the final answer line, e.g. `Distance H ........ mm`) + the mark `[X]`; large working boxes are cut out and the two halves stitched.
4. Mark scheme pages are landscape tables — `autotrim_bottom()` strips empty table space (check short trailing words aren't clipped).
5. Resource naming: `fig-N.jpg` / `fig-Na.jpg` → "Fig. N" / "Fig. Na"; whole RB text pages → `rb-pN.jpg` → "Resource Booklet – page N".
