"""
CSA08 CO4 - Task 2 & 3: Biometric Attendance & Custom Exception Handling
Parses biometric log files, raises and handles custom 'InvalidRecord' exceptions,
computes student attendance percentages, and generates attendance shortage reports (<75%).
"""

import tempfile
import os

class InvalidRecord(Exception):
    """Raised when attendance file records are damaged or non-standard."""
    pass

def parse_record(line: str, line_no: int) -> tuple:
    parts = [p.strip() for p in line.split(",")]
    if len(parts) != 3:
        raise InvalidRecord(f"Line {line_no}: expected 3 fields, found {len(parts)}")
    reg, dt, status = parts
    status = status.upper()
    if status not in ("P", "A"):
        raise InvalidRecord(f"Line {line_no}: invalid attendance flag '{status}', must be 'P' or 'A'")
    return reg, dt, status

def process_attendance(filepath: str):
    totals = {}
    presents = {}
    corrupted = []

    with open(filepath, "r", encoding="utf-8") as f:
        for lno, raw in enumerate(f, start=1):
            line = raw.strip()
            if not line:
                continue
            try:
                reg, dt, st = parse_record(line, lno)
                totals[reg] = totals.get(reg, 0) + 1
                if st == "P":
                    presents[reg] = presents.get(reg, 0) + 1
            except InvalidRecord as err:
                corrupted.append(str(err))

    percentages = {}
    shortages = []
    for reg, tot in totals.items():
        p = presents.get(reg, 0)
        pct = round((p / tot) * 100.0, 1)
        percentages[reg] = pct
        if pct < 75.0:
            shortages.append((reg, pct, p, tot))

    return percentages, shortages, corrupted

def main():
    print("=" * 68)
    print("  CSA08 CO4 TASK 2 & 3: BIOMETRIC ATTENDANCE & EXCEPTION HANDLING")
    print("=" * 68)

    with tempfile.TemporaryDirectory() as td:
        log_file = os.path.join(td, "biometric_log.csv")
        with open(log_file, "w", encoding="utf-8") as f:
            f.write("19231101, 2026-10-01, P\n")
            f.write("19231101, 2026-10-02, P\n")
            f.write("19231101, 2026-10-03, P\n")
            f.write("19231101, 2026-10-04, P\n")
            f.write("19231102, 2026-10-01, P\n")
            f.write("19231102, 2026-10-02, A\n")
            f.write("19231102, 2026-10-03, A\n")
            f.write("19231102, 2026-10-04, A\n")
            f.write("19231103, 2026-10-01\n")     # Corrupted: missing status
            f.write("19231104, 2026-10-01, L\n")  # Corrupted: invalid status 'L'

        pcts, shorts, corrupts = process_attendance(log_file)

        print("  Student Attendance Summary:")
        for reg, pct in pcts.items():
            status = "Satisfactory" if pct >= 75.0 else "SHORTAGE (<75%)"
            print(f"    • Student {reg} : {pct:5.1f}%  [{status}]")

        print("\n  Official Shortage List for Review:")
        for reg, pct, p, t in shorts:
            print(f"    ✗ Student {reg}: {pct}% ({p}/{t} sessions attended)")

        print("\n  Handled InvalidRecord Exceptions:")
        for err in corrupts:
            print(f"    • {err}")

    print("=" * 68)

if __name__ == "__main__":
    main()
