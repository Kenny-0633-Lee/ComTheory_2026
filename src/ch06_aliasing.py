import numpy as np
import matplotlib.pyplot as plt
import os

def run():
    print("   [Ch06] Generating Aliasing Demo...", end=" ", flush=True)

    f_sig = 9.0; f_s = 10.0; duration = 1.0
    t_cont = np.linspace(0, duration, 1000)
    t_samp = np.arange(0, duration, 1/f_s)
    
    y_orig = np.cos(2 * np.pi * f_sig * t_cont)
    y_samp = np.cos(2 * np.pi * f_sig * t_samp)
    f_alias = abs(f_s - f_sig)
    y_alias = np.cos(2 * np.pi * f_alias * t_cont)
    
    plt.figure(figsize=(8, 5))
    plt.plot(t_cont, y_orig, 'b-', alpha=0.3, label=f'Original ({f_sig} Hz)')
    plt.stem(t_samp, y_samp, linefmt='k:', markerfmt='ko', basefmt=" ", label=f'Samples ({f_s} Hz)')
    plt.plot(t_cont, y_alias, 'r--', linewidth=2, label=f'Aliased ({f_alias} Hz)')
    
    plt.title("Aliasing Effect: 9Hz Signal Sampled at 10Hz")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # [저장] 3종 세트 생성
    os.makedirs("assets", exist_ok=True)
    base_name = "assets/fig_06_aliasing"
    plt.savefig(f"{base_name}.pdf", bbox_inches='tight')
    plt.savefig(f"{base_name}.svg", bbox_inches='tight')
    plt.savefig(f"{base_name}.png", dpi=150, bbox_inches='tight')

    plt.close()
    print("✅ Done")

