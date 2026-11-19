"""
CSA08 CO3 - Q6: Nested Data Structures (Railway Timetable Inverted Index)
Builds a station-to-train inverted lookup index to provide instant O(1)
enquiry responses for train departures and running days.
"""

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

def build_inverted_index(timetable: dict) -> dict:
    index = {}
    for train_no, info in timetable.items():
        for st_name, dep in info["stops"]:
            if st_name not in index:
                index[st_name] = []
            index[st_name].append({
                "no": train_no,
                "name": info["name"],
                "departure": dep,
                "days_count": len(info["days"])
            })
    return index

def main():
    print("=" * 68)
    print("  CSA08 CO3 Q6: RAILWAY TIMETABLE INVERTED INDEX & ENQUIRY")
    print("=" * 68)

    station_idx = build_inverted_index(TIMETABLE)
    test_stations = ["Chennai Central", "Katpadi", "Madurai"]

    for st in test_stations:
        departures = station_idx.get(st, [])
        print(f"\n  Enquiry for Station: [{st}] ({len(departures)} departing trains):")
        print("  " + "─" * 60)
        for t in departures:
            print(f"    Train #{t['no']} ({t['name']:<20}) Departs: {t['departure']} | {t['days_count']} days/week")

    print("\n" + "=" * 68)

if __name__ == "__main__":
    main()
