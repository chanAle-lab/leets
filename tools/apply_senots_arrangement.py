import re
import os

html_path = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update status bar HTML to include selection actions
old_status_bar = '''    <!-- Results Status Bar -->
    <div class="status-bar" id="status-bar">
      <span id="results-count-msg">Loading...</span>
      <span id="results-active-tag"></span>
    </div>'''

new_status_bar = '''    <!-- Results Status Bar -->
    <div class="status-bar" id="status-bar">
      <div>
        <span id="results-count-msg">Loading...</span>
        <span id="results-selection-actions" style="margin-left:12px;display:inline-flex;align-items:center;gap:6px"></span>
      </div>
      <span id="results-active-tag"></span>
    </div>'''

if old_status_bar in content:
    content = content.replace(old_status_bar, new_status_bar, 1)
    print("Updated status bar HTML")
else:
    print("Status bar HTML already updated or not found")

# 2. Add selection-dock and print-container right before Lightbox Modal
old_modal_anchor = '''<!-- Lightbox Modal -->
<div class="modal-overlay" id="modal-box"'''

new_modal_anchor = '''<!-- Floating Selection Dock for Print / Export -->
<div id="selection-dock" class="selection-dock hidden" role="region" aria-label="Selected questions toolbar">
  <div class="selection-dock-info">
    <span id="sel-count-txt"><b>0</b> questions selected</span> · <span id="sel-marks-txt">0m</span>
  </div>
  <div class="selection-dock-opts">
    <label title="Include official OCR mark schemes">
      <input type="checkbox" id="sel-dock-ms">
      <span>Include mark schemes</span>
    </label>
    <label title="Include resource diagrams & photos">
      <input type="checkbox" id="sel-dock-fig" checked>
      <span>Include figures</span>
    </label>
  </div>
  <div class="selection-dock-actions">
    <button type="button" class="btn-minimal" id="btn-dock-clear" onclick="clearSelection()" title="Clear selected questions">Clear</button>
    <button type="button" class="btn-print-primary" id="btn-dock-print" onclick="printSelectedQuestions()" title="Print or save selected questions to PDF">
      Export PDF / Print
    </button>
  </div>
</div>

<!-- Dedicated Print & PDF Export Mount -->
<div id="print-container"></div>

<!-- Lightbox Modal -->
<div class="modal-overlay" id="modal-box"'''

if 'id="selection-dock"' not in content and old_modal_anchor in content:
    content = content.replace(old_modal_anchor, new_modal_anchor, 1)
    print("Added selection dock and print container markup")
else:
    print("Selection dock markup already present or anchor not found")

# 3. Update renderCard and figLabel
old_render_card_block = '''function renderCard(x) {
  const p = D.P[x.paper] || { series: 'Exam', year: 2023, unit: 'Design Engineering', code: 'H404/01' };
  const isMastered = mastered.has(x.id);
  const isBookmarked = bookmarked.has(x.id);

  const tags = x.topics.map(t => `<a class="q-tag" href="#view=cards&topic=${t}">${esc(t)} ${esc(T[t] ? T[t].name : '')}</a>`).join('')
    + x.skills.map(s => `<span class="q-tag">${esc(S[s] ? S[s].name : s)}</span>`).join('');

  return `
    <article class="q-card" id="q-${x.id}">
      <div class="q-card-header">
        <div class="q-title-wrap">
          <h2 class="q-title">Question ${esc(x.question)}</h2>
          <span class="q-mark">${x.marks} ${x.marks === 1 ? 'mark' : 'marks'}</span>
        </div>
        <div class="q-actions">
          <button type="button" class="btn-q-action ${isBookmarked ? 'active-star' : ''}" onclick="toggleBookmark('${x.id}', this)">
            ${isBookmarked ? 'Bookmarked' : 'Bookmark'}
          </button>
          <button type="button" class="btn-q-action ${isMastered ? 'active-check' : ''}" onclick="toggleMastered('${x.id}', this)">
            ${isMastered ? 'Mastered' : 'Mark done'}
          </button>
          <button type="button" class="btn-q-action" onclick="copyQuestionLink('${x.id}')" title="Copy link">Link</button>
        </div>
      </div>

      <div class="q-citation">${esc(p.series)} ${p.year} · ${esc(p.unit)} (${esc(p.code)}) · Page ${x.page || 1}</div>

      <p class="q-summary"><b>Summary:</b> ${esc(x.summary)}</p>

      ${x.prompt ? `
        <div class="q-prompt-box">
          ${x.prompt}
        </div>
      ` : ''}

      <div class="q-tags">${tags}</div>

      ${x.image ? `
        <div class="img-container">
          <img loading="lazy" src="${esc(x.image)}" alt="Question ${esc(x.question)}" onclick="openModal('${x.id}', 'question')">
        </div>
      ` : ''}

      ${(x.figures || []).map((f, fi) => `
        <details class="details-clean">
          <summary>Resource figure: ${figLabel(f)}</summary>
          <div class="details-body">
            <div class="img-container">
              <img loading="lazy" src="${esc(f)}" alt="${figLabel(f)}" onclick="openModal('${x.id}', 'figure', ${fi})">
            </div>
          </div>
        </details>
      `).join('')}

      ${(x.markscheme_text || x.markscheme) ? `
        <details class="details-clean">
          <summary>Official Mark Scheme & Model Answer</summary>
          <div class="details-body">
            ${x.markscheme_text ? `<div>${x.markscheme_text}</div>` : ''}
            ${x.markscheme ? `
              <div class="img-container">
                <img loading="lazy" src="${esc(x.markscheme)}" alt="Mark Scheme" onclick="openModal('${x.id}', 'markscheme')">
              </div>
            ` : ''}
          </div>
        </details>
      ` : ''}

      <div class="q-footer" style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px">
        <a href="javascript:void(0)" class="btn-compare-link" onclick="openSheet('${x.topics[0]}')">Cheatsheet: ${esc(x.topics[0])} ${esc(T[x.topics[0]] ? T[x.topics[0]].name : '')}</a>
        ${(x.markscheme || x.markscheme_text) ? `
          <button type="button" class="btn-compare-link" onclick="openModal('${x.id}', 'split')">View side-by-side with mark scheme</button>
        ` : ''}
      </div>
    </article>
  `;
}

function figLabel(f) {
  if (f.includes('data')) return 'Engineering Data Sheet';
  if (f.includes('fig')) return 'Figure Diagram';
  return 'Technical Resource';
}'''

