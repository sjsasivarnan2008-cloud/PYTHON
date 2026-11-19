"""
Generate a realistic, high-resolution terminal screenshot
of the program execution.
"""

import subprocess
import os
import shutil
from PIL import Image, ImageDraw, ImageFont

# Execute the program and get real stdout
res = subprocess.run(["python", "milk_payment_calculator.py"], capture_output=True, text=True)
stdout = res.stdout

# Setup dimensions and styling
FONT_PATH = "C:\\Windows\\Fonts\\consola.ttf"
FONT_BOLD_PATH = "C:\\Windows\\Fonts\\consolab.ttf"
FONT_SIZE = 18

try:
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    font_bold = ImageFont.truetype(FONT_BOLD_PATH, FONT_SIZE)
except Exception:
    font = ImageFont.load_default()
    font_bold = font

# Lines to display in the terminal
terminal_lines = [
    ("PS C:\\Users\\Admin\\OneDrive\\Documents\\PYTHON> ", "#569CD6", "python milk_payment_calculator.py", "#DCDCDC")
]

# Parse stdout into lines
for raw_line in stdout.splitlines():
    line = raw_line.rstrip()
    if not line:
        terminal_lines.append(("", "#D4D4D4", "", ""))
        continue

    # Color coding based on content
    if "=" * 20 in line:
        terminal_lines.append((line, "#4EC9B0", "", ""))
    elif "─" * 20 in line:
        terminal_lines.append((line, "#608B4E", "", ""))
    elif "🐄" in line or "KSHEERA" in line:
        terminal_lines.append((line, "#FFD700", "", ""))
    elif "Rate Card" in line:
        terminal_lines.append((line, "#9CDCFE", "", ""))
    elif "Farmer" in line and "Litres" in line:
        terminal_lines.append((line, "#4FC1FF", "", ""))
    elif "10-DAY TOTAL" in line:
        terminal_lines.append((line, "#50FA7B", "", ""))
    elif "Validation Errors" in line:
        terminal_lines.append((line, "#FFB86C", "", ""))
    elif "✗" in line:
        terminal_lines.append((line, "#FF5555", "", ""))
    elif "Decimal vs Float" in line:
        terminal_lines.append((line, "#BD93F9", "", ""))
    elif "rounding error" in line:
        terminal_lines.append((line, "#F1FA8C", "", ""))
    elif "Report generated" in line:
        terminal_lines.append((line, "#50FA7B", "", ""))
    else:
        terminal_lines.append((line, "#E0E0E0", "", ""))

# Calculate canvas size
pad_x = 24
pad_y = 20
title_bar_height = 42
line_height = 26
num_lines = len(terminal_lines)

img_width = 980
img_height = title_bar_height + pad_y + (num_lines * line_height) + pad_y + 20

# Create base image (dark terminal background #1E1E1E)
img = Image.new("RGBA", (img_width, img_height), (30, 30, 30, 255))
draw = ImageDraw.Draw(img)

# Title bar background #252526
draw.rectangle([(0, 0), (img_width, title_bar_height)], fill=(37, 37, 38, 255))
draw.line([(0, title_bar_height), (img_width, title_bar_height)], fill=(50, 50, 50, 255), width=1)

# Window buttons (macOS/Terminal style dots)
button_radius = 6
btn_y = title_bar_height // 2
draw.ellipse([(18, btn_y - button_radius), (30, btn_y + button_radius)], fill=(255, 95, 86, 255))   # Close (Red)
draw.ellipse([(38, btn_y - button_radius), (50, btn_y + button_radius)], fill=(255, 189, 46, 255))  # Min (Yellow)
draw.ellipse([(58, btn_y - button_radius), (70, btn_y + button_radius)], fill=(39, 201, 63, 255))   # Max (Green)

# Title text
title_font = ImageFont.truetype(FONT_PATH, 14) if os.path.exists(FONT_PATH) else font
draw.text((img_width // 2 - 170, 12), "Administrator: Windows PowerShell - CSA08 Assignment CO1", font=title_font, fill=(180, 180, 180, 255))

# Draw lines
curr_y = title_bar_height + pad_y
for item in terminal_lines:
    if len(item) == 4 and item[2]: # prompt line
        draw.text((pad_x, curr_y), item[0], font=font_bold, fill=item[1])
        prompt_w = draw.textlength(item[0], font=font_bold)
        draw.text((pad_x + prompt_w, curr_y), item[2], font=font, fill=item[3])
    else:
        text, color = item[0], item[1]
        draw.text((pad_x, curr_y), text, font=font, fill=color)
    curr_y += line_height

# Save in current directory
out_path = os.path.abspath("program_execution_screenshot.png")
img.save(out_path, format="PNG")
print(f"Saved workspace screenshot: {out_path}")

# Copy to conversation artifact directory if available
artifact_dir = r"C:\Users\Admin\.gemini\antigravity\brain\e9202e20-2e2c-4aeb-91f6-e707a8e7894b"
if os.path.exists(artifact_dir):
    dest = os.path.join(artifact_dir, "program_execution_screenshot.png")
    shutil.copyfile(out_path, dest)
    print(f"Copied to artifact directory: {dest}")
