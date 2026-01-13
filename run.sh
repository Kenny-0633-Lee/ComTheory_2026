#!/bin/bash

# [Windows 호환성] 복사 모드 강제
export UV_LINK_MODE=copy

# ------------------------------------------------------------------
# [설정] 가상환경 이름
# ------------------------------------------------------------------
VENV_DIR=".venv"

echo "🚀 [Step 1] Python 가상환경 점검"
# 1. 가상환경 폴더가 없으면 생성 (이게 가장 먼저 와야 함!)
if [ ! -d "$VENV_DIR" ]; then
    echo "   -> 가상환경 생성 및 라이브러리 설치..."
    if command -v uv &> /dev/null; then
        uv venv --python 3.12
        uv pip install numpy matplotlib
    else
        python3 -m venv $VENV_DIR
        # 가상환경 내의 pip 사용
        if [ -f "$VENV_DIR/bin/python" ]; then
            "$VENV_DIR/bin/python" -m pip install numpy matplotlib
        elif [ -f "$VENV_DIR/Scripts/python" ]; then
            "$VENV_DIR/Scripts/python" -m pip install numpy matplotlib
        fi
    fi
fi

# 2. 실행할 Python 경로 결정 (이제는 무조건 존재함)
if [ -f "$VENV_DIR/bin/python" ]; then
    PYTHON="$VENV_DIR/bin/python"      # Mac/Linux
elif [ -f "$VENV_DIR/Scripts/python" ]; then
    PYTHON="$VENV_DIR/Scripts/python"  # Windows (Git Bash)
else
    echo "❌ 치명적 에러: 가상환경 생성 실패. Python을 찾을 수 없습니다."
    exit 1
fi

echo "   -> 사용 중인 Python: $PYTHON"

echo "🎨 [Step 2] 에셋 생성 (Asset Factory)"
$PYTHON generate_assets.py

if [ $? -ne 0 ]; then
    echo "❌ [Error] Python 스크립트 실행 실패!"
    exit 1
fi

echo "📦 [Step 3] 강의 배포 패키지 생성 (USB_Lecture_Pack)"
OUT_DIR="USB_Lecture_Pack"

# 폴더 초기화 및 복사
rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"

echo "   -> Flashcards 및 Assets 복사 중..."
cp flashcards.html "$OUT_DIR/"
cp flashcard_data.js "$OUT_DIR/"
cp -r assets "$OUT_DIR/"

echo "   -> 챕터별 PDF 수집 중..."
# PDF 수집 로직 (파일명에 공백이 있어도 안전하도록 따옴표 처리)
find slides -name "lecture.pdf" | while read -r pdf_path; do
    chapter_name=$(basename "$(dirname "$pdf_path")")
    target_path="$OUT_DIR/${chapter_name}.pdf"
    cp "$pdf_path" "$target_path"
    echo "      Checking: $chapter_name.pdf (Saved)"
done

echo "--------------------------------------------------------"
echo "🎉 모든 작업 완료! (USB_Lecture_Pack 폴더 확인)"
echo "--------------------------------------------------------"