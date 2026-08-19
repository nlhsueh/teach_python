# 09_digital_filter.py - 數位一階低通濾波器 (Low-Pass Filter) 模擬設計

import numpy as np
import matplotlib.pyplot as plt

class LowPassFilter:
    """ 一階 RC 數位低通濾波器：y[k] = alpha * x[k] + (1 - alpha) * y[k-1] """
    def __init__(self, alpha):
        self.alpha = alpha
        self.y_prev = None

    def filter_value(self, x):
        if self.y_prev is None:
            self.y_prev = x
            return x
        y_curr = self.alpha * x + (1 - self.alpha) * self.y_prev
        self.y_prev = y_curr
        return y_curr

if __name__ == '__main__':
    # 1. 合成一個帶有高頻高斯噪聲的類比正弦波
    t = np.linspace(0, 2.0, 400)
    clean_signal = 10.0 * np.sin(2 * np.pi * 1.5 * t) # 1.5 Hz 乾淨主訊號
    noise = np.random.normal(0, 1.8, len(t))
    noisy_signal = clean_signal + noise

    # 2. 初始化兩個不同強度的濾波器
    lpf_weak = LowPassFilter(alpha=0.2)   # 弱濾波器 (反應快，有些許殘留噪聲)
    lpf_strong = LowPassFilter(alpha=0.05) # 強濾波器 (噪音抑制佳，有輕微相位延遲)

    filtered_weak = []
    filtered_strong = []

    for val in noisy_signal:
        filtered_weak.append(lpf_weak.filter_value(val))
        filtered_strong.append(lpf_strong.filter_value(val))

    print(f"原始訊號標準差 (含雜訊): {np.std(noisy_signal):.4f}")
    print(f"弱濾波後標準差: {np.std(filtered_weak):.4f}")
    print(f"強濾波後標準差: {np.std(filtered_strong):.4f}")

    # 3. 繪製比較圖
    plt.figure(figsize=(12, 6))
    plt.plot(t, noisy_signal, color='gray', alpha=0.5, label='Raw Noisy Signal')
    plt.plot(t, clean_signal, color='black', linewidth=2.5, label='Ideal Signal (1.5 Hz)')
    plt.plot(t, filtered_weak, color='orange', linewidth=1.8, label='LPF Weak (alpha=0.2)')
    plt.plot(t, filtered_strong, color='green', linewidth=2.0, label='LPF Strong (alpha=0.05)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Real-time Digital Low-Pass Filter Simulation')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
