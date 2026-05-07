import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# 1. Update Fonts & Core variables
html = re.sub(
    r"@import url\('https://fonts\.googleapis\.com/css2\?family=Space\+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap'\);",
    r"@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');",
    html
)
html = html.replace("--color-accent: #7B5EA7;", "--color-accent: #00e5ff;")
html = html.replace("--color-accent-glow: rgba(123, 94, 167, 0.4);", "--color-accent-glow: rgba(0, 229, 255, 0.4);")
html = html.replace("--project-hover: rgba(123, 94, 167, 0.06);", "--project-hover: rgba(0, 229, 255, 0.06);")
html = html.replace("--font-display: 'Space Grotesk', sans-serif;", "--font-display: 'Outfit', sans-serif;")
html = html.replace("--font-body: 'Inter', sans-serif;", "--font-body: 'Outfit', sans-serif;")
html = html.replace("  cursor: none;\n", "")

# Remove .light-mode block
html = re.sub(r"\.light-mode \{[^\}]+\}\n\n", "", html, flags=re.MULTILINE)

# Remove Cursor CSS
html = re.sub(r"/\* CUSTOM CURSOR \*/.*?@media \(max-width: 768px\) \{.*?\}\n\n", "", html, flags=re.DOTALL)

# Remove Theme toggle CSS
html = re.sub(r"/\* THEME TOGGLE \*/.*?/\* HERO \*/", "/* HERO */", html, flags=re.DOTALL)

# Remove parallax & typed cursor CSS
html = re.sub(r"  will-change: transform;\n", "", html)
html = re.sub(r"  height: 2\.5rem;\n", "", html)
html = re.sub(r"\.typed-cursor \{[^\}]+\}\n@keyframes blink \{[^\}]+\}\n\n", "", html, flags=re.MULTILINE|re.DOTALL)

# Update Stats CSS (not needed strictly, just make HTML static)

# Update Skills Marquee CSS
skills_css_old = """/* SKILLS MARQUEE */
.skills-track {
  display: flex; gap: 1.5rem; padding: 2rem 0;
  animation: marquee 25s linear infinite;
  width: max-content;
}
.skills-track:hover { animation-play-state: paused; }
@keyframes marquee { 0%{transform:translateX(0)} 100%{transform:translateX(-50%)} }

.skill-tag {
  display: inline-block; padding: 0.6rem 1.4rem;
  border: 1px solid var(--color-border);
  border-radius: 50px; font-size: 0.95rem;
  font-weight: 500; white-space: nowrap;
  transition: transform 0.3s, box-shadow 0.3s, border-color 0.3s;
}
.skill-tag:hover {
  transform: scale(1.12);
  border-color: var(--color-accent);
  box-shadow: 0 0 18px var(--color-accent-glow);
  color: var(--color-accent);
}"""

skills_css_new = """/* SKILLS */
.skills-track {
  display: flex; gap: 1rem; padding: 1rem 0;
  flex-wrap: wrap;
}

.skill-tag {
  display: inline-block; padding: 0.6rem 1.4rem;
  border: 1px solid var(--color-border);
  border-radius: 50px; font-size: 0.95rem;
  font-weight: 500; white-space: nowrap;
  transition: box-shadow 0.3s, border-color 0.3s, color 0.3s;
}
.skill-tag:hover {
  border-color: var(--color-accent);
  box-shadow: 0 0 12px var(--color-accent-glow);
  color: var(--color-accent);
}"""
html = html.replace(skills_css_old, skills_css_new)

# Remove theme-toggle from responsive CSS
html = html.replace("  .theme-toggle { bottom: 1rem; right: 1rem; padding: 0.6rem 1rem; font-size: 0.8rem; }\n", "")

# --- HTML Replacements ---
# Remove cursor dots & theme toggle
html = html.replace('  <!-- Custom Cursor -->\n  <div class="cursor-dot"></div>\n  <div class="cursor-ring"></div>\n\n  <!-- Theme Toggle -->\n  <button class="theme-toggle" id="themeToggle">☀️ Light</button>\n\n', '')

# Remove Nav Logo
html = html.replace('    <a href="#" class="nav-logo">portfolio.</a>\n', '    <div></div>\n')

