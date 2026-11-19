"""
Launch a real, visible PowerShell console window, execute the assignments,
and capture an actual screenshot of the desktop with the live terminal.
"""

import subprocess
import time
import os
from PIL import ImageGrab

# Prepare the batch script to run inside PowerShell
script_to_run = (
    "cd 'C:\\Users\\Admin\\OneDrive\\Documents\\PYTHON'; "
    "Clear-Host; "
    "Write-Host '========================================================================' -ForegroundColor Cyan; "
    "Write-Host '             CSA08 PYTHON PROGRAMMING: LIVE EXECUTION                   ' -ForegroundColor Yellow; "
    "Write-Host '========================================================================' -ForegroundColor Cyan; "
    "Write-Host ''; "
    "Write-Host '>>> python milk_payment_calculator.py' -ForegroundColor Green; "
    "python milk_payment_calculator.py; "
    "Write-Host ''; "
    "Write-Host '>>> python co2_assignments.py' -ForegroundColor Green; "
    "python co2_assignments.py; "
)

# Launch a new visible PowerShell console window
cmd = f'start "CSA08 Live Execution" powershell.exe -NoExit -Command "{script_to_run}"'
os.system(cmd)

# Wait for window to spawn, clear, and render output
time.sleep(3.5)

# Grab the full desktop screenshot
screenshot = ImageGrab.grab()
screenshot_path = os.path.abspath("actual_terminal_screenshot.png")
screenshot.save(screenshot_path)
print(f"Captured live desktop screenshot: {screenshot_path} ({screenshot.size})")

# Copy to conversation artifact directory as well
artifact_dir = r"C:\Users\Admin\.gemini\antigravity\brain\e9202e20-2e2c-4aeb-91f6-e707a8e7894b"
if os.path.exists(artifact_dir):
    import shutil
    shutil.copyfile(screenshot_path, os.path.join(artifact_dir, "actual_terminal_screenshot.png"))
    print("Copied to artifact directory.")
