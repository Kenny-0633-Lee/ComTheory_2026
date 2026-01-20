import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os

# 1. Path Settings
ASSET_DIR = "assets"
if not os.path.exists(ASSET_DIR):
    os.makedirs(ASSET_DIR)

# 2. Lathi Textbook Style Settings (Project-Local Fonts)
def set_lathi_style():
    # (1) 기본 설정
    try:
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
    except: pass 
    plt.rcParams['mathtext.fontset'] = 'stixsans'

    # (2) 프로젝트 내장 폰트 로드 (가장 확실한 방법)
    # 현재 스크립트 위치(src) 기준으로 상위 폴더의 fonts/NotoSansKR-Regular.ttf 찾기
    current_dir = os.path.dirname(os.path.abspath(__file__)) # src 폴더
    project_root = os.path.dirname(current_dir)              # 루트 폴더
    font_path = os.path.join(project_root, "fonts", "NotoSansKR-Regular.ttf")
    
    if os.path.exists(font_path):
        try:
            fm.fontManager.addfont(font_path)
            prop = fm.FontProperties(fname=font_path)
            # 로드한 폰트를 최우선 순위로 설정
            plt.rcParams['font.sans-serif'] = [prop.get_name()] + plt.rcParams['font.sans-serif']
            print(f"   -> [Font] Loaded Local Font: {os.path.basename(font_path)}")
        except Exception as e:
            print(f"   -> [Font Error] Failed to load local font: {e}")
    else:
        print(f"   -> [Font Warning] Local font not found at: {font_path}")
        print("      Using system default fonts.")

    # (3) 스타일 상세 설정
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['figure.dpi'] = 150
    plt.rcParams['axes.grid'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['lines.linewidth'] = 1.5

set_lathi_style()

# ... (나머지 그래프 그리는 함수들은 그대로 유지) ...
# plot_lathi_signal, plot_lathi_spectrum, plot_lathi_constellation 등...
# 이 아래 코드는 이전과 동일하므로 생략하지 말고 기존 파일 내용 유지하세요.

# 3. Common Save Function
def save_plot(filename):
    if filename.endswith('.pdf'): filename = filename[:-4]
    plt.savefig(os.path.join(ASSET_DIR, f"{filename}.pdf"), bbox_inches='tight')
    plt.savefig(os.path.join(ASSET_DIR, f"{filename}.svg"), bbox_inches='tight')
    plt.close()
    print(f"   -> 💾 Saved: {filename}")

# 4. [Lathi Style] Continuous Signal (Title Check 추가)
def plot_lathi_signal(t, x, title, filename, color='black', xlabel="t", ylabel=None, show_ticks=True):
    fig, ax = plt.subplots(figsize=(6, 2.5))
    
    ax.plot(t, x, color=color, linewidth=1.5)
    
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
    if not show_ticks:
        ax.set_xticks([])
        ax.set_yticks([])
    
    ax.set_xlabel(xlabel, loc='right', fontsize=11, style='italic')
    if ylabel:
        ax.set_ylabel(ylabel, loc='top', rotation=0, fontsize=11, style='italic')
        
    if title:
        ax.set_title(title, y=1.05, fontsize=12)
        
    ax.grid(False)
    save_plot(filename)

# 5. [Lathi Style] Spectrum (Title Check 추가)
def plot_lathi_spectrum(freqs, values, title, filename, y_label="|X(f)|", show_ticks=True):
    fig, ax = plt.subplots(figsize=(6, 2.5))
    
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    if not show_ticks:
        ax.set_xticks([])
        ax.set_yticks([])

    is_discrete = len(freqs) < 50 
    
    if not is_discrete:
        ax.plot(freqs, values, color='black', linewidth=1.5)
        ax.fill_between(freqs, values, color='gray', alpha=0.2)
    else:
        for f, v in zip(freqs, values):
            if abs(v) > 0.001:
                ax.plot([f, f], [0, v], color='black', linewidth=1.5)
                ax.annotate('', xy=(f, v), xytext=(f, 0),
                            arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
                if show_ticks:
                    ax.text(f, v + (0.1 if v>0 else -0.2), f"{v:.1f}", ha='center', fontsize=9)

    if title:
        ax.set_title(title, y=1.05, fontsize=12)
        
    ax.set_xlabel("f", loc='right', style='italic')
    ax.set_ylabel(y_label, loc='top', rotation=0, style='italic')
    ax.grid(False)
    save_plot(filename)

# 6. [Lathi Style] Constellation (Title Check 추가)
def plot_lathi_constellation(symbols, title, filename, show_ticks=True):
    fig, ax = plt.subplots(figsize=(4, 4))
    
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    if not show_ticks:
        ax.set_xticks([])
        ax.set_yticks([])

    ax.scatter(symbols.real, symbols.imag, color='black', s=80, marker='o')
    
    for s in symbols:
        ax.text(s.real + 0.1, s.imag + 0.1, 
                f"{s.real:.0f}{'+' if s.imag>=0 else ''}{s.imag:.0f}j", fontsize=10)

    if title:
        ax.set_title(title, y=1.05)
        
    ax.set_xlabel("I", loc='right')
    ax.set_ylabel("Q", loc='top', rotation=0)
    ax.set_aspect('equal')
    ax.grid(False)
    save_plot(filename)