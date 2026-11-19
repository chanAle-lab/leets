import os

html_path = r'C:\Users\Alexander\.gemini\antigravity\scratch\leets\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update nav tabs to exactly match screenshot (4 tabs)
old_nav = '''      <nav class="view-tabs" role="tablist">
        <button class="tab-link active" data-view="strata" role="tab" aria-selected="true">Specification</button>
        <button class="tab-link" data-view="cards" role="tab" aria-selected="false">Questions</button>
        <button class="tab-link" data-view="practice" role="tab" aria-selected="false">Practice</button>
        <button class="tab-link" data-view="cheatsheets" role="tab" aria-selected="false">Cheatsheets</button>
        <button class="tab-link" data-view="teachers" role="tab" aria-selected="false">Teacher's Hub</button>
      </nav>'''

new_nav = '''      <nav class="view-tabs" role="tablist">
        <button class="tab-link active" data-view="strata" role="tab" aria-selected="true">Specification</button>
        <button class="tab-link" data-view="cards" role="tab" aria-selected="false">Questions</button>
        <button class="tab-link" data-view="practice" role="tab" aria-selected="false">Practice</button>
        <button class="tab-link" data-view="cheatsheets" role="tab" aria-selected="false">Cheatsheets</button>
      </nav>'''

if old_nav in content:
    content = content.replace(old_nav, new_nav, 1)
    print("Updated nav tabs")
else:
    print("old_nav not found, check if already changed")

# 2. Update footer to keep Teacher's Hub accessible
old_footer = '''    <footer>
      OCR A Level Design and Technology: Design Engineering (H404). Specification © OCR (Oxford Cambridge and RSA).
    </footer>'''

new_footer = '''    <footer>
      <span>OCR A Level Design and Technology: Design Engineering (H404). Specification © OCR (Oxford Cambridge and RSA).</span>
      <span style="opacity:0.4;margin:0 8px;">·</span>
      <a href="#view=teachers" id="footer-teachers-link" style="color:var(--muted);text-decoration:none;transition:color 0.15s;">Teacher's Hub</a>
    </footer>'''

if old_footer in content:
    content = content.replace(old_footer, new_footer, 1)
    print("Updated footer")
else:
    print("old_footer not found, check if already changed")

# 3. Add footer link click handler in JS
old_footer_bind = '''/* Formula modal controls */
$('#btn-open-formulae').onclick = () => {'''

new_footer_bind = '''/* Footer Teacher Hub Link */
const footerTeacherBtn = $('#footer-teachers-link');
if (footerTeacherBtn) {
  footerTeacherBtn.onclick = (e) => {
    e.preventDefault();
    state.view = 'teachers';
    state.teacherTab = 'hub';
    syncViewButtons();
    toHash();
    render();
  };
}

/* Formula modal controls */
$('#btn-open-formulae').onclick = () => {'''

if old_footer_bind in content:
    content = content.replace(old_footer_bind, new_footer_bind, 1)
    print("Updated JS footer listener")
else:
    print("old_footer_bind not found, check if already changed")

# 4. Add return button to Teacher Dashboard
old_hub_head = '''<div class="teacher-hub-wrap">
      <nav class="teacher-nav">'''

new_hub_head = '''<div class="teacher-hub-wrap">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
        <a href="#" onclick="event.preventDefault();state.view='strata';syncViewButtons();toHash();render();" style="color:var(--muted);text-decoration:none;font-size:0.85rem;font-weight:600;display:inline-flex;align-items:center;gap:6px;">← Back to Revision Portal</a>
      </div>
      <nav class="teacher-nav">'''

if old_hub_head in content:
    content = content.replace(old_hub_head, new_hub_head, 1)
    print("Updated Teacher Hub return banner")
else:
    print("old_hub_head not found, check if already changed")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved index.html successfully")
