import numpy as np
import matplotlib.pyplot as plt
import os

def run():
    print("   [Ch02] Generating Fourier Step Images...", end=" ", flush=True)
    
    # 설정
    T_END = 2.0
    F0 = 1.0
    t = np.linspace(0, T_END, 1000)
    ideal_square = np.sign(np.sin(2 * np.pi * F0 * t))
    
    # 저장할 고조파 단계 (N=1, N=5, N=29)
    steps = [1, 5, 29]
    output_dir = "assets"
    os.makedirs(output_dir, exist_ok=True)

    for max_n in steps:
        # 푸리에 합 계산 (홀수항만)
        current_sum = np.zeros_like(t)
        for n in range(1, max_n + 1, 2):
            term = (4 / (n * np.pi)) * np.sin(2 * np.pi * n * F0 * t)
            current_sum += term
        
        # 그래프 그리기
        plt.figure(figsize=(6, 4))
        plt.plot(t, ideal_square, 'k--', alpha=0.2, label='Ideal')
        plt.plot(t, current_sum, 'b-', linewidth=2, label=f'Approximation (N={max_n})')
        
        plt.title(f"Fourier Series Approximation (N={max_n})")
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.ylim(-1.5, 1.5)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        # 파일 저장
        filename = f"{output_dir}/fourier_step_{max_n}.png"
        plt.savefig(filename, dpi=150)
        plt.close()
        
    print("✅ Done (N=1, 5, 29 saved)")

if __name__ == "__main__":
    run()