new_render_card_block = '''function renderCard(x) {
  const p = D.P[x.paper] || { series: 'Exam', year: 2023, unit: 'Design Engineering', code: 'H404/01' };
  const isMastered = mastered.has(x.id);
  const isBookmarked = bookmarked.has(x.id);
  const isSelected = selectedQuestions.has(x.id);

  const tags = x.topics.map(t => `<a class="q-tag" href="#view=cards&topic=${t}">${esc(t)} ${esc(T[t] ? T[t].name : '')}</a>`).join('')
    + x.skills.map(s => `<span class="q-tag">${esc(S[s] ? S[s].name : s)}</span>`).join('');

  return `
    <article class="q-card ${isSelected ? 'is-selected' : ''}" id="q-${x.id}">
      <div class="q-card-header">
        <div class="q-title-wrap">
          <label class="q-select-chk-label" title="Select for export / print">
            <input type="checkbox" class="q-select-chk" data-qid="${x.id}" ${isSelected ? 'checked' : ''} onchange="toggleSelectQuestion('${x.id}', this.checked)">
          </label>
          <h2 class="q-title">Question ${esc(x.question)}</h2>
          <span class="q-mark">${x.marks} ${x.marks === 1 ? 'mark' : 'marks'}</span>
        </div>
        <div class="q-actions">
          <button type="button" class="btn-q-action" onclick="printSingleQuestion('${x.id}')" title="Print or save as PDF">Print / PDF</button>
          <button type="button" class="btn-q-action ${isBookmarked ? 'active-star' : ''}" onclick="toggleBookmark('${x.id}', this)">
            ${isBookmarked ? 'Bookmarked' : 'Bookmark'}
          </button>
          <button type="button" class="btn-q-action ${isMastered ? 'active-check' : ''}" onclick="toggleMastered('${x.id}', this)">
            ${isMastered ? 'Mastered' : 'Mark done'}
          </button>
          <button type="button" class="btn-q-action" onclick="copyQuestionLink('${x.id}')" title="Copy link">Link</button>
        </div>
      </div>

      <div class="q-citation">${esc(p.series)} ${p.year} · ${esc(p.unit)} (${esc(p.code)}) · Page ${x.page || 1}</div>

      <p class="q-summary">${esc(x.summary)}</p>
      ${x.note ? `<div class="q-note">${esc(x.note)}</div>` : ''}

      <div class="q-tags">${tags}</div>

      ${x.image ? `
        <div class="img-container">
          <img loading="lazy" src="${esc(x.image)}" alt="Question ${esc(x.question)}" onclick="openModal('${x.id}', 'question')">
        </div>
      ` : (x.prompt ? `
        <div class="q-prompt-box">
          ${x.prompt}
        </div>
      ` : '')}

      ${(x.figures || []).map((f, fi) => `
        <details class="details-clean">
          <summary>${figLabel(f)}</summary>
          <div class="details-body">
            <div class="img-container">
              <img loading="lazy" src="${esc(f)}" alt="${figLabel(f)}" onclick="openModal('${x.id}', 'figure', ${fi})">
            </div>
          </div>
        </details>
      `).join('')}

      ${x.markscheme ? `
        <details class="details-clean">
          <summary>Mark scheme</summary>
          <div class="details-body">
            <div class="img-container">
              <img loading="lazy" src="${esc(x.markscheme)}" alt="Mark Scheme" onclick="openModal('${x.id}', 'markscheme')">
            </div>
          </div>
        </details>
      ` : (x.markscheme_text ? `
        <details class="details-clean">
          <summary>Mark scheme</summary>
          <div class="details-body">
            <div style="line-height:1.6;font-size:0.9rem">${x.markscheme_text}</div>
          </div>
        </details>
      ` : '')}

      <div class="q-footer" style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px">
        <a href="javascript:void(0)" class="btn-compare-link" onclick="openSheet('${x.topics[0]}')">Cheatsheet: ${esc(x.topics[0])} ${esc(T[x.topics[0]] ? T[x.topics[0]].name : '')}</a>
        ${(x.markscheme || x.markscheme_text) ? `
          <button type="button" class="btn-compare-link" onclick="openModal('${x.id}', 'split')">View side-by-side with mark scheme</button>
        ` : ''}
      </div>
    </article>
  `;
}

function figLabel(f) {
  if (f.includes('formulae') || f.includes('datasheet') || f.includes('data')) return 'Engineering Formulae & Data Sheet';
  if (f.includes('flowcode') || f.includes('flowchart')) return 'System Flowchart & Algorithm Logic';
  if (f.includes('gear')) return 'Compound Gear Train Layout';
  if (f.includes('circuit') || f.includes('schematic')) return 'Microcontroller Circuit Schematic';
  if (f.includes('system-diagram')) return 'Telemetry System Block Diagram';
  if (f.includes('propeller')) return 'Propeller Pitch & Velocity Vectors';
  if (f.includes('diagram')) return 'Exemplar Model Solution Diagram';

  const m2 = f.match(/fig-(\d+)-(\d+)([a-z]?)\.jpg/i);
  if (m2) {
    const sub = m2[3] ? `(${m2[3]})` : '';
    return `Fig. ${m2[1]}.${m2[2]}${sub}`;
  }
  const m1 = f.match(/fig-(\d+)\.jpg/i);
  if (m1) {
    return `Fig. ${m1[1]}`;
  }
  return 'Resource Diagram';
}'''

