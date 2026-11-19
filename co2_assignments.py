"""
CSA08 – CO2 Assignment: Control Flow, Strings, Functions & Recursion
--------------------------------------------------------------------
Covers:
  Q1. Decisions with Many Boundaries: Electricity Subsidy Eligibility
  Q2. Loops that Count Attempts: Bank OTP Verification
  Q3. Vehicle Registration Number Validator (String manipulation only)
  Q4. String Concatenation Benchmark: '+' vs 'join()'
  Q5. Default Mutable Argument Bug & Scope: Canteen Order System
  Q6. Recursion & Memoisation: Temple Step Climbing with @lru_cache
"""

import time
import functools
import sys

# ═════════════════════════════════════════════════════════════════
# Q1. Decisions with Many Boundaries: Electricity Subsidy
# ═════════════════════════════════════════════════════════════════
def calculate_subsidy(units: float, has_ration_card: bool, max_age: int) -> str:
    """
    Rules:
      - units <= 100: Full subsidy (100% free)
      - 101 <= units <= 200 and ration card: Partial subsidy (50% discount)
      - units > 200: No subsidy UNLESS any household member is > 80 years (Senior rebate)
    """
    if units <= 100:
        return "Full Subsidy (100% Free)"
    elif 101 <= units <= 200 and has_ration_card:
        return "Partial Subsidy (50% Discount)"
    elif units > 200 and max_age > 80:
        return "Senior Citizen Special Rebate (30% Discount)"
    else:
        return "No Subsidy (Standard Tariff)"


# ═════════════════════════════════════════════════════════════════
# Q2. Loops that Count Attempts: OTP Verification
# ═════════════════════════════════════════════════════════════════
def verify_otp_simulation(correct_otp: str, inputs: list) -> tuple:
    """
    3 allowed attempts. Blank entries do not consume an attempt.
    Locks after 3 failed attempts.
    """
    max_attempts = 3
    attempts_used = 0
    log = []

    for entry in inputs:
        entry_clean = entry.strip()
        if not entry_clean:
            log.append("Blank input ignored – attempt count not consumed.")
            continue
        
        attempts_used += 1
        if entry_clean == correct_otp:
            log.append(f"OTP Verified successfully on attempt {attempts_used}/{max_attempts}.")
            return True, log
        else:
            remaining = max_attempts - attempts_used
            log.append(f"Incorrect OTP '{entry_clean}'. Attempts remaining: {remaining}")
            if attempts_used >= max_attempts:
                log.append("ACCOUNT LOCKED: 3 consecutive failed attempts.")
                return False, log

    return False, log


# ═════════════════════════════════════════════════════════════════
# Q3. Vehicle Registration Number Validator (NO REGEX)
# ═════════════════════════════════════════════════════════════════
def normalise_reg_number(text: str) -> str:
    """Removes spaces, hyphens, and converts to uppercase."""
    clean = text.strip().upper()
    clean = clean.replace(" ", "").replace("-", "")
    return clean

def validate_reg_number(raw_text: str) -> tuple:
    """
    Format: 2 letters (state) + 2 digits (district) + 1-2 letters (series) + 4 digits (number)
    Length: 9 or 10 characters.
    Uses purely str operations: isalpha(), isdigit(), slicing.
    """
    s = normalise_reg_number(raw_text)
    if len(s) not in (9, 10):
        return False, s, f"Invalid length ({len(s)} chars; expected 9 or 10)"

    state = s[0:2]
    district = s[2:4]
    digits_part = s[-4:]
    series = s[4:-4]

    if not state.isalpha():
        return False, s, f"State code '{state}' must be alphabetic"
    if not district.isdigit():
        return False, s, f"District code '{district}' must be numeric"
    if not series.isalpha():
        return False, s, f"Series '{series}' must be 1-2 alphabetic characters"
    if not digits_part.isdigit():
        return False, s, f"Vehicle number '{digits_part}' must be 4 digits"

    formatted = f"{state} {district} {series} {digits_part}"
    return True, formatted, "Valid"


# ═════════════════════════════════════════════════════════════════
# Q4. Building Long Text: '+' vs 'join()' Benchmark
# ═════════════════════════════════════════════════════════════════
def benchmark_string_building(n: int = 100_000) -> dict:
    parts = [f"SMS-RECORD-{i:06d}: Paid Rs 49.00\n" for i in range(n)]

    # Method A: Repeated concatenation (+ in loop) on a smaller subset (15,000) to avoid slow O(n^2)
    sample_n = min(n, 15_000)
    t0 = time.perf_counter()
    s_concat = ""
    for p in parts[:sample_n]:
        s_concat += p
    t_concat = time.perf_counter() - t0

    # Method B: list + str.join() on full n
    t1 = time.perf_counter()
    s_join = "".join(parts)
    t_join = time.perf_counter() - t1

    return {
        "n_join": n,
        "time_join_sec": t_join,
        "n_concat": sample_n,
        "time_concat_sec": t_concat,
        "join_length": len(s_join)
    }


