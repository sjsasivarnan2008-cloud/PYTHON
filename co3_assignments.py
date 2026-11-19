"""
CSA08 – CO3 Assignment: Data Structures (Lists, Tuples, Dictionaries, Sets)
-------------------------------------------------------------------------
Covers:
  Q1. Lists & Slicing: 365-Day Daily Rainfall Records
  Q2. Tuples, Mutability & Shallow/Deep Copying: GPS Bus Stops & Grid Aliasing Trap
  Q3. Dictionaries & Sets: Kisan Call Centre Complaint Word Frequencies
  Q4. Sets: Elective Course Registration Clash Detection
  Q5. List Comprehensions: Cold-Storage Vaccine Temperature Sensor Cleaning
  Q6. Nested Structures: Railway Timetable Index & Query
  Q7. Contact-Merging Program from First Principles
"""

import copy
import sys

# ═════════════════════════════════════════════════════════════════
# Q1. Lists and Slicing: Daily Rainfall Records
# ═════════════════════════════════════════════════════════════════
def analyze_rainfall(readings: list) -> dict:
    """Analyze 365 daily rainfall readings (mm)."""
    dry_days = [day for day, val in enumerate(readings, 1) if val == 0.0]
    total_annual = sum(readings)

    # 52 complete weeks (7 days each)
    weekly_totals = [sum(readings[i:i+7]) for i in range(0, 52 * 7, 7)]
    max_week_idx = weekly_totals.index(max(weekly_totals)) + 1
    min_week_idx = weekly_totals.index(min(weekly_totals)) + 1

    # 7-day moving average (first 30 days preview)
    moving_avg_30 = [round(sum(readings[i:i+7]) / 7.0, 2) for i in range(30)]

    return {
        "annual_total_mm": round(total_annual, 1),
        "dry_days_count": len(dry_days),
        "wettest_week": (max_week_idx, round(max(weekly_totals), 1)),
        "driest_week": (min_week_idx, round(min(weekly_totals), 1)),
        "moving_avg_first_7": moving_avg_30[:7]
    }


# ═════════════════════════════════════════════════════════════════
# Q2. Tuples, Mutability & Copying: City Bus Stops & Grid Trap
# ═════════════════════════════════════════════════════════════════
def demonstrate_grid_and_copying():
    # Tuples as immutable dictionary keys
    stops_coords = {
        (13.0827, 80.2707): "Central Station",
        (13.0500, 80.2500): "T Nagar Depot",
        (12.9800, 80.2200): "Guindy Terminal"
    }

    # Grid Aliasing Bug
    rows, cols = 3, 4
    bad_grid = [[0] * cols] * rows
    bad_grid[0][1] = 7  # Intending to modify only row 0, col 1

    # Fixed Grid using List Comprehension
    good_grid = [[0] * cols for _ in range(rows)]
    good_grid[0][1] = 7

    # Shallow vs Deep Copy
    original = [["A", "B"], ["C", "D"]]
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)
    original[0][0] = "MODIFIED"

    return {
        "bad_is_aliased": bad_grid[0] is bad_grid[1],
        "bad_grid_sample": bad_grid,
        "good_is_aliased": good_grid[0] is good_grid[1],
        "good_grid_sample": good_grid,
        "shallow_affected": shallow[0][0] == "MODIFIED",
        "deep_isolated": deep[0][0] == "A"
    }


# ═════════════════════════════════════════════════════════════════
# Q3. Dictionaries: Kisan Call Centre Complaint Word Frequencies
# ═════════════════════════════════════════════════════════════════
STOP_WORDS = {"the", "is", "at", "which", "on", "not", "high", "and", "in", "to", "for", "a", "of"}

def word_frequencies(complaints: list, stop_set: set) -> dict:
    freq = {}
    for comp in complaints:
        # Simple punctuation cleaning
        clean_text = comp.lower().replace(".", "").replace(",", "").replace("!", "")
        for word in clean_text.split():
            if word not in stop_set:
                freq[word] = freq.get(word, 0) + 1
    return freq

def top_k_words(freq: dict, k: int = 5) -> list:
    return sorted(freq.items(), key=lambda item: item[1], reverse=True)[:k]


# ═════════════════════════════════════════════════════════════════
# Q4. Sets: Elective Course Registration Clash Detection
# ═════════════════════════════════════════════════════════════════
def detect_registration_clashes(all_students: set, ai_set: set, iot_set: set) -> dict:
    clash_both = ai_set & iot_set
    exactly_one = ai_set ^ iot_set
    neither = all_students - (ai_set | iot_set)
    return {
        "clash_count": len(clash_both),
        "clash_list": sorted(list(clash_both)),
        "one_only_count": len(exactly_one),
        "one_only_list": sorted(list(exactly_one)),
        "neither_count": len(neither),
        "neither_list": sorted(list(neither))
    }


