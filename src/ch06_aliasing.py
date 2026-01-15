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

# import numpy as np
# import matplotlib.pyplot as plt
# import os

# def run():
#     print("   [Ch06] Generating Aliasing Demo...", end=" ", flush=True)

#     # 설정: 9Hz 신호를 10Hz로 샘플링 (Nyquist 위반: 2*9=18Hz 이상이어야 함)
#     f_sig = 9.0   # 원본 신호 주파수
#     f_s = 10.0    # 샘플링 주파수
#     duration = 1.0
    
#     t_cont = np.linspace(0, duration, 1000) # 연속 시간
#     t_samp = np.arange(0, duration, 1/f_s)  # 샘플링 시간
    
#     # 원본 신호 (cos(2*pi*9*t))
#     y_orig = np.cos(2 * np.pi * f_sig * t_cont)
    
#     # 샘플링된 점들
#     y_samp = np.cos(2 * np.pi * f_sig * t_samp)
    
#     # 알리어싱된 신호 (10Hz - 9Hz = 1Hz 로 보임)
#     f_alias = abs(f_s - f_sig) # 1Hz
#     y_alias = np.cos(2 * np.pi * f_alias * t_cont) # 위상 고려 안 한 단순 주파수 비교용
    
#     plt.figure(figsize=(8, 5))
    
#     # 1. 원본 신호 (흐리게)
#     plt.plot(t_cont, y_orig, 'b-', alpha=0.3, label=f'Original Signal ({f_sig} Hz)')
    
#     # 2. 샘플링 포인트 (점)
#     plt.stem(t_samp, y_samp, linefmt='k:', markerfmt='ko', basefmt=" ", label=f'Samples ({f_s} Hz)')
    
#     # 3. 잘못 복원된 신호 (빨간 점선)
#     plt.plot(t_cont, y_alias, 'r--', linewidth=2, label=f'Aliased Signal ({f_alias} Hz)')
    
#     plt.title("Aliasing Effect: 9Hz Signal Sampled at 10Hz looks like 1Hz")
#     plt.xlabel("Time (s)")
#     plt.ylabel("Amplitude")
#     plt.legend(loc='upper right')
#     plt.grid(True, alpha=0.3)
#     plt.tight_layout()
    
#     os.makedirs("assets", exist_ok=True)
#     plt.savefig("assets/fig_06_aliasing.png", dpi=150)
#     plt.close()
    
#     print("✅ Done")

# if __name__ == "__main__":
#     run()