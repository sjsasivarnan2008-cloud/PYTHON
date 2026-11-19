"""
CSA08 CO2 - Q2: Loops that Count Attempts (Bank Kiosk OTP Verification)
Allows 3 attempts. Blank entries do not consume an attempt.
Locks account on 3 consecutive wrong tries.
"""

def simulate_otp_verification(correct_otp: str, user_entries: list):
    max_attempts = 3
    attempts_used = 0
    account_locked = False

    print("=" * 65)
    print("  CSA08 CO2 Q2: BANK KIOSK OTP ATTEMPT COUNTING LOOP")
    print("=" * 65)
    print(f"  Target Correct OTP: '{correct_otp}' | Maximum Attempts Allowed: {max_attempts}")
    print("─" * 65)

    for entry in user_entries:
        cleaned = entry.strip()
        if not cleaned:
            print(f"  [Input: ''] -> Blank entry ignored. Attempts remaining: {max_attempts - attempts_used}")
            continue

        attempts_used += 1
        if cleaned == correct_otp:
            print(f"  [Input: '{cleaned}'] -> ✓ SUCCESS: OTP Verified on attempt #{attempts_used}!")
            return True
        else:
            remaining = max_attempts - attempts_used
            print(f"  [Input: '{cleaned}'] -> ✗ INCORRECT: Attempt #{attempts_used} failed. Remaining: {remaining}")
            if attempts_used >= max_attempts:
                account_locked = True
                break

    if account_locked:
        print("─" * 65)
        print("  ALERT: Maximum 3 attempts exceeded. ACCOUNT TEMPORARILY LOCKED!")
        return False
    return False

def main():
    # Test scenario with blank space and invalid entries
    test_inputs = ["", "1234", "   ", "5678", "7492"]
    simulate_otp_verification("7492", test_inputs)

    print("\n  Lockout Test Scenario (All Wrong Attempts):")
    lockout_inputs = ["1111", "2222", " ", "3333"]
    simulate_otp_verification("9999", lockout_inputs)
    print("=" * 65)

if __name__ == "__main__":
    main()
