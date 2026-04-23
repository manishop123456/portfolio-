import os

file_path = "c:/Users/manis/Videos/TCSC/sab saman/vs code projects/portfolio/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Replace the entire #hero HTML
html_start = text.find('    <section id="hero">')
html_end = text.find('<!-- TICKER -->')
if html_start != -1 and html_end != -1:
    new_html = """    <section id="hero">
      <div class="hud hud-tl"><span class="rec">REC</span>&nbsp;<span id="tc">00:00:00:00</span></div>
      <div class="hud hud-tr">SYS.STATUS: ONLINE<br />MANISH_STUDIO v4.0</div>
      <div class="hud hud-bl">COORD: 19.0760° N, 72.8777° E &nbsp;·&nbsp; MUMBAI</div>
      <div class="hud hud-br" id="fps-el">60 FPS</div>

      <!-- EYEBROW / TOP TOPTEXT -->
      <div class="hero-top-accent">
        <div class="hero-eyebrow" id="h-eye">Full Stack Developer</div>
      </div>

      <!-- CENTRIC MASSIVE POSTER -->
      <div class="hero-center-block">
        <div class="hero-massive-text">
          <div class="hero-line hl-top" id="hl1">MANISH</div>
          <div class="hero-line hl-bot" id="hl2">CHOUDHARY</div>
        </div>

        <div class="hero-photo-cyber" id="hero-photo">
          <div class="cyber-frame"></div>
          <div class="cyber-img-wrap">
            <img src="profile.png" alt="Manish Choudhary" id="hero-img" />
            <div class="hero-photo-scan"></div>
            <div class="hero-photo-glitch"></div>
            <div class="cyber-overlay"></div>
          </div>
          <div class="cyber-accent ca-tl"></div>
          <div class="cyber-accent ca-br"></div>
          <div class="cyber-tag"><span id="hp-mode">DEVELOPER</span></div>
        </div>
      </div>

      <!-- BOTTOM CTA -->
      <div class="hero-bottom-accent">
        <div class="hero-sub" id="h-sub">Code · Build · Deploy</div>
        <a href="#about" class="hero-cta">Explore Studio &nbsp;↓</a>
      </div>

      <div class="scroll-ind" id="scroll-ind"><span>Scroll</span>
        <div class="scroll-ln"></div>
      </div>
    </section>
    """
    text = text[:html_start] + new_html + text[html_end:]


