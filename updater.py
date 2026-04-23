import sys

file_path = "c:/Users/manis/Videos/TCSC/sab saman/vs code projects/portfolio/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace HTML
old_html = """    <section id="hero">
      <div class="hud hud-tl"><span class="rec">REC</span>&nbsp;<span id="tc">00:00:00:00</span></div>
      <div class="hud hud-tr">SYS.STATUS: ONLINE<br />MANISH_STUDIO v4.0</div>
      <div class="hud hud-bl">COORD: 19.0760° N, 72.8777° E &nbsp;·&nbsp; MUMBAI</div>
      <div class="hud hud-br" id="fps-el">60 FPS</div>

      <div class="hero-inner">
        <!-- FIXED PHOTO -->
        <div class="hero-photo" id="hero-photo">
          <img src="profile.png" alt="Manish Choudhary" id="hero-img" />
          <div class="hero-photo-tint"></div>
          <div class="hero-photo-scan"></div>
          <div class="hero-photo-shimmer"></div>
          <div class="hp-c tl"></div>
          <div class="hp-c tr"></div>
          <div class="hp-c bl"></div>
          <div class="hp-c br"></div>
          <div class="hero-photo-lbl"><span id="hp-mode">Developer</span><span>2025</span></div>
        </div>

        <!-- TEXT -->
        <div class="hero-text">
          <div class="hero-eyebrow" id="h-eye">Full Stack Developer</div>
          <div class="hero-line" id="hl1">MANISH</div>
          <div class="hero-line" id="hl2">CHOUDHARY</div>
          <div class="hero-sub" id="h-sub">Code · Build · Deploy</div>
          <a href="#about" class="hero-cta">Explore Studio &nbsp;↓</a>
        </div>
      </div>

      <div class="scroll-ind" id="scroll-ind"><span>Scroll</span>
        <div class="scroll-ln"></div>
      </div>
    </section>"""

new_html = """    <section id="hero">
      <div class="hud hud-tl"><span class="rec">REC</span>&nbsp;<span id="tc">00:00:00:00</span></div>
      <div class="hud hud-tr">SYS.STATUS: ONLINE<br />MANISH_STUDIO v4.0</div>
      <div class="hud hud-bl">COORD: 19.0760° N, 72.8777° E &nbsp;·&nbsp; MUMBAI</div>
      <div class="hud hud-br" id="fps-el">60 FPS</div>

      <div class="hero-inner">
        <!-- EYEBROW -->
        <div class="hero-eyebrow" id="h-eye">Full Stack Developer</div>

        <!-- NAME TOP -->
        <div class="hero-line" id="hl1">MANISH</div>

        <!-- CENTERED CUTOUT PHOTO -->
        <div class="hero-photo-wrap">
          <div class="hero-photo" id="hero-photo">
            <img src="profile.png" alt="Manish Choudhary" id="hero-img" />
            <div class="hero-photo-tint"></div>
            <div class="hero-photo-scan"></div>
            <div class="hero-photo-shimmer"></div>
            <div class="hero-photo-glitch"></div>
            <div class="hp-c tl"></div>
            <div class="hp-c tr"></div>
            <div class="hp-c bl"></div>
            <div class="hp-c br"></div>
            <div class="hero-photo-lbl"><span id="hp-mode">Developer</span><span>2025</span></div>
          </div>
          <!-- Orbital rings -->
          <div class="hero-orbit hero-orbit-1"><span class="orbit-dot orbit-dot-1"></span></div>
          <div class="hero-orbit hero-orbit-2"><span class="orbit-dot orbit-dot-2"></span></div>
          <div class="hero-orbit hero-orbit-3"></div>
          <!-- Floating particles -->
          <div class="hero-particle"></div>
          <div class="hero-particle"></div>
          <div class="hero-particle"></div>
          <div class="hero-particle"></div>
          <div class="hero-particle"></div>
          <div class="hero-particle"></div>
        </div>

        <!-- NAME BOTTOM -->
        <div class="hero-line" id="hl2">CHOUDHARY</div>

        <div class="hero-sub" id="h-sub">Code · Build · Deploy</div>
        <a href="#about" class="hero-cta">Explore Studio &nbsp;↓</a>
      </div>

      <div class="scroll-ind" id="scroll-ind"><span>Scroll</span>
        <div class="scroll-ln"></div>
      </div>
    </section>"""

