"""
CSA08 – CO5 Assignment: Data Acquisition, Cleaning, SQLite, Visualization & AI
------------------------------------------------------------------------------
Covers:
  Part A & B1: CSV Data Cleaning & Min-Max Normalisation
  B2: SQLite Storage with Parameterized Queries & SQL Injection Immunity
  B3: Matplotlib Multi-Panel Visualizations (Line, Bar, Scatter, Histogram)
  B4: AI Applications:
      - Lexicon Sentiment Analysis with Negation Handling
      - Extractive Text Summarization
      - Air Quality Query Chatbot
"""

import os
import csv
import sqlite3
import shutil
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for automated environments
import matplotlib.pyplot as plt
import numpy as np

# ═════════════════════════════════════════════════════════════════
# 1. Data Cleaning & Normalisation Pipeline
# ═════════════════════════════════════════════════════════════════
def clean_air_quality_data(csv_text: str) -> list:
    """
    Cleans raw CSV air quality records:
      - Filters out missing ('NA', blank) PM2.5
      - Rejects sensor faults (negative values or PM2.5 > 500)
      - Converts Fahrenheit temperatures to Celsius if temp > 55
    """
    reader = csv.DictReader(csv_text.strip().splitlines())
    cleaned_rows = []

    for row in reader:
        station = row["station"].strip()
        date_str = row["date"].strip()
        raw_pm25 = row.get("pm25", "").strip()
        raw_temp = row.get("temperature", "").strip()

        # Check for missing values
        if not raw_pm25 or raw_pm25.upper() == "NA":
            continue

        try:
            pm25 = float(raw_pm25)
            if pm25 < 0.0 or pm25 > 500.0:  # Sensor fault
                continue
        except ValueError:
            continue

        # Temperature handling
        temp_c = 28.0  # default reasonable ambient temp
        if raw_temp and raw_temp.upper() != "NA":
            try:
                t = float(raw_temp)
                if t > 55.0:  # Recorded in Fahrenheit!
                    temp_c = round((t - 32.0) * 5.0 / 9.0, 1)
                else:
                    temp_c = t
            except ValueError:
                pass

        cleaned_rows.append({
            "station": station,
            "date": date_str,
            "pm25": pm25,
            "temperature": temp_c
        })

    return cleaned_rows


def min_max_normalize(values: list) -> list:
    """Min-Max normalization scales values into [0.0, 1.0]."""
    if not values:
        return []
    min_v = min(values)
    max_v = max(values)
    if min_v == max_v:
        return [0.0 for _ in values]
    return [round((v - min_v) / (max_v - min_v), 3) for v in values]


