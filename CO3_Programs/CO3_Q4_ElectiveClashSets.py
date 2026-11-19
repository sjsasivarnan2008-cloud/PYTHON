"""
CSA08 CO3 - Q4: Sets (Elective Course Registration Clash Detection)
Detects timetable clashes for students registering for AI and IoT electives
in the same time slot using set operations (&, ^, -).
"""

def main():
    print("=" * 68)
    print("  CSA08 CO3 Q4: ELECTIVE COURSE REGISTRATION CLASH DETECTION")
    print("=" * 68)

    all_students = {f"1923110{i:02d}" for i in range(1, 11)}
    ai_elective = {"192311001", "192311004", "192311007", "192311009"}
    iot_elective = {"192311002", "192311004", "192311009", "192311010"}

    # Set operations
    both_clash = ai_elective & iot_elective
    exactly_one = ai_elective ^ iot_elective
    neither = all_students - (ai_elective | iot_elective)

    print("  Enrolled in AI Elective  :", sorted(list(ai_elective)))
    print("  Enrolled in IoT Elective :", sorted(list(iot_elective)))
    print("─" * 68)
    print(f"  Clash / Both (ai & iot)      : {sorted(list(both_clash))}  ({len(both_clash)} students)")
    print(f"  Exactly One (ai ^ iot)       : {sorted(list(exactly_one))}  ({len(exactly_one)} students)")
    print(f"  Neither (all - (ai | iot))   : {sorted(list(neither))}  ({len(neither)} students)")
    print("=" * 68)

if __name__ == "__main__":
    main()
