"""
CSA08 CO1 - Task 4: Write Correct Expressions for Rate Calculation
Demonstrates step count calculation, operator precedence, and rounding.
"""

from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")
FAT_STEP = Decimal("0.40")
SNF_STEP = Decimal("0.30")

def calculate_rate(fat: Decimal, snf: Decimal) -> Decimal:
    """Calculate rate per litre with proper step count expressions."""
    fat_steps = (fat - BASE_FAT) / Decimal("0.1")
    snf_steps = (snf - BASE_SNF) / Decimal("0.1")
    rate = BASE_RATE + (fat_steps * FAT_STEP) + (snf_steps * SNF_STEP)
    return rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def main():
    print("=" * 65)
    print("  CSA08 CO1 TASK 4: MILK RATE EXPRESSIONS & STEP FORMULAS")
    print("=" * 65)
    print(f"  Base Parameters: Base Rate = Rs {BASE_RATE}/L | Fat = {BASE_FAT}% | SNF = {BASE_SNF}%")
    print(f"  Incentive Steps: Fat Step  = Rs {FAT_STEP}/0.1% | SNF Step = Rs {SNF_STEP}/0.1%")
    print("─" * 65)
    print(f"  {'Fat%':>6} {'SNF%':>6} {'Fat Steps':>11} {'SNF Steps':>11} {'Rate/Litre':>13} {'Status':>12}")
    print("─" * 65)

    test_samples = [
        (Decimal("3.5"), Decimal("8.5")),   # Base rate
        (Decimal("4.2"), Decimal("8.7")),   # Premium fat and snf
        (Decimal("2.8"), Decimal("8.0")),   # Below base penalties
        (Decimal("5.0"), Decimal("9.2")),   # High quality buffalo milk
        (Decimal("6.5"), Decimal("9.8")),   # Maximum grade
    ]

    for fat, snf in test_samples:
        f_steps = (fat - BASE_FAT) / Decimal("0.1")
        s_steps = (snf - BASE_SNF) / Decimal("0.1")
        rate = calculate_rate(fat, snf)
        status = "Base" if rate == BASE_RATE else ("Premium" if rate > BASE_RATE else "Deduction")
        print(f"  {str(fat):>6} {str(snf):>6} {str(f_steps):>11} {str(s_steps):>11} {str(rate):>13} {status:>12}")

    print("=" * 65)

if __name__ == "__main__":
    main()
