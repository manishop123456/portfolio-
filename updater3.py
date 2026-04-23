import os

file_path = "c:/Users/manis/Videos/TCSC/sab saman/vs code projects/portfolio/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update HTML
html_start = text.find('    <section id="hero">')
html_end = text.find('<!-- TICKER -->')
if html_start != -1 and html_end != -1:
    new_html = """    <section id="hero">
      <div class="hud hud-tl"><span class="rec">REC</span>&nbsp;<span id="tc">00:00:00:00</span></div>
      <div class="hud hud-tr">SYS.STATUS: ONLINE<br />MANISH_STUDIO v4.0</div>
      <div class="hud hud-bl">COORD: 19.0760° N, 72.8777° E &nbsp;·&nbsp; MUMBAI</div>
      <div class="hud hud-br" id="fps-el">60 FPS</div>

      <!-- EYEBROW / TOP TEXT -->
      <div class="hero-top-accent">
        <div class="hero-eyebrow" id="h-eye">Full Stack Developer</div>
      </div>

      <!-- CENTRIC MASSIVE POSTER -->
      <div class="hero-center-block">
        <div class="hero-massive-text">
          <div class="hero-line hl-top" id="hl1">MANISH</div>
          <div class="hero-line hl-bot" id="hl2">CHOUDHARY</div>
        </div>

        <div class="hero-photo-premium" id="hero-photo">
          <div class="premium-glass-backing"></div>
          <img src="profile.png" alt="Manish Choudhary" id="hero-img" />
          <div class="hero-photo-grain"></div>
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


# 2. Update CSS
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
      gap: 16px;
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

    /* PREMIUM CENTERED PHOTO */
    .hero-photo-premium {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: clamp(140px, 20vw, 280px);
      aspect-ratio: 3 / 4;
      z-index: 10;
      transition: transform 0.8s cubic-bezier(0.23, 1, 0.32, 1);
      cursor: none;
    }

    .hero-photo-premium:hover {
      transform: translate(-50%, -52%) scale(1.05);
    }

    .premium-glass-backing {
      position: absolute;
      inset: -10px;
      background: rgba(var(--ar), var(--ag), var(--ab), 0.02);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(var(--ar), var(--ag), var(--ab), 0.1);
      z-index: 1;
      opacity: 0;
      transition: opacity 0.8s, inset 0.8s;
    }

    .hero-photo-premium:hover .premium-glass-backing {
      opacity: 1;
      inset: -16px;
    }

    #hero-img {
      position: relative;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center top;
      z-index: 2;
      filter: grayscale(0.85) contrast(1.1) brightness(0.9);
      box-shadow: 0 30px 80px rgba(0,0,0,0.6);
      transition: filter 0.8s, box-shadow 0.8s;
    }

    .hero-photo-premium:hover #hero-img {
      filter: grayscale(0) contrast(1.05) brightness(1);
      box-shadow: 0 40px 100px rgba(0,0,0,0.9), 0 0 0 1px rgba(var(--ar), var(--ag), var(--ab), 0.3);
    }

    .hero-photo-grain {
      position: absolute;
      inset: 0;
      z-index: 3;
      pointer-events: none;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 400'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.5'/%3E%3C/svg%3E");
      opacity: 0.15;
      mix-blend-mode: overlay;
    }

    /* Minimalist Accents */
    .hero-photo-premium::before {
      content: '';
      position: absolute;
      top: -6px;
      left: -6px;
      width: 30%;
      height: 30%;
      border-top: 1px solid rgba(255,255,255,0.4);
      border-left: 1px solid rgba(255,255,255,0.4);
      z-index: 4;
      transition: transform 0.6s, border-color 0.6s;
    }

    .hero-photo-premium::after {
      content: '';
      position: absolute;
      bottom: -6px;
      right: -6px;
      width: 30%;
      height: 30%;
      border-bottom: 2px solid var(--accent);
      border-right: 2px solid var(--accent);
      z-index: 4;
      transition: transform 0.6s, border-color 0.6s;
    }

    .hero-photo-premium:hover::before {
      transform: translate(-6px, -6px);
      border-color: rgba(var(--ar), var(--ag), var(--ab), 1);
    }
    
    .hero-photo-premium:hover::after {
      transform: translate(6px, 6px);
      border-color: rgba(var(--ar), var(--ag), var(--ab), 1);
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

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)
print("done updater3")
