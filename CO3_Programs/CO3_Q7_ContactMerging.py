"""
CSA08 CO3 - Q7: Contact-Merging Program from First Principles
Merges contacts from multiple sources (Phone 1, Phone 2, SIM).
Normalises phone numbers, picks richest contact name, and unions emails.
"""

def normalise_phone(phone: str) -> str:
    digits = "".join(ch for ch in phone if ch.isdigit())
    if digits.startswith("91") and len(digits) == 12:
        return digits[2:]
    if digits.startswith("0") and len(digits) == 11:
        return digits[1:]
    return digits

def merge_contacts(records: list) -> dict:
    merged = {}
    for r in records:
        phone = normalise_phone(r["phone"])
        if not phone:
            continue
        name = r["name"].strip()
        email = r.get("email", "").strip().lower()

        if phone not in merged:
            merged[phone] = {
                "name": name,
                "phone": phone,
                "emails": {email} if email else set()
            }
        else:
            if len(name) > len(merged[phone]["name"]):
                merged[phone]["name"] = name
            if email:
                merged[phone]["emails"].add(email)
    return merged

def main():
    print("=" * 68)
    print("  CSA08 CO3 Q7: CONTACT MERGING & DEDUPLICATION SYSTEM")
    print("=" * 68)

    raw_input = [
        {"name": "ravi", "phone": "+91 98400 12345", "email": "ravi@gmail.com"},
        {"name": "Dr. Ravi Kumar", "phone": "09840012345", "email": "r.kumar@hospital.org"},
        {"name": "Priya", "phone": "9876543210", "email": "priya@work.com"},
        {"name": "Priya S.", "phone": "+91-98765-43210", "email": "priya_personal@gmail.com"},
    ]

    print("  Incoming Raw Contact Records Across Devices:")
    for item in raw_input:
        print(f"    • {item['name']:<16} | Raw Phone: {item['phone']:<16} | Email: {item['email']}")

    merged = merge_contacts(raw_input)
    print("\n  Consolidated Clean Master Contacts:")
    print("─" * 68)
    for num, data in merged.items():
        emails_str = ", ".join(sorted(list(data["emails"])))
        print(f"    Phone: {num} | Name: {data['name']:<16} | Emails: [{emails_str}]")

    print("=" * 68)

if __name__ == "__main__":
    main()