text = text.replace(old_html, new_html)

# Replace Media Query 1
old_m1 = """      .hero-inner {
        flex-direction: column-reverse;
        gap: 20px
      }

      .hero-photo {
        width: clamp(100px, 25vw, 160px)
      }"""
new_m1 = """      .hero-inner {
        gap: 0px
      }

      .hero-photo {
        width: clamp(120px, 22vw, 180px);
        height: clamp(120px, 22vw, 180px);
      }
      .hero-orbit-3 { display: none }"""
text = text.replace(old_m1, new_m1)

# Replace Media Query 2
old_m2 = """      #hl1 {
        font-size: 18vw
      }

      #hl2 {
        font-size: 14vw
      }"""
new_m2 = """      #hl1 {
        font-size: 14vw
      }

      #hl2 {
        font-size: 11vw
      }
      .hero-photo {
        width: 110px;
        height: 110px
      }
      .hero-orbit-2, .hero-orbit-3, .hero-particle {
        display: none
      }"""
text = text.replace(old_m2, new_m2)

lines = text.split('\n')
new_css = """    /* ═══ HERO ═══ */
    #hero {
      position: relative;
      z-index: 5;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 0 20px;
      overflow: hidden
    }

    .hero-inner {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
      z-index: 2;
      gap: 0;
    }

    .hero-text {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center
    }

    .hero-eyebrow {
      font-family: var(--fm);
      font-size: 10px;
      letter-spacing: .5em;
      text-transform: uppercase;
      color: var(--accent);
      margin-bottom: 24px;
      opacity: 0;
      transition: color .6s
    }

    .hero-line {
      display: block;
      font-family: var(--fd);
      line-height: .88;
      letter-spacing: .06em;
      text-align: center;
      text-shadow: 0 0 60px rgba(var(--ar), var(--ag), var(--ab), .1)
    }

    #hl1 {
      font-size: clamp(60px, 13vw, 200px);
      margin-bottom: 12px
    }

    #hl2 {
      font-size: clamp(50px, 10vw, 160px);
      margin-top: 12px
    }

    .kc {
      display: inline-block;
      will-change: transform;
      font-size: inherit
    }

    .hero-sub {
      margin-top: 28px;
      font-family: var(--fm);
      font-size: 10px;
      letter-spacing: .3em;
      text-transform: uppercase;
      opacity: .28
    }

    .hero-cta {
      margin-top: 40px;
      padding: 13px 32px;
      border: 1px solid rgba(var(--ar), var(--ag), var(--ab), .22);
      font-family: var(--fm);
      font-size: 9px;
      letter-spacing: .22em;
      text-transform: uppercase;
      color: var(--accent);
      opacity: 0;
      transition: all .3s;
      position: relative;
      overflow: hidden
    }

    .hero-cta::after {
      content: '';
      position: absolute;
      inset: 0;
      background: rgba(var(--ar), var(--ag), var(--ab), .05);
      transform: translateX(-101%);
      transition: transform .4s
    }

    .hero-cta:hover {
      border-color: var(--accent);
      box-shadow: 0 0 28px rgba(var(--ar), var(--ag), var(--ab), .09);
      transform: translateY(-2px)
    }

    .hero-cta:hover::after {
      transform: translateX(0)
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
      opacity: 0
    }

    .scroll-ind span {
      font-family: var(--fm);
      font-size: 7px;
      letter-spacing: .25em;
      text-transform: uppercase;
      opacity: .28
    }

    .scroll-ln {
      width: 1px;
      height: 38px;
      background: var(--border);
      position: relative;
      overflow: hidden
    }

    .scroll-ln::after {
      content: '';
      position: absolute;
      top: -50%;
      left: 0;
      width: 100%;
      height: 50%;
      background: var(--accent);
      animation: sp 1.8s ease infinite
    }

    @keyframes sp {
      0% {
        top: -50%
      }

      100% {
        top: 150%
      }
    }

    /* ═══ HERO PHOTO (CENTERED CUTOUT) ═══ */
    .hero-photo-wrap {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto;
    }

    .hero-photo {
      position: relative;
      width: clamp(160px, 18vw, 260px);
      height: clamp(160px, 18vw, 260px);
      flex-shrink: 0;
      overflow: hidden;
      border-radius: 50%;
      border: 2px solid rgba(var(--ar), var(--ag), var(--ab), .2);
      box-shadow: 0 0 60px rgba(var(--ar), var(--ag), var(--ab), .12), 0 0 120px rgba(var(--ar), var(--ag), var(--ab), .05), 0 24px 80px rgba(0, 0, 0, .7);
      transition: border-color .6s, box-shadow .6s
    }

    .hero-photo img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top center;
      display: block;
      filter: grayscale(.15) contrast(1.08);
      transition: filter .6s
    }

    .hero-photo:hover img {
      filter: grayscale(0) contrast(1.12)
    }

    .hero-photo-tint {
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 50% 35%, transparent 30%, rgba(0, 0, 0, .5) 100%);
      border-radius: 50%;
      transition: background .6s
    }

    .hero-photo-scan {
      position: absolute;
      inset: 0;
      overflow: hidden;
      pointer-events: none;
      border-radius: 50%
    }

    .hero-photo-scan::after {
      content: '';
      position: absolute;
      top: -40%;
      left: 0;
      right: 0;
      height: 40%;
      background: linear-gradient(to bottom, transparent, rgba(var(--ar), var(--ag), var(--ab), .08), transparent);
      animation: pcScan 3s ease infinite
    }

    @keyframes pcScan {
      0% {
        top: -40%
      }

      100% {
        top: 110%
      }
    }

    .hero-photo-shimmer {
      position: absolute;
      inset: 0;
      border-radius: 50%;
      background: linear-gradient(105deg, transparent 40%, rgba(var(--ar), var(--ag), var(--ab), .06) 50%, transparent 60%);
      background-size: 200% 100%;
      animation: shimmer 4s ease infinite;
      pointer-events: none
    }

    @keyframes shimmer {
      0% {
        background-position: 200% 0
      }

      100% {
        background-position: -200% 0
      }
    }

    /* Cutout corners */
    .hp-c {
      position: absolute;
      width: 18px;
      height: 18px;
      border-color: rgba(var(--ar), var(--ag), var(--ab), .35);
      border-style: solid;
      transition: border-color .6s;
      z-index: 5
    }

    .hp-c.tl {
      top: -4px;
      left: -4px;
      border-width: 2px 0 0 2px
    }

    .hp-c.tr {
      top: -4px;
      right: -4px;
      border-width: 2px 2px 0 0
    }

    .hp-c.bl {
      bottom: -4px;
      left: -4px;
      border-width: 0 0 2px 2px
    }

    .hp-c.br {
      bottom: -4px;
      right: -4px;
      border-width: 0 2px 2px 0
    }

    .hero-photo-lbl {
      position: absolute;
      bottom: 12px;
      left: 50%;
      transform: translateX(-50%);
      padding: 4px 14px;
      background: rgba(0, 0, 0, .75);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(var(--ar), var(--ag), var(--ab), .15);
      border-radius: 20px;
      font-family: var(--fm);
      font-size: 7px;
      letter-spacing: .22em;
      text-transform: uppercase;
      color: rgba(var(--ar), var(--ag), var(--ab), .6);
      display: flex;
      gap: 10px;
      white-space: nowrap;
      transition: color .6s;
      z-index: 5
    }

    /* Glow pulse ring */
    .hero-photo::before {
      content: '';
      position: absolute;
      inset: -4px;
      border-radius: 50%;
      border: 1px solid rgba(var(--ar), var(--ag), var(--ab), .15);
      z-index: 2;
      pointer-events: none;
      animation: photoGlow 3s ease infinite;
      transition: border-color .6s
    }

    @keyframes photoGlow {

      0%,
      100% {
        border-color: rgba(var(--ar), var(--ag), var(--ab), .1);
        box-shadow: 0 0 30px rgba(var(--ar), var(--ag), var(--ab), .03)
      }

      50% {
        border-color: rgba(var(--ar), var(--ag), var(--ab), .35);
        box-shadow: 0 0 50px rgba(var(--ar), var(--ag), var(--ab), .1)
      }
    }

    /* Outer glow ring */
    .hero-photo::after {
      content: '';
      position: absolute;
      inset: -14px;
      border-radius: 50%;
      border: 1px solid rgba(var(--ar), var(--ag), var(--ab), .06);
      z-index: -1;
      pointer-events: none;
      animation: outerRingPulse 4s ease infinite
    }

    @keyframes outerRingPulse {

      0%,
      100% {
        transform: scale(1);
        opacity: .6
      }

      50% {
        transform: scale(1.06);
        opacity: 1
      }
    }

    /* Orbital rings */
    .hero-orbit {
      position: absolute;
      border-radius: 50%;
      border: 1px solid rgba(var(--ar), var(--ag), var(--ab), .06);
      pointer-events: none;
      transition: border-color .6s
    }

    .hero-orbit-1 {
      width: calc(100% + 60px);
      height: calc(100% + 60px);
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) rotate(0deg);
      animation: orbitSpin 20s linear infinite
    }

    .hero-orbit-2 {
      width: calc(100% + 100px);
      height: calc(100% + 100px);
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) rotate(0deg);
      animation: orbitSpin 30s linear infinite reverse;
      border-style: dashed
    }

    .hero-orbit-3 {
      width: calc(100% + 150px);
      height: calc(100% + 150px);
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      border-style: dotted;
      opacity: .3
    }

    @keyframes orbitSpin {
      from {
        transform: translate(-50%, -50%) rotate(0deg)
      }

      to {
        transform: translate(-50%, -50%) rotate(360deg)
      }
    }

    /* Orbital dots */
    .orbit-dot {
      position: absolute;
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--accent);
      box-shadow: 0 0 12px rgba(var(--ar), var(--ag), var(--ab), .5);
      transition: background .6s, box-shadow .6s
    }

    .orbit-dot-1 {
      top: -3px;
      left: 50%;
      transform: translateX(-50%)
    }

    .orbit-dot-2 {
      bottom: -3px;
      right: 20%;
    }

    .orbit-dot-3 {
      top: 30%;
      left: -3px;
    }

    /* Floating particles around photo */
    .hero-particle {
      position: absolute;
      width: 3px;
      height: 3px;
      border-radius: 50%;
      background: var(--accent);
      opacity: .4;
      pointer-events: none;
      transition: background .6s
    }

    .hero-particle:nth-child(1) {
      top: 10%;
      left: -30px;
      animation: floatP 4s ease-in-out infinite
    }

    .hero-particle:nth-child(2) {
      top: 60%;
      right: -25px;
      animation: floatP 3.5s ease-in-out infinite .5s;
      width: 4px;
      height: 4px;
      opacity: .6
    }

    .hero-particle:nth-child(3) {
      bottom: 15%;
      left: -20px;
      animation: floatP 5s ease-in-out infinite 1s;
      width: 2px;
      height: 2px
    }

    .hero-particle:nth-child(4) {
      top: 20%;
      right: -35px;
      animation: floatP 4.5s ease-in-out infinite 1.5s
    }

    .hero-particle:nth-child(5) {
      bottom: 30%;
      right: -18px;
      animation: floatP 3s ease-in-out infinite .8s;
      width: 5px;
      height: 5px;
      opacity: .3
    }

    .hero-particle:nth-child(6) {
      top: 45%;
      left: -40px;
      animation: floatP 6s ease-in-out infinite 2s;
      width: 2px;
      height: 2px
    }

    @keyframes floatP {

      0%,
      100% {
        transform: translateY(0) scale(1);
        opacity: .4
      }

      50% {
        transform: translateY(-12px) scale(1.3);
        opacity: .8
      }
    }

    /* Glitch line effect */
    .hero-photo-glitch {
      position: absolute;
      inset: 0;
      border-radius: 50%;
      overflow: hidden;
      pointer-events: none;
      z-index: 3
    }

    .hero-photo-glitch::before {
      content: '';
      position: absolute;
      top: 30%;
      left: 0;
      right: 0;
      height: 2px;
      background: rgba(var(--ar), var(--ag), var(--ab), .12);
      animation: glitchLine 6s ease infinite;
      opacity: 0
    }

    @keyframes glitchLine {

      0%,
      88%,
      100% {
        opacity: 0
      }

      90% {
        opacity: 1;
        top: 30%;
        transform: translateX(-3px)
      }

      92% {
        top: 55%;
        transform: translateX(2px)
      }

      94% {
        top: 20%;
        transform: translateX(-1px)
      }

      96% {
        opacity: 0
      }
    }"""

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if "/* ═══ HERO ═══ */" in line:
        start_idx = i
    if "/* ═══ TICKER ═══ */" in line:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    lines = lines[:start_idx] + [new_css] + lines[end_idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("Done")