if old_render_card_block in content:
    content = content.replace(old_render_card_block, new_render_card_block, 1)
    print("Updated renderCard and figLabel functions")
else:
    print("renderCard block not found, check matching")

# 4. Update modal split-view rendering in renderModalContent
old_modal_content_block = '''  } else if (activeModalTab === 'split') {
    body.innerHTML = `
      <div class="split-view">
        <div class="split-pane">
          <div class="split-pane-head">Question & Specification Prompt</div>
          <div class="split-pane-body">
            ${q.image ? `<img src="${esc(q.image)}" alt="Question">` : ''}
            <div style="line-height:1.6">${q.prompt || esc(q.summary)}</div>
            ${(q.figures || []).map(f => `<img src="${esc(f)}" alt="${figLabel(f)}">`).join('')}
          </div>
        </div>
        <div class="split-pane">
          <div class="split-pane-head">Mark Scheme & Model Calculations</div>
          <div class="split-pane-body">
            ${q.markscheme ? `<img src="${esc(q.markscheme)}" alt="Mark Scheme">` : ''}
            <div style="line-height:1.6">${q.markscheme_text || 'Mark scheme available in syllabus reference.'}</div>
          </div>
        </div>
      </div>`;
  }'''

new_modal_content_block = '''  } else if (activeModalTab === 'split') {
    body.innerHTML = `
      <div class="split-view">
        <div class="split-pane">
          <div class="split-pane-head">Question & Resource</div>
          <div class="split-pane-body">
            ${q.image ? `<img src="${esc(q.image)}" alt="Question">` : (q.prompt ? `<div style="line-height:1.6">${q.prompt}</div>` : '')}
            ${(q.figures || []).map(f => `<img src="${esc(f)}" alt="${figLabel(f)}">`).join('')}
          </div>
        </div>
        <div class="split-pane">
          <div class="split-pane-head">Mark Scheme</div>
          <div class="split-pane-body">
            ${q.markscheme ? `<img src="${esc(q.markscheme)}" alt="Mark Scheme">` : ''}
            ${!q.markscheme && q.markscheme_text ? `<div style="line-height:1.6">${q.markscheme_text}</div>` : ''}
          </div>
        </div>
      </div>`;
  }'''

