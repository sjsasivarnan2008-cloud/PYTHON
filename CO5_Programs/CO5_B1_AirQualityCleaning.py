"""
CSA08 CO5 - Task B1: Air Quality Data Cleaning & Min-Max Normalisation
Cleans CSV air quality streams: filters sensor anomalies, drops missing values,
converts Fahrenheit to Celsius, and normalizes PM2.5 to [0.0, 1.0].
"""

import csv

def clean_air_quality(csv_text: str) -> list:
    reader = csv.DictReader(csv_text.strip().splitlines())
    clean_data = []
    for row in reader:
        st = row["station"].strip()
        dt = row["date"].strip()
        raw_pm = row.get("pm25", "").strip()
        raw_temp = row.get("temperature", "").strip()

        if not raw_pm or raw_pm.upper() == "NA":
            continue
        try:
            pm = float(raw_pm)
            if pm < 0.0 or pm > 500.0:
                continue
        except ValueError:
            continue

        temp_c = 28.0
        if raw_temp and raw_temp.upper() != "NA":
            try:
                t = float(raw_temp)
                temp_c = round((t - 32.0) * 5.0 / 9.0, 1) if t > 55.0 else t
            except ValueError:
                pass

        clean_data.append({"station": st, "date": dt, "pm25": pm, "temp": temp_c})
    return clean_data

def min_max_scale(values: list) -> list:
    if not values:
        return []
    min_v, max_v = min(values), max(values)
    if min_v == max_v:
        return [0.0 for _ in values]
    return [round((v - min_v) / (max_v - min_v), 3) for v in values]

def main():
    print("=" * 68)
    print("  CSA08 CO5 TASK B1: AIR QUALITY DATA CLEANING & NORMALISATION")
    print("=" * 68)

    sample_csv = """station,date,pm25,temperature
Adyar,2026-10-01,48.0,86.0
Adyar,2026-10-02,54.0,29.5
Adyar,2026-10-03,NA,30.0
Adyar,2026-10-04,,31.0
Adyar,2026-10-05,62.0,28.0
Guindy,2026-10-01,95.0,29.0
Guindy,2026-10-02,-5.0,29.5
Guindy,2026-10-03,121.0,89.6
Guindy,2026-10-04,108.0,32.0
"""
    cleaned = clean_air_quality(sample_csv)
    print(f"  Raw Rows: 9 -> Valid Cleaned Rows: {len(cleaned)}")
    print("─" * 68)
    print(f"  {'Station':<10} {'Date':<12} {'PM2.5 (µg/m³)':>15} {'Temperature':>15}")
    print("─" * 68)
    for r in cleaned:
        print(f"  {r['station']:<10} {r['date']:<12} {r['pm25']:>15.1f} {str(r['temp']) + '°C':>15}")

    pm_values = [r["pm25"] for r in cleaned]
    scaled = min_max_scale(pm_values)

    print("\n  Min-Max Normalisation (Scaled to [0.0, 1.0]):")
    print(f"    • Original PM2.5 : {pm_values}")
    print(f"    • Scaled PM2.5   : {scaled}")
    print("=" * 68)

if __name__ == "__main__":
    main()
