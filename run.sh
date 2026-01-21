#!/bin/bash

# ==============================================================================
# [설정] 환경 변수 및 패키지 목록
# ==============================================================================
# 스크립트 실행 중 에러 발생 시 즉시 중단
set -e

# [Windows 호환성] uv 복사 모드 강제
export UV_LINK_MODE=copy

VENV_DIR=".venv"
PYTHON_VERSION="3.12"
OUT_DIR="USB_Lecture_Pack"

# 설치할 Python 라이브러리 목록 (통합 관리)
REQUIREMENTS="numpy matplotlib scipy scikit-dsp-comm diagrams"

# 로그 출력 헬퍼 함수
log() {
    echo -e "\033[1;32m[Info]\033[0m $1"
}

error() {
    echo -e "\033[1;31m[Error]\033[0m $1"
    exit 1
}

# ==============================================================================
# [함수 1] Python 가상환경 감지 및 실행 파일 경로 반환
# ==============================================================================
get_venv_python() {
    if [ -f "$VENV_DIR/Scripts/python" ]; then
        echo "$VENV_DIR/Scripts/python"  # Windows
    elif [ -f "$VENV_DIR/bin/python" ]; then
        echo "$VENV_DIR/bin/python"      # macOS / Linux
    else
        echo ""
    fi
}

# ==============================================================================
# [Step 1] 가상환경 구축 및 라이브러리 설치
# ==============================================================================
setup_environment() {
    log "🚀 [Step 1] Python 가상환경 점검 및 라이브러리 동기화"

    # 1. 가상환경 생성 (없을 경우)
    if [ ! -d "$VENV_DIR" ]; then
        log "   -> 가상환경($VENV_DIR)을 생성합니다..."
        if command -v uv &> /dev/null; then
            uv venv --python $PYTHON_VERSION "$VENV_DIR"
        else
            python3 -m venv "$VENV_DIR"
        fi
    fi

    # 2. Python 실행 경로 확보
    PYTHON=$(get_venv_python)
    if [ -z "$PYTHON" ]; then
        error "가상환경 생성에 실패했거나 Python 실행 파일을 찾을 수 없습니다."
    fi
    log "   -> 사용 중인 Python: $PYTHON"

    # 3. 라이브러리 통합 설치 (항상 최신 상태 유지)
    log "   -> 라이브러리 설치/업데이트 중 ($REQUIREMENTS)..."
    if command -v uv &> /dev/null; then
        uv pip install $REQUIREMENTS
    else
        "$PYTHON" -m pip install $REQUIREMENTS
    fi
}

# ==============================================================================
# [Step 2] 에셋 생성 (Python 스크립트 실행)
# ==============================================================================
generate_assets() {
    log "🎨 [Step 2] 에셋 생성 (Asset Factory)"
    
    # Python 스크립트 실행 (set -e 덕분에 실패 시 여기서 스크립트 자동 종료)
    "$PYTHON" generate_assets.py
}

# ==============================================================================
# [Step 3] 배포 패키지 생성
# ==============================================================================
package_artifacts() {
    log "📦 [Step 3] 강의 배포 패키지 생성 ($OUT_DIR)"

    # 폴더 초기화
    if [ -d "$OUT_DIR" ]; then
        rm -rf "$OUT_DIR"
    fi
    mkdir -p "$OUT_DIR"

    # 기본 파일 복사
    log "   -> Flashcards 및 Assets 복사 중..."
    # 파일 존재 여부 체크 후 복사 (오류 방지)
    [ -f "flashcards.html" ] && cp flashcards.html "$OUT_DIR/"
    [ -f "flashcard_data.js" ] && cp flashcard_data.js "$OUT_DIR/"
    [ -d "assets" ] && cp -r assets "$OUT_DIR/"

    # PDF 수집 및 이름 변경 복사
    log "   -> 챕터별 PDF 수집 중..."
    find slides -name "lecture.pdf" | while read -r pdf_path; do
        # 경로에서 챕터명 추출 (예: slides/02_signals/lecture.pdf -> 02_signals)
        chapter_name=$(basename "$(dirname "$pdf_path")")
        target_path="$OUT_DIR/${chapter_name}.pdf"
        
        cp "$pdf_path" "$target_path"
        echo "      Checking: $chapter_name.pdf (Saved)"
    done
}

# ==============================================================================
# [Main] 실행 진입점
# ==============================================================================
main() {
    setup_environment
    generate_assets
    package_artifacts

    echo "--------------------------------------------------------"
    log "🎉 모든 작업 완료! ($OUT_DIR 폴더 확인)"
    echo "--------------------------------------------------------"
}

# 스크립트 실행
main