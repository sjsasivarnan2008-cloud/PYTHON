"""
CSA08 CO2 - Q3: Vehicle Registration Number Validator (Toll Plaza)
Validates vehicle registration plate formats strictly using str methods
(No regular expressions).
Expected Format: 2 letters (state) + 2 digits (dist) + 1-2 letters (series) + 4 digits
"""

def normalise(raw_text: str) -> str:
    """Removes whitespace, hyphens, and standardizes to uppercase."""
    return raw_text.strip().upper().replace(" ", "").replace("-", "")

def validate_registration(raw_text: str) -> tuple:
    s = normalise(raw_text)
    if len(s) not in (9, 10):
        return False, s, f"Invalid length ({len(s)} chars; expected 9 or 10)"

    state = s[0:2]
    district = s[2:4]
    digits_part = s[-4:]
    series = s[4:-4]

    if not state.isalpha():
        return False, s, f"State code '{state}' must be alphabetic"
    if not district.isdigit():
        return False, s, f"District code '{district}' must be 2 digits"
    if not series.isalpha():
        return False, s, f"Series '{series}' must be 1-2 letters"
    if not digits_part.isdigit():
        return False, s, f"Vehicle number '{digits_part}' must be 4 digits"

    formatted = f"{state} {district} {series} {digits_part}"
    return True, formatted, "Valid"

def main():
    print("=" * 70)
    print("  CSA08 CO2 Q3: TOLL PLAZA VEHICLE REGISTRATION VALIDATOR")
    print("=" * 70)
    print("  Testing input variations without regex (Pure string manipulation):")
    print("─" * 70)

    test_plates = [
        "tn 09 ab 1234",      # lower case with spaces
        "TN-09-AB-1234",      # hyphens
        "Tn09Ab1234",         # mixed case, no delimiter
        "KL 01 Z 9999",       # single letter series
        "TN9AB1234",          # missing district digit -> invalid
        "DL 04 1234",         # missing series -> invalid
        "MH 12 ABCD 1234",    # series too long -> invalid
    ]

    for p in test_plates:
        ok, formatted, reason = validate_registration(p)
        status = "✓ VALID  " if ok else "✗ INVALID"
        print(f"  {p:<17} -> {status} [{formatted:<14}] ({reason})")

    print("=" * 70)

if __name__ == "__main__":
    main()
