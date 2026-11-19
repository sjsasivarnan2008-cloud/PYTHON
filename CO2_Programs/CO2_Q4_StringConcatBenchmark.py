"""
CSA08 CO2 - Q4: Building Long Text: '+' vs 'join()' Performance Benchmark
Benchmarks monthly SMS bill generation for 100,000 lines.
Explains string immutability and memory allocation costs.
"""

import time

def benchmark():
    n_lines = 100_000
    parts = [f"SMS-RECORD-{i:06d}: Sent to +919840000000 | Charge: Rs 1.50\n" for i in range(n_lines)]

    print("=" * 68)
    print("  CSA08 CO2 Q4: STRING CONCATENATION BENCHMARK (+ vs join)")
    print("=" * 68)
    print(f"  Dataset: {n_lines:,} billing statement lines")
    print("─" * 68)

    # Method 1: str.join() on all 100,000 lines (O(n))
    t0 = time.perf_counter()
    joined_text = "".join(parts)
    t_join = time.perf_counter() - t0
    print(f"  [1] str.join(list) on {n_lines:,} lines   : {t_join * 1000:8.2f} ms  (O(n) time)")

    # Method 2: Repeated '+' in loop on 15,000 lines (O(n^2))
    sample_size = 15_000
    t1 = time.perf_counter()
    concat_text = ""
    for line in parts[:sample_size]:
        concat_text += line
    t_concat = time.perf_counter() - t1
    print(f"  [2] Repeated '+='  on {sample_size:,} lines    : {t_concat * 1000:8.2f} ms  (O(n²) time)")

    # Normalize speedup comparison
    per_unit_join = t_join / n_lines
    per_unit_concat = t_concat / sample_size
    speedup = per_unit_concat / per_unit_join

    print("─" * 68)
    print(f"  Result: 'str.join()' is approximately {speedup:.1f}x faster per line.")
    print("  Reason: Python strings are immutable. Repeated '+' creates and copies")
    print("          a new string on each iteration, causing quadratic memory copies.")
    print("=" * 68)

if __name__ == "__main__":
    benchmark()
