"""
CSA08 – CO4 Assignment: File Handling, Exceptions, Modules & Packages
---------------------------------------------------------------------
Covers:
  Task 1. File-Processing Review: Safe Hostel Mess Bill Totaling
  Task 2. Biometric Attendance Processor with Custom 'InvalidRecord' Exception
  Task 3. Robust Exception Handling (try/except/else/finally)
  Task 4. File Forensics: Overwrite ('w') vs Append ('a') Trap
  Task 5. College Fest Registration Desk:
          - Multiple Department File Reading
          - Duplicate Student Removal (Sets)
          - String-method based E-mail Validation
          - Master List & Event-wise Participant Files
"""

import os
import shutil
import tempfile

# ═════════════════════════════════════════════════════════════════
# Task 2 & 3: Custom Exception Definition
# ═════════════════════════════════════════════════════════════════
class InvalidRecord(Exception):
    """Raised when an attendance or registration record format is corrupted."""
    pass


# ═════════════════════════════════════════════════════════════════
# Task 1: Safe File Processing (Hostel Mess Bills)
# ═════════════════════════════════════════════════════════════════
def process_mess_bills(filepath: str) -> tuple:
    """
    Safely reads mess bills using context manager, line by line.
    Line format: register_number,name,amount
    """
    valid_records = []
    rejected_lines = []
    total_amount = 0.0

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line_no, raw_line in enumerate(f, start=1):
                line = raw_line.strip()
                if not line:
                    continue  # skip empty lines
                
                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 3:
                    rejected_lines.append((line_no, line, f"Expected 3 fields, found {len(parts)}"))
                    continue

                reg_no, name, amt_str = parts
                try:
                    amt = float(amt_str)
                    if amt < 0:
                        raise ValueError("Negative amount")
                    valid_records.append((reg_no, name, amt))
                    total_amount += amt
                except ValueError as ve:
                    rejected_lines.append((line_no, line, f"Invalid bill amount '{amt_str}': {ve}"))
    except FileNotFoundError:
        return 0.0, [], [(0, filepath, "File not found")]

    return total_amount, valid_records, rejected_lines


# ═════════════════════════════════════════════════════════════════
# Task 2: Biometric Attendance Processing
# ═════════════════════════════════════════════════════════════════
def parse_biometric_line(line: str, line_no: int) -> tuple:
    """Parses a single attendance line: reg_no, date, P/A"""
    parts = [p.strip() for p in line.split(",")]
    if len(parts) != 3:
        raise InvalidRecord(f"Line {line_no}: expected 3 fields, found {len(parts)}")
    
    reg_no, date_str, status = parts
    status_upper = status.upper()
    if status_upper not in ("P", "A"):
        raise InvalidRecord(f"Line {line_no}: invalid status '{status}', must be 'P' or 'A'")
    
    return reg_no, date_str, status_upper

