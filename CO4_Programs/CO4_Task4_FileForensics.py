"""
CSA08 CO4 - Task 4: File and Exception Forensics (Overwrite vs Append Trap)
Demonstrates how using 'w' mode inadvertently wipes prior historical records,
and proves how 'a' (append) mode preserves multi-day data safely.
"""

import tempfile
import os

def main():
    print("=" * 68)
    print("  CSA08 CO4 TASK 4: FILE FORENSICS (w vs a MODES TRAP)")
    print("=" * 68)

    with tempfile.TemporaryDirectory() as td:
        buggy_log = os.path.join(td, "library_returns_buggy.txt")
        fixed_log = os.path.join(td, "library_returns_fixed.txt")

        daily_returns = [
            ["Day 1: Book #101 returned by 19231101", "Day 1: Book #102 returned by 19231102"],
            ["Day 2: Book #201 returned by 19231103"],
            ["Day 3: Book #301 returned by 19231104", "Day 3: Book #302 returned by 19231105"],
        ]

        # Buggy implementation: opened with 'w' each day
        for day in daily_returns:
            with open(buggy_log, "w", encoding="utf-8") as f:
                f.write("\n".join(day))

        # Fixed implementation: opened with 'a' each day
        for day in daily_returns:
            with open(fixed_log, "a", encoding="utf-8") as f:
                for entry in day:
                    f.write(entry + "\n")

        # Read results
        with open(buggy_log, "r", encoding="utf-8") as f:
            b_lines = [l.strip() for l in f if l.strip()]

        with open(fixed_log, "r", encoding="utf-8") as f:
            f_lines = [l.strip() for l in f if l.strip()]

        print(f"  [1] Buggy Implementation ('w' overwrite mode):")
        print(f"      Remaining Lines in File: {len(b_lines)} / 5 (Days 1 & 2 WIPED OUT!)")
        for l in b_lines:
            print(f"        • {l}")

        print(f"\n  [2] Fixed Implementation ('a' append mode):")
        print(f"      Total Preserved Lines  : {len(f_lines)} / 5 (All 3 days fully preserved)")
        for l in f_lines:
            print(f"        • {l}")

    print("=" * 68)

if __name__ == "__main__":
    main()
