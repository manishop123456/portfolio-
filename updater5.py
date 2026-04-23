import os

file_path = "c:/Users/manis/Videos/TCSC/sab saman/vs code projects/portfolio/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update hero-massive-text
old_hero_text = """    .hero-massive-text {
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 30px;
    }"""
new_hero_text = """    .hero-massive-text {
      width: 100%;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;
      gap: clamp(15px, 4vw, 40px);
      flex-wrap: wrap;
    }"""
text = text.replace(old_hero_text, new_hero_text)

# 2. Update hero-line
old_hero_line = """    .hero-line {
      font-family: var(--fd);
      line-height: .75;
      text-shadow: 0 0 60px rgba(var(--ar), var(--ag), var(--ab), .08);
      display: flex;
      justify-content: space-between;
      width: 100%;
    }

    .hl-top { font-size: clamp(60px, 16vw, 320px); color: var(--fg); }
    .hl-bot { font-size: clamp(45px, 12vw, 240px); color: var(--accent); }"""
new_hero_line = """    .hero-line {
      font-family: var(--fd);
      line-height: .75;
      text-shadow: 0 0 60px rgba(var(--ar), var(--ag), var(--ab), .08);
      display: flex;
      justify-content: center;
    }

    .hl-top { font-size: clamp(40px, 10vw, 150px); color: var(--fg); }
    .hl-bot { font-size: clamp(40px, 10vw, 150px); color: var(--accent); }"""
text = text.replace(old_hero_line, new_hero_line)

# 3. Update hero-photo-premium
old_photo = """    /* PREMIUM CENTERED PHOTO */
    .hero-photo-premium {
      position: relative;
      width: clamp(140px, 20vw, 320px);
      aspect-ratio: 3 / 4;
      z-index: 10;
      transition: transform 0.8s cubic-bezier(0.23, 1, 0.32, 1);
      cursor: none;
    }"""
new_photo = """    /* PREMIUM CENTERED PHOTO */
    .hero-photo-premium {
      position: relative;
      width: clamp(80px, 14vw, 220px);
      aspect-ratio: 3 / 4;
      z-index: 10;
      transition: transform 0.8s cubic-bezier(0.23, 1, 0.32, 1);
      cursor: none;
      flex-shrink: 0;
    }"""
text = text.replace(old_photo, new_photo)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("done updater5")
