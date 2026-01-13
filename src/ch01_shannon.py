import numpy as np
import matplotlib.pyplot as plt
from . import plot_lib as lib  # 기존 라이브러리 활용

def run():
    print("--- [Ch1] Shannon Capacity generating... ---")

    # 1. Data Configuration
    operators = ['SKT', 'KT', 'LGU+', 'Target']
    bandwidths = [100, 100, 100, 120]  # MHz
    snr_db = 20
    
    snr_linear = 10**(snr_db / 10)
    capacities = [(b * 1e6 * np.log2(1 + snr_linear)) / 1e9 for b in bandwidths]

    # 2. Visualization
    # plot_lib가 plt 전역 상태를 사용하므로, 변수에 할당하기보다 plt 조작 후 바로 저장
    fig, ax1 = plt.subplots(figsize=(8, 5))

    # Bar Chart (Bandwidth)
    color_b = 'tab:blue'
    ax1.set_xlabel('Operators')
    ax1.set_ylabel('Bandwidth (MHz)', color=color_b, fontsize=12)
    ax1.bar(operators, bandwidths, color=color_b, alpha=0.6, width=0.5, label='Bandwidth (B)')
    ax1.tick_params(axis='y', labelcolor=color_b)
    ax1.set_ylim(0, 150)

    # Line Chart (Capacity)
    ax2 = ax1.twinx()
    color_c = 'tab:red'
    ax2.set_ylabel('Theoretical Capacity (Gbps)', color=color_c, fontsize=12)
    ax2.plot(operators, capacities, color=color_c, marker='o', linewidth=3, markersize=10, label='Capacity (C)')
    ax2.tick_params(axis='y', labelcolor=color_c)
    ax2.set_ylim(0, max(capacities) * 1.5)

    plt.title('Impact of Bandwidth (B) on Capacity (C)')
    fig.tight_layout()

    # 3. Save Assets (수정된 부분)
    # 기존 plot_lib.save_plot은 인자로 filename만 받습니다. (fig 객체 전달 X)
    # 내부적으로 plt.savefig를 호출하므로 현재 활성화된 figure가 저장됩니다.
    lib.save_plot("fig_ch01_shannon") 
    
    # 4. Return Flashcard Data
    return [
        {
            "front": "What is the Shannon-Hartley equation for Channel Capacity?",
            "back": "C = B * log2(1 + S/N)"
        },
        {
            "front": "Why do telcos prefer increasing Bandwidth (B) over Signal Power (S)?",
            "back": "Capacity increases linearly with B, but only logarithmically with S.",
            "image": "assets/fig_ch01_shannon.svg"
        }
    ]