# ═════════════════════════════════════════════════════════════════
# 2. SQLite Database & SQL Injection Defense
# ═════════════════════════════════════════════════════════════════
def setup_sqlite_database(cleaned_records: list) -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            station TEXT NOT NULL,
            reading_date TEXT NOT NULL,
            pm25 REAL NOT NULL,
            temperature REAL NOT NULL
        )
    """)

    insert_sql = "INSERT INTO readings (station, reading_date, pm25, temperature) VALUES (?, ?, ?, ?)"
    rows = [(r["station"], r["date"], r["pm25"], r["temperature"]) for r in cleaned_records]
    cursor.executemany(insert_sql, rows)
    conn.commit()
    return conn


def get_station_average(conn: sqlite3.Connection, station_name: str):
    """Safe parameterized query using '?' placeholder."""
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(pm25) FROM readings WHERE station = ?", (station_name,))
    row = cursor.fetchone()
    return round(row[0], 2) if (row and row[0] is not None) else None


# ═════════════════════════════════════════════════════════════════
# 3. Matplotlib Visualizations (4 Subplots)
# ═════════════════════════════════════════════════════════════════
def generate_air_quality_charts(cleaned_data: list, output_image_path: str):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("City Air-Quality Monitoring Network – CSA08 CO5 Analysis", fontsize=16, fontweight="bold")

    # 1. PM2.5 Daily Trend Line Chart
    ax1 = axes[0, 0]
    dates = sorted(list({r["date"] for r in cleaned_data}))
    adyar_vals = [r["pm25"] for r in cleaned_data if r["station"] == "Adyar"]
    guindy_vals = [r["pm25"] for r in cleaned_data if r["station"] == "Guindy"]

    ax1.plot(range(len(adyar_vals)), adyar_vals, marker="o", color="#1f77b4", label="Adyar", linewidth=2)
    if guindy_vals:
        ax1.plot(range(len(guindy_vals)), guindy_vals, marker="s", color="#d62728", label="Guindy", linewidth=2)
    ax1.axhline(60, color="orange", linestyle="--", label="Safe Limit (60 µg/m³)")
    ax1.set_title("PM2.5 Daily Trend (Line Chart)", fontweight="bold")
    ax1.set_xlabel("Day Index")
    ax1.set_ylabel("PM2.5 (µg/m³)")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # 2. Station Comparison Bar Chart
    ax2 = axes[0, 1]
    station_stats = {}
    for r in cleaned_data:
        st = r["station"]
        station_stats.setdefault(st, []).append(r["pm25"])
    
    stations = list(station_stats.keys())
    means = [np.mean(station_stats[s]) for s in stations]
    colors = ["#2ca02c" if m <= 60 else "#d62728" for m in means]

    bars = ax2.bar(stations, means, color=colors, width=0.5, edgecolor="black")
    ax2.axhline(60, color="orange", linestyle="--", label="Safe Limit")
    ax2.set_title("Average PM2.5 by Station (Bar Chart)", fontweight="bold")
    ax2.set_ylabel("Mean PM2.5 (µg/m³)")
    for b in bars:
        ax2.text(b.get_x() + b.get_width()/2., b.get_height() + 1.5, f"{b.get_height():.1f}", ha="center", fontweight="bold")
    ax2.grid(True, axis="y", alpha=0.3)

    # 3. Temperature vs PM2.5 Scatter Plot
    ax3 = axes[1, 0]
    temps = [r["temperature"] for r in cleaned_data]
    pm25s = [r["pm25"] for r in cleaned_data]
    ax3.scatter(temps, pm25s, color="#9467bd", alpha=0.8, edgecolors="k", s=60)
    ax3.set_title("Temperature vs PM2.5 (Scatter Plot)", fontweight="bold")
    ax3.set_xlabel("Temperature (°C)")
    ax3.set_ylabel("PM2.5 (µg/m³)")
    ax3.grid(True, alpha=0.3)

    # 4. PM2.5 Distribution Histogram
    ax4 = axes[1, 1]
    ax4.hist(pm25s, bins=8, color="#17becf", edgecolor="black", alpha=0.7)
    ax4.set_title("PM2.5 Pollution Distribution (Histogram)", fontweight="bold")
    ax4.set_xlabel("PM2.5 Concentration Range")
    ax4.set_ylabel("Frequency of Readings")
    ax4.grid(True, axis="y", alpha=0.3)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(output_image_path, dpi=200)
    plt.close()
    print(f"Air quality visualization saved to: {output_image_path}")


# ═════════════════════════════════════════════════════════════════
# 4. AI Applications: Sentiment, Summarizer & Chatbot
# ═════════════════════════════════════════════════════════════════
POSITIVE_WORDS = {"clean", "good", "fresh", "fast", "helpful", "improved", "clear", "safe", "healthy"}
NEGATIVE_WORDS = {"smoke", "dust", "bad", "cough", "dirty", "smell", "hazardous", "burning", "slow", "severe", "pollution"}
NEGATORS = {"not", "never", "no", "hardly", "barely"}

def analyze_sentiment(text: str) -> dict:
    """
    Lexicon sentiment scorer with negation look-behind:
      - 'not helpful' -> negative
      - 'not bad' -> positive
    """
    words = text.lower().replace(".", "").replace(",", "").split()
    score = 0
    i = 0
    while i < len(words):
        w = words[i]
        is_negated = (i > 0 and words[i - 1] in NEGATORS)

        if w in POSITIVE_WORDS:
            score += -1 if is_negated else 1
        elif w in NEGATIVE_WORDS:
            score += 1 if is_negated else -1
        i += 1

    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {"text": text, "score": score, "sentiment": sentiment}


def extractive_summarize(complaints: list, top_n: int = 2) -> list:
    """Extracts top N most representative sentences based on keyword prominence."""
    keywords = POSITIVE_WORDS | NEGATIVE_WORDS
    scored_sentences = []

    for comp in complaints:
        words = comp.lower().split()
        match_count = sum(1 for w in words if w.strip(".,!") in keywords)
        scored_sentences.append((match_count, comp))

    scored_sentences.sort(key=lambda x: x[0], reverse=True)
    return [s[1] for s in scored_sentences[:top_n]]


def rule_based_chatbot(query: str, conn: sqlite3.Connection) -> str:
    """Keyword-driven query assistant for citizen air quality inquiries."""
    q_lower = query.lower()

    # Detect station query
    stations = ["adyar", "guindy", "velachery", "anna nagar", "t nagar"]
    found_station = None
    for s in stations:
        if s in q_lower:
            found_station = s.title()
            break

    if "pm2.5" in q_lower or "pm25" in q_lower or "air quality" in q_lower or "pollution" in q_lower:
        if found_station:
            avg = get_station_average(conn, found_station)
            if avg:
                status = "Satisfactory" if avg <= 60 else "Poor / Moderate"
                return f"The current average PM2.5 in {found_station} is {avg} µg/m³ ({status})."
            else:
                return f"Sorry, no monitoring data available for {found_station}."
        else:
            return "Please specify which station you want to check (e.g., Adyar, Guindy, Velachery)."
    elif "hello" in q_lower or "hi" in q_lower:
        return "Hello! I am the City Air-Quality Assistant. You can ask me about PM2.5 levels at various monitoring stations."
    else:
        return "I can answer questions regarding air quality and PM2.5 levels at city stations."


# ═════════════════════════════════════════════════════════════════
# Demonstration Runner
# ═════════════════════════════════════════════════════════════════
def run_co5_suite():
    print("=" * 70)
    print("   CSA08 CO5: DATA ACQUISITION, CLEANING, SQLITE, VIZ & AI")
    print("=" * 70)

    # 1. Clean Data
    raw_csv = """station,date,pm25,temperature
