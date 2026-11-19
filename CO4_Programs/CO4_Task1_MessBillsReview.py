"""
CSA08 CO4 - Task 1: File-Processing Design Review (Hostel Mess Bills)
Reads bills line by line using a context manager, validates fields,
computes total amounts safely, and maintains a rejection audit log.
"""

import tempfile
import os

def process_mess_bills(filepath: str) -> tuple:
    valid_records = []
    rejected_lines = []
    total_amount = 0.0

    with open(filepath, "r", encoding="utf-8") as f:
        for line_no, raw_line in enumerate(f, start=1):
            line = raw_line.strip()
            if not line:
                continue

            parts = [p.strip() for p in line.split(",")]
            if len(parts) != 3:
                rejected_lines.append((line_no, line, f"Expected 3 fields, found {len(parts)}"))
                continue

            reg_no, name, amt_str = parts
            try:
                amt = float(amt_str)
                if amt < 0:
                    raise ValueError("Negative bill amount")
                valid_records.append((reg_no, name, amt))
                total_amount += amt
            except ValueError as ve:
                rejected_lines.append((line_no, line, f"Invalid bill amount '{amt_str}': {ve}"))

    return total_amount, valid_records, rejected_lines

def main():
    print("=" * 68)
    print("  CSA08 CO4 TASK 1: SAFE FILE PROCESSING (HOSTEL MESS BILLS)")
    print("=" * 68)

    # Create realistic test file
    with tempfile.TemporaryDirectory() as td:
        bill_path = os.path.join(td, "mess_october.txt")
        with open(bill_path, "w", encoding="utf-8") as f:
            f.write("19231101, Akash, 3450.50\n")
            f.write("19231102, Bharath, 4120.00\n")
            f.write("19231103, Chandru, corrupt_amt\n")  # Damaged amount
            f.write("19231104, Divya\n")                 # Missing fields
            f.write("19231105, Eswar, 2980.75\n")

        total, valids, rejections = process_mess_bills(bill_path)

        print(f"  Valid Student Bills Processed: {len(valids)} records")
        for reg, name, amt in valids:
            print(f"    • {reg} | {name:<12} | Rs {amt:8.2f}")
        print("─" * 68)
        print(f"  Total Valid Collection       : Rs {total:,.2f}")
        print(f"\n  Rejected Lines Audit Log ({len(rejections)} issues detected):")
        for lno, text, reason in rejections:
            print(f"    • Line {lno}: {reason}")

    print("=" * 68)

if __name__ == "__main__":
    main()
