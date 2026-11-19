"""
CSA08 CO3 - Q1: Lists and Slicing (Village Rain-Gauge Station)
Analyzes 365 daily rainfall readings: weekly totals, wettest/driest weeks,
7-day moving averages, and dry days list.
"""

def main():
    print("=" * 68)
    print("  CSA08 CO3 Q1: 365-DAY RAINFALL SLICING & MOVING AVERAGES")
    print("=" * 68)

    # 365 daily readings (mm) - synthetic realistic monsoon and dry seasonal pattern
    readings = [0.0 if (i % 3 != 0) else float((i * 7) % 65) for i in range(365)]

    # Analysis using list operations & slicing
    dry_days = [day for day, val in enumerate(readings, 1) if val == 0.0]
    total_rain = sum(readings)

    # Slicing for 52 weekly blocks
    weekly_totals = [sum(readings[i:i+7]) for i in range(0, 52 * 7, 7)]
    max_week = weekly_totals.index(max(weekly_totals)) + 1
    min_week = weekly_totals.index(min(weekly_totals)) + 1

    # 7-day moving average preview
    moving_avg_preview = [round(sum(readings[i:i+7]) / 7.0, 2) for i in range(7)]

    print(f"  Annual Rainfall Total : {total_rain:.1f} mm")
    print(f"  Dry Days Count (0 mm) : {len(dry_days)} / 365 days")
    print(f"  Wettest Week Recorded : Week #{max_week} ({max(weekly_totals):.1f} mm)")
    print(f"  Driest Week Recorded  : Week #{min_week} ({min(weekly_totals):.1f} mm)")
    print(f"  7-Day Moving Avg (1-7): {moving_avg_preview}")
    print("=" * 68)

if __name__ == "__main__":
    main()
