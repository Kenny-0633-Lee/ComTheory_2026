import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def run():
    print("   [Ch03] Generating AM Frequency Shift Plot...", end=" ", flush=True)

    fig, ax = plt.subplots(figsize=(8, 4))
    
    # 1. Baseband Signal
    baseband_x = [-1, 0, 1]
    baseband_y = [0, 1, 0]
    ax.add_patch(patches.Polygon(list(zip(baseband_x, baseband_y)), closed=True, 
                                 facecolor='gray', alpha=0.5, edgecolor='black', label='Baseband m(t)'))
    
    # 2. Modulated Signal
    fc = 4
    # Positive Freq
    mod_pos_x = [fc-1, fc, fc+1]
    mod_pos_y = [0, 0.5, 0]
    ax.add_patch(patches.Polygon(list(zip(mod_pos_x, mod_pos_y)), closed=True, 
                                 facecolor='tab:red', alpha=0.6, edgecolor='red', label='Modulated x(t)'))
    # Negative Freq
    mod_neg_x = [-fc-1, -fc, -fc+1]
    mod_neg_y = [0, 0.5, 0]
    ax.add_patch(patches.Polygon(list(zip(mod_neg_x, mod_neg_y)), closed=True, 
                                 facecolor='tab:red', alpha=0.6, edgecolor='red'))

    # 3. Annotations
    ax.annotate("", xy=(fc, 0.25), xytext=(1.2, 0.5),
                arrowprops=dict(arrowstyle="->", linestyle="dashed", color='blue'))
    ax.text(2.0, 0.4, "Shift by $f_c$", color='blue', fontsize=10)

    ax.set_xlim(-6, 6)
    ax.set_ylim(0, 1.2)
    ax.set_xlabel("Frequency (f)")
    ax.set_ylabel("Magnitude |X(f)|")
    ax.set_title("Modulation Theorem: Frequency Shifting")
    ax.set_xticks([-fc, 0, fc])
    ax.set_xticklabels(['$-f_c$', '$0$', '$+f_c$'])
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right')
    
    # [저장] 3종 세트 생성
    os.makedirs("assets", exist_ok=True)
    base_name = "assets/fig_03_am_shift"
    plt.savefig(f"{base_name}.pdf", bbox_inches='tight')
    plt.savefig(f"{base_name}.svg", bbox_inches='tight')
    plt.savefig(f"{base_name}.png", dpi=150, bbox_inches='tight')
    
    plt.close()
    print("✅ Done")
    

import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# import os

# def run():
#     print("   [Ch03] Generating AM Frequency Shift Plot...", end=" ", flush=True)

#     fig, ax = plt.subplots(figsize=(8, 4))
    
#     # -----------------------------------------------------
#     # 1. Baseband Signal (원래 신호) - 중심이 0
#     # -----------------------------------------------------
#     # 삼각형 그리기 (x, y 좌표)
#     baseband_x = [-1, 0, 1]
#     baseband_y = [0, 1, 0]
    
#     # fill_between이나 Polygon으로 채우기
#     ax.add_patch(patches.Polygon(list(zip(baseband_x, baseband_y)), closed=True, 
#                                  facecolor='gray', alpha=0.5, edgecolor='black', label='Baseband Message m(t)'))
    
#     # -----------------------------------------------------
#     # 2. Modulated Signal (이사간 신호) - 중심이 +fc, -fc
#     # -----------------------------------------------------
#     fc = 4 # 반송파 주파수 위치
    
#     # Positive Frequency (+fc)
#     mod_pos_x = [fc-1, fc, fc+1]
#     mod_pos_y = [0, 0.5, 0] # 진폭은 절반으로 줄어듦 (1/2 M(f-fc))
#     ax.add_patch(patches.Polygon(list(zip(mod_pos_x, mod_pos_y)), closed=True, 
#                                  facecolor='tab:red', alpha=0.6, edgecolor='red', label='Modulated Signal x(t)'))

#     # Negative Frequency (-fc)
#     mod_neg_x = [-fc-1, -fc, -fc+1]
#     mod_neg_y = [0, 0.5, 0]
#     ax.add_patch(patches.Polygon(list(zip(mod_neg_x, mod_neg_y)), closed=True, 
#                                  facecolor='tab:red', alpha=0.6, edgecolor='red'))

#     # -----------------------------------------------------
#     # 3. 꾸미기 (화살표 및 텍스트)
#     # -----------------------------------------------------
#     # 이동 화살표
#     ax.annotate("", xy=(fc, 0.25), xytext=(1.2, 0.5),
#                 arrowprops=dict(arrowstyle="->", linestyle="dashed", color='blue'))
#     ax.text(2.0, 0.4, "Shift by $f_c$", color='blue', fontsize=10)

#     # 축 설정
#     ax.set_xlim(-6, 6)
#     ax.set_ylim(0, 1.2)
#     ax.set_xlabel("Frequency (f)")
#     ax.set_ylabel("Magnitude |X(f)|")
#     ax.set_title("Modulation Theorem: Frequency Shifting")
    
#     # X축 눈금 커스텀
#     ax.set_xticks([-fc, 0, fc])
#     ax.set_xticklabels(['$-f_c$', '$0$', '$+f_c$'])
    
#     ax.grid(True, alpha=0.3)
#     ax.legend(loc='upper right')
    
#     os.makedirs("assets", exist_ok=True)
#     plt.savefig("assets/fig_03_am_shift.png", dpi=150)
#     plt.close()
    
#     print("✅ Done")

# if __name__ == "__main__":
#     run()
    
    