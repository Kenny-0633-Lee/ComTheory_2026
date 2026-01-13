import numpy as np
import matplotlib.pyplot as plt
from . import plot_lib as lib

def run():
    print("--- [Ch7] Digital Comm generating... ---")
    cards = []

    # QPSK Symbols: 1+j, -1+j, -1-j, 1-j
    qpsk = np.array([1+1j, -1+1j, -1-1j, 1-1j])
    
    # [수정 포인트] plot_constellation -> plot_lathi_constellation
    lib.plot_lathi_constellation(qpsk, "QPSK Constellation", "fig_ch7_qpsk")

    cards.append({
        "title": "QPSK Characteristics",
        "latex": "M=4, \\text{ 2 bits/symbol}",
        "image": "assets/fig_ch7_qpsk.svg"
    })
    
    return cards


# from . import plot_lib as lib 
# import numpy as np

# def run():
#     print("--- [Ch7] Digital Comm generating... ---")
    
#     # QPSK Constellation
#     qpsk = np.array([1+1j, -1+1j, -1-1j, 1-1j])
#     lib.plot_constellation(qpsk, "QPSK Constellation", "fig_ch7_qpsk")

#     return [
#         { "title": "QPSK 성단도", "latex": "M=4, 2bits/symbol", "image": "assets/fig_ch7_qpsk.svg" }
#     ]