def summarize_attendance(filepath: str) -> dict:
    present_counts = {}
    total_days = {}
    corrupted_lines = []

    with open(filepath, "r", encoding="utf-8") as f:
        for line_no, raw_line in enumerate(f, start=1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                reg_no, _, status = parse_biometric_line(line, line_no)
                total_days[reg_no] = total_days.get(reg_no, 0) + 1
                if status == "P":
                    present_counts[reg_no] = present_counts.get(reg_no, 0) + 1
            except InvalidRecord as e:
                corrupted_lines.append(str(e))

    # Calculate percentages
    percentages = {}
    shortage_list = []  # Below 75%
    for reg, days in total_days.items():
        p_count = present_counts.get(reg, 0)
        pct = round((p_count / days) * 100.0, 1)
        percentages[reg] = pct
        if pct < 75.0:
            shortage_list.append((reg, pct))

    return {
        "attendance_percentages": percentages,
        "shortage_below_75": shortage_list,
        "corrupted_records": corrupted_lines
    }


# ═════════════════════════════════════════════════════════════════
# Task 4: File Forensics: Overwrite ('w') vs Append ('a')
# ═════════════════════════════════════════════════════════════════
def demonstrate_file_forensics(workdir: str) -> dict:
    buggy_path = os.path.join(workdir, "library_buggy_log.txt")
    fixed_path = os.path.join(workdir, "library_fixed_log.txt")

    days_data = [
        ["Day 1: Book #101 returned", "Day 1: Book #102 returned"],
        ["Day 2: Book #201 returned"],
        ["Day 3: Book #301 returned", "Day 3: Book #302 returned"]
    ]

    # Buggy version uses "w" every day (overwrites history!)
    for day_entries in days_data:
        with open(buggy_path, "w", encoding="utf-8") as f:
            f.write("\n".join(day_entries))

    # Fixed version uses "a" (appends each day's returns)
    for day_entries in days_data:
        with open(fixed_path, "a", encoding="utf-8") as f:
            for entry in day_entries:
                f.write(entry + "\n")

    with open(buggy_path, "r", encoding="utf-8") as f:
        buggy_result = f.read().splitlines()

    with open(fixed_path, "r", encoding="utf-8") as f:
        fixed_result = f.read().splitlines()

    return {
        "buggy_lines_count": len(buggy_result),
        "buggy_content": buggy_result,
        "fixed_lines_count": len(fixed_result),
        "fixed_content": fixed_result
    }


# ═════════════════════════════════════════════════════════════════
# Task 6: College Fest Registration Desk
# ═════════════════════════════════════════════════════════════════
def is_valid_email(email: str) -> bool:
    """Validates email without regex using string operations."""
    if "@" not in email or email.count("@") != 1:
        return False
    local_part, domain = email.split("@")
    if not local_part or not domain:
        return False
    if "." not in domain:
        return False
    domain_parts = domain.split(".")
    if any(len(p) == 0 for p in domain_parts):
        return False
    return True

def process_fest_registrations(dept_files: dict, output_dir: str) -> dict:
    os.makedirs(output_dir, exist_ok=True)
    seen_reg_nos = set()
    master_records = []
    rejected_log = []
    events_map = {}

    for dept, filepath in dept_files.items():
        if not os.path.exists(filepath):
            rejected_log.append(f"Department file missing: {filepath}")
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            for line_no, raw_line in enumerate(f, start=1):
                line = raw_line.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(",")]
                if len(parts) < 5:
                    rejected_log.append(f"[{dept} L{line_no}] Corrupted line: '{line}'")
                    continue

                reg_no, name, d_code, email = parts[0], parts[1], parts[2], parts[3]
                events = [e.strip() for e in parts[4].split(";") if e.strip()]

                # Email check
                if not is_valid_email(email):
                    rejected_log.append(f"[{dept} L{line_no}] Invalid email '{email}' for student {reg_no}")
                    continue

                # Duplicate student check
                if reg_no in seen_reg_nos:
                    rejected_log.append(f"[{dept} L{line_no}] Duplicate registration for student {reg_no} ({name}) - Ignored.")
                    continue

                seen_reg_nos.add(reg_no)
                master_records.append({
                    "reg_no": reg_no,
                    "name": name,
                    "dept": d_code,
                    "email": email,
                    "events": events
                })

                for ev in events:
                    if ev not in events_map:
                        events_map[ev] = []
                    events_map[ev].append((reg_no, name, d_code))

    # Write Master List
    master_file = os.path.join(output_dir, "master_registrations.csv")
    with open(master_file, "w", encoding="utf-8") as f:
        f.write("RegisterNumber,Name,Department,Email,Events\n")
        for rec in master_records:
            ev_str = ";".join(rec["events"])
            f.write(f"{rec['reg_no']},{rec['name']},{rec['dept']},{rec['email']},{ev_str}\n")

    # Write Event-wise Files
    for ev_name, participants in events_map.items():
        clean_ev_name = ev_name.replace(" ", "_").lower()
        ev_file = os.path.join(output_dir, f"event_{clean_ev_name}.csv")
        with open(ev_file, "w", encoding="utf-8") as f:
            f.write("RegisterNumber,Name,Department\n")
            for reg, name, d_code in participants:
                f.write(f"{reg},{name},{d_code}\n")

    return {
        "total_registered": len(master_records),
        "total_rejected": len(rejected_log),
        "events_summary": {ev: len(parts) for ev, parts in events_map.items()},
        "rejected_log": rejected_log
    }


