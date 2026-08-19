# 03_fft_signal_analysis.py - 訊號處理與頻域分析 (FFT 快速傅立葉變換)

import numpy as np
import matplotlib.pyplot as plt

# 1. 產生模擬時域訊號
sampling_rate = 1000  # 取樣頻率: 1000 Hz
t = np.linspace(0, 1.0, sampling_rate, endpoint=False) # 1 秒的時間長度

# 合成訊號: 50Hz 正弦波 + 120Hz 正弦波 + 隨機白噪音
pure_signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)
noise = np.random.normal(0, 1.5, len(t)) # 標準差為 1.5 的強噪聲
noisy_signal = pure_signal + noise

# 2. 進行快速傅立葉變換 (FFT)
n = len(t)
fft_result = np.fft.fft(noisy_signal)
fft_freq = np.fft.fftfreq(n, 1 / sampling_rate)

# 取前半段正頻率部分，並計算振幅大小
half_n = n // 2
frequencies = fft_freq[:half_n]
# 振幅標準化
amplitude = np.abs(fft_result[:half_n]) * 2 / n

# 3. 繪製時域與頻域比較圖
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# 時域圖
ax1.plot(t[:200] * 1000, noisy_signal[:200], label='Noisy Signal', color='red', alpha=0.6)
ax1.plot(t[:200] * 1000, pure_signal[:200], label='Pure Signal', color='blue', linewidth=2)
ax1.set_xlabel('Time (ms)')
ax1.set_ylabel('Amplitude')
ax1.set_title('Time Domain Signal (First 200ms)')
ax1.grid(True)
ax1.legend()

# 頻域圖
ax2.plot(frequencies, amplitude, color='purple', linewidth=2)
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Amplitude (Scaled)')
ax2.set_title('Frequency Domain - FFT Analysis (Peaks at 50Hz and 120Hz)')
ax2.set_xlim(0, 250) # 限制觀察頻率範圍在 0 ~ 250 Hz
ax2.grid(True)

plt.tight_layout()
plt.show()