# Update Hero
html = html.replace('<p class="hero-subtitle"><span id="typed"></span><span class="typed-cursor"></span></p>', '<p class="hero-subtitle">Cybersecurity Researcher | Usable Security Specialist | M.Sc. Student</p>')

# Update Stats to remove data-target
html = html.replace('<div class="stat-number" data-target="20" data-suffix="+">0</div>', '<div class="stat-number">20+</div>')
html = html.replace('<div class="stat-number" data-target="1000" data-suffix="+">0</div>', '<div class="stat-number">1000+</div>')
html = html.replace('<div class="stat-number" data-target="3" data-suffix="+">0</div>', '<div class="stat-number">3+</div>')

# Update Skills HTML - remove duplication and overflow
skills_html_old = """      <div style="overflow:hidden">
        <div class="skills-track">"""
skills_html_new = """      <div>
        <div class="skills-track">"""
html = html.replace(skills_html_old, skills_html_new)

duplicated_skills = """          <!-- duplicated for seamless loop -->
          <span class="skill-tag">Risk Assessment</span>
          <span class="skill-tag">Vulnerability Analysis</span>
          <span class="skill-tag">Incident Response</span>
          <span class="skill-tag">Phishing Analysis</span>
          <span class="skill-tag">SOC Workflows</span>
          <span class="skill-tag">Usable Security</span>
          <span class="skill-tag">Access Control</span>
          <span class="skill-tag">ISO 27001</span>
          <span class="skill-tag">ISMS</span>
          <span class="skill-tag">Data Governance</span>
          <span class="skill-tag">Privacy Frameworks</span>
          <span class="skill-tag">Python</span>
          <span class="skill-tag">SQL</span>
          <span class="skill-tag">JavaScript</span>
          <span class="skill-tag">HTML/CSS</span>
          <span class="skill-tag">C/C++</span>
          <span class="skill-tag">Java</span>
          <span class="skill-tag">Linux</span>
          <span class="skill-tag">Wireshark</span>
          <span class="skill-tag">Figma</span>
          <span class="skill-tag">R</span>
          <span class="skill-tag">VBA</span>
          <span class="skill-tag">Jira</span>
          <span class="skill-tag">Confluence</span>
          <span class="skill-tag">Prolific</span>
          <span class="skill-tag">Semi-Structured Interviews</span>
          <span class="skill-tag">Think-Aloud Studies</span>
          <span class="skill-tag">Thematic Coding</span>
          <span class="skill-tag">Mixed Methods</span>
          <span class="skill-tag">Qualitative Research</span>
          <span class="skill-tag">Study Design</span>
          <span class="skill-tag">Ethics/IRB</span>
          <span class="skill-tag">Affinity Mapping</span>
          <span class="skill-tag">Statistical Analysis</span>"""
html = html.replace(duplicated_skills, "")

cert_html_old = """<div style="overflow:hidden; white-space: nowrap; padding-bottom: 1rem;">"""
cert_html_new = """<div style="display: flex; flex-wrap: wrap; gap: 1rem; padding-bottom: 1rem;">"""
html = html.replace(cert_html_old, cert_html_new)
html = html.replace('display:inline-block; margin-right:2rem; ', '')

# --- JS Replacements ---
# Remove Theme toggle logic & cursor logic
html = re.sub(r"  // ─── THEME TOGGLE ───.*?// ─── NAV SCROLL ───", "  // ─── NAV SCROLL ───", html, flags=re.DOTALL)

# Remove Typed subtitle & parallax logic & stat counters
html = re.sub(r"  // ─── TYPED SUBTITLE ───.*?// ─── SCROLL REVEAL ───", "  // ─── SCROLL REVEAL ───", html, flags=re.DOTALL)
html = re.sub(r"  // ─── STAT COUNTERS ───.*?// ─── ACTIVE NAV LINK ───", "  // ─── ACTIVE NAV LINK ───", html, flags=re.DOTALL)

# Remove Tag Rotation logic
html = re.sub(r"  // ─── RANDOM SKILL TAG ROTATION ───.*?\}\);\n", "});\n", html, flags=re.DOTALL)

with open('portfolio.html', 'w') as f:
    f.write(html)
