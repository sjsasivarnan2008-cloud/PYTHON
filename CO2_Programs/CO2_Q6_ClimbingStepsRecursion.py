"""
CSA08 CO2 - Q6: Recursion and Its Limits (Temple Steps Climbing)
Counts ways to climb n steps (1 or 2 steps at a time).
Compares naive recursion vs @functools.lru_cache memoisation.
"""

import time
import functools

naive_calls = 0

def ways_naive(n: int) -> int:
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)

@functools.lru_cache(maxsize=None)
def ways_memo(n: int) -> int:
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)

def main():
    print("=" * 68)
    print("  CSA08 CO2 Q6: RECURSION VS MEMOISATION (TEMPLE STEP CLIMBING)")
    print("=" * 68)

    n = 25
    print(f"  Calculating combinations to climb {n} temple steps:")
    print("─" * 68)

    # Naive recursion
    global naive_calls
    naive_calls = 0
    t0 = time.perf_counter()
    res_naive = ways_naive(n)
    t_naive = time.perf_counter() - t0
    print(f"  [1] Naive Recursion : {res_naive:,} ways | Calls: {naive_calls:,} ({t_naive*1000:6.2f} ms)")

    # Memoized recursion
    t1 = time.perf_counter()
    res_memo = ways_memo(n)
    t_memo = time.perf_counter() - t1
    print(f"  [2] @lru_cache Memo : {res_memo:,} ways | Cache size: {n+1} ({t_memo*1000:6.3f} ms)")

    # Scaling up to large n
    large_n = 100
    res_large = ways_memo(large_n)
    print(f"\n  [3] Scaled to n={large_n} steps (via Memoisation):")
    print(f"      Total ways = {res_large:,}")
    print("      Computed instantly without hitting Python call-stack limits!")
    print("=" * 68)

if __name__ == "__main__":
    main()
