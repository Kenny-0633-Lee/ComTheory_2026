import numpy as np
import matplotlib.pyplot as plt
import os

def run():
    print("   [Ch04] Generating FM Time Domain Plot...", end=" ", flush=True)

    t = np.linspace(0, 2, 1000)
    fm = 1.0; fc = 15.0; beta = 10.0

    m_t = np.cos(2 * np.pi * fm * t)
    x_fm = np.cos(2 * np.pi * fc * t + beta * np.sin(2 * np.pi * fm * t))

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

    # Top: Message
    ax1.plot(t, m_t, 'k-', linewidth=2)
    ax1.set_title("Message Signal $m(t)$")
    ax1.set_ylabel("Amplitude")
    ax1.grid(True, alpha=0.3)
    ax1.fill_between(t, m_t, 0, where=(m_t > 0), color='gray', alpha=0.2)

    # Bottom: FM
    ax2.plot(t, x_fm, 'b-', linewidth=1.0)
    ax2.set_title("FM Signal $x_{FM}(t)$ (Accordion Effect)")
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Amplitude")
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(-1.5, 2.2)

    # Annotations
    t_high = 0.0; t_low = 0.5
    ax2.annotate("High Freq", xy=(t_high, 1.2), xytext=(t_high, 1.8),
                 arrowprops=dict(facecolor='red', arrowstyle="->"), ha='center', color='red')
    ax2.annotate("Low Freq", xy=(t_low, 1.2), xytext=(t_low, 1.8),
                 arrowprops=dict(facecolor='green', arrowstyle="->"), ha='center', color='green')

    plt.tight_layout()
    
    # [저장] 3종 세트 생성
    os.makedirs("assets", exist_ok=True)
    base_name = "assets/fig_04_fm_accordion"
    plt.savefig(f"{base_name}.pdf", bbox_inches='tight')
    plt.savefig(f"{base_name}.svg", bbox_inches='tight')
    plt.savefig(f"{base_name}.png", dpi=150, bbox_inches='tight')

    plt.close()
    print("✅ Done")


# import numpy as np
# import matplotlib.pyplot as plt
# import os

# def run():
#     print("   [Ch04] Generating FM Time Domain Plot...", end=" ", flush=True)

#     # 설정
#     t = np.linspace(0, 2, 1000)
#     fm = 1.0  # 메시지 주파수 (1Hz)
#     fc = 15.0 # 반송파 주파수 (15Hz)
#     beta = 10.0 # 변조 지수 (클수록 주파수 변화가 심함)

#     # 1. 메시지 신호 m(t)
#     m_t = np.cos(2 * np.pi * fm * t)

#     # 2. FM 신호 x(t) = cos(2*pi*fc*t + beta*sin(2*pi*fm*t))
#     # 적분(m(t)) -> sin, 그래서 위상항에 sin이 들어감
#     x_fm = np.cos(2 * np.pi * fc * t + beta * np.sin(2 * np.pi * fm * t))

#     # 그래프 그리기 (Subplot 2개)
#     fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

#     # 상단: 메시지 신호
#     ax1.plot(t, m_t, 'k-', linewidth=2)
#     ax1.set_title("Message Signal $m(t)$ (Low Frequency info)")
#     ax1.set_ylabel("Amplitude")
#     ax1.grid(True, alpha=0.3)
    
#     # 메시지가 높은 구간 표시
#     ax1.fill_between(t, m_t, 0, where=(m_t > 0), color='gray', alpha=0.2)

#     # 하단: FM 신호
#     ax2.plot(t, x_fm, 'b-', linewidth=1.0)
#     ax2.set_title("FM Signal $x_{FM}(t)$ (Information is in Frequency)")
#     ax2.set_xlabel("Time (s)")
#     ax2.set_ylabel("Amplitude")
#     ax2.grid(True, alpha=0.3)

#     # 시각적 가이드 (화살표)
#     # 메시지가 높을 때 -> 주파수 높음 (촘촘함)
#     # 메시지가 낮을 때 -> 주파수 낮음 (느슨함)
#     t_high = 0.0 # cos(0)=1 (최대)
#     t_low = 0.5  # cos(pi)=-1 (최소)
    
#     ax2.annotate("High Freq\n(Compressed)", xy=(t_high, 1.2), xytext=(t_high, 1.8),
#                  arrowprops=dict(facecolor='red', arrowstyle="->"), ha='center', color='red')
    
#     ax2.annotate("Low Freq\n(Relaxed)", xy=(t_low, 1.2), xytext=(t_low, 1.8),
#                  arrowprops=dict(facecolor='green', arrowstyle="->"), ha='center', color='green')

#     # Y축 범위 조정 (텍스트 공간 확보)
#     ax2.set_ylim(-1.5, 2.2)

#     plt.tight_layout()
    
#     os.makedirs("assets", exist_ok=True)
#     plt.savefig("assets/fig_04_fm_accordion.png", dpi=150)
#     plt.close()
    
#     print("✅ Done")

# if __name__ == "__main__":
#     run()