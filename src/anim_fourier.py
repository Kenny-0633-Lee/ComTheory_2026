import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import os

# ---------------------------------------------------------
# [설정] 애니메이션 파라미터
# ---------------------------------------------------------
FILENAME = "assets/anim_01_square_wave_synthesis.gif" # 저장될 파일명
FRAMES = 30         # 총 프레임 수 (더할 고조파의 개수)
INTERVAL = 400      # 프레임 간 간격 (ms) - 속도 조절
F0 = 1.0            # 기본 주파수 (Hz)
T_END = 2.0         # 시간축 길이 (초)

# ---------------------------------------------------------
# [핵심 이론] 푸리에 급수 항 계산 함수
# ---------------------------------------------------------
def get_harmonic_term(n, t):
    """n번째 고조파(Harmonic) 항을 계산합니다."""
    # 구형파의 푸리에 급수: (4/pi) * sum( (1/n) * sin(2*pi*n*f0*t) ) for odd n
    if n % 2 == 0: return np.zeros_like(t) # 짝수항은 0
    return (4 / (n * np.pi)) * np.sin(2 * np.pi * n * F0 * t)

# ---------------------------------------------------------
# [메인] 애니메이션 생성 및 저장 함수
# ---------------------------------------------------------
def run():
    print(f"🎥 [Animation] Generating Fourier Synthesis GIF ({FILENAME})...")
    
    # 1. 데이터 및 그래프 초기화
    t = np.linspace(0, T_END, 1000)
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 배경: 이상적인 구형파 (회색 점선)
    ideal_square = np.sign(np.sin(2 * np.pi * F0 * t))
    ax.plot(t, ideal_square, 'k--', alpha=0.3, label='Ideal Square Wave')

    # 동적 요소: 현재 더해지는 항(파란색), 누적 합(빨간색)
    line_current, = ax.plot([], [], 'b-', alpha=0.5, linewidth=1.5, label='Current Harmonic Adding')
    line_sum, = ax.plot([], [], 'r-', linewidth=2.5, label='Fourier Sum Approximation')
    
    # 그래프 꾸미기
    ax.set_xlim(0, T_END)
    ax.set_ylim(-1.5, 1.5)
    ax.set_title("Fourier Series: Building a Square Wave from Sines", fontsize=14, fontweight='bold')
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    # 누적 합을 저장할 변수
    current_sum = np.zeros_like(t)
    
    # 2. 애니메이션 초기화 함수 (첫 프레임 직전 상태)
    def init():
        line_current.set_data([], [])
        line_sum.set_data([], [])
        return line_current, line_sum

    # 3. 애니메이션 업데이트 함수 (매 프레임마다 호출됨)
    # frame_idx는 0부터 시작하여 FRAMES-1 까지 증가
    def update(frame_idx):
        nonlocal current_sum
        
        # 이번 프레임에 더할 홀수 고조파 차수 (n = 1, 3, 5, ...)
        n = 2 * frame_idx + 1
        
        # 새로운 고조파 항 계산
        new_term = get_harmonic_term(n, t)
        
        # 누적 합 업데이트
        current_sum += new_term
        
        # 그래프 데이터 업데이트
        line_current.set_data(t, new_term)
        line_sum.set_data(t, current_sum)
        
        # 제목 업데이트 (현재 몇 번째 항까지 더했는지 표시)
        ax.set_title(f"Fourier Synthesis: Summing up to N={n} Harmonic")
        
        return line_current, line_sum

    # 4. 애니메이션 객체 생성
    ani = FuncAnimation(
        fig, update, frames=FRAMES, init_func=init, 
        blit=True, interval=INTERVAL, repeat=True, repeat_delay=2000
    )
    
    # 5. GIF 파일로 저장 (PillowWriter 사용 - 별도 설치 불필요)
    # assets 폴더가 없으면 생성
    os.makedirs(os.path.dirname(FILENAME), exist_ok=True)
    
    writer = PillowWriter(fps=1000//INTERVAL)
    ani.save(FILENAME, writer=writer, dpi=100)
    
    plt.close(fig) # 메모리 해제
    print("✅ Done! Animation saved.")

if __name__ == "__main__":
    # 직접 실행 테스트용
    run()