"""
CSA08 CO1 - Task 10: Compare Expectations with Execution (Float vs Decimal)
Times and compares floating-point vs Decimal performance & rounding deviations
over large scales (300, 6000, 150000 transactions).
"""

from decimal import Decimal
import time

def compare_scales(n: int):
    # Benchmark float
    rate_flt = 33.40
    step_flt = 0.10
    t0 = time.perf_counter()
    tot_flt = 0.0
    for _ in range(n):
        tot_flt += (10.0 * rate_flt + 3.0 * step_flt)
    t_flt = time.perf_counter() - t0

    # Benchmark Decimal
    rate_dec = Decimal("33.40")
    step_dec = Decimal("0.10")
    ten_dec = Decimal("10.0")
    three_dec = Decimal("3.0")
    t1 = time.perf_counter()
    tot_dec = Decimal("0.0")
    for _ in range(n):
        tot_dec += (ten_dec * rate_dec + three_dec * step_dec)
    t_dec = time.perf_counter() - t1

    diff = abs(Decimal(str(round(tot_flt, 2))) - tot_dec)
    return tot_flt, tot_dec, diff, t_flt, t_dec

def main():
    print("=" * 65)
    print("  CSA08 CO1 TASK 10: FLOAT VS DECIMAL BENCHMARK & PRECISION")
    print("=" * 65)

    scales = [
        (300, "1 Village Centre (300 farmers)"),
        (6_000, "1 Block Union (6,000 farmers)"),
        (150_000, "1 District Union (150,000 farmers)")
    ]

    for count, label in scales:
        flt_val, dec_val, deviation, t_f, t_d = compare_scales(count)
        print(f"\n  Scale: {label}")
        print(f"    • Float Total   : Rs {flt_val:,.4f}  (Time: {t_f*1000:6.2f} ms)")
        print(f"    • Decimal Total : Rs {dec_val:,.2f}  (Time: {t_d*1000:6.2f} ms)")
        print(f"    • Accumulated Discrepancy : Rs {deviation}  (Risk to Farmers/Union!)")

    print("\n" + "=" * 65)
    print("  Engineering Recommendation: Use Decimal for co-op accounts to eliminate cumulative error.")
    print("=" * 65)

if __name__ == "__main__":
    main()
