"""
CSA08 CO2 - Q1: Decisions with Many Boundaries (State Electricity Subsidy)
Rules:
  - units <= 100: Full subsidy (100% Free)
  - 101 <= units <= 200 and has ration card: Partial subsidy (50% Discount)
  - units > 200: No subsidy unless a household member is > 80 years (Senior Rebate)
"""

def evaluate_subsidy(units: float, has_ration_card: bool, max_age: int) -> str:
    if units <= 100:
        return "Full Subsidy (100% Free)"
    elif 101 <= units <= 200 and has_ration_card:
        return "Partial Subsidy (50% Discount)"
    elif units > 200 and max_age > 80:
        return "Senior Citizen Special Rebate (30% Discount)"
    else:
        return "No Subsidy (Standard Tariff)"

def main():
    print("=" * 68)
    print("  CSA08 CO2 Q1: ELECTRICITY SUBSIDY DECISION BOUNDARIES")
    print("=" * 68)

    households = [
        ("Household 1", 85, False, 45, "<= 100 units limit"),
        ("Household 2", 100, False, 52, "Boundary 100 units"),
        ("Household 3", 101, True, 38, "Boundary 101 units with card"),
        ("Household 4", 150, True, 60, "101-200 units with card"),
        ("Household 5", 150, False, 60, "101-200 units WITHOUT card"),
        ("Household 6", 200, True, 70, "Boundary 200 units with card"),
        ("Household 7", 201, True, 72, "Boundary 201 units (Exceeds limit)"),
        ("Household 8", 260, False, 84, ">200 units WITH senior member (>80y)"),
    ]

    print(f"  {'Household':<13} {'Units':>5} {'Card':<6} {'Age':>4} {'Boundary Note':<28} -> Decision")
    print("─" * 68)

    for name, units, card, age, note in households:
        decision = evaluate_subsidy(units, card, age)
        card_str = "Yes" if card else "No"
        print(f"  {name:<13} {units:>5} {card_str:<6} {age:>4} {note:<28} -> {decision}")

    print("=" * 68)

if __name__ == "__main__":
    main()