if old_modal_content_block in content:
    content = content.replace(old_modal_content_block, new_modal_content_block, 1)
    print("Updated modal split-view rendering")
else:
    print("Modal split-view block not found, check matching")

# 5. Add selection dock & print functions in JavaScript
selection_code = '''
/* ========================================================
   Selection Dock & Batch Print / PDF Export (Senots Engine)
   ======================================================== */
let selectedQuestions = new Set();

function toggleSelectQuestion(id, checked) {
  if (checked) {
    selectedQuestions.add(id);
  } else {
    selectedQuestions.delete(id);
  }
  const card = $(`#q-${id}`);
  if (card) {
    card.classList.toggle('is-selected', checked);
    const chk = card.querySelector('.q-select-chk');
    if (chk) chk.checked = checked;
  }
  updateSelectionDock();
  updateStatusSelectionInfo();
}

function selectAllFiltered() {
  const list = filtered();
  list.forEach(q => {
    selectedQuestions.add(q.id);
    const card = $(`#q-${q.id}`);
    if (card) {
      card.classList.add('is-selected');
      const chk = card.querySelector('.q-select-chk');
      if (chk) chk.checked = true;
    }
  });
  updateSelectionDock();
  updateStatusSelectionInfo();
  showToast(`Selected ${list.length} questions`);
}

function clearSelection() {
  selectedQuestions.clear();
  $$('.q-card.is-selected').forEach(c => c.classList.remove('is-selected'));
  $$('.q-select-chk').forEach(c => c.checked = false);
  updateSelectionDock();
  updateStatusSelectionInfo();
  showToast('Selection cleared');
}

function updateSelectionDock() {
  const dock = $('#selection-dock');
  if (!dock) return;
  const count = selectedQuestions.size;
  if (count === 0 || state.view !== 'cards') {
    dock.classList.add('hidden');
    return;
  }
  dock.classList.remove('hidden');

  let marks = 0;
  if (D && D.questions) {
    D.questions.forEach(q => {
      if (selectedQuestions.has(q.id)) marks += q.marks;
    });
  }

  $('#sel-count-txt').innerHTML = `<b>${count}</b> ${count === 1 ? 'question' : 'questions'} selected`;
  $('#sel-marks-txt').textContent = `${marks}m`;
  $('#btn-dock-print').textContent = `Export PDF / Print (${count})`;
}

function updateStatusSelectionInfo() {
  const container = $('#results-selection-actions');
  if (!container) return;
  if (state.view !== 'cards') {
    container.style.display = 'none';
    return;
  }
  container.style.display = 'inline-flex';
  const list = filtered();
  const count = selectedQuestions.size;
  if (count === 0) {
    container.innerHTML = `<button type="button" class="btn-minimal" style="padding:2px 8px;font-size:0.75rem" onclick="selectAllFiltered()">Select All (${list.length})</button>`;
  } else {
    container.innerHTML = `
      <span style="font-size:0.78rem;color:var(--ink);font-weight:600">${count} selected</span>
      <button type="button" class="btn-minimal" style="padding:2px 8px;font-size:0.75rem" onclick="selectAllFiltered()">Select All (${list.length})</button>
      <button type="button" class="btn-minimal" style="padding:2px 8px;font-size:0.75rem" onclick="clearSelection()">Clear</button>
    `;
  }
}

function printSingleQuestion(id) {
  const q = D.questions.find(x => x.id === id);
  if (!q) return;
  const includeMS = $('#sel-dock-ms') && $('#sel-dock-ms').checked;
  const withMS = includeMS || (q.markscheme && confirm('Include mark scheme in this print / PDF export?\\n\\n• OK: Question and Mark Scheme\\n• Cancel: Question only'));
  executePrintQuestions([q], {
    title: `Question ${q.question} (${q.marks}m)`,
    includeMS: withMS,
    includeFigures: true
  });
}

function printSelectedQuestions() {
  if (!selectedQuestions.size) {
    showToast('No questions selected. Use checkboxes to select questions first.');
    return;
  }
  const qs = D.questions.filter(q => selectedQuestions.has(q.id));
  const includeMS = $('#sel-dock-ms') ? $('#sel-dock-ms').checked : false;
  const includeFig = $('#sel-dock-fig') ? $('#sel-dock-fig').checked : true;
  executePrintQuestions(qs, {
    title: 'Selected Questions Pack',
    includeMS: includeMS,
    includeFigures: includeFig
  });
}

async function executePrintQuestions(questions, options = {}) {
  if (!questions || !questions.length) {
    showToast('No questions to print.');
    return;
  }

  const includeMS = !!options.includeMS;
  const includeFigures = options.includeFigures !== false;

  let printContainer = $('#print-container');
  if (!printContainer) {
    printContainer = document.createElement('div');
    printContainer.id = 'print-container';
    document.body.appendChild(printContainer);
  }

  let itemsHtml = questions.map(q => {
    let figHtml = '';
    if (includeFigures && q.figures && q.figures.length) {
      figHtml = q.figures.map(f => `
        <div class="print-pack-img-block">
          <img src="${esc(f)}" alt="${esc(figLabel(f))}">
        </div>
      `).join('');
    }

    let msHtml = '';
    if (includeMS && q.markscheme) {
      msHtml = `
        <div class="print-pack-ms-block">
          <div class="print-pack-img-block">
            <img src="${esc(q.markscheme)}" alt="Mark Scheme Question ${esc(q.question)}">
          </div>
        </div>
      `;
    } else if (includeMS && q.markscheme_text) {
      msHtml = `
        <div class="print-pack-ms-block" style="padding:16px;font-size:9pt;line-height:1.5">
          <b>Mark Scheme Question ${esc(q.question)}:</b><br>
          ${q.markscheme_text}
        </div>
      `;
    }

    let qImg = q.image ? `
      <div class="print-pack-img-block">
        <img src="${esc(q.image)}" alt="Question ${esc(q.question)}">
      </div>
    ` : `
      <div style="padding:16px;font-size:10pt;line-height:1.5">
        <b>Question ${esc(q.question)} (${q.marks} marks):</b><br>
        ${q.prompt || esc(q.summary)}
      </div>
    `;

    return `
      <article class="print-pack-q-item">
        ${qImg}
        ${figHtml}
        ${msHtml}
      </article>
    `;
  }).join('');

  printContainer.innerHTML = `
    <main class="print-pack-list">
      ${itemsHtml}
    </main>
  `;

  showToast('Preparing PDF / print preview...');

  const imgs = Array.from(printContainer.querySelectorAll('img'));
  await Promise.all(imgs.map(img => {
    if (img.complete && img.naturalWidth > 0) return Promise.resolve();
    return new Promise(resolve => {
      img.onload = img.onerror = resolve;
      if (img.decode) {
        img.decode().then(resolve).catch(resolve);
      }
    });
  }));

  document.body.classList.add('is-printing-pack');

  setTimeout(() => {
    window.print();
  }, 100);
}

window.addEventListener('afterprint', () => {
  document.body.classList.remove('is-printing-pack');
  const pc = $('#print-container');
  if (pc) pc.innerHTML = '';
});
'''

