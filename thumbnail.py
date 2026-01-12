# scripts/thumbnail.py
from PIL import Image, ImageDraw, ImageFont
import random

def create_thumbnail(title, outfile="thumb.png"):
    bg_colors = ["#ff0000","#00ff00","#0000ff","#ff9900"]
    bg = Image.new("RGB", (1280,720), color=random.choice(bg_colors))
    draw = ImageDraw.Draw(bg)
    font = ImageFont.truetype("arial.ttf", 60)
    lines = text_wrap(title, font, 1200)
    y = 50
    for line in lines:
        draw.text((40,y), line, font=font, fill="white")
        y += 70
    bg.save(outfile)

def text_wrap(text, font, max_width):
    lines=[]
    words=text.split()
    while words:
        line=''
        while words and font.getsize(line + words[0])[0]<=max_width:
            line+=words.pop(0)+" "
        lines.append(line.strip())
    return lines
