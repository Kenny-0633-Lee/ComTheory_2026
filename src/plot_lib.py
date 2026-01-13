import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os
import glob
import platform

# 1. Path Settings
ASSET_DIR = "assets"
if not os.path.exists(ASSET_DIR):
    os.makedirs(ASSET_DIR)

# 2. Font Settings
def set_font():
    system_name = platform.system()
    target_fonts = ["Pretendard", "Malgun Gothic", "AppleSDGothicNeo-Regular"]
    
    font_path = None
    for font_name in target_fonts:
        if system_name == "Darwin":
            paths = glob.glob(f"/Users/*/Library/Fonts/*{font_name}*.otf") + \
                    glob.glob(f"/Library/Fonts/*{font_name}*.otf") + \
                    glob.glob(f"/System/Library/Fonts/{font_name}.*")
        else:
            paths = glob.glob(f"C:\\Windows\\Fonts\\*{font_name}*.ttf") + \
                    glob.glob(f"C:\\Users\\*\\AppData\\Local\\Microsoft\\Windows\\Fonts\\*{font_name}*.ttf")
        
        if paths:
            font_path = paths[0]
            break
    
    if font_path:
        try:
            fm.fontManager.addfont(font_path)
            prop = fm.FontProperties(fname=font_path)
            plt.rcParams['font.family'] = prop.get_name()
        except: pass
    else:
        plt.rcParams['font.family'] = 'sans-serif'

    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['figure.dpi'] = 150

set_font()

# 3. Common Save Function
def save_plot(filename):
    if filename.endswith('.pdf'): filename = filename[:-4]
    plt.savefig(os.path.join(ASSET_DIR, f"{filename}.pdf"), bbox_inches='tight')
    plt.savefig(os.path.join(ASSET_DIR, f"{filename}.svg"), bbox_inches='tight')
    plt.close()
    print(f"   -> 💾 Saved: {filename}")

# 4. [Lathi Style] Signal Plot
def plot_lathi_signal(t, x, title, filename, color='#2980b9', xlabel="Time (t)", ylabel="x(t)"):
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(t, x, color=color, linewidth=2)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, linestyle=':', alpha=0.6)
    save_plot(filename)

# 5. [Lathi Style] Spectrum Plot
def plot_lathi_spectrum(freqs, values, title, filename, y_label="|X(f)|"):
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.axhline(0, color='black', linewidth=0.8)
    is_discrete = len(freqs) < 50 
    if not is_discrete:
        ax.plot(freqs, values, color='#c0392b', linewidth=1.5)
        ax.fill_between(freqs, values, color='#c0392b', alpha=0.1)
    else:
        for f, v in zip(freqs, values):
            if abs(v) > 0.001:
                ax.plot([f, f], [0, v], color='#c0392b', linewidth=1.5)
                ax.annotate('', xy=(f, v), xytext=(f, 0),
                            arrowprops=dict(arrowstyle='->', color='#c0392b', lw=1.5))
                ax.text(f, v + (0.1 if v>0 else -0.2), f"{v:.1f}", 
                        ha='center', fontsize=9, color='#333')
    ax.set_title(title)
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel(y_label)
    ax.grid(True, linestyle='--', alpha=0.4)
    save_plot(filename)

# 6. [Lathi Style] Constellation Plot (부활!)
def plot_lathi_constellation(symbols, title, filename):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.axhline(0, color='gray', linewidth=1)
    ax.axvline(0, color='gray', linewidth=1)
    
    # 심볼 찍기
    ax.scatter(symbols.real, symbols.imag, color='#8e44ad', s=100, zorder=5)
    
    # 좌표 텍스트
    for s in symbols:
        ax.text(s.real + 0.1, s.imag + 0.1, 
                f"{s.real:.0f}{'+' if s.imag>=0 else ''}{s.imag:.0f}j", 
                fontsize=9, color='#555')

    ax.set_title(title)
    ax.set_xlabel("In-Phase (I)")
    ax.set_ylabel("Quadrature (Q)")
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_aspect('equal', adjustable='box')
    save_plot(filename)