# ═════════════════════════════════════════════════════════════════
# Q5. List Comprehension: Cold-Storage Vaccine Temperature
# ═════════════════════════════════════════════════════════════════
def clean_and_analyze_temperatures(readings: list) -> dict:
    """
    Cold-storage rules:
      - Valid range: -50°C to +50°C (others are sensor errors)
      - Alarm threshold: outside +2°C to +8°C
    """
    valid_celsius = [t for t in readings if -50.0 <= t <= 50.0]
    valid_fahrenheit = [round((c * 9.0/5.0) + 32.0, 2) for c in valid_celsius]
    alarm_minutes = [minute for minute, t in enumerate(readings) if -50.0 <= t <= 50.0 and (t < 2.0 or t > 8.0)]

    return {
        "valid_count": len(valid_celsius),
        "dropped_errors": len(readings) - len(valid_celsius),
        "valid_celsius_sample": valid_celsius[:5],
        "valid_fahrenheit_sample": valid_fahrenheit[:5],
        "alarm_minutes": alarm_minutes
    }


# ═════════════════════════════════════════════════════════════════
# Q6. Nested Data: Railway Timetable Index & Query
# ═════════════════════════════════════════════════════════════════
TIMETABLE = {
    "12637": {
        "name": "Pandian Express",
        "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"},
        "stops": [("Chennai Egmore", "21:40"), ("Viluppuram", "23:50"), ("Madurai", "05:35")]
    },
    "12638": {
        "name": "Pandian Return",
        "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"},
        "stops": [("Madurai", "21:20"), ("Viluppuram", "03:00"), ("Chennai Egmore", "05:15")]
    },
    "20607": {
        "name": "Vande Bharat Express",
        "days": {"Mon", "Wed", "Thu", "Fri", "Sat", "Sun"},
        "stops": [("Chennai Central", "05:50"), ("Katpadi", "07:13"), ("Bengaluru", "10:10")]
    },
    "12007": {
        "name": "Shatabdi Express",
        "days": {"Mon", "Tue", "Wed", "Fri", "Sat", "Sun"},
        "stops": [("Chennai Central", "06:00"), ("Katpadi", "07:38"), ("Bengaluru", "10:50")]
    }
}

def build_station_index(timetable: dict) -> dict:
    """Inverted index mapping Station Name -> list of (train_no, name, dep_time, days)"""
    index = {}
    for train_no, data in timetable.items():
        for station, dep in data["stops"]:
            if station not in index:
                index[station] = []
            index[station].append({
                "train_no": train_no,
                "train_name": data["name"],
                "departure": dep,
                "days": data["days"]
            })
    return index


# ═════════════════════════════════════════════════════════════════
# Q7. Contact-Merging Program from First Principles
# ═════════════════════════════════════════════════════════════════
def normalise_phone(phone: str) -> str:
    """Normalises numbers like '+91 98400 12345' or '09840012345' to '9840012345'."""
    digits = "".join(ch for ch in phone if ch.isdigit())
    if digits.startswith("91") and len(digits) == 12:
        return digits[2:]
    if digits.startswith("0") and len(digits) == 11:
        return digits[1:]
    return digits

def merge_contacts(contact_records: list) -> dict:
    """
    Merges duplicate contacts across phones and SIM card.
    Primary key: normalised 10-digit phone number.
    Names: pick the most descriptive (longest/proper case).
    Emails: set union of all unique emails.
    """
    merged = {}
    for rec in contact_records:
        norm_phone = normalise_phone(rec["phone"])
        if not norm_phone:
            continue
        
        name = rec["name"].strip()
        email = rec.get("email", "").strip().lower()

        if norm_phone not in merged:
            merged[norm_phone] = {
                "name": name,
                "phone": norm_phone,
                "emails": {email} if email else set()
            }
        else:
            # Update name if current one has more detail (e.g. 'Dr. Ravi Kumar' over 'ravi')
            if len(name) > len(merged[norm_phone]["name"]):
                merged[norm_phone]["name"] = name
            if email:
                merged[norm_phone]["emails"].add(email)

    return merged


