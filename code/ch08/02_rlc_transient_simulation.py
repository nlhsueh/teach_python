# 02_rlc_transient_simulation.py - 二階 RLC 暫態響應模擬 (常微分方程數值求解)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1. 電路元件參數設定
R = 50.0    # 電阻: 50 Ohm (調校此值可觀察過阻尼/欠阻尼/臨界阻尼)
L = 0.1     # 電感: 0.1 H
C = 100e-6  # 電容: 100 uF
Vs = 10.0   # 直流電源電壓: 10 V

# 2. 定義微分方程組 (系統狀態方程)
# t: 時間 (s)
# y: 狀態變數陣列，其中 y[0] 為電容電壓 Vc，y[1] 為電感電流 IL (迴路電流 i)
def rlc_ode(t, y):
    Vc = y[0]
    IL = y[1]
    
    dVc_dt = IL / C
    dIL_dt = (Vs - R * IL - Vc) / L
    
    return [dVc_dt, dIL_dt]

# 3. 設定時間範圍與觀測點
t_span = (0, 0.05)  # 模擬前 50 毫秒的暫態行為
t_eval = np.linspace(0, 0.05, 500) # 生成 500 個高精度時間取樣點

# 4. 設定初始狀態 (t=0 時，電容無電荷且迴路無電流)
initial_state = [0.0, 0.0]

# 5. 求解常微分方程組 (使用 Runge-Kutta 45 算法)
sol = solve_ivp(rlc_ode, t_span, initial_state, t_eval=t_eval)

print(f"求解完成：共計算了 {len(sol.t)} 個時間點")
print(f"終點電容電壓: {sol.y[0][-1]:.4f} V, 終點電流: {sol.y[1][-1]:.6f} A")

# 6. 繪製電容電壓暫態圖
plt.figure(figsize=(10, 6))
plt.plot(sol.t * 1000, sol.y[0], label='Capacitor Voltage $V_c(t)$ (V)', color='blue', linewidth=2)
plt.plot(sol.t * 1000, sol.y[1] * 10, label='Loop Current $i(t) \\times 10$ (A)', color='orange', linestyle='--')
plt.axhline(y=Vs, color='red', linestyle=':', label='Source Voltage $V_s$ (10V)')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.title('RLC Series Circuit Transient Charging Response')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
