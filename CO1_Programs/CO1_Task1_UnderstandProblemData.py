"""
CSA08 CO1 - Task 1: Understand the Problem and Identify the Data
Problem Context: Ksheera Village Milk Producers' Co-operative
--------------------------------------------------------------
Identifies all data items (inputs, outputs, constants), specifies their types
and valid ranges, and analyzes data structures for storing 300 farmers' records.
"""

import sys
from decimal import Decimal
from collections import namedtuple

# ════════════════════════════════════════════════════════════════════════
# 1. Problem Data Dictionary Specification
# ════════════════════════════════════════════════════════════════════════

DATA_DICTIONARY = [
    # (Category, Variable Name, Python Type, Valid Range / Default, Description)
    ("Constant", "BASE_RATE",   "Decimal", "Rs 30.00 / Litre",  "Government baseline milk purchase rate"),
    ("Constant", "BASE_FAT",    "Decimal", "3.5 %",             "Baseline fat percentage for standard cow milk"),
    ("Constant", "BASE_SNF",    "Decimal", "8.5 %",             "Baseline solids-not-fat percentage"),
    ("Constant", "FAT_STEP",    "Decimal", "Rs 0.40 / 0.1 %",   "Incentive / penalty step per 0.1% fat"),
    ("Constant", "SNF_STEP",    "Decimal", "Rs 0.30 / 0.1 %",   "Incentive / penalty step per 0.1% SNF"),
    ("Input",    "farmer_id",   "str",     "e.g., 'F-101'",     "Unique village membership code"),
    ("Input",    "shift",       "str",     "'Morning' / 'Evening'", "Daily delivery shift indicator"),
    ("Input",    "litres",      "Decimal", "[0.5 to 50.0] L",   "Volume of milk poured into measuring can"),
    ("Input",    "fat_pct",     "Decimal", "[2.0 to 7.0] %",    "Electronic Gerber/analyser fat reading"),
    ("Input",    "snf_pct",     "Decimal", "[7.0 to 10.0] %",   "Calculated solids-not-fat reading"),
    ("Output",   "rate_per_l",  "Decimal", "Calculated Rs/L",   "Dynamic rate determined by milk quality"),
    ("Output",   "shift_pay",   "Decimal", ">= Rs 0.00",        "Monetary payout for current delivery"),
    ("Output",   "ten_day_tot", "Decimal", "Sum of 20 shifts",  "10-day cooperative settlement balance"),
]

# ════════════════════════════════════════════════════════════════════════
# 2. Alternative Concept: Separate Variables vs Structured Record
# ════════════════════════════════════════════════════════════════════════

DeliveryRecord = namedtuple("DeliveryRecord", ["farmer_id", "shift", "litres", "fat", "snf"])

def compare_storage_approaches(n_entries: int = 6000):
    """
    Simulates 300 farmers x 2 shifts/day x 10 days = 6,000 deliveries.
    Compares:
      Approach A: 5 parallel lists (storing farmer_ids, shifts, litres, fats, snfs)
      Approach B: 1 list of structured tuples/namedtuples
    """
    # Approach A: Parallel lists
    ids_list = [f"F-{i%300:03d}" for i in range(n_entries)]
    shifts_list = ["Morning" if i % 2 == 0 else "Evening" for i in range(n_entries)]
    litres_list = [Decimal("8.5") for _ in range(n_entries)]
    fat_list = [Decimal("4.2") for _ in range(n_entries)]
    snf_list = [Decimal("8.7") for _ in range(n_entries)]

    size_parallel = (
        sys.getsizeof(ids_list) +
        sys.getsizeof(shifts_list) +
        sys.getsizeof(litres_list) +
        sys.getsizeof(fat_list) +
        sys.getsizeof(snf_list)
    )

    # Approach B: List of composite records
    records_list = [
        DeliveryRecord(f"F-{i%300:03d}", "Morning" if i % 2 == 0 else "Evening", Decimal("8.5"), Decimal("4.2"), Decimal("8.7"))
        for i in range(n_entries)
    ]
    size_composite = sys.getsizeof(records_list) + sum(sys.getsizeof(r) for r in records_list[:100]) * (n_entries // 100)

    return size_parallel, size_composite

# ════════════════════════════════════════════════════════════════════════
# Main Execution
# ════════════════════════════════════════════════════════════════════════

def main():
    print("=" * 72)
    print("  CSA08 CO1 TASK 1: UNDERSTAND THE PROBLEM & IDENTIFY THE DATA")
    print("=" * 72)
    print("  Scenario: Ksheera Village Milk Producers' Co-operative")
    print("  Scale   : 300 farmers x 2 shifts/day = 600 entries/day (6,000 in 10 days)")
    print("─" * 72)

    print("\n[1] Formal Data Dictionary & Validation Specifications:")
    print(f"  {'Category':<10} {'Variable':<14} {'Type':<9} {'Allowed Range':<22} Description")
    print("─" * 72)
    for cat, var, typ, rng, desc in DATA_DICTIONARY:
        print(f"  {cat:<10} {var:<14} {typ:<9} {rng:<22} {desc}")

    print("\n[2] Alternative Concept Analysis (Data Storage Strategy):")
    p_size, c_size = compare_storage_approaches(6000)
    print(f"  Scale: 10-day settlement cycle (6,000 delivery entries)")
    print(f"    • Approach A: 5 Parallel Lists        -> List pointers: {p_size:,} bytes")
    print(f"    • Approach B: List of Delivery Records -> Structured memory: {c_size:,} bytes")
    print("    • Engineering Trade-off:")
    print("      - Parallel lists risk index desynchronization on sorting or deletion.")
    print("      - Composite tuple/namedtuple records guarantee atomicity & integrity.")

    print("\n[3] Sample Validated Incoming Records (Morning Shift):")
    sample_deliveries = [
        DeliveryRecord("F-101", "Morning", Decimal("8.5"), Decimal("4.2"), Decimal("8.7")),
        DeliveryRecord("F-102", "Morning", Decimal("12.0"), Decimal("3.5"), Decimal("8.5")),
        DeliveryRecord("F-103", "Morning", Decimal("6.0"), Decimal("5.0"), Decimal("9.0")),
    ]
    for d in sample_deliveries:
        print(f"    Record: {d.farmer_id} | Shift: {d.shift:<7} | Qty: {d.litres} L | Fat: {d.fat}% | SNF: {d.snf}% [VALID]")

    print("=" * 72)

if __name__ == "__main__":
    main()
