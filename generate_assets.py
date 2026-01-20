import json
import os
import sys

# [수정] src 패키지에서 모듈 불러오기
# 폴더명(srs) . 파일명(ch04_am) 형식으로 임포트
from src import ch01_shannon, ch02_signals, ch03_spectrum, ch04_am, ch07_digital, fig_network, anim_fourier, ch02_fourier_steps, ch05_eye, ch06_aliasing, ch03_am_shift, ch04_fm_accordion
# ... 기존 import 아래에 추가
from src import ch02_fig2_1  # <--- [NEW] 추가


def main():
    print("🚀 Asset Factory Started (Modular Structure)...")
    
    all_cards = []

    # Ch02 기존 코드 아래에 추가
    if hasattr(ch02_fig2_1, 'run'):
        all_cards.extend(ch02_fig2_1.run())

    # 1. 각 챕터 실행 및 카드 데이터 수집
    # ----------------------------------
    # 각 모듈의 run() 함수 실행
    # [Chapter 01]
    if hasattr(ch01_shannon, 'run'):
        all_cards.extend(ch01_shannon.run())

    # [Chapter 02] 실행 구역
    print("   👉 Running Chapter 02...", end=" ")
    try:
        if hasattr(ch02_signals, 'run'):
            # 여기서 실제 그래프 그리기 함수가 호출됩니다.
            ch02_cards = ch02_signals.run()
            if ch02_cards:
                all_cards.extend(ch02_cards)
            print("✅ Success")
        else:
            print("⚠️ Skipped (No run function)")
    except Exception as e:
        print(f"\n❌ Error in Ch02: {e}")
        import traceback
        traceback.print_exc() # 상세 에러 로그 출력
        
    # --- Ch 02 ---
    if hasattr(ch02_fourier_steps, 'run'):
        ch02_fourier_steps.run()
    # (anim_fourier는 시간 걸리니 필요할 때만 주석 해제하거나 맨 뒤로)


    # # [Chapter 03]
    if hasattr(ch03_spectrum, 'run'):
        all_cards.extend(ch03_spectrum.run())

    # # [Chapter 04]
    if hasattr(ch04_am, 'run'):
        all_cards.extend(ch04_am.run())
    
    # # --- Ch 05 ---
    if hasattr(ch05_eye, 'run'):
        ch05_eye.run()
    
    # # --- Ch 06 ---
    if hasattr(ch06_aliasing, 'run'):
        ch06_aliasing.run()
    
    # 신규 추가될 모듈 실행
    if hasattr(ch03_am_shift, 'run'): ch03_am_shift.run()
    if hasattr(ch04_fm_accordion, 'run'): ch04_fm_accordion.run()
    
    # [Chapter 07]
    if hasattr(ch07_digital, 'run'):
        all_cards.extend(ch07_digital.run())
    # ----------------------------------

    # ----------------------------------
    # [추가] Diagrams (Network) 생성
    # ----------------------------------
    if hasattr(fig_network, 'run'):
        fig_network.run()
    # ----------------------------------
    
    # # -------------------------------------
    # # [추가] 애니메이션 생성 (시간이 좀 걸릴 수 있음)
    # # -------------------------------------
    # if hasattr(anim_fourier, 'run'):
    #     anim_fourier.run()
    # # ----------------------------------

    # 2. 통합 Flashcard 데이터 저장 (root 폴더)
    # [수정] ensure_ascii=False 옵션을 추가하여 한글이 깨지지 않고 그대로 저장되게 함
    js_content = f"const FLASHCARD_DATA = {json.dumps(all_cards, indent=2, ensure_ascii=False)};"
    
    with open("flashcard_data.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    
    print(f"✅ All Done! Generated {len(all_cards)} flashcards.")

if __name__ == "__main__":
    main()