import os
import re

file_path = "c:/Users/manis/Videos/TCSC/sab saman/vs code projects/portfolio/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Refactoring HTML so photo sits statically between MANISH and CHOUDHARY
html_start = text.find('      <!-- CENTRIC MASSIVE POSTER -->')
html_end = text.find('      <!-- BOTTOM CTA -->')

new_html_block = """      <!-- CENTRIC MASSIVE POSTER -->
      <div class="hero-center-block">
        <div class="hero-massive-text">
          <div class="hero-line hl-top" id="hl1">MANISH</div>

          <div class="hero-photo-premium" id="hero-photo">
            <div class="premium-glass-backing"></div>
            <img src="profile.png" alt="Manish Choudhary" id="hero-img" />
            <div class="hero-photo-grain"></div>
          </div>

          <div class="hero-line hl-bot" id="hl2">CHOUDHARY</div>
        </div>
      </div>

"""

if html_start != -1 and html_end != -1:
    text = text[:html_start] + new_html_block + text[html_end:]


# Adjusting CSS for the clean document flow
# 1. Update hero-massive-text
text = re.sub(
    r'\.hero-massive-text\s*{[^}]+}',
    '.hero-massive-text {\n      width: 100%;\n      display: flex;\n      flex-direction: column;\n      align-items: center;\n      gap: 30px;\n    }',
    text
)

# 2. Update .hero-photo-premium
old_photo_css = """    /* PREMIUM CENTERED PHOTO */
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
    }"""
new_photo_css = """    /* PREMIUM CENTERED PHOTO */
    .hero-photo-premium {
      position: relative;
      width: clamp(140px, 20vw, 320px);
      aspect-ratio: 3 / 4;
      z-index: 10;
      transition: transform 0.8s cubic-bezier(0.23, 1, 0.32, 1);
      cursor: none;
    }"""
text = text.replace(old_photo_css, new_photo_css)

# 3. Update .hero-photo-premium:hover
old_photo_hover = """    .hero-photo-premium:hover {
      transform: translate(-50%, -52%) scale(1.05);
    }"""
new_photo_hover = """    .hero-photo-premium:hover {
      transform: translateY(-8px) scale(1.03);
    }"""
text = text.replace(old_photo_hover, new_photo_hover)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)
print("Done updater4")
