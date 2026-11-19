"""
CSA08 CO2 - Q5: Functions, Parameters & Scope (Mutable Default Trap)
Exposes the common Python trap where default mutable arguments (list)
are created once at function definition and shared across invocations.
"""

def buggy_add_item(item: str, order: list = []) -> list:
    """Buggy: order default list persists between separate customer calls!"""
    order.append(item)
    return order

def fixed_add_item(item: str, order: list = None) -> list:
    """Fixed: order defaults to None, instantiating a fresh list each time."""
    if order is None:
        order = []
    order.append(item)
    return order

def main():
    print("=" * 68)
    print("  CSA08 CO2 Q5: CANTEEN ORDERING & DEFAULT MUTABLE ARGUMENT BUG")
    print("=" * 68)

    print("\n[1] Buggy Implementation (def add_item(item, order=[])):")
    cust1 = buggy_add_item("Tea")
    print(f"  Customer 1 orders 'Tea'  -> Order List: {cust1}")
    cust2 = buggy_add_item("Vada")
    print(f"  Customer 2 orders 'Vada' -> Order List: {cust2}  (BUG: Prior items leaked!)")

    print("\n[2] Fixed Implementation (def add_item(item, order=None)):")
    fix1 = fixed_add_item("Tea")
    print(f"  Customer 1 orders 'Tea'  -> Order List: {fix1}")
    fix2 = fixed_add_item("Vada")
    print(f"  Customer 2 orders 'Vada' -> Order List: {fix2}  (CORRECT: Isolated orders)")

    print("\n" + "=" * 68)
    print("  Scope Rule: Python default arguments evaluate once at definition time.")
    print("              Always use None for default mutable collections (list, dict).")
    print("=" * 68)

if __name__ == "__main__":
    main()
