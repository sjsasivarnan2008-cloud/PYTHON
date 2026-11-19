"""
CSA08 CO3 - Q2: Tuples, Mutability & Copying
Demonstrates GPS coordinates as immutable dictionary keys,
diagnoses the [[0]*cols]*rows aliasing trap, and compares shallow vs deep copy.
"""

import copy

def main():
    print("=" * 68)
    print("  CSA08 CO3 Q2: TUPLES, MUTABILITY & GRID ALIASING TRAP")
    print("=" * 68)

    # 1. Tuples as immutable dictionary keys
    bus_stops = {
        (13.0827, 80.2707): "Chennai Central Station",
        (13.0500, 80.2500): "T Nagar Bus Depot",
        (12.9800, 80.2200): "Guindy Terminal"
    }
    print("[1] Tuples as Dictionary Keys (GPS Coordinates):")
    for coords, name in bus_stops.items():
        print(f"  GPS: {coords} -> {name}")

    # 2. Grid Aliasing Bug
    print("\n[2] Grid Aliasing Trap vs List Comprehension:")
    rows, cols = 3, 4
    bad_grid = [[0] * cols] * rows
    bad_grid[0][1] = 7  # Intending to update row 0, col 1 only

    good_grid = [[0] * cols for _ in range(rows)]
    good_grid[0][1] = 7

    print(f"  Bad Grid  : [[0]*cols]*rows -> row[0] is row[1]: {bad_grid[0] is bad_grid[1]} (BUGGY!)")
    print(f"              Result: {bad_grid}")
    print(f"  Good Grid : [comprehension] -> row[0] is row[1]: {good_grid[0] is good_grid[1]} (CORRECT)")
    print(f"              Result: {good_grid}")

    # 3. Shallow copy vs Deep copy
    print("\n[3] Shallow Copy vs Deep Copy:")
    original = [["Stop A", "Stop B"], ["Stop C", "Stop D"]]
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)
    original[0][0] = "MUTATED"

    print(f"  Shallow Copy affected by nested change: {shallow[0][0] == 'MUTATED'} (Inner lists shared)")
    print(f"  Deep Copy completely isolated         : {deep[0][0] == 'Stop A'} (Fully independent)")
    print("=" * 68)

if __name__ == "__main__":
    main()
