import numpy as np
import matplotlib.pyplot as plt
from . import plot_lib as lib

def run():
    print("--- [Ch4] AM Modulation generating... ---")
    cards = []

    # -----------------------------------------------------------
    # 1. Time Domain Simulation (AM Waveform)
    # -----------------------------------------------------------
    # 설정: Carrier 1kHz, Message 100Hz
    t = np.linspace(0, 0.02, 1000) # 20ms 구간
    fc = 1000 
    fm = 100  
    Ac = 1.0
    mu = 0.8  # 변조지수 (Modulation Index) 0.8

    # 수식: s(t) = Ac * [1 + mu * m(t)] * cos(2*pi*fc*t)
    m_t = np.cos(2 * np.pi * fm * t)
    s_t = Ac * (1 + mu * m_t) * np.cos(2 * np.pi * fc * t)

    # [수정 포인트] lib.plot_time -> lib.plot_lathi_signal 로 변경
    lib.plot_lathi_signal(t, s_t, 
                          title=f"AM Waveform (Index $\\mu={mu}$)", 
                          filename="fig_ch4_am_time",
                          xlabel="Time (s)",
                          ylabel="Amplitude")

    cards.append({
        "front": "Expression for AM Signal s(t)?",
        "back": "s(t) = Ac[1 + \u03BC m(t)]cos(\u03C9c t)", # Unicode for mu, omega
        "image": "assets/fig_ch4_am_time.svg"
    })

    # -----------------------------------------------------------
    # 2. Frequency Domain (Spectrum)
    # -----------------------------------------------------------
    # AM 스펙트럼은 Carrier(fc)와 Sidebands(fc ± fm)에 델타 함수가 뜸
    # Lathi 스타일의 '화살표' 플롯을 활용
    
    freqs = np.array([fc - fm, fc, fc + fm])
    # 크기: Carrier=Ac, Sidebands=Ac*mu/2
    values = np.array([Ac * mu / 2, Ac, Ac * mu / 2])
    
    # [수정 포인트] lib.plot_freq -> lib.plot_lathi_spectrum 으로 변경
    lib.plot_lathi_spectrum(freqs, values, 
                            title="AM Spectrum (Magnitude)", 
                            filename="fig_ch4_am_spec",
                            y_label="|S(f)|")

    cards.append({
        "front": "Bandwidth of Standard AM?",
        "back": "BW = 2 * fm (Twice the message bandwidth)",
        "image": "assets/fig_ch4_am_spec.svg"
    })

    return cards