# ═════════════════════════════════════════════════════════════════
# Demonstration Runner
# ═════════════════════════════════════════════════════════════════
def run_co3_suite():
    print("=" * 70)
    print("   CSA08 CO3: DATA STRUCTURES (LISTS, TUPLES, DICTS, SETS)")
    print("=" * 70)

    # Q1. Rainfall
    print("\n[Q1] Daily Rainfall Analysis (365 Days Synthetic Dataset):")
    # Generate realistic seasonal rainfall (mostly 0-10mm, with monsoon spikes)
    rainfall_data = [0.0 if (i % 3 != 0) else float((i * 7) % 65) for i in range(365)]
    rf_report = analyze_rainfall(rainfall_data)
    print(f"  Annual Rainfall: {rf_report['annual_total_mm']} mm | Dry Days: {rf_report['dry_days_count']}/365")
    print(f"  Wettest Week: Week #{rf_report['wettest_week'][0]} ({rf_report['wettest_week'][1]} mm)")
    print(f"  Driest Week:  Week #{rf_report['driest_week'][0]} ({rf_report['driest_week'][1]} mm)")
    print(f"  7-Day Moving Avg (Day 1-7): {rf_report['moving_avg_first_7']}")

    # Q2. Tuples & Copying
    print("\n[Q2] Tuples, Mutability & The [[0]*cols]*rows Aliasing Bug:")
    grid_info = demonstrate_grid_and_copying()
    print(f"  Bad Grid: [[0]*cols]*rows -> row[0] is row[1]: {grid_info['bad_is_aliased']} (BUGGY!)")
    print(f"  Bad Grid Output:  {grid_info['bad_grid_sample']}")
    print(f"  Good Grid: [comprehension]-> row[0] is row[1]: {grid_info['good_is_aliased']} (FIXED!)")
    print(f"  Good Grid Output: {grid_info['good_grid_sample']}")
    print(f"  Shallow copy affected by inner mutation: {grid_info['shallow_affected']}")
    print(f"  Deep copy fully isolated: {grid_info['deep_isolated']}")

    # Q3. Dictionaries
    print("\n[Q3] Kisan Call Centre Complaint Word Frequencies:")
    complaints = [
        "Cotton crop damaged due to high price seeds not germinating.",
        "Fertilizer price is too high and seeds received were bad quality.",
        "Paddy harvest delayed. Received damaged seeds from local store."
    ]
    freq = word_frequencies(complaints, STOP_WORDS)
    top_words = top_k_words(freq, 4)
    print(f"  Top Complaint Keywords: {top_words}")

    # Q4. Sets
    print("\n[Q4] Elective Registration Clash Detection (AI vs IoT):")
    all_stud = {f"1923110{i:02d}" for i in range(1, 11)}
    ai_stud = {"192311001", "192311004", "192311007", "192311009"}
    iot_stud = {"192311002", "192311004", "192311009", "192311010"}
    clash_res = detect_registration_clashes(all_stud, ai_stud, iot_stud)
    print(f"  Clash (Both AI & IoT)  : {clash_res['clash_list']}")
    print(f"  Exactly One Elective   : {clash_res['one_only_list']}")
    print(f"  Neither Registered     : {clash_res['neither_list']}")

    # Q5. List Comprehension
    print("\n[Q5] Vaccine Cold-Storage Temperature Sensor Cleaning:")
    raw_temps = [4.2, 5.1, 95.0, 3.8, -60.0, 1.5, 8.5, 6.0, 4.0, 12.0]
    temp_res = clean_and_analyze_temperatures(raw_temps)
    print(f"  Valid Readings Count   : {temp_res['valid_count']} (Filtered out {temp_res['dropped_errors']} faulty sensor readings)")
    print(f"  Celsius Readings       : {temp_res['valid_celsius_sample']}")
    print(f"  Fahrenheit Converted   : {temp_res['valid_fahrenheit_sample']}")
    print(f"  Alarm Minutes (Outside 2-8°C): Minute indices {temp_res['alarm_minutes']}")

    # Q6. Railway Timetable Index
    print("\n[Q6] Nested Timetable Inverted Index Query (Katpadi Station):")
    station_idx = build_station_index(TIMETABLE)
    katpadi_trains = station_idx.get("Katpadi", [])
    for t in katpadi_trains:
        print(f"  Train {t['train_no']} ({t['train_name']}) departs Katpadi at {t['departure']} on {len(t['days'])} days/week")

    # Q7. Contact-Merging
    print("\n[Q7] Contact-Merging from Multiple Sources:")
    raw_contacts = [
        {"name": "ravi", "phone": "+91 98400 12345", "email": "ravi@gmail.com"},
        {"name": "Dr. Ravi Kumar", "phone": "09840012345", "email": "r.kumar@hospital.org"},
        {"name": "Priya", "phone": "9876543210", "email": "priya@work.com"},
        {"name": "Priya S.", "phone": "+91-98765-43210", "email": "priya_personal@gmail.com"},
    ]
    merged = merge_contacts(raw_contacts)
    for num, data in merged.items():
        print(f"  Merged Contact: {data['name']:<16} | Phone: {num} | Emails: {list(data['emails'])}")

    print("=" * 70)


if __name__ == "__main__":
    run_co3_suite()
