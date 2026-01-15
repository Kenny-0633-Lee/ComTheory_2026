import numpy as np
import matplotlib.pyplot as plt
import os

def run():
    print("   [Ch05] Generating Eye Diagram...", end=" ", flush=True)

    # 파라미터
    num_bits = 500
    samples_per_symbol = 50
    noise_level = 0.2
    
    bits = 2 * (np.random.randint(0, 2, num_bits) - 0.5)
    signal = np.repeat(bits, samples_per_symbol)
    filter_window = np.ones(samples_per_symbol) / samples_per_symbol
    smooth_signal = np.convolve(signal, filter_window, mode='same')
    received_signal = smooth_signal + np.random.normal(0, noise_level, len(smooth_signal))
    
    plt.figure(figsize=(8, 5))
    
    trace_len = samples_per_symbol * 2
    num_traces = (len(received_signal) // samples_per_symbol) - 2
    t_axis = np.linspace(-1, 1, trace_len)

    # 수많은 선 그리기
    for i in range(num_traces):
        start_idx = i * samples_per_symbol
        segment = received_signal[start_idx : start_idx + trace_len]
        if len(segment) == trace_len:
            # SVG 용량 최적화를 위해 alpha값과 선 굵기를 조절
            plt.plot(t_axis, segment, color='tab:blue', alpha=0.05, linewidth=0.5)
            
    plt.title(f"Eye Diagram (Noise Level = {noise_level})")
    plt.xlabel("Time (Symbol Periods)")
    plt.ylabel("Amplitude")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # [저장] 3종 세트 생성
    # Eye Diagram은 복잡하므로 PDF/SVG 생성 시 시간이 조금 더 걸릴 수 있습니다.
    os.makedirs("assets", exist_ok=True)
    base_name = "assets/fig_05_eye_diagram"
    
    # PDF/SVG에 rasterized=True를 쓰면 데이터 부분만 비트맵 처리되어 가볍고 빨라집니다.
    # 하지만 완전한 벡터를 원하시면 rasterized 옵션을 빼셔도 됩니다. (여기선 뺍니다)
    plt.savefig(f"{base_name}.pdf", bbox_inches='tight') 
    plt.savefig(f"{base_name}.svg", bbox_inches='tight')
    plt.savefig(f"{base_name}.png", dpi=300, bbox_inches='tight') # PNG는 고화질로
    
    plt.close()
    print("✅ Done")


# import numpy as np
# import matplotlib.pyplot as plt
# import os

# def run():
#     print("   [Ch05] Generating Eye Diagram...", end=" ", flush=True)

#     # 설정
#     num_bits = 500
#     samples_per_symbol = 50
#     noise_level = 0.2  # 잡음 강도 (0.0: 깨끗, 0.2: 약간 지저분)
    
#     # 1. 랜덤 비트 생성 (-1, 1)
#     bits = 2 * (np.random.randint(0, 2, num_bits) - 0.5)
    
#     # 2. 펄스 성형 (Pulse Shaping) - 간단한 RC 필터 효과 시뮬레이션
#     # (급격하게 변하지 않고 부드럽게 변하도록 하여 ISI 유발)
#     signal = np.repeat(bits, samples_per_symbol)
    
#     # 스무딩 (Low-pass filter 효과)
#     filter_window = np.ones(samples_per_symbol) / samples_per_symbol
#     smooth_signal = np.convolve(signal, filter_window, mode='same')
    
#     # 3. 잡음 추가
#     noise = np.random.normal(0, noise_level, len(smooth_signal))
#     received_signal = smooth_signal + noise
    
#     # 4. 아이 다이어그램 그리기 (신호를 2심볼 주기로 잘라서 겹쳐 그리기)
#     plt.figure(figsize=(8, 5))
    
#     # 2주기(2 Symbols) 길이로 잘라서 겹치기
#     trace_len = samples_per_symbol * 2
#     num_traces = (len(received_signal) // samples_per_symbol) - 2
    
#     t_axis = np.linspace(-1, 1, trace_len) # 시간축 (Symbol Period)

#     for i in range(num_traces):
#         start_idx = i * samples_per_symbol
#         segment = received_signal[start_idx : start_idx + trace_len]
#         if len(segment) == trace_len:
#             # 투명도(alpha)를 낮게 주어 겹치는 효과 극대화
#             plt.plot(t_axis, segment, color='tab:blue', alpha=0.05)
            
#     plt.title(f"Eye Diagram (Noise Level = {noise_level})")
#     plt.xlabel("Time (Symbol Periods)")
#     plt.ylabel("Amplitude")
#     plt.grid(True, alpha=0.3)
#     plt.tight_layout()
    
#     os.makedirs("assets", exist_ok=True)
#     plt.savefig("assets/fig_05_eye_diagram.png", dpi=150)
#     plt.close()
    
#     print("✅ Done")

# if __name__ == "__main__":
#     run()