# ═════════════════════════════════════════════════════════════════
# Q5. Functions, Parameters & Mutable Default Bug
# ═════════════════════════════════════════════════════════════════
def buggy_add_item(item: str, order: list = []) -> list:
    """Demonstrates mutable default parameter trap."""
    order.append(item)
    return order

def fixed_add_item(item: str, order: list = None) -> list:
    """Fixed version creating a fresh list when order is None."""
    if order is None:
        order = []
    order.append(item)
    return order


# ═════════════════════════════════════════════════════════════════
# Q6. Recursion & Memoisation: Temple Step Climbing
# ═════════════════════════════════════════════════════════════════
call_count_naive = 0

def ways_naive(n: int) -> int:
    """Naively counts ways to climb n steps (1 or 2 at a time)."""
    global call_count_naive
    call_count_naive += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)

@functools.lru_cache(maxsize=None)
def ways_memo(n: int) -> int:
    """Optimized step counting with LRU memoisation."""
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)


# ═════════════════════════════════════════════════════════════════
# Demonstration Runner
# ═════════════════════════════════════════════════════════════════
def run_co2_suite():
    print("=" * 70)
    print("   CSA08 CO2: CONTROL FLOW, STRINGS, FUNCTIONS & RECURSION")
    print("=" * 70)

    # Q1. Decisions
    print("\n[Q1] Electricity Subsidy Boundaries:")
    test_cases = [
        (85, False, 45, "<=100 units"),
        (100, False, 50, "Boundary 100 units"),
        (150, True, 60, "101-200 units with ration card"),
        (150, False, 60, "101-200 units NO ration card"),
        (200, True, 70, "Boundary 200 units with card"),
        (250, True, 75, ">200 units with card, no senior"),
        (280, False, 84, ">200 units with senior (>80 yrs)"),
    ]
    for units, card, age, desc in test_cases:
        res = calculate_subsidy(units, card, age)
        print(f"  {units:>3} units | Card={str(card):<5} | Age={age} ({desc:<30}) -> {res}")

    # Q2. Loops
    print("\n[Q2] Bank Kiosk OTP Attempt Simulation (Secret: '7492'):")
    inputs = ["", "1234", "    ", "5678", "7492"]
    success, log = verify_otp_simulation("7492", inputs)
    for l in log:
        print("  •", l)

    # Q3. String Validator
    print("\n[Q3] Vehicle Registration Number Validator (String Methods Only):")
    plates = ["tn 09 ab 1234", "TN-09-AB-1234", "Tn09Ab1234", "KL 01 Z 9999", "TN9AB1234", "DL 04 1234", "MH 12 ABC 1234"]
    for p in plates:
        ok, formatted, msg = validate_reg_number(p)
        status = "✓ VALID  " if ok else "✗ INVALID"
        print(f"  {p:<17} -> {status} [{formatted}] ({msg})")

    # Q4. Benchmark
    print("\n[Q4] String Building: '+' vs 'join()' Benchmark:")
    bm = benchmark_string_building(100_000)
    print(f"  join() on {bm['n_join']:,} lines:   {bm['time_join_sec']*1000:8.2f} ms (O(n))")
    print(f"  '+='   on {bm['n_concat']:,} lines:   {bm['time_concat_sec']*1000:8.2f} ms (O(n²))")
    speedup = (bm['time_concat_sec'] / bm['n_concat']) / (bm['time_join_sec'] / bm['n_join'])
    print(f"  → str.join() is ~{speedup:.1f}x faster per string unit!")

    # Q5. Mutable Default Trap
    print("\n[Q5] Default Mutable Argument Trap (Canteen Orders):")
    b1 = buggy_add_item("Tea")
    b2 = buggy_add_item("Vada")
    print(f"  Buggy (shared list): order 1={b1}, order 2={b2}  <- ACCUMULATES!")
    f1 = fixed_add_item("Tea")
    f2 = fixed_add_item("Vada")
    print(f"  Fixed (order=None):  order 1={f1}, order 2={f2}  <- ISOLATED!")

    # Q6. Recursion & Memoisation
    print("\n[Q6] Recursion vs Memoisation (Temple Steps for n=25):")
    global call_count_naive
    call_count_naive = 0
    t0 = time.perf_counter()
    w_naive = ways_naive(25)
    t_naive = time.perf_counter() - t0

    t1 = time.perf_counter()
    w_memo = ways_memo(25)
    t_memo = time.perf_counter() - t1

    print(f"  Naive ways(25) = {w_naive:,} | Function calls: {call_count_naive:,} ({t_naive*1000:.2f} ms)")
    print(f"  Memo  ways(25) = {w_memo:,} | Distinct subproblems: 26 ({t_memo*1000:.3f} ms)")
    print(f"  Memo  ways(100) = {ways_memo(100):,} (Instant O(n) calculation!)")
    print("=" * 70)


if __name__ == "__main__":
    run_co2_suite()
