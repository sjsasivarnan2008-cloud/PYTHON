"""
CSA08 CO5 - Task B3: Multi-Panel Matplotlib Air Quality Visualizations
Produces line, bar, scatter, and histogram plots from environmental telemetry.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def generate_dashboard(output_path: str):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("City Air-Quality Monitoring Dashboard (CSA08 CO5)", fontsize=16, fontweight="bold")

    days = [f"Day {i}" for i in range(1, 8)]
    adyar = [45, 52, 58, 62, 49, 44, 48]
    guindy = [92, 105, 118, 98, 110, 115, 102]

    # Line Chart
    ax1 = axes[0, 0]
    ax1.plot(days, adyar, marker="o", color="#1f77b4", label="Adyar", linewidth=2)
    ax1.plot(days, guindy, marker="s", color="#d62728", label="Guindy", linewidth=2)
    ax1.axhline(60, color="orange", linestyle="--", label="Safe Threshold (60 µg/m³)")
    ax1.set_title("PM2.5 Daily Trend (Line Chart)", fontweight="bold")
    ax1.set_ylabel("PM2.5 (µg/m³)")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Bar Chart
    ax2 = axes[0, 1]
    stations = ["Adyar", "Guindy", "Velachery", "T Nagar"]
    means = [51.1, 108.6, 42.4, 76.5]
    colors = ["#2ca02c" if m <= 60 else "#d62728" for m in means]
    bars = ax2.bar(stations, means, color=colors, edgecolor="black", width=0.5)
    ax2.axhline(60, color="orange", linestyle="--")
    ax2.set_title("Station Mean Comparison (Bar Chart)", fontweight="bold")
    ax2.set_ylabel("Mean PM2.5 (µg/m³)")
    for b in bars:
        ax2.text(b.get_x() + b.get_width()/2., b.get_height() + 1.5, f"{b.get_height():.1f}", ha="center", fontweight="bold")
    ax2.grid(True, axis="y", alpha=0.3)

    # Scatter Plot
    ax3 = axes[1, 0]
    temps = [28.0, 29.5, 31.0, 32.5, 27.5, 30.0, 33.0, 26.5]
    pm25s = [48, 55, 68, 95, 42, 60, 112, 38]
    ax3.scatter(temps, pm25s, color="#9467bd", edgecolors="k", s=70)
    ax3.set_title("Temperature vs PM2.5 (Scatter Plot)", fontweight="bold")
    ax3.set_xlabel("Temperature (°C)")
    ax3.set_ylabel("PM2.5 (µg/m³)")
    ax3.grid(True, alpha=0.3)

    # Histogram
    ax4 = axes[1, 1]
    all_pm = [42, 45, 48, 49, 52, 55, 58, 62, 76, 92, 95, 98, 102, 105, 110, 115, 118]
    ax4.hist(all_pm, bins=7, color="#17becf", edgecolor="black", alpha=0.7)
    ax4.set_title("Pollution Distribution (Histogram)", fontweight="bold")
    ax4.set_xlabel("PM2.5 Range (µg/m³)")
    ax4.set_ylabel("Frequency Count")
    ax4.grid(True, axis="y", alpha=0.3)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(output_path, dpi=200)
    plt.close()

def main():
    print("=" * 68)
    print("  CSA08 CO5 TASK B3: AIR QUALITY MATPLOTLIB VISUALIZATIONS")
    print("=" * 68)
    out_img = os.path.abspath("co5_air_quality_charts.png")
    generate_dashboard(out_img)
    print(f"  Successfully rendered 4-panel environmental dashboard:")
    print(f"    1. PM2.5 Daily Trend (Line Chart)")
    print(f"    2. Station Average Pollution (Bar Chart)")
    print(f"    3. Temperature vs PM2.5 Correlation (Scatter Plot)")
    print(f"    4. PM2.5 Distribution Profile (Histogram)")
    print(f"  Saved Image: {out_img} ({os.path.getsize(out_img):,} bytes)")
    print("=" * 68)

if __name__ == "__main__":
    main()
