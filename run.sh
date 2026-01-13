#!/bin/bash

# [Windows 호환성] 복사 모드 강제
export UV_LINK_MODE=copy

# ------------------------------------------------------------------
# [설정] 가상환경 및 파이썬 경로 설정
# ------------------------------------------------------------------
VENV_DIR=".venv"

if [ -f "$VENV_DIR/bin/python" ]; then
    PYTHON="$VENV_DIR/bin/python"
elif [ -f "$VENV_DIR/Scripts/python" ]; then
    PYTHON="$VENV_DIR/Scripts/python"
else
    PYTHON="python3"
fi

echo "🚀 [Step 1] Python 가상환경 점검"
if [ ! -d "$VENV_DIR" ]; then
    echo "   -> 가상환경 생성 및 라이브러리 설치..."
    if command -v uv &> /dev/null; then
        uv venv --python 3.12
        uv pip install numpy matplotlib
    else
        python3 -m venv $VENV_DIR
        $PYTHON -m pip install numpy matplotlib
    fi
fi

echo "🎨 [Step 2] 에셋 생성 (Asset Factory)"
$PYTHON generate_assets.py
if [ $? -ne 0 ]; then
    echo "❌ [Error] Python 스크립트 실행 실패!"
    exit 1
fi

echo "📦 [Step 3] 강의 배포 패키지 생성 (USB_Lecture_Pack)"
OUT_DIR="USB_Lecture_Pack"

# 1. 폴더 초기화
rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"

# 2. 웹/퀴즈 파일 복사
echo "   -> Flashcards 및 Assets 복사 중..."
cp flashcards.html "$OUT_DIR/"
cp flashcard_data.js "$OUT_DIR/"
cp -r assets "$OUT_DIR/"

# 3. [핵심] 각 챕터별 PDF 수집 및 이름 변경 복사
# slides 폴더 아래에 있는 모든 lecture.pdf를 찾습니다.
echo "   -> 챕터별 PDF 수집 중..."
count=0

# find 명령어로 slides 폴더 내의 lecture.pdf 파일들을 찾음
find slides -name "lecture.pdf" | while read pdf_path; do
    # pdf_path 예시: slides/ch01_intro/lecture.pdf
    
    # 폴더 이름 추출 (예: ch01_intro)
    chapter_name=$(basename $(dirname "$pdf_path"))
    
    # 복사될 파일명 (예: USB_Lecture_Pack/ch01_intro.pdf)
    target_path="$OUT_DIR/${chapter_name}.pdf"
    
    cp "$pdf_path" "$target_path"
    echo "      Checking: $chapter_name.pdf (Saved)"
    ((count++))
done

echo "--------------------------------------------------------"
echo "🎉 모든 작업 완료! (USB_Lecture_Pack 폴더 확인)"
echo "   ⚠️ 주의: PDF는 자동으로 컴파일되지 않습니다."
echo "      각 챕터 폴더에서 미리 컴파일해둔(lecture.pdf) 파일만 수집됩니다."
echo "--------------------------------------------------------"