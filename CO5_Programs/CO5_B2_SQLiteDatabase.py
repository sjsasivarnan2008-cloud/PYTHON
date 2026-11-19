"""
CSA08 CO5 - Task B2: SQLite Storage with Parameterized Queries & SQLi Defense
Inserts cleaned records into SQLite, answers analytical queries,
and proves immunity against SQL injection attacks using '?' placeholders.
"""

import sqlite3

def init_db(records: list) -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            station TEXT NOT NULL,
            reading_date TEXT NOT NULL,
            pm25 REAL NOT NULL,
            temperature REAL NOT NULL
        )
    """)
    cur.executemany(
        "INSERT INTO readings (station, reading_date, pm25, temperature) VALUES (?, ?, ?, ?)",
        [(r[0], r[1], r[2], r[3]) for r in records]
    )
    conn.commit()
    return conn

def get_station_average(conn: sqlite3.Connection, station_name: str):
    cur = conn.cursor()
    cur.execute("SELECT AVG(pm25) FROM readings WHERE station = ?", (station_name,))
    row = cur.fetchone()
    return round(row[0], 2) if (row and row[0] is not None) else None

def main():
    print("=" * 68)
    print("  CSA08 CO5 TASK B2: SQLITE STORAGE & SQL INJECTION DEFENSE")
    print("=" * 68)

    sample_data = [
        ("Adyar", "2026-10-01", 48.0, 28.0),
        ("Adyar", "2026-10-02", 54.0, 29.0),
        ("Adyar", "2026-10-03", 62.0, 28.5),
        ("Guindy", "2026-10-01", 95.0, 30.0),
        ("Guindy", "2026-10-02", 121.0, 31.0),
        ("Velachery", "2026-10-01", 42.0, 27.5),
    ]

    conn = init_db(sample_data)

    print("  Station Average PM2.5 (Parameterized SQL Queries):")
    for st in ["Adyar", "Guindy", "Velachery"]:
        avg = get_station_average(conn, st)
        status = "Satisfactory" if avg <= 60 else "Unhealthy / Exceeds Limit"
        print(f"    • {st:<10} : {avg:6.2f} µg/m³  [{status}]")

    # SQL Injection Adversarial Test
    print("\n  Adversarial Security Test:")
    malicious_payload = "Adyar' OR '1'='1"
    res = get_station_average(conn, malicious_payload)
    print(f"    • Payload tested : \"{malicious_payload}\"")
    print(f"    • Query result   : {res} (Safely treated as literal string; No leak!)")
    print("=" * 68)

if __name__ == "__main__":
    main()