# 2. Replace the CSS block
css_start = text.find('    /* ═══ HERO ═══ */')
css_end = text.find('    /* ═══ TICKER ═══ */')
if css_start != -1 and css_end != -1:
    new_css = """    /* ═══ HERO ═══ */
    #hero {
      position: relative;
      z-index: 5;
      height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 0 20px;
      overflow: hidden;
      gap: 6vh;
    }

    .hero-top-accent {
      z-index: 2;
      opacity: 0;
      animation: fadeIn 1s 2s forwards;
    }

    .hero-eyebrow {
      font-family: var(--fm);
      font-size: 10px;
      letter-spacing: .6em;
      text-transform: uppercase;
      color: var(--accent);
      transition: color .6s;
    }

    .hero-center-block {
      position: relative;
      width: 100%;
      max-width: 1200px;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 2;
    }

    .hero-massive-text {
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .hero-line {
      font-family: var(--fd);
      line-height: .75;
      text-shadow: 0 0 60px rgba(var(--ar), var(--ag), var(--ab), .08);
      display: flex;
      justify-content: space-between;
      width: 100%;
    }

    .hl-top { font-size: clamp(60px, 16vw, 320px); color: var(--fg); }
    .hl-bot { font-size: clamp(45px, 12vw, 240px); color: var(--accent); }

    .kc {
      display: inline-block;
      will-change: transform;
    }

    /* CYBERPUNK PHOTO OVERLAY */
    .hero-photo-cyber {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: clamp(240px, 35vw, 450px);
      height: clamp(140px, 20vw, 260px);
      z-index: 10;
      transition: transform 0.6s cubic-bezier(0.23, 1, 0.32, 1);
    }

    .hero-photo-cyber:hover {
      transform: translate(-50%, -52%) scale(1.04);
    }

    .cyber-frame {
      position: absolute;
      inset: -3px;
      clip-path: polygon(15% 0, 100% 0, 85% 100%, 0 100%);
      background: linear-gradient(135deg, var(--accent) 0%, transparent 40%, rgba(var(--ar), var(--ag), var(--ab), 0.3) 60%, var(--accent) 100%);
      animation: framePulse 4s infinite alternate;
    }

    @keyframes framePulse {
      0% { opacity: 0.4; filter: blur(2px) }
      100% { opacity: 1; filter: blur(0px) }
    }

    .cyber-img-wrap {
      position: absolute;
      inset: 0;
      clip-path: polygon(15% 0, 100% 0, 85% 100%, 0 100%);
      background: var(--surface);
      overflow: hidden;
    }

    #hero-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center top;
      filter: grayscale(0.4) contrast(1.1) brightness(0.8);
      transition: filter 0.6s, transform 0.6s;
    }

    .hero-photo-cyber:hover #hero-img {
      filter: grayscale(0) contrast(1.15) brightness(1);
      transform: scale(1.05);
    }

    .cyber-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, transparent 40%),
                  repeating-linear-gradient(to bottom, transparent, transparent 2px, rgba(0,0,0,0.2) 2px, rgba(0,0,0,0.2) 4px);
      mix-blend-mode: multiply;
      pointer-events: none;
    }

    .hero-photo-scan {
      position: absolute;
      inset: 0;
      pointer-events: none;
    }

    .hero-photo-scan::after {
      content: '';
      position: absolute;
      top: -50%;
      left: 0;
      right: 0;
      height: 50%;
      background: linear-gradient(to bottom, transparent, rgba(var(--ar), var(--ag), var(--ab), 0.4), transparent);
      animation: cyberScan 3s linear infinite;
    }

    @keyframes cyberScan {
      0% { top: -50% }
      100% { top: 150% }
    }

    .hero-photo-glitch {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 5;
    }

    .hero-photo-glitch::before {
      content: "";
      position: absolute;
      width: 100%;
      height: 4px;
      background: var(--accent);
      top: 50%;
      left: 0;
      opacity: 0;
      mix-blend-mode: overlay;
      animation: sliceGlitch 6s infinite;
    }

    @keyframes sliceGlitch {
      0%, 94%, 100% { opacity: 0; transform: translateX(0); }
      95% { opacity: 0.9; transform: translateX(-15px); }
      97% { opacity: 0.6; top: 40%; transform: translateX(15px); }
    }

    .cyber-accent {
      position: absolute;
      width: 24px;
      height: 24px;
      border-color: var(--accent);
      border-style: solid;
      z-index: 12;
      transition: all 0.4s;
    }

    .ca-tl { top: -14px; left: 12%; border-width: 2px 0 0 2px; }
    .ca-br { bottom: -14px; right: 12%; border-width: 0 2px 2px 0; }

    .hero-photo-cyber:hover .ca-tl { transform: translate(-6px, -6px); box-shadow: -4px -4px 10px rgba(var(--ar),var(--ag),var(--ab),0.3); }
    .hero-photo-cyber:hover .ca-br { transform: translate(6px, 6px); box-shadow: 4px 4px 10px rgba(var(--ar),var(--ag),var(--ab),0.3); }

    .cyber-tag {
      position: absolute;
      bottom: 20px;
      right: -10px;
      background: var(--accent);
      color: #000;
      padding: 4px 10px;
      font-family: var(--fm);
      font-size: 8px;
      letter-spacing: .2em;
      font-weight: bold;
      transform: rotate(-90deg) translateY(100%);
      transform-origin: bottom right;
      z-index: 15;
      box-shadow: 0 4px 12px rgba(var(--ar), var(--ag), var(--ab), 0.3);
    }

    .hero-bottom-accent {
      display: flex;
      flex-direction: column;
      align-items: center;
      z-index: 2;
    }

    .hero-sub {
      font-family: var(--fm);
      font-size: 10px;
      letter-spacing: .3em;
      text-transform: uppercase;
      opacity: .28;
      margin-bottom: 30px;
    }

    .hero-cta {
      padding: 13px 32px;
      border: 1px solid rgba(var(--ar), var(--ag), var(--ab), .22);
      font-family: var(--fm);
      font-size: 9px;
      letter-spacing: .22em;
      text-transform: uppercase;
      color: var(--accent);
      transition: all .3s;
      position: relative;
      overflow: hidden;
    }

    .hero-cta::after {
      content: '';
      position: absolute;
      inset: 0;
      background: rgba(var(--ar), var(--ag), var(--ab), .05);
      transform: translateX(-101%);
      transition: transform .4s;
    }

    .hero-cta:hover {
      border-color: var(--accent);
      box-shadow: 0 0 28px rgba(var(--ar), var(--ag), var(--ab), .09);
      transform: translateY(-2px);
    }

    .hero-cta:hover::after {
      transform: translateX(0);
    }

    @keyframes fadeIn {
      to { opacity: 1; }
    }

    .scroll-ind {
      position: absolute;
      bottom: 40px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
      opacity: 0;
    }

    .scroll-ind span {
      font-family: var(--fm);
      font-size: 7px;
      letter-spacing: .25em;
      text-transform: uppercase;
      opacity: .28;
    }

    .scroll-ln {
      width: 1px;
      height: 38px;
      background: var(--border);
      position: relative;
      overflow: hidden;
    }

    .scroll-ln::after {
      content: '';
      position: absolute;
      top: -50%;
      left: 0;
      width: 100%;
      height: 50%;
      background: var(--accent);
      animation: sp 1.8s ease infinite;
    }

    @keyframes sp {
      0% { top: -50% }
      100% { top: 150% }
    }

"""
    text = text[:css_start] + new_css + text[css_end:]

# Now we need to remove the previous media query overrides for hero that we injected, 
# since our clamp and display: flex will dynamically handle sizing natively perfectly.

# Simple regex or replace for those blocks if they exist:
import re
text = re.sub(r'#hl1\s*{\s*font-size:[^}]+}', '', text)
text = re.sub(r'#hl2\s*{\s*font-size:[^}]+}', '', text)
text = re.sub(r'\.hero-inner\s*{\s*gap:[^}]+}', '', text)
text = re.sub(r'\.hero-inner\s*{\s*flex-direction:[^}]+}', '', text)
text = re.sub(r'\.hero-photo\s*{\s*width:[^}]+}', '', text)
text = re.sub(r'\.hero-orbit-3\s*{\s*display:[^}]+}', '', text)
text = re.sub(r'\.hero-orbit-2,\s*\.hero-orbit-3,\s*\.hero-particle\s*{\s*display:[^}]+}', '', text)

# Just checking for empty ones now
text = re.sub(r'\s*\n\s*\n', '\n\n', text)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)
print("done updater2")
