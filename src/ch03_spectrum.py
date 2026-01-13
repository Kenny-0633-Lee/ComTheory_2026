from . import plot_lib as lib
import matplotlib.pyplot as plt
import numpy as np

def run():
    print("--- [Ch3] Mobile Spectrum Allocation generating... ---")
    
    # 데이터 정의
    carriers = {
        "SKT": "#e11d48", # Red-600
        "KT": "#1e293b",  # Slate-800
        "LG U+": "#db2777" # Pink-500
    }
    
    # 5G Mid-Band (Sub-6) 시각화 예시
    fig, ax = plt.subplots(figsize=(10, 2))
    data = [
        {"carrier": "LG U+", "start": 3.42, "width": 0.1},
        {"carrier": "KT", "start": 3.52, "width": 0.1},
        {"carrier": "SKT", "start": 3.62, "width": 0.1},
    ]
    
    for item in data:
        ax.broken_barh([(item["start"], item["width"])], (0, 1), 
                       facecolors=carriers[item["carrier"]], edgecolor='white')
        ax.text(item["start"] + 0.05, 0.5, item["carrier"], 
                color='white', ha='center', va='center', fontweight='bold')

    ax.set_xlim(3.4, 3.8)
    ax.set_yticks([])
    ax.set_xlabel("Frequency (GHz)")
    ax.set_title("5G Mid-Band Allocation (3.5 GHz)")
    
    lib.save_plot("fig_ch3_5g_spectrum")

    return [
        {
            "title": "Shannon's Law & Bandwidth",
            "latex": "C = B \\log_2(1 + \\text{SNR}) \\text{ (B: Bandwidth)}",
            "image": "assets/fig_ch3_5g_spectrum.svg"
        }
    ]