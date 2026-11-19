"""
CSA08 CO1 - Task 2: Explore Values and Types in Python
Demonstrates type inspection, integer vs float division,
and floating-point inaccuracies vs Decimal precision.
"""

from decimal import Decimal

def main():
    print("=" * 65)
    print("  CSA08 CO1 TASK 2: VALUES, TYPES & DECIMAL EXACTNESS")
    print("=" * 65)

    # 1. Type exploration
    v_int = 42
    v_flt = 3.14
    v_str = "Ksheera"
    v_bool = True
    v_lst = [3.5, 8.5, 30.0]

    print("\n[1] Type Inspection:")
    print(f"  type({v_int:<7})  ->  {type(v_int)}")
    print(f"  type({v_flt:<7})  ->  {type(v_flt)}")
    print(f"  type({v_str:<7})  ->  {type(v_str)}")
    print(f"  type({str(v_bool):<7})  ->  {type(v_bool)}")
    print(f"  type({str(v_lst):<7})  ->  {type(v_lst)}")

    # 2. Division behaviors
    print("\n[2] Division Operations:")
    print(f"   7 / 2   = {7 / 2:<5} (Float division)")
    print(f"   7 // 2  = {7 // 2:<5} (Floor division)")
    print(f"   7 % 2   = {7 % 2:<5} (Modulo remainder)")
    print(f"  -7 // 2  = {-7 // 2:<5} (Floor rounds towards -infinity)")

    # 3. Floating-point inaccuracy
    print("\n[3] Floating-Point Representation Problem:")
    sum_flt = 0.1 + 0.2
    print(f"  0.1 + 0.2 == 0.3          : {sum_flt == 0.3}")
    print(f"  Actual 0.1 + 0.2 value    : {sum_flt:.17f}")

    # 4. Financial calculation comparison
    print("\n[4] Complete the Code - Decimal Precision for Co-operative Money:")
    n_payments = 1000
    rate_flt = 33.40
    step_flt = 0.10
    total_flt = n_payments * rate_flt + 3 * step_flt

    rate_dec = Decimal("33.40")
    step_dec = Decimal("0.10")
    total_dec = n_payments * rate_dec + 3 * step_dec

    print(f"  Float calculation (1000 x 33.40 + 3 x 0.10)   : Rs {total_flt:.10f}  (Error!)")
    print(f"  Decimal calculation (Exact string conversion) : Rs {total_dec}  (Exact!)")
    print("=" * 65)

if __name__ == "__main__":
    main()
