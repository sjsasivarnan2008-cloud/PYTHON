"""
CSA08 CO3 - Q5: List Comprehensions (Cold-Storage Vaccine Temperature Monitor)
Filters sensor anomalies (outside -50 to +50 C), converts Celsius to Fahrenheit,
and identifies alarm minutes (outside safe storage range of 2 to 8 C).
"""

def main():
    print("=" * 68)
    print("  CSA08 CO3 Q5: VACCINE COLD-STORAGE TEMPERATURE CLEANING")
    print("=" * 68)

    raw_readings = [4.2, 5.1, 95.0, 3.8, -60.0, 1.5, 8.5, 6.0, 4.0, 12.0]

    # List comprehensions
    valid_celsius = [t for t in raw_readings if -50.0 <= t <= 50.0]
    valid_fahrenheit = [round((c * 9.0/5.0) + 32.0, 2) for c in valid_celsius]
    alarm_minutes = [min_idx for min_idx, t in enumerate(raw_readings) if -50.0 <= t <= 50.0 and (t < 2.0 or t > 8.0)]

    print(f"  Raw Sensor Readings Stream (°C) : {raw_readings}")
    print(f"  Cleaned Valid Readings Count     : {len(valid_celsius)} / {len(raw_readings)} (Filtered {len(raw_readings)-len(valid_celsius)} faulty readings)")
    print(f"  Cleaned Celsius Readings (°C)    : {valid_celsius}")
    print(f"  Converted Fahrenheit (°F)        : {valid_fahrenheit}")
    print(f"  Alarm Triggered Minutes (!=2-8°C): Minute indices {alarm_minutes}")
    print("=" * 68)

if __name__ == "__main__":
    main()
