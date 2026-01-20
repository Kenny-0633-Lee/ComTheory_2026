import numpy as np
import matplotlib.pyplot as plt
from . import plot_lib as lib

def run():
    print("   [Ch02] Generating Lathi Fig 2.1 (No Title)... ", end="", flush=True)
    cards = []

    # -------------------------------------------------------
    # (a) Signal with Finite Energy
    # -------------------------------------------------------
    t_a = np.linspace(-3, 5, 1000)
    energy_signal = 2.5 * np.exp(-(t_a + 0.5)**2 / 1.5)
    
    lib.plot_lathi_signal(t_a, energy_signal, 
                          title=None,  # <--- [수정] 제목 제거
                          filename="fig_ch02_energy_sig", 
                          xlabel="t", ylabel="g(t)",
                          show_ticks=False)

    cards.append({
        "front": "Characteristics of Energy Signals?",
        "back": "Total Energy is finite.\nAverage Power is zero.",
        "image": "assets/fig_ch02_energy_sig.svg"
    })

    # -------------------------------------------------------
    # (b) Signal with Finite Power
    # -------------------------------------------------------
    t_b = np.linspace(-5, 5, 2000)
    power_signal = (0.7 * np.sin(2.3 * t_b) + 
                    0.5 * np.cos(5.1 * t_b + 0.5) + 
                    0.4 * np.sin(8.7 * t_b + 1.0))

    lib.plot_lathi_signal(t_b, power_signal, 
                          title=None,  # <--- [수정] 제목 제거
                          filename="fig_ch02_power_sig", 
                          xlabel="t", ylabel="g(t)",
                          show_ticks=False)

    cards.append({
        "front": "Characteristics of Power Signals?",
        "back": "Total Energy is infinite.\nAverage Power is finite.",
        "image": "assets/fig_ch02_power_sig.svg"
    })

    print("Done!")
    return cards