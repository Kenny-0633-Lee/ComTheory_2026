import numpy as np
import matplotlib.pyplot as plt
from . import plot_lib as lib

def u(t):
    """ Unit Step Function: u(t) """
    return np.where(t >= 0, 1.0, 0.0)

def tri(t):
    """ Triangle Pulse: 1 - |t| for |t|<1 """
    return np.maximum(0, 1 - np.abs(t))

def run():
    print("   [Ch02] Generating plots... ", end="", flush=True)
    cards = []

    # -------------------------------------------------------
    # 1. Unit Step Function (u(t))
    # -------------------------------------------------------
    t = np.linspace(-2, 2, 500)
    x_step = u(t)
    
    # plot_lib의 함수가 내부적으로 plt.figure를 생성하고 저장까지 수행함
    lib.plot_lathi_signal(t, x_step, 
                         title="Unit Step Function u(t)", 
                         filename="fig_ch02_unit_step", 
                         ylabel="u(t)")
    
    cards.append({
        "front": "Definition of Unit Step Function u(t)?",
        "back": "u(t) = 1 for t >= 0, and 0 for t < 0.",
        "image": "assets/fig_ch02_unit_step.svg"
    })

    # -------------------------------------------------------
    # 2. Signal Operations: x(t) vs x(2t-1)
    # -------------------------------------------------------
    # x(t) = tri(t)
    x_original = tri(t)
    # x(2t - 1) = tri(2t - 1)
    x_transformed = tri(2*t - 1) 

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
    
    # Graph 1: Original
    ax1.plot(t, x_original, 'b-', label='Original x(t)')
    ax1.set_title("Original Signal x(t) = tri(t)")
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.axhline(0, color='black', linewidth=0.5)
    ax1.axvline(0, color='black', linewidth=0.5)
    
    # Graph 2: Transformed
    ax2.plot(t, x_transformed, 'r-', label='Transformed x(2t-1)')
    ax2.set_title("Operation: x(2t - 1) (Shift right by 0.5, then compress by 2)")
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.axvline(0.5, color='green', linestyle=':', label='Center at 0.5')
    ax2.axhline(0, color='black', linewidth=0.5)
    
    plt.tight_layout()
    
    # [수정] lib.save_plot은 현재 활성화된(active) figure를 저장합니다.
    # plt.subplots()로 생성한 fig가 active 상태이므로 바로 호출하면 됩니다.
    lib.save_plot("fig_ch02_operations")
    
    cards.append({
        "front": "Order of operations for x(at - b)?",
        "back": "Shift by b (delay), THEN scale by a (compress). Center: t = b/a.",
        "image": "assets/fig_ch02_operations.svg"
    })

    # -------------------------------------------------------
    # 3. Correlation (Overlap Area)
    # -------------------------------------------------------
    # Signal A: Rectangular pulse shifted
    signal_a = np.where(np.abs(t - 0.5) <= 0.5, 1.0, 0.0) 
    # Signal B: Exponential decay
    signal_b = np.exp(-t) * u(t)
    
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(t, signal_a, label='x(t): Rect', alpha=0.7)
    ax.plot(t, signal_b, label='y(t): Exp Decay', alpha=0.7)
    
    # Overlap visualization
    overlap = np.minimum(signal_a, signal_b)
    ax.fill_between(t, 0, overlap, where=(overlap>0), 
                    color='purple', alpha=0.3, label='Correlation Area')
    
    ax.set_title("Concept of Signal Correlation")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.5)
    
    lib.save_plot("fig_ch02_correlation")

    cards.append({
        "front": "Physical meaning of Correlation?",
        "back": "A measure of similarity between two signals (calculated as overlapping area).",
        "image": "assets/fig_ch02_correlation.svg"
    })

    print("Done! (3 files created)")
    return cards