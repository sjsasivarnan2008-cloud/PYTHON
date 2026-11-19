"""
CSA08 CO5 - Task B4: AI Applications (Sentiment Analysis with Negation & Summarizer)
Analyzes citizen complaints using lexicon sentiment analysis with negation look-behind,
and extracts salient sentences for municipal board review.
"""

POSITIVE_WORDS = {"clean", "fresh", "good", "helpful", "improved", "clear", "safe", "fast"}
NEGATIVE_WORDS = {"smoke", "dust", "bad", "toxic", "burning", "slow", "severe", "pollution", "dirty"}
NEGATORS = {"not", "never", "no", "barely", "hardly"}

def analyze_sentiment(text: str) -> tuple:
    words = text.lower().replace(".", "").replace(",", "").split()
    score = 0
    for idx, w in enumerate(words):
        negated = (idx > 0 and words[idx - 1] in NEGATORS)
        if w in POSITIVE_WORDS:
            score += -1 if negated else 1
        elif w in NEGATIVE_WORDS:
            score += 1 if negated else -1

    label = "Positive" if score > 0 else ("Negative" if score < 0 else "Neutral")
    return label, score

def extractive_summary(sentences: list, top_k: int = 2) -> list:
    keywords = POSITIVE_WORDS | NEGATIVE_WORDS
    scored = []
    for s in sentences:
        hits = sum(1 for w in s.lower().split() if w.strip(".,!") in keywords)
        scored.append((hits, s))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [s[1] for s in scored[:top_k]]

def main():
    print("=" * 68)
    print("  CSA08 CO5 TASK B4: AI SENTIMENT ANALYSIS & EXTRACTIVE SUMMARY")
    print("=" * 68)

    complaints = [
        "Roads are clean and the air is fresh today.",
        "Smoke from the factory, air is bad and toxic.",
        "The response from the pollution desk was not helpful.",
        "Not bad, the air quality improved significantly."
    ]

    print("[1] Sentiment Analysis with Negation Look-Behind:")
    print("─" * 68)
    for c in complaints:
        lbl, sc = analyze_sentiment(c)
        print(f"  \"{c}\"")
        print(f"    -> Classified: {lbl:<8} (Polarity Score: {sc:+d})")

    print("\n[2] Extractive Text Summarization for Executive Action:")
    print("─" * 68)
    summary = extractive_summary(complaints, top_k=2)
    for rank, line in enumerate(summary, start=1):
        print(f"  {rank}. {line}")

    print("=" * 68)

if __name__ == "__main__":
    main()