Adyar,2026-10-01,48.0,86.0
Adyar,2026-10-02,54.0,29.5
Adyar,2026-10-03,NA,30.0
Adyar,2026-10-04,,31.0
Adyar,2026-10-05,62.0,28.0
Guindy,2026-10-01,95.0,29.0
Guindy,2026-10-02,-5.0,29.5
Guindy,2026-10-03,121.0,89.6
Guindy,2026-10-04,108.0,32.0
Velachery,2026-10-01,42.0,27.5
Velachery,2026-10-02,51.0,28.0
Velachery,2026-10-03,45.0,28.5
"""
    cleaned = clean_air_quality_data(raw_csv)
    print(f"\n[1. Cleaning Pipeline] Raw rows: 12 -> Valid clean rows: {len(cleaned)}")
    print(f"  Sample cleaned records:")
    for r in cleaned[:4]:
        print(f"    • {r['station']:<10} | Date: {r['date']} | PM2.5: {r['pm25']:5.1f} | Temp: {r['temperature']}°C")

    # Normalization
    pm_vals = [r["pm25"] for r in cleaned]
    norm_vals = min_max_normalize(pm_vals)
    print(f"\n[Min-Max Normalisation (0.0 to 1.0)]:")
    print(f"  Original PM2.5 sample   : {pm_vals[:5]}")
    print(f"  Normalized values sample: {norm_vals[:5]}")

    # 2. SQLite Database
    conn = setup_sqlite_database(cleaned)
    print("\n[2. SQLite Database & SQL Injection Defense]:")
    print(f"  Adyar Average PM2.5     : {get_station_average(conn, 'Adyar')} µg/m³")
    print(f"  Guindy Average PM2.5    : {get_station_average(conn, 'Guindy')} µg/m³")
    print(f"  Velachery Average PM2.5 : {get_station_average(conn, 'Velachery')} µg/m³")
    # Injection attempt
    malicious_input = "Adyar' OR '1'='1"
    safe_result = get_station_average(conn, malicious_input)
    print(f"  SQL Injection Attempt ('{malicious_input}'): Result = {safe_result} (Safely Neutralized!)")

    # 3. Visualizations
    chart_file = os.path.abspath("co5_air_quality_charts.png")
    generate_air_quality_charts(cleaned, chart_file)
    # Copy to artifact dir
    artifact_dir = r"C:\Users\Admin\.gemini\antigravity\brain\e9202e20-2e2c-4aeb-91f6-e707a8e7894b"
    if os.path.exists(artifact_dir):
        shutil.copyfile(chart_file, os.path.join(artifact_dir, "co5_air_quality_charts.png"))

    # 4. AI Applications
    print("\n[4. AI Applications]:")
    print("─── A. Sentiment Analysis with Negation Handling ───")
    test_complaints = [
        "Roads are clean and the air is fresh today.",
        "Smoke from the factory, air is bad and toxic.",
        "The response from the pollution desk was not helpful.",
        "Not bad, the air quality improved significantly."
    ]
    for comp in test_complaints:
        res = analyze_sentiment(comp)
        print(f"  '{comp}'")
        print(f"    → Sentiment: {res['sentiment']} (Score: {res['score']:+d})")

    print("\n─── B. Extractive Text Summarization ───")
    summary = extractive_summarize(test_complaints, top_n=2)
    print(f"  Key Extracted Complaints for Executive Action:")
    for s in summary:
        print(f"    • {s}")

    print("\n─── C. Air Quality Query Chatbot ───")
    sample_queries = [
        "Hi there!",
        "What is the PM2.5 in Adyar today?",
        "Tell me about the pollution in Guindy",
        "How is the weather?"
    ]
    for q in sample_queries:
        bot_reply = rule_based_chatbot(q, conn)
        print(f"  User: '{q}'")
        print(f"  Bot : {bot_reply}")

    print("=" * 70)


if __name__ == "__main__":
    run_co5_suite()