# ═════════════════════════════════════════════════════════════════
# Demonstration Runner
# ═════════════════════════════════════════════════════════════════
def run_co4_suite():
    print("=" * 70)
    print("   CSA08 CO4: FILE HANDLING, EXCEPTIONS, MODULES & PACKAGES")
    print("=" * 70)

    temp_dir = tempfile.mkdtemp(prefix="csa08_co4_")

    try:
        # Task 1: Hostel Mess Bill
        print("\n[Task 1] Safe Mess Bill Totaling (with-statement & Line-by-Line):")
        mess_file = os.path.join(temp_dir, "mess_bills.txt")
        with open(mess_file, "w", encoding="utf-8") as f:
            f.write("19231101, Akash, 3450.50\n")
            f.write("19231102, Bharath, 4120.00\n")
            f.write("19231103, Chandru, invalid_num\n")  # Damaged amount
            f.write("19231104, Divya\n")                # Missing fields
            f.write("19231105, Eswar, 2980.75\n")
        
        tot, valids, rejections = process_mess_bills(mess_file)
        print(f"  Valid Bills Totaled  : Rs {tot:,.2f} ({len(valids)} students)")
        print(f"  Rejections Logged    : {len(rejections)} issues:")
        for lno, text, reason in rejections:
            print(f"    Line {lno}: {reason}")

        # Task 2 & 3: Biometric Attendance
        print("\n[Task 2 & 3] Biometric Attendance Processing & Custom Exceptions:")
        bio_file = os.path.join(temp_dir, "biometric_oct.csv")
        with open(bio_file, "w", encoding="utf-8") as f:
            f.write("19231101, 2026-10-01, P\n")
            f.write("19231101, 2026-10-02, P\n")
            f.write("19231101, 2026-10-03, P\n")
            f.write("19231101, 2026-10-04, P\n")
            f.write("19231102, 2026-10-01, P\n")
            f.write("19231102, 2026-10-02, A\n")
            f.write("19231102, 2026-10-03, A\n")
            f.write("19231102, 2026-10-04, A\n")  # 25% attendance
            f.write("19231103, 2026-10-01\n")      # Corrupted: missing field
            f.write("19231104, 2026-10-01, L\n")   # Corrupted: invalid status 'L'

        bio_summary = summarize_attendance(bio_file)
        print(f"  Attendance Rates     : {bio_summary['attendance_percentages']}")
        print(f"  Shortage (<75%)      : {bio_summary['shortage_below_75']}")
        print(f"  Handled Exceptions   : {bio_summary['corrupted_records']}")

        # Task 4: Forensics
        print("\n[Task 4] File Forensics: Overwrite ('w') vs Append ('a'):")
        forensics = demonstrate_file_forensics(temp_dir)
        print(f"  Buggy ('w' mode) final line count : {forensics['buggy_lines_count']} lines (Prior days WIPED OUT!)")
        print(f"  Buggy File Contents               : {forensics['buggy_content']}")
        print(f"  Fixed ('a' mode) final line count : {forensics['fixed_lines_count']} lines (All days preserved!)")

        # Task 6: College Fest Registration
        print("\n[Task 6] College Fest Multi-Department Registration Pipeline:")
        cse_file = os.path.join(temp_dir, "cse_reg.csv")
        ece_file = os.path.join(temp_dir, "ece_reg.csv")
        with open(cse_file, "w", encoding="utf-8") as f:
            f.write("19231101, Anand, CSE, anand@college.edu, Coding;Web Design\n")
            f.write("19231102, Bala, CSE, bala_invalid_email, Coding\n")  # Invalid email
            f.write("19231103, Chitra, CSE, chitra@college.edu, Robotics;Quiz\n")
        with open(ece_file, "w", encoding="utf-8") as f:
            f.write("19231104, Deepa, ECE, deepa@college.edu, Robotics;Coding\n")
            f.write("19231101, Anand, ECE, anand@college.edu, Gaming\n")  # Duplicate student ID!

        fest_out = os.path.join(temp_dir, "fest_output")
        fest_res = process_fest_registrations({"CSE": cse_file, "ECE": ece_file}, fest_out)
        print(f"  Clean Master Registrations: {fest_res['total_registered']} students accepted")
        print(f"  Event Distribution        : {fest_res['events_summary']}")
        print(f"  Rejection Audit Log ({fest_res['total_rejected']} items):")
        for rej in fest_res['rejected_log']:
            print("    •", rej)

        print("=" * 70)

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    run_co4_suite()