# Check if selection_code is already added
if 'let selectedQuestions = new Set();' not in content:
    # Insert right before function renderCards
    target = 'function renderCards(list) {'
    assert target in content, "renderCards not found"
    content = content.replace(target, selection_code + '\n' + target, 1)
    print("Inserted selection dock & print functions into JS")

# 6. Ensure render() calls updateStatusSelectionInfo and updateSelectionDock
old_render_call = """  if (state.pick) {
    $('#results-count-msg').innerHTML = `1 question (${totalM} marks) · <a href="javascript:void(0)" onclick="state.pick='';toHash();render();" style="color:inherit;text-decoration:underline">Show all</a>`;
  } else {
    $('#results-count-msg').innerHTML = `${list.length.toLocaleString()} questions (${totalM.toLocaleString()} marks)`;
  }"""

new_render_call = """  if (state.pick) {
    $('#results-count-msg').innerHTML = `1 question (${totalM} marks) · <a href="javascript:void(0)" onclick="state.pick='';toHash();render();" style="color:inherit;text-decoration:underline">Show all</a>`;
  } else {
    $('#results-count-msg').innerHTML = `${list.length.toLocaleString()} questions (${totalM.toLocaleString()} marks)`;
  }
  updateStatusSelectionInfo();
  updateSelectionDock();"""

if old_render_call in content:
    content = content.replace(old_render_call, new_render_call, 1)
    print("Updated render() to call selection updates")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated index.html successfully!")
