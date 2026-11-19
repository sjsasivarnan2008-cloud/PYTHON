"""
CSA08 CO4 - Task 6: College Fest Multi-Department Registration Pipeline
Processes departmental files, handles duplicates across departments,
validates emails using string operations, and generates master & event lists.
"""

import tempfile
import os

def is_valid_email(email: str) -> bool:
    if "@" not in email or email.count("@") != 1:
        return False
    local_part, domain = email.split("@")
    if not local_part or not domain or "." not in domain:
        return False
    return not any(len(p) == 0 for p in domain.split("."))

def process_registrations(dept_files: dict, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    seen_ids = set()
    master = []
    rejected = []
    events = {}

    for dept, fpath in dept_files.items():
        with open(fpath, "r", encoding="utf-8") as f:
            for lno, raw in enumerate(f, start=1):
                line = raw.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(",")]
                if len(parts) < 5:
                    rejected.append(f"[{dept} L{lno}] Corrupted format: {line}")
                    continue

                reg, name, dcode, email = parts[0], parts[1], parts[2], parts[3]
                ev_list = [e.strip() for e in parts[4].split(";") if e.strip()]

                if not is_valid_email(email):
                    rejected.append(f"[{dept} L{lno}] Invalid email '{email}' for {reg} ({name})")
                    continue

                if reg in seen_ids:
                    rejected.append(f"[{dept} L{lno}] Duplicate student ID {reg} ({name}) - Skipped")
                    continue

                seen_ids.add(reg)
                master.append({"reg": reg, "name": name, "dept": dcode, "email": email, "events": ev_list})
                for ev in ev_list:
                    events.setdefault(ev, []).append((reg, name, dcode))

    return master, events, rejected

def main():
    print("=" * 68)
    print("  CSA08 CO4 TASK 6: COLLEGE FEST REGISTRATION PIPELINE")
    print("=" * 68)

    with tempfile.TemporaryDirectory() as td:
        cse_p = os.path.join(td, "cse.csv")
        ece_p = os.path.join(td, "ece.csv")

        with open(cse_p, "w", encoding="utf-8") as f:
            f.write("19231101, Anand, CSE, anand@college.edu, Coding;Web Design\n")
            f.write("19231102, Bala, CSE, bala_invalid_mail, Coding\n")
            f.write("19231103, Chitra, CSE, chitra@college.edu, Robotics;Quiz\n")

        with open(ece_p, "w", encoding="utf-8") as f:
            f.write("19231104, Deepa, ECE, deepa@college.edu, Robotics;Coding\n")
            f.write("19231101, Anand, ECE, anand@college.edu, Gaming\n")  # Duplicate

        master, ev_map, rejections = process_registrations({"CSE": cse_p, "ECE": ece_p}, os.path.join(td, "out"))

        print(f"  Accepted Clean Master Registrations: {len(master)} students")
        for m in master:
            print(f"    • {m['reg']} | {m['name']:<8} | Dept: {m['dept']:<4} | Events: {'; '.join(m['events'])}")

        print("\n  Event Participation Breakdown:")
        for ev, parts in ev_map.items():
            print(f"    • Event '{ev:<12}': {len(parts)} participants")

        print(f"\n  Rejection Audit Log ({len(rejections)} issues handled):")
        for r in rejections:
            print(f"    • {r}")

    print("=" * 68)

if __name__ == "__main__":
    main()
