"""
CSA08 CO1 - Task 9: Complete Milk Payment Calculator & Validation
Includes entry range validations, error trapping, and 10-day sum report.
"""

from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")
FAT_STEP = Decimal("0.40")
SNF_STEP = Decimal("0.30")

def rate_per_litre(fat: Decimal, snf: Decimal) -> Decimal:
    fat_steps = (fat - BASE_FAT) / Decimal("0.1")
    snf_steps = (snf - BASE_SNF) / Decimal("0.1")
    rate = BASE_RATE + (fat_steps * FAT_STEP) + (snf_steps * SNF_STEP)
    return rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def payout(litres: Decimal, fat: Decimal, snf: Decimal) -> Decimal:
    rate = rate_per_litre(fat, snf)
    return (litres * rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def validate_entry(litres: Decimal, fat: Decimal, snf: Decimal) -> list:
    errs = []
    if not (Decimal("0.5") <= litres <= Decimal("50.0")):
        errs.append(f"Litres {litres} out of range [0.5–50.0]")
    if not (Decimal("2.0") <= fat <= Decimal("7.0")):
        errs.append(f"Fat {fat}% out of range [2.0–7.0]")
    if not (Decimal("7.0") <= snf <= Decimal("10.0")):
        errs.append(f"SNF {snf}% out of range [7.0–10.0]")
    return errs

def main():
    print("=" * 65)
    print("  CSA08 CO1 TASK 9: VILLAGE CO-OPERATIVE PAYMENT CALCULATOR")
    print("=" * 65)

    entries = [
        ("Farmer 101", Decimal("8.5"), Decimal("4.2"), Decimal("8.7")),
        ("Farmer 102", Decimal("12.0"), Decimal("3.5"), Decimal("8.5")),
        ("Farmer 103", Decimal("6.0"), Decimal("5.0"), Decimal("9.0")),
        ("Farmer 104", Decimal("10.0"), Decimal("2.8"), Decimal("7.5")),
        ("Farmer 105", Decimal("15.5"), Decimal("4.8"), Decimal("9.2")),
    ]

    print(f"  {'Farmer':<12} {'Litres':>7} {'Fat%':>6} {'SNF%':>6} {'Rate/L':>9} {'Amount (Rs)':>13}")
    print("─" * 65)

    total_10day = Decimal("0.00")
    for f_id, lit, fat, snf in entries:
        errs = validate_entry(lit, fat, snf)
        if not errs:
            r = rate_per_litre(fat, snf)
            amt = payout(lit, fat, snf)
            total_10day += amt
            print(f"  {f_id:<12} {str(lit):>7} {str(fat):>6} {str(snf):>6} {str(r):>9} {str(amt):>13}")

    print("─" * 65)
    print(f"  {'10-DAY TOTAL':<12} {'(' + str(len(entries)) + ' deliveries)':>20} {'Rs':>16} {str(total_10day):>13}")

    # Invalid entries validation test
    print("\n  Input Validation Boundary Checks:")
    invalid_tests = [
        ("Farmer 201", Decimal("65.0"), Decimal("4.0"), Decimal("8.5")),  # Exceeds max litres
        ("Farmer 202", Decimal("8.0"), Decimal("1.5"), Decimal("8.5")),   # Fat below 2.0%
        ("Farmer 203", Decimal("10.0"), Decimal("4.5"), Decimal("11.5")), # SNF above 10.0%
    ]
    for f_id, lit, fat, snf in invalid_tests:
        errs = validate_entry(lit, fat, snf)
        print(f"  ✗ {f_id} (Litres={lit}, Fat={fat}%, SNF={snf}%) -> REJECTED: {', '.join(errs)}")

    print("=" * 65)

if __name__ == "__main__":
    main()
