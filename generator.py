import random
from PIL import Image, ImageDraw, ImageFont

# Open errors.txt and add every line without whitespace
errors = []
with open("errors.txt", "r", encoding="utf-8") as f:
    for line in f:
        stripped_line = line.strip()
        if stripped_line:
            errors.append(stripped_line)

# Select a random error and user
error = random.choice(errors)
users = ["user", "root", "yougo-rgb", "octocat", "tux"]
user = random.choice(users)

content = f"{user}@linux:~$ {error}"

# Write the error in ERROR.md
with open("ERROR.md", "w", encoding="utf-8") as f:
    f.write(f"```txt\n{content}\n```")

# Image generation settings
padding = 20
background = (0, 0, 0)
border_radius = 12
font = ImageFont.truetype("./DejaVuSansMono.ttf", 25)
font_colors = [ (255, 255, 255), (255, 0, 0), (0, 255, 0)]

lines = content.split("\n")

# Creat a temp image to measure text sizes
temp_img = Image.new("RGB", (1, 1))
draw = ImageDraw.Draw(temp_img)

# Compute minimal image size
width = max(draw.textbbox((0, 0), line, font=font)[2] for line in lines) + padding * 2
height = max(draw.textbbox((0, 0), line, font=font)[3] for line in lines) + padding * 2

# Create transparent canvas and rounded background
img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
draw.rounded_rectangle(
    [(0, 0), (width, height)],
    radius=border_radius,
    fill=background
)
# Render each line of text and select a random color
x = padding
foreground = random.choice(font_colors)
for line in lines:
    bbox = draw.textbbox((0, 0), line, font=font)
    line_height = bbox[3]
    draw.text((padding, x), line, fill=foreground, font=font)
    x += line_height

# Save final image
img.save("ERROR.png")