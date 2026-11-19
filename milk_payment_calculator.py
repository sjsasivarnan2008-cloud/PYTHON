"""
CSA08 – CO1 Assignment
Ksheera Village Milk Co-operative Payment Calculator
------------------------------------------------------
Calculates per-litre rate and payout based on fat% and SNF%
with Decimal precision and 10-day totals.
"""

from decimal import Decimal, ROUND_HALF_UP
import time

# ─────────────── Constants (Rate Card) ───────────────
BASE_RATE   = Decimal("30.00")   # Rs/litre at 3.5% fat, 8.5% SNF
BASE_FAT    = Decimal("3.5")
BASE_SNF    = Decimal("8.5")
FAT_STEP    = Decimal("0.40")    # Rs per 0.1% fat step
SNF_STEP    = Decimal("0.30")    # Rs per 0.1% SNF step
FAT_MIN     = Decimal("2.0")
FAT_MAX     = Decimal("7.0")
SNF_MIN     = Decimal("7.0")
SNF_MAX     = Decimal("10.0")
LITRES_MIN  = Decimal("0.5")
LITRES_MAX  = Decimal("50.0")

# ─────────────── Functions ────────────────────────────

def rate_per_litre(fat: Decimal, snf: Decimal) -> Decimal:
    """Calculate rate per litre based on fat% and SNF%."""
    fat_steps = (fat - BASE_FAT) / Decimal("0.1")
    snf_steps = (snf - BASE_SNF) / Decimal("0.1")
    rate = BASE_RATE + (fat_steps * FAT_STEP) + (snf_steps * SNF_STEP)
    return rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def payout(litres: Decimal, fat: Decimal, snf: Decimal) -> Decimal:
    """Calculate total payout for one delivery."""
    rate = rate_per_litre(fat, snf)
    amount = litres * rate
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def validate_entry(litres: Decimal, fat: Decimal, snf: Decimal) -> list:
    """Return list of validation error messages (empty = valid)."""
    errors = []
    if not (LITRES_MIN <= litres <= LITRES_MAX):
        errors.append(f"  ✗ Litres {litres} out of range [{LITRES_MIN}–{LITRES_MAX}]")
    if not (FAT_MIN <= fat <= FAT_MAX):
        errors.append(f"  ✗ Fat% {fat} out of range [{FAT_MIN}–{FAT_MAX}]")
    if not (SNF_MIN <= snf <= SNF_MAX):
        errors.append(f"  ✗ SNF% {snf} out of range [{SNF_MIN}–{SNF_MAX}]")
    return errors


def ten_day_total(entries: list) -> Decimal:
    """Sum payouts for all valid entries in a 10-day period."""
    total = Decimal("0.00")
    for litres, fat, snf in entries:
        total += payout(litres, fat, snf)
    return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


# ─────────────── Sample Data ──────────────────────────

SAMPLE_ENTRIES = [
    # (Farmer, Litres,  Fat,  SNF)
    ("Farmer A",  Decimal("8.5"),  Decimal("4.2"), Decimal("8.7")),
    ("Farmer B",  Decimal("12.0"), Decimal("3.5"), Decimal("8.5")),   # base rate
    ("Farmer C",  Decimal("6.0"),  Decimal("5.0"), Decimal("9.0")),
    ("Farmer D",  Decimal("10.0"), Decimal("2.8"), Decimal("7.5")),
    ("Farmer E",  Decimal("15.5"), Decimal("4.8"), Decimal("9.2")),
    ("Farmer F",  Decimal("7.0"),  Decimal("3.2"), Decimal("8.1")),   # below base
    ("Farmer G",  Decimal("9.5"),  Decimal("6.0"), Decimal("9.8")),   # premium
    ("Farmer H",  Decimal("11.0"), Decimal("3.5"), Decimal("8.5")),   # base rate
    ("Farmer I",  Decimal("5.5"),  Decimal("4.5"), Decimal("8.9")),
    ("Farmer J",  Decimal("13.0"), Decimal("3.9"), Decimal("8.6")),
]

INVALID_ENTRIES = [
    ("Bad #1", Decimal("60.0"), Decimal("4.0"), Decimal("8.5")),   # litres too high
    ("Bad #2", Decimal("8.0"),  Decimal("1.5"), Decimal("8.5")),   # fat too low
    ("Bad #3", Decimal("8.0"),  Decimal("4.0"), Decimal("11.0")),  # SNF too high
]


# ─────────────── Main Report ──────────────────────────

def print_separator(char="─", width=65):
    print(char * width)

def run_report():
    start = time.perf_counter()

    print()
    print("=" * 65)
    print("   🐄  KSHEERA VILLAGE MILK CO-OPERATIVE  |  PAYMENT REPORT")
    print("=" * 65)
    print(f"   Rate Card  →  Base: Rs {BASE_RATE}/L  |  Fat step: Rs {FAT_STEP}/0.1%  |  SNF step: Rs {SNF_STEP}/0.1%")
    print_separator()

    # Header
    print(f"{'Farmer':<12} {'Litres':>7} {'Fat%':>6} {'SNF%':>6} {'Rate/L':>9} {'Amount (Rs)':>12}")
    print_separator()

    valid_entries_data = []
    for farmer, litres, fat, snf in SAMPLE_ENTRIES:
        errors = validate_entry(litres, fat, snf)
        if not errors:
            rate = rate_per_litre(fat, snf)
            amount = payout(litres, fat, snf)
            valid_entries_data.append((litres, fat, snf))
            print(f"{farmer:<12} {str(litres):>7} {str(fat):>6} {str(snf):>6} {str(rate):>9} {str(amount):>12}")

    print_separator()

    # 10-day total
    total = ten_day_total(valid_entries_data)
    count = len(valid_entries_data)
    print(f"{'10-DAY TOTAL':<12} {'(' + str(count) + ' entries)':>21}  {'Rs':>18} {str(total):>12}")
    print_separator()

    # Invalid entries section
    print()
    print("─── Validation Errors (Rejected Entries) ───────────────────────")
    for farmer, litres, fat, snf in INVALID_ENTRIES:
        errors = validate_entry(litres, fat, snf)
        print(f"  {farmer}: Litres={litres}, Fat={fat}%, SNF={snf}%")
        for err in errors:
            print(err)

    # Decimal precision vs float comparison
    print()
    print("─── Decimal vs Float Precision Demo ────────────────────────────")
    n = 1000
    unit_price_dec = Decimal("33.40")
    unit_price_flt = 33.40
    paise_dec = Decimal("0.10")
    paise_flt = 0.10

    total_dec = n * unit_price_dec + 3 * paise_dec
    total_flt = n * unit_price_flt + 3 * paise_flt

    print(f"  Decimal  → 1000 × Rs33.40 + 3 × Rs0.10 = Rs {total_dec}")
    print(f"  Float    → 1000 × 33.40 + 3 × 0.10     = Rs {total_flt:.10f}  ← rounding error!")
    print(f"  0.1 + 0.2 == 0.3 ?  →  {0.1 + 0.2 == 0.3}  (float cannot represent exactly)")

    elapsed = time.perf_counter() - start
    print()
    print("=" * 65)
    print(f"   Report generated in {elapsed*1000:.3f} ms  |  CSA08 CO1 – Python Programming")
    print("=" * 65)
    print()


if __name__ == "__main__":
    run_report()
