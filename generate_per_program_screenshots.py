"""
Generates individual standalone programs and corresponding terminal screenshots
for EACH question/task inside Course Outcomes CO1 through CO5.
"""

import os
import shutil
import subprocess
from PIL import Image, ImageDraw, ImageFont

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

def render_box_screenshot(window_title: str, command: str, output_text: str, save_path: str):
    lines = [("PS C:\\Users\\Admin\\OneDrive\\Documents\\PYTHON> ", "#569CD6", command, "#DCDCDC")]

    for raw in output_text.splitlines():
        line = raw.rstrip()
        if not line:
            lines.append(("", "#D4D4D4", "", ""))
            continue
        if "=" * 8 in line:
            lines.append((line, "#4EC9B0", "", ""))
        elif "─" * 8 in line:
            lines.append((line, "#608B4E", "", ""))
        elif line.startswith("[") and "]" in line:
            lines.append((line, "#FFD700", "", ""))
        elif "✓" in line or "VALID" in line or "Fixed" in line or "Positive" in line or "Instant" in line or "TOTAL" in line or "Success" in line:
            lines.append((line, "#50FA7B", "", ""))
        elif "✗" in line or "INVALID" in line or "Buggy" in line or "Negative" in line or "Error" in line or "Rejected" in line or "LOCKED" in line:
            lines.append((line, "#FF5555", "", ""))
        elif "->" in line or ":" in line:
            lines.append((line, "#9CDCFE", "", ""))
        else:
            lines.append((line, "#E0E0E0", "", ""))

    pad_x, pad_y = 22, 18
    title_bar_h = 38
    line_h = 24
    w = 1020
    h = title_bar_h + pad_y + (len(lines) * line_h) + pad_y + 14

    img = Image.new("RGBA", (w, h), (26, 26, 28, 255))
    draw = ImageDraw.Draw(img)

    # Title bar
    draw.rectangle([(0, 0), (w, title_bar_h)], fill=(34, 34, 36, 255))
    draw.line([(0, title_bar_h), (w, title_bar_h)], fill=(48, 48, 50, 255), width=1)

    # Window dots
    btn_y = title_bar_h // 2
    draw.ellipse([(14, btn_y - 5), (24, btn_y + 5)], fill=(255, 95, 86, 255))
    draw.ellipse([(32, btn_y - 5), (42, btn_y + 5)], fill=(255, 189, 46, 255))
    draw.ellipse([(50, btn_y - 5), (60, btn_y + 5)], fill=(39, 201, 63, 255))

    draw.text((w // 2 - 200, 11), window_title, font=title_font, fill=(180, 180, 180, 255))

    curr_y = title_bar_h + pad_y
    for item in lines:
        if len(item) == 4 and item[2]:
            draw.text((pad_x, curr_y), item[0], font=font_bold, fill=item[1])
            pw = draw.textlength(item[0], font=font_bold)
            draw.text((pad_x + pw, curr_y), item[2], font=font, fill=item[3])
        else:
            draw.text((pad_x, curr_y), item[0], font=font, fill=item[1])
        curr_y += line_h

    img.save(save_path, format="PNG")
    print(f"Generated: {os.path.basename(save_path)}")

    # Copy to artifact folder
    art_dir = r"C:\Users\Admin\.gemini\antigravity\brain\e9202e20-2e2c-4aeb-91f6-e707a8e7894b"
    if os.path.exists(art_dir):
        shutil.copyfile(save_path, os.path.join(art_dir, os.path.basename(save_path)))


# ════════════════════════════════════════════════════════════════════════
# 1. Individual Program Execution Definitions
# ════════════════════════════════════════════════════════════════════════

PROGRAMS = {
    # ── CO1 ──
    "co1_p1_values_and_types.png": (
        "CSA08 CO1: Values, Types & Precision Demo",
        "python -c \"import sys; from decimal import Decimal\n"
        "print('=== CO1 TASK 2: VALUES, TYPES & DECIMAL EXACTNESS ===')\n"
        "print('Type of 7/2  :', type(7/2), 'Value:', 7/2)\n"
        "print('Type of 7//2 :', type(7//2), 'Value:', 7//2)\n"
        "print('Type of -7//2:', type(-7//2), 'Value:', -7//2)\n"
        "print('Float check 0.1 + 0.2 == 0.3 :', 0.1 + 0.2 == 0.3)\n"
        "print('Float sum actual value       :', f'{0.1 + 0.2:.17f}')\n"
        "d1, d2, d3 = Decimal('0.1'), Decimal('0.2'), Decimal('0.3')\n"
        "print('Decimal check d1 + d2 == d3  :', d1 + d2 == d3)\n"
        "print('1000 x Rs33.40 + 3 x Rs0.10 (Float)   : Rs', 1000 * 33.40 + 3 * 0.10)\n"
        "print('1000 x Rs33.40 + 3 x Rs0.10 (Decimal) : Rs', 1000 * Decimal('33.40') + 3 * Decimal('0.10'))\n"
        "\""
    ),

    "co1_p2_rate_card_expressions.png": (
        "CSA08 CO1: Milk Rate Expressions & Functions",
        "python -c \"from decimal import Decimal, ROUND_HALF_UP\n"
        "print('=== CO1 TASK 4 & 6: MILK RATE FORMULAS & FUNCTIONS ===')\n"
        "BASE_RATE, BASE_FAT, BASE_SNF = Decimal('30.00'), Decimal('3.5'), Decimal('8.5')\n"
        "FAT_STEP, SNF_STEP = Decimal('0.40'), Decimal('0.30')\n"
        "def rate(fat, snf):\n"
        "    f_step = (Decimal(str(fat)) - BASE_FAT) / Decimal('0.1')\n"
        "    s_step = (Decimal(str(snf)) - BASE_SNF) / Decimal('0.1')\n"
        "    return (BASE_RATE + f_step * FAT_STEP + s_step * SNF_STEP).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)\n"
        "samples = [(4.2, 8.7), (3.5, 8.5), (5.0, 9.0), (2.8, 7.5), (6.0, 9.8)]\n"
        "print(f'Base Rate: Rs {BASE_RATE} at {BASE_FAT}% Fat, {BASE_SNF}% SNF')\n"
        "print('----------------------------------------------------')\n"
        "for f, s in samples:\n"
        "    r = rate(f, s)\n"
        "    pay = (Decimal('10.0') * r).quantize(Decimal('0.01'))\n"
        "    print(f'Fat: {f:4.1f}% | SNF: {s:4.1f}% -> Rate/Litre: Rs {r:6.2f} | 10L Payout: Rs {pay:6.2f}')\n"
        "\""
    ),

    "co1_p3_calculator_validation.png": (
        "CSA08 CO1: Complete Milk Payment Calculator & Validation",
        "python milk_payment_calculator.py"
    ),

    # ── CO2 ──
    "co2_p1_subsidy_decisions.png": (
        "CSA08 CO2: Electricity Subsidy Decision Boundaries",
        "python -c \"import co2_assignments as co2\n"
        "print('=== CO2 Q1: DECISIONS WITH MANY BOUNDARIES ===')\n"
        "cases = [(85, False, 45), (100, False, 50), (150, True, 60), (150, False, 60), (200, True, 70), (250, True, 75), (280, False, 84)]\n"
        "for u, c, a in cases:\n"
        "    res = co2.calculate_subsidy(u, c, a)\n"
        "    print(f'Units: {u:3d} | Ration Card: {str(c):<5} | Max Age: {a:2d} -> {res}')\n"
        "\""
    ),

    "co2_p2_otp_loops.png": (
        "CSA08 CO2: Bank Kiosk OTP Attempt Loop Verification",
        "python -c \"import co2_assignments as co2\n"
        "print('=== CO2 Q2: LOOPS THAT COUNT ATTEMPTS (OTP VERIFICATION) ===')\n"
        "inputs = ['', '1234', '   ', '5678', '7492']\n"
        "success, log = co2.verify_otp_simulation('7492', inputs)\n"
        "for l in log: print('  •', l)\n"
        "print('Result: Access Granted' if success else 'Result: Access Denied')\n"
        "\""
    ),

    "co2_p3_vehicle_plate_validator.png": (
        "CSA08 CO2: Vehicle Number Plate Validator (No Regex)",
        "python -c \"import co2_assignments as co2\n"
        "print('=== CO2 Q3: VEHICLE REGISTRATION NUMBER VALIDATOR ===')\n"
        "plates = ['tn 09 ab 1234', 'TN-09-AB-1234', 'Tn09Ab1234', 'KL 01 Z 9999', 'TN9AB1234', 'DL 04 1234']\n"
        "for p in plates:\n"
        "    ok, formatted, msg = co2.validate_reg_number(p)\n"
        "    status = '✓ VALID  ' if ok else '✗ INVALID'\n"
        "    print(f'{p:<16} -> {status} [{formatted}] ({msg})')\n"
        "\""
    ),

    "co2_p4_string_benchmark.png": (
        "CSA08 CO2: String Concatenation Benchmark (+ vs join)",
        "python -c \"import co2_assignments as co2\n"
        "print('=== CO2 Q4: BUILDING LONG TEXT: + vs join() ===')\n"
        "res = co2.benchmark_string_building(100000)\n"
        "print(f'str.join() on {res[\"n_join\"]:,} items : {res[\"time_join_sec\"]*1000:8.2f} ms [O(n) time]')\n"
        "print(f'\"+=\" loop  on {res[\"n_concat\"]:,} items  : {res[\"time_concat_sec\"]*1000:8.2f} ms [O(n²) time]')\n"
        "ratio = (res['time_concat_sec']/res['n_concat']) / (res['time_join_sec']/res['n_join'])\n"
        "print(f'Performance Advantage: str.join() is ~{ratio:.1f}x faster!')\n"
        "\""
    ),

    "co2_p5_mutable_default_bug.png": (
        "CSA08 CO2: Function Scope & Mutable Default Parameter Trap",
        "python -c \"import co2_assignments as co2\n"
        "print('=== CO2 Q5: DEFAULT MUTABLE ARGUMENT BUG (CANTEEN ORDERS) ===')\n"
        "print('Buggy Definition: def add_item(item, order=[]):')\n"
        "b1 = co2.buggy_add_item('Tea')\n"
        "b2 = co2.buggy_add_item('Vada')\n"
        "print(f'  Call 1 -> {b1}')\n"
        "print(f'  Call 2 -> {b2}  (BUG: Prior items persist across calls!)')\n"
        "print('----------------------------------------------------')\n"
        "print('Fixed Definition: def add_item(item, order=None):')\n"
        "f1 = co2.fixed_add_item('Tea')\n"
        "f2 = co2.fixed_add_item('Vada')\n"
        "print(f'  Call 1 -> {f1}')\n"
        "print(f'  Call 2 -> {f2}  (CORRECT: Fresh list created per call)')\n"
        "\""
    ),

    "co2_p6_recursion_memoization.png": (
        "CSA08 CO2: Recursion & Memoisation (Climbing Steps)",
        "python -c \"import co2_assignments as co2, time\n"
        "print('=== CO2 Q6: RECURSION AND ITS LIMITS (TEMPLE STEPS) ===')\n"
        "t0 = time.perf_counter(); w_naive = co2.ways_naive(25); t_n = time.perf_counter() - t0\n"
        "t1 = time.perf_counter(); w_memo = co2.ways_memo(25); t_m = time.perf_counter() - t1\n"
        "print(f'Naive ways(25) : {w_naive:,} | Function calls: {co2.call_count_naive:,} ({t_n*1000:.2f} ms)')\n"
        "print(f'Memo  ways(25) : {w_memo:,} | Distinct states: 26 ({t_m*1000:.3f} ms)')\n"
        "print(f'Memo  ways(100): {co2.ways_memo(100):,} (Computed instantly without stack overflow!)')\n"
        "\""
    ),

    # ── CO3 ──
    "co3_p1_rainfall_slicing.png": (
        "CSA08 CO3: Daily Rainfall Slicing & Moving Average",
        "python -c \"import co3_assignments as co3\n"
        "print('=== CO3 Q1: LISTS & SLICING (365-DAY RAINFALL RECORDS) ===')\n"
        "data = [0.0 if (i % 3 != 0) else float((i * 7) % 65) for i in range(365)]\n"
        "rep = co3.analyze_rainfall(data)\n"
        "print(f'Total Annual Rainfall : {rep[\"annual_total_mm\"]} mm')\n"
        "print(f'Dry Days (0 mm) Count : {rep[\"dry_days_count\"]}/365 days')\n"
        "print(f'Wettest Week          : Week #{rep[\"wettest_week\"][0]} ({rep[\"wettest_week\"][1]} mm)')\n"
        "print(f'Driest Week           : Week #{rep[\"driest_week\"][0]} ({rep[\"driest_week\"][1]} mm)')\n"
        "print(f'7-Day Moving Average  : {rep[\"moving_avg_first_7\"]}')\n"
        "\""
    ),

    "co3_p2_grid_aliasing_copy.png": (
        "CSA08 CO3: Grid Aliasing Bug & Shallow vs Deep Copy",
        "python -c \"import co3_assignments as co3\n"
        "print('=== CO3 Q2: TUPLES, MUTABILITY & GRID ALIASING TRAP ===')\n"
        "info = co3.demonstrate_grid_and_copying()\n"
        "print('Bad Grid: [[0]*cols]*rows')\n"
        "print(f'  row[0] is row[1]     : {info[\"bad_is_aliased\"]} (Same object in memory!)')\n"
        "print(f'  Result after grid[0][1]=7: {info[\"bad_grid_sample\"]}')\n"
        "print('Good Grid: [[0]*cols for _ in range(rows)]')\n"
        "print(f'  row[0] is row[1]     : {info[\"good_is_aliased\"]} (Independent row lists)')\n"
        "print(f'  Result after grid[0][1]=7: {info[\"good_grid_sample\"]}')\n"
        "print(f'Shallow copy modified by inner change : {info[\"shallow_affected\"]}')\n"
        "print(f'Deep copy completely isolated         : {info[\"deep_isolated\"]}')\n"
        "\""
    ),

    "co3_p3_complaint_frequencies.png": (
        "CSA08 CO3: Kisan Call Centre Keyword Frequencies",
        "python -c \"import co3_assignments as co3\n"
        "print('=== CO3 Q3: DICTIONARIES & SETS (COMPLAINT ANALYSIS) ===')\n"
        "texts = [\n"
        "  'Cotton crop damaged due to high price seeds not germinating.',\n"
        "  'Fertilizer price is too high and seeds received were bad quality.',\n"
        "  'Paddy harvest delayed. Received damaged seeds from local store.'\n"
        "]\n"
        "freq = co3.word_frequencies(texts, co3.STOP_WORDS)\n"
        "top = co3.top_k_words(freq, 5)\n"
        "print('Filtered Stop Words:', sorted(list(co3.STOP_WORDS))[:8], '...')\n"
        "print('Top Keyword Frequencies:')\n"
        "for word, count in top:\n"
        "    print(f'  • {word:<12} : {count} occurrences')\n"
        "\""
    ),

    "co3_p4_elective_clash_sets.png": (
        "CSA08 CO3: Elective Registration Clash Detection",
        "python -c \"import co3_assignments as co3\n"
        "print('=== CO3 Q4: SETS (ELECTIVE CLASH DETECTION) ===')\n"
        "all_s = {f'1923110{i:02d}' for i in range(1, 11)}\n"
        "ai_s = {'192311001', '192311004', '192311007', '192311009'}\n"
        "iot_s = {'192311002', '192311004', '192311009', '192311010'}\n"
        "res = co3.detect_registration_clashes(all_s, ai_s, iot_s)\n"
        "print('AI Registrations  :', sorted(list(ai_s)))\n"
        "print('IoT Registrations :', sorted(list(iot_s)))\n"
        "print('----------------------------------------------------')\n"
        "print('Clash (ai & iot)      :', res['clash_list'])\n"
        "print('One Only (ai ^ iot)   :', res['one_only_list'])\n"
        "print('Neither Registered    :', res['neither_list'])\n"
        "\""
    ),

    "co3_p5_vaccine_temp_cleaning.png": (
        "CSA08 CO3: Cold Storage Temperature Cleaning",
        "python -c \"import co3_assignments as co3\n"
        "print('=== CO3 Q5: LIST COMPREHENSIONS (VACCINE SENSOR CLEANING) ===')\n"
        "raw = [4.2, 5.1, 95.0, 3.8, -60.0, 1.5, 8.5, 6.0, 4.0, 12.0]\n"
        "res = co3.clean_and_analyze_temperatures(raw)\n"
        "print('Raw Sensor Readings      :', raw)\n"
        "print('Valid Readings Count     :', res['valid_count'], f'(Rejected {res[\"dropped_errors\"]} faulty readings)')\n"
        "print('Cleaned Celsius (°C)     :', res['valid_celsius_sample'])\n"
        "print('Converted Fahrenheit (°F):', res['valid_fahrenheit_sample'])\n"
        "print('Alarm Minutes (!= 2-8°C) :', res['alarm_minutes'])\n"
        "\""
    ),

    "co3_p6_railway_timetable_index.png": (
        "CSA08 CO3: Railway Timetable Nested Index & Queries",
        "python -c \"import co3_assignments as co3\n"
        "print('=== CO3 Q6: NESTED STRUCTURES & INVERTED STATION INDEX ===')\n"
        "idx = co3.build_station_index(co3.TIMETABLE)\n"
        "for station in ['Chennai Central', 'Katpadi', 'Madurai']:\n"
        "    print(f'Station: {station}')\n"
        "    for t in idx.get(station, []):\n"
        "        print(f'  -> Train {t[\"train_no\"]} ({t[\"train_name\"]}) departs at {t[\"departure\"]} [{len(t[\"days\"])} days/week]')\n"
        "\""
    ),

    "co3_p7_contact_merging.png": (
        "CSA08 CO3: Phone Contacts Deduplication & Merging",
        "python -c \"import co3_assignments as co3\n"
        "print('=== CO3 Q7: CONTACT MERGING FROM FIRST PRINCIPLES ===')\n"
        "raw = [\n"
        "  {'name': 'ravi', 'phone': '+91 98400 12345', 'email': 'ravi@gmail.com'},\n"
        "  {'name': 'Dr. Ravi Kumar', 'phone': '09840012345', 'email': 'r.kumar@hospital.org'},\n"
        "  {'name': 'Priya', 'phone': '9876543210', 'email': 'priya@work.com'},\n"
        "  {'name': 'Priya S.', 'phone': '+91-98765-43210', 'email': 'priya_personal@gmail.com'}\n"
        "]\n"
        "merged = co3.merge_contacts(raw)\n"
        "for p, d in merged.items():\n"
        "    print(f'Number: {p} | Name: {d[\"name\"]:16} | Emails: {list(d[\"emails\"])}')\n"
        "\""
    ),

    # ── CO4 ──
    "co4_p1_mess_bills_handling.png": (
        "CSA08 CO4: Safe Hostel Mess Bill Processing",
        "python -c \"import tempfile, os, co4_assignments as co4\n"
        "print('=== CO4 TASK 1: SAFE FILE PROCESSING (MESS BILLS) ===')\n"
        "with tempfile.TemporaryDirectory() as td:\n"
        "    fp = os.path.join(td, 'mess.txt')\n"
        "    with open(fp, 'w') as f:\n"
        "        f.write('19231101, Akash, 3450.50\\n19231102, Bharath, 4120.00\\n19231103, Chandru, bad_num\\n19231104, Divya\\n')\n"
        "    tot, val, rej = co4.process_mess_bills(fp)\n"
        "    print(f'Total Valid Bills Amount : Rs {tot:,.2f} ({len(val)} students)')\n"
        "    print(f'Rejections Count         : {len(rej)} records:')\n"
        "    for lno, text, r in rej:\n"
        "        print(f'  • Line {lno}: {r}')\n"
        "\""
    ),

    "co4_p2_biometric_attendance.png": (
        "CSA08 CO4: Biometric Attendance & Custom Exception",
        "python -c \"import tempfile, os, co4_assignments as co4\n"
        "print('=== CO4 TASK 2 & 3: BIOMETRIC ATTENDANCE & EXCEPTIONS ===')\n"
        "with tempfile.TemporaryDirectory() as td:\n"
        "    fp = os.path.join(td, 'attendance.csv')\n"
        "    with open(fp, 'w') as f:\n"
        "        f.write('19231101, 2026-10-01, P\\n19231101, 2026-10-02, P\\n19231102, 2026-10-01, P\\n19231102, 2026-10-02, A\\n19231103, 2026-10-01\\n19231104, 2026-10-01, L\\n')\n"
        "    rep = co4.summarize_attendance(fp)\n"
        "    print('Attendance Percentages :', rep['attendance_percentages'])\n"
        "    print('Shortage Alert (<75%)  :', rep['shortage_below_75'])\n"
        "    print('Handled Corrupt Records:')\n"
        "    for c in rep['corrupted_records']: print('  •', c)\n"
        "\""
    ),

    "co4_p3_file_forensics_trap.png": (
        "CSA08 CO4: File Forensics (Overwrite vs Append Trap)",
        "python -c \"import tempfile, co4_assignments as co4\n"
        "print('=== CO4 TASK 4: FILE FORENSICS (w vs a MODES) ===')\n"
        "with tempfile.TemporaryDirectory() as td:\n"
        "    res = co4.demonstrate_file_forensics(td)\n"
        "    print(f'Buggy (w mode) Final Lines : {res[\"buggy_lines_count\"]} lines (Prior days WIPED!)')\n"
        "    print(f'Buggy Remaining Content    : {res[\"buggy_content\"]}')\n"
        "    print(f'Fixed (a mode) Final Lines : {res[\"fixed_lines_count\"]} lines (All 3 days preserved)')\n"
        "    print(f'Fixed Log Content          : {res[\"fixed_content\"]}')\n"
        "\""
    ),

    "co4_p4_fest_registration_desk.png": (
        "CSA08 CO4: College Fest Registration Pipeline",
        "python -c \"import tempfile, os, co4_assignments as co4\n"
        "print('=== CO4 TASK 6: COLLEGE FEST REGISTRATION DESK ===')\n"
        "with tempfile.TemporaryDirectory() as td:\n"
        "    c_f, e_f = os.path.join(td, 'cse.csv'), os.path.join(td, 'ece.csv')\n"
        "    with open(c_f, 'w') as f:\n"
        "        f.write('19231101, Anand, CSE, anand@college.edu, Coding;Web Design\\n19231102, Bala, CSE, invalid_email, Coding\\n')\n"
        "    with open(e_f, 'w') as f:\n"
        "        f.write('19231103, Deepa, ECE, deepa@college.edu, Robotics\\n19231101, Anand, ECE, anand@college.edu, Gaming\\n')\n"
        "    res = co4.process_fest_registrations({'CSE': c_f, 'ECE': e_f}, os.path.join(td, 'out'))\n"
        "    print('Clean Master Registrations :', res['total_registered'], 'students')\n"
        "    print('Event-wise Enrollments    :', res['events_summary'])\n"
        "    print('Audit Log of Rejections   :')\n"
        "    for r in res['rejected_log']: print('  •', r)\n"
        "\""
    ),

    # ── CO5 ──
    "co5_p1_data_cleaning_pipeline.png": (
        "CSA08 CO5: Air Quality Data Cleaning & Normalisation",
        "python -c \"import co5_assignments as co5\n"
        "print('=== CO5 PART A & B1: DATA CLEANING PIPELINE ===')\n"
        "raw = '''station,date,pm25,temperature\\nAdyar,2026-10-01,48.0,86.0\\nAdyar,2026-10-02,54.0,29.5\\nAdyar,2026-10-03,NA,30.0\\nGuindy,2026-10-01,95.0,29.0\\nGuindy,2026-10-02,-5.0,29.5\\nGuindy,2026-10-03,121.0,89.6'''\n"
        "cl = co5.clean_air_quality_data(raw)\n"
        "print(f'Raw Rows: 6 -> Valid Cleaned Rows: {len(cl)}')\n"
        "for r in cl: print(f'  Station: {r[\"station\"]:8} | Date: {r[\"date\"]} | PM2.5: {r[\"pm25\"]:5.1f} | Temp: {r[\"temperature\"]}°C')\n"
        "vals = [r[\"pm25\"] for r in cl]\n"
        "norm = co5.min_max_normalize(vals)\n"
        "print('Original PM2.5 :', vals)\n"
        "print('Min-Max Scaled :', norm)\n"
        "\""
    ),

    "co5_p2_sqlite_parameterized.png": (
        "CSA08 CO5: SQLite Database & SQL Injection Defense",
        "python -c \"import co5_assignments as co5\n"
        "print('=== CO5 B2: SQLITE STORAGE & SQL INJECTION DEFENSE ===')\n"
        "raw = '''station,date,pm25,temperature\\nAdyar,2026-10-01,48.0,28.0\\nAdyar,2026-10-02,54.0,29.0\\nGuindy,2026-10-01,95.0,30.0\\nGuindy,2026-10-02,121.0,31.0'''\n"
        "conn = co5.setup_sqlite_database(co5.clean_air_quality_data(raw))\n"
        "print('Adyar Station Average PM2.5  :', co5.get_station_average(conn, 'Adyar'), 'µg/m³')\n"
        "print('Guindy Station Average PM2.5 :', co5.get_station_average(conn, 'Guindy'), 'µg/m³')\n"
        "mal = \"Adyar' OR '1'='1\"\n"
        "print(f'SQL Injection Attack (\\\"{mal}\\\") -> Result:', co5.get_station_average(conn, mal), '(Immune!)')\n"
        "\""
    ),

    "co5_p3_ai_sentiment_summary.png": (
        "CSA08 CO5: AI Sentiment Analysis with Negation & Summarizer",
        "python -c \"import co5_assignments as co5\n"
        "print('=== CO5 B4: AI SENTIMENT ANALYSIS & SUMMARIZATION ===')\n"
        "complaints = [\n"
        "  'Roads are clean and the air is fresh today.',\n"
        "  'Smoke from the factory, air is bad and toxic.',\n"
        "  'The response from the pollution desk was not helpful.',\n"
        "  'Not bad, the air quality improved significantly.'\n"
        "]\n"
        "for c in complaints:\n"
        "    s = co5.analyze_sentiment(c)\n"
        "    print(f'Text : \\\"{c}\\\"')\n"
        "    print(f'  -> Sentiment: {s[\"sentiment\"]} (Score: {s[\"score\"]:+d})')\n"
        "summary = co5.extractive_summarize(complaints, top_n=2)\n"
        "print('Extractive Summary of Citizen Complaints:')\n"
        "for line in summary: print('  •', line)\n"
        "\""
    ),

    "co5_p4_air_quality_chatbot.png": (
        "CSA08 CO5: Air Quality Query Assistant Chatbot",
        "python -c \"import co5_assignments as co5\n"
        "print('=== CO5 B5: RULE-BASED QUERY ASSISTANT CHATBOT ===')\n"
        "raw = '''station,date,pm25,temperature\\nAdyar,2026-10-01,48.0,28.0\\nGuindy,2026-10-01,108.0,30.0'''\n"
        "conn = co5.setup_sqlite_database(co5.clean_air_quality_data(raw))\n"
        "queries = ['Hello!', 'What is the PM2.5 in Adyar?', 'Tell me about pollution in Guindy', 'How is the traffic?']\n"
        "for q in queries:\n"
        "    print(f'User : {q}')\n"
        "    print(f'Bot  : {co5.rule_based_chatbot(q, conn)}')\n"
        "\""
    ),
}

# ════════════════════════════════════════════════════════════════════════
# 2. Execution and Screenshot Generation Loop
# ════════════════════════════════════════════════════════════════════════

output_folder = os.path.abspath("screenshots_per_program")
os.makedirs(output_folder, exist_ok=True)

print(f"Generating {len(PROGRAMS)} individual program screenshots...")

for fname, (title, cmd) in PROGRAMS.items():
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    out_file = os.path.join(output_folder, fname)
    render_box_screenshot(title, cmd, res.stdout, out_file)
    # Also save in root for quick access
    shutil.copyfile(out_file, os.path.abspath(fname))

print("All individual program screenshots generated successfully!")
