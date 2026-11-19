"""
CSA08 CO3 - Q3: Dictionaries (Kisan Call Centre Complaint Analysis)
Counts word frequencies, eliminates stop-words using a set,
and extracts top-k most frequent complaints.
"""

STOP_WORDS = {"the", "is", "at", "which", "on", "not", "high", "and", "in", "to", "for", "a", "of", "were", "from", "too"}

def word_frequencies(complaint_texts: list, stop_set: set) -> dict:
    counts = {}
    for text in complaint_texts:
        clean = text.lower().replace(".", "").replace(",", "").replace("!", "")
        for word in clean.split():
            if word not in stop_set:
                counts[word] = counts.get(word, 0) + 1
    return counts

def top_k(counts: dict, k: int = 5) -> list:
    return sorted(counts.items(), key=lambda item: item[1], reverse=True)[:k]

def main():
    print("=" * 68)
    print("  CSA08 CO3 Q3: KISAN CALL CENTRE COMPLAINT WORD FREQUENCIES")
    print("=" * 68)

    complaints = [
        "Cotton crop damaged due to high price seeds not germinating.",
        "Fertilizer price is too high and seeds received were bad quality.",
        "Paddy harvest delayed. Received damaged seeds from local store."
    ]

    freq = word_frequencies(complaints, STOP_WORDS)
    top_complaints = top_k(freq, 4)

    print("  Analyzed Complaint Records:")
    for c in complaints:
        print(f"    • \"{c}\"")

    print("\n  Top Identified Complaint Keywords (Stop-words removed):")
    print("─" * 68)
    for word, count in top_complaints:
        print(f"    Keyword: {word:<12} | Occurrences: {count}")

    print("=" * 68)

if __name__ == "__main__":
    main()
