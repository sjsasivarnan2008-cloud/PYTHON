"""
Generate all 5 separate individual output screenshots (CO1 to CO5)
and capture the actual desktop screenshot.
"""

import subprocess
import os
import shutil
from PIL import Image, ImageDraw, ImageFont, ImageGrab

FONT_PATH = "C:\\Windows\\Fonts\\consola.ttf"
FONT_BOLD_PATH = "C:\\Windows\\Fonts\\consolab.ttf"
FONT_SIZE = 16

try:
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    font_bold = ImageFont.truetype(FONT_BOLD_PATH, FONT_SIZE)
    title_font = ImageFont.truetype(FONT_PATH, 13)
except Exception:
    font = ImageFont.load_default()
    font_bold = font
    title_font = font

def render_terminal_screenshot(window_title: str, command: str, output_text: str, filename: str):
    lines = [("PS C:\\Users\\Admin\\OneDrive\\Documents\\PYTHON> ", "#569CD6", command, "#DCDCDC")]

    for raw in output_text.splitlines():
        line = raw.rstrip()
        if not line:
            lines.append(("", "#D4D4D4", "", ""))
            continue
        if "=" * 10 in line:
            lines.append((line, "#4EC9B0", "", ""))
        elif "─" * 10 in line:
            lines.append((line, "#608B4E", "", ""))
        elif line.startswith("[") and "]" in line:
            lines.append((line, "#FFD700", "", ""))
        elif "✓" in line or "Fixed" in line or "Positive" in line or "Instant" in line or "10-DAY TOTAL" in line:
            lines.append((line, "#50FA7B", "", ""))
        elif "✗" in line or "Buggy" in line or "Negative" in line or "Error" in line or "Rejected" in line or "Shortage" in line:
            lines.append((line, "#FF5555", "", ""))
        elif "->" in line or ":" in line:
            lines.append((line, "#9CDCFE", "", ""))
        else:
            lines.append((line, "#E0E0E0", "", ""))

    pad_x, pad_y = 22, 18
    title_bar_h = 40
    line_h = 24
    w = 1020
    h = title_bar_h + pad_y + (len(lines) * line_h) + pad_y + 15

    img = Image.new("RGBA", (w, h), (28, 28, 30, 255))
    draw = ImageDraw.Draw(img)

    # Title bar
    draw.rectangle([(0, 0), (w, title_bar_h)], fill=(36, 36, 38, 255))
    draw.line([(0, title_bar_h), (w, title_bar_h)], fill=(50, 50, 52, 255), width=1)

    # Window controls
    btn_y = title_bar_h // 2
    draw.ellipse([(14, btn_y - 6), (26, btn_y + 6)], fill=(255, 95, 86, 255))
    draw.ellipse([(34, btn_y - 6), (46, btn_y + 6)], fill=(255, 189, 46, 255))
    draw.ellipse([(54, btn_y - 6), (66, btn_y + 6)], fill=(39, 201, 63, 255))

    # Title text
    draw.text((w // 2 - 200, 12), window_title, font=title_font, fill=(190, 190, 190, 255))

    # Output lines
    curr_y = title_bar_h + pad_y
    for item in lines:
        if len(item) == 4 and item[2]:
            draw.text((pad_x, curr_y), item[0], font=font_bold, fill=item[1])
            pw = draw.textlength(item[0], font=font_bold)
            draw.text((pad_x + pw, curr_y), item[2], font=font, fill=item[3])
        else:
            draw.text((pad_x, curr_y), item[0], font=font, fill=item[1])
        curr_y += line_h

    img.save(filename, format="PNG")
    print(f"Saved: {filename}")

    # Copy to artifact directory
    art_dir = r"C:\Users\Admin\.gemini\antigravity\brain\e9202e20-2e2c-4aeb-91f6-e707a8e7894b"
    if os.path.exists(art_dir):
        shutil.copyfile(filename, os.path.join(art_dir, filename))

# 1. CO1 Screenshot
r1 = subprocess.run(["python", "milk_payment_calculator.py"], capture_output=True, text=True)
render_terminal_screenshot("Windows PowerShell - CSA08 Assignment CO1 (Milk Calculator)", "python milk_payment_calculator.py", r1.stdout, "co1_output_screenshot.png")

# 2. CO2 Screenshot
r2 = subprocess.run(["python", "co2_assignments.py"], capture_output=True, text=True)
render_terminal_screenshot("Windows PowerShell - CSA08 Assignment CO2 (Control Flow & Strings)", "python co2_assignments.py", r2.stdout, "co2_output_screenshot.png")

# 3. CO3 Screenshot
r3 = subprocess.run(["python", "co3_assignments.py"], capture_output=True, text=True)
render_terminal_screenshot("Windows PowerShell - CSA08 Assignment CO3 (Data Structures)", "python co3_assignments.py", r3.stdout, "co3_output_screenshot.png")

# 4. CO4 Screenshot
r4 = subprocess.run(["python", "co4_assignments.py"], capture_output=True, text=True)
render_terminal_screenshot("Windows PowerShell - CSA08 Assignment CO4 (Files & Exceptions)", "python co4_assignments.py", r4.stdout, "co4_output_screenshot.png")

# 5. CO5 Screenshot
r5 = subprocess.run(["python", "co5_assignments.py"], capture_output=True, text=True)
co5_clean = "\n".join([l for l in r5.stdout.splitlines() if "matplotlib" not in l.lower() and "mkdir" not in l.lower()])
render_terminal_screenshot("Windows PowerShell - CSA08 Assignment CO5 (SQLite, Viz & AI)", "python co5_assignments.py", co5_clean, "co5_output_screenshot.png")

# 6. Actual Desktop / Live Screen Capture
live_screen = ImageGrab.grab()
live_path = os.path.abspath("actual_terminal_screenshot.png")
live_screen.save(live_path)
print(f"Captured actual live desktop screenshot: {live_path}")

art_dir = r"C:\Users\Admin\.gemini\antigravity\brain\e9202e20-2e2c-4aeb-91f6-e707a8e7894b"
if os.path.exists(art_dir):
    shutil.copyfile(live_path, os.path.join(art_dir, "actual_terminal_screenshot.png"))
