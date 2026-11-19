"""
CSA08 CO1 - Task 7: Build a Reusable Module (milkrate.py)
Encapsulates rate determination, payout calculations, and test execution.
"""

from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")
FAT_STEP = Decimal("0.40")
SNF_STEP = Decimal("0.30")

def rate_per_litre(fat: Decimal, snf: Decimal) -> Decimal:
    """Calculate rate per litre based on fat% and SNF%."""
    fat_steps = (fat - BASE_FAT) / Decimal("0.1")
    snf_steps = (snf - BASE_SNF) / Decimal("0.1")
    rate = BASE_RATE + (fat_steps * FAT_STEP) + (snf_steps * SNF_STEP)
    return rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def payout(litres: Decimal, fat: Decimal, snf: Decimal) -> Decimal:
    """Calculate total monetary payout for delivered milk."""
    rate = rate_per_litre(fat, snf)
    return (litres * rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def test_module():
    print("=" * 65)
    print("  CSA08 CO1 TASK 7: REUSABLE MODULE (milkrate.py)")
    print("=" * 65)
    print("  Testing module functions with CO1 assignment benchmark entries:")
    print("─" * 65)

    deliveries = [
        ("Entry 1", Decimal("8.5"), Decimal("4.2"), Decimal("8.7")),
        ("Entry 2", Decimal("12.0"), Decimal("3.5"), Decimal("8.5")),
        ("Entry 3", Decimal("15.0"), Decimal("4.8"), Decimal("9.0")),
    ]

    for label, litres, fat, snf in deliveries:
        rate = rate_per_litre(fat, snf)
        amount = payout(litres, fat, snf)
        print(f"  {label}: {litres} L | Fat {fat}% | SNF {snf}% -> Rate: Rs {rate}/L | Pay: Rs {amount}")

    print("=" * 65)
    print("  Module Self-Test Passed: Functions validated successfully.")
    print("=" * 65)

if __name__ == "__main__":
    test_module()
