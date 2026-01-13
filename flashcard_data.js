const FLASHCARD_DATA = [
  {
    "front": "What is the Shannon-Hartley equation for Channel Capacity?",
    "back": "C = B * log2(1 + S/N)"
  },
  {
    "front": "Why do telcos prefer increasing Bandwidth (B) over Signal Power (S)?",
    "back": "Capacity increases linearly with B, but only logarithmically with S.",
    "image": "assets/fig_ch01_shannon.svg"
  },
  {
    "front": "Definition of Unit Step Function u(t)?",
    "back": "u(t) = 1 for t >= 0, and 0 for t < 0.",
    "image": "assets/fig_ch02_unit_step.svg"
  },
  {
    "front": "Order of operations for x(at - b)?",
    "back": "Shift by b (delay), THEN scale by a (compress). Center: t = b/a.",
    "image": "assets/fig_ch02_operations.svg"
  },
  {
    "front": "Physical meaning of Correlation?",
    "back": "A measure of similarity between two signals (calculated as overlapping area).",
    "image": "assets/fig_ch02_correlation.svg"
  },
  {
    "title": "Shannon's Law & Bandwidth",
    "latex": "C = B \\log_2(1 + \\text{SNR}) \\text{ (B: Bandwidth)}",
    "image": "assets/fig_ch3_5g_spectrum.svg"
  },
  {
    "front": "Expression for AM Signal s(t)?",
    "back": "s(t) = Ac[1 + μ m(t)]cos(ωc t)",
    "image": "assets/fig_ch4_am_time.svg"
  },
  {
    "front": "Bandwidth of Standard AM?",
    "back": "BW = 2 * fm (Twice the message bandwidth)",
    "image": "assets/fig_ch4_am_spec.svg"
  },
  {
    "title": "QPSK Characteristics",
    "latex": "M=4, \\text{ 2 bits/symbol}",
    "image": "assets/fig_ch7_qpsk.svg"
  }
];