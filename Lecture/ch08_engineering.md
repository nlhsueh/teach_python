Ch08 Python Engineering Applications
===

# Python 工程與資電應用

![Python與智慧系統工程](../img/ch08/gemini_nb/Python_Smart_System_Engineering.002.jpeg)

本章將帶領你探討 Python 在資電學群（資訊、電機、電子、自控、通訊等工程領域）的專業應用。當你掌握了基本語法、資料容器與物件導向觀念後，更重要的課題是：如何用程式碼解決電路求解、訊號處理、自動控制、機器人運動學以及軟硬體通訊等實務工程問題。

本章包含以下核心單元：
* **8.1 科學運算與電路求解**：利用矩陣求解電路方程組，並使用微積分求解器對 RLC 二階系統進行動態模擬。
* **8.2 訊號處理與頻域分析**：理解傅立葉變換與頻譜分析。
* **8.3 自動控制與機械手臂運動學**：實作 PID 控制器與機器人二軸關節運動求解。
* **8.4 虛擬序列埠與實體硬體互動**：模擬感測器串口數據流讀取。
* **8.5 網路通訊與 Socket 程式**：建構多用戶 TCP 聊天室。

---

## 8.1 科學運算與電路求解 (NumPy / SciPy)

### 8.1.1 網目電流與節點電壓求解 (線性代數應用)

![線性聯立方程式與電路網目電流法](../img/ch08/gemini_nb/Python_Smart_System_Engineering.003.jpeg)

在電路分析中，解線性聯立方程式是最基礎的工作。我們透過基爾霍夫電壓定律 (KVL) 或電流定律 (KCL)，可以將電路表示成矩陣形式：

$$A \cdot I = B \quad \text{或} \quad A \cdot V = B$$

#### 電路實例分析
考慮以下含有三個獨立網目的電路，其網目方程式如下：

$$\begin{aligned}
(R_1 + R_2) I_1 - R_2 I_2 + 0 \cdot I_3 &= V_1 \\
-R_2 I_1 + (R_2 + R_3 + R_4) I_2 - R_4 I_3 &= 0 \\
0 \cdot I_1 - R_4 I_2 + (R_4 + R_5) I_3 &= -V_2
\end{aligned}$$

假設電阻值為 $R_1=5\,\Omega$, $R_2=10\,\Omega$, $R_3=15\,\Omega$, $R_4=20\,\Omega$, $R_5=25\,\Omega$。
電源電壓為 $V_1=24\,\text{V}$, $V_2=12\,\text{V}$。

我們可以使用 `numpy.linalg.solve` 來解此聯立方程式：

```python
import numpy as np

# 1. 定義電路常數
R1, R2, R3, R4, R5 = 5, 10, 15, 20, 25
V1, V2 = 24, 12

# 2. 建立係數矩陣 A (R矩陣)
# 第一列: [ R1+R2,  -R2,       0 ]
# 第二列: [ -R2,    R2+R3+R4,  -R4 ]
# 第三列: [ 0,      -R4,       R4+R5 ]
A = np.array([
    [R1 + R2, -R2, 0],
    [-R2, R2 + R3 + R4, -R4],
    [0, -R4, R4 + R5]
])

# 3. 建立常數矩陣 B (V矩陣)
B = np.array([V1, 0, -V2])

print("係數矩陣 A (歐姆):")
print(A)
print("\n常數矩陣 B (伏特):")
print(B)

# 4. 呼叫 numpy.linalg.solve 進行高斯消去法計算
try:
    I = np.linalg.solve(A, B)
    print("\n[求解成功] 網目電流計算結果如下：")
    print(f"網目 1 電流 I1 = {I[0]:.4f} A")
    print(f"網目 2 電流 I2 = {I[1]:.4f} A")
    print(f"網目 3 電流 I3 = {I[2]:.4f} A")
    
    # 驗證計算是否正確: A * I 是否等於 B
    B_verify = np.dot(A, I)
    print(f"\n驗證結果 A * I (應等於 B): {B_verify}")
except np.linalg.LinAlgError as e:
    print(f"電路矩陣無解或為奇異矩陣：{e}")
```

#### 程式碼細部解析
* `np.array`：用來建立二維或一維陣列。係數矩陣必須是方陣（即列數等於行數）。
* `np.linalg.solve(A, B)`：其底層採用 LAPACK 函式庫中的 LU 分解法（LU Decomposition）求解，這比我們手動求逆矩陣 `np.linalg.inv(A) @ B` 更具數值穩定性且速度更快。

---

### 8.1.2 二階 RLC 暫態響應模擬 (常微分方程求解)

![常微分方程與 RLC 暫態響應模擬](../img/ch08/gemini_nb/Python_Smart_System_Engineering.004.jpeg)

包含電容與電感的電路稱為二階電路（Second-Order Circuit）。以 RLC 串聯充電電路為例，其動態行為可以由基爾霍夫電壓定律列出：

$$L \frac{d^2 q(t)}{d t^2} + R \frac{d q(t)}{d t} + \frac{1}{C} q(t) = V_s$$

由於電流量 $i(t) = \frac{d q(t)}{d t}$，且電容電壓 $v_c(t) = \frac{q(t)}{C}$。若我們將二階微分方程拆解為聯立的一階微分方程組，則可以定義狀態變數向量 $x(t) = [v_c(t), i(t)]^T$：

$$\frac{d v_c(t)}{d t} = \frac{i(t)}{C}$$
$$\frac{d i(t)}{d t} = \frac{V_s - R \cdot i(t) - v_c(t)}{L}$$

我們使用 `SciPy` 的 `solve_ivp` 工具對此進行動態數值求解：

```python
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
# y: 狀態變數陣列，其中 y[0] 為電容電壓 Vc，y[1] 為電感電流 IL (也是串聯迴路電流 i)
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

# 5. 求解常微分方程組 (使用預設的 Runge-Kutta 45 算法)
sol = solve_ivp(rlc_ode, t_span, initial_state, t_eval=t_eval)

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
plt.show()
```

#### RLC 阻尼特性深入探討
* **欠阻尼 (Underdamped, $R < 2 \sqrt{L/C}$)**：本例中 $R = 50 < 2\sqrt{0.1/0.0001} = 63.24$，因此波形會產生上下震盪，最後緩慢趨於穩態值 10V。
* **過阻尼 (Overdamped, $R > 63.24$)**：電壓平滑上升，沒有震盪，但達到穩態的時間極長。
* **臨界阻尼 (Critically Damped, $R \approx 63.24$)**：系統以最快的速度達到穩態且無震盪。

---

### 8.1.3 隨堂測驗 (CCQ 1)

**問題**

給定下列電路方程組的 NumPy 方程求解程式碼片段：
```python
import numpy as np
R_matrix = np.array([[8, -3], [-3, 12]])
V_matrix = np.array([5, 0])
I = np.linalg.solve(R_matrix, V_matrix)
```
下列關於 `I` 變數的敘述，何者正確？

A) `I` 是一個逆矩陣物件，可用 `I.apply()` 進行線性變換。
B) `I` 是一個含有兩個浮點數元素的一維 NumPy 陣列，儲存求解出來的電流數值。
C) `I` 包含了 `R_matrix` 的特徵值與特徵向量。
D) 若 `R_matrix` 是一個行列式值 (Determinant) 為 0 的矩陣，此程式仍可順利執行並回傳全 0 的電流。

<details>
<summary>點擊查看【隨堂測驗】答案與解析</summary>

**正確答案：B) `I` 是一個含有兩個浮點數元素的一維 NumPy 陣列，儲存求解出來的電流數值。**

* **解析**：
  * `np.linalg.solve` 返回的是方程式的特徵解向量，在本例中是一個 1D Array 儲存 $[I_1, I_2]$。
  * 行列式值為 0（奇異矩陣）時，線性方程式無解或有無限多組解，此時呼叫此方法會拋出 `LinAlgError`，不會返回全 0 結果，故 D 錯誤。
  * 此方法不計算特徵值與特徵向量（那需要使用 `np.linalg.eig`），故 C 錯誤。

</details>

---

### 8.1.4 隨堂測驗 (CCQ 2)

**問題**

在利用 `scipy.integrate.solve_ivp` 求解 RC 充電電路的暫態電壓隨時間變化時，我們需要傳入微分方程函數。下列哪一個微分方程函數的宣告與返回值設計是正確的？（已知 $dV_c/dt = (V_s - V_c)/(RC)$）

A)
```python
def rc_ode(Vc, t):
    return (Vs - Vc) / (R * C)
```
B)
```python
def rc_ode(t, Vc):
    return (Vs - Vc) / (R * C)
```
C)
```python
def rc_ode(t, y):
    return (Vs - y) * (R * C)
```
D)
```python
def rc_ode(y, t):
    return (y - Vs) / (R * C)
```

<details>
<summary>點擊查看【隨堂測驗】答案與解析</summary>

**正確答案：B) `def rc_ode(t, Vc): return (Vs - Vc) / (R * C)`**

* **解析**：
  * 在 `scipy.integrate.solve_ivp` 中，微分方程回呼函數的簽章格式預設為 `func(t, y)`，第一個參數為獨立變數時間 `t`，第二個參數為狀態變數 `y`（或是狀態變數陣列）。
  * 物理公式中電壓隨時間變化為 $dV_c/dt = (V_s - V_c)/(RC)$。選項 B 的命名與公式邏輯完全正確。選項 A 和 D 參數順序顛倒，`solve_ivp` 會報錯；選項 C 公式乘除法有誤。

</details>

---

## 8.2 訊號處理與頻域分析 (Signal Processing & FFT)

![訊號處理與快速傅立葉變換](../img/ch08/gemini_nb/Python_Smart_System_Engineering.005.jpeg)

通訊與電子工程的核心工作是訊號傳輸與濾波。由於物理世界中接收到的訊號通常混雜了環境噪聲，我們必須利用傅立葉變換將「時域（Time Domain）」訊號轉換為「頻域（Frequency Domain）」，以分析其頻率成分。

### 8.2.1 訊號合成與快速傅立葉變換 (FFT)

假設我們接收到一個訊號，包含 $50\,\text{Hz}$ 與 $120\,\text{Hz}$ 兩個主要頻率成分，同時混雜了隨機白噪聲。
我們將使用 `numpy.fft` 來提取並視覺化其頻率特性：

```python
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

# 由於 FFT 的結果是對稱的，我們只取前半段正頻率部分，並計算振幅大小
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
ax2.set_title('Frequency Domain - FFT Analysis')
ax2.set_xlim(0, 250) # 限制觀察頻率範圍在 0 ~ 250 Hz
ax2.grid(True)

plt.tight_layout()
plt.show()
```

#### 頻率分析與工程應用
* 從時域圖中，受強力噪聲影響，我們幾乎無法肉眼辨識原始波形。
* 但在下方的頻域圖中，FFT 演算法在 $50\,\text{Hz}$ 與 $120\,\text{Hz}$ 處產生了兩個清晰且尖銳的振幅峰值，這正是傅立葉變換在濾波器設計與頻譜偵測上的巨大威力。

---

## 8.3 自動控制與機械手臂運動學 (Control & Robotics)

![自動控制與回授系統](../img/ch08/gemini_nb/Python_Smart_System_Engineering.006.jpeg)

自動控制與機器人技術是機電工程的最核心支柱。本節探討如何用 Python 設計與模擬控制元件。

### 8.3.1 寫一個自己的 PID 控制器

![PID 控制器原理與架構](../img/ch08/gemini_nb/Python_Smart_System_Engineering.007.jpeg)

**比例-積分-微分控制器 (PID Controller)** 是自動化系統中最常見的回授控制演算法。我們設計一個物件導向的 `PID` 控制器類別，並用它來控制一個虛擬加熱系統的溫度：

```python
import time
import matplotlib.pyplot as plt

class PIDController:
    """ 客製化 PID 控制器類別 """
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp  # 比例增益 (Proportional Gain)
        self.Ki = Ki  # 積分增益 (Integral Gain)
        self.Kd = Kd  # 微分增益 (Derivative Gain)
        self.setpoint = setpoint  # 目標設定值
        
        self.prev_error = 0.0
        self.integral = 0.0

    def update(self, current_value, dt):
        # 1. 計算誤差
        error = self.setpoint - current_value
        
        # 2. 比例項 (P)
        P_out = self.Kp * error
        
        # 3. 積分項 (I) - 累積歷史誤差，消除靜態誤差
        self.integral += error * dt
        I_out = self.Ki * self.integral
        
        # 4. 微分項 (D) - 預測誤差變化趨勢，抑制震盪
        derivative = (error - self.prev_error) / dt if dt > 0 else 0.0
        D_out = self.Kd * derivative
        
        # 5. 保存此次誤差
        self.prev_error = error
        
        # 輸出控制訊號
        return P_out + I_out + D_out

# 模擬一個簡單的一階熱滯後加熱系統
# 室溫 25 度，加熱係數 0.1，自然散熱係數 0.05
class ThermalSystem:
    def __init__(self, initial_temp=25.0):
        self.temp = initial_temp
        
    def step(self, heat_input, dt):
        # 溫度受加熱輸入與外界溫差散熱共同決定
        cooling = 0.05 * (self.temp - 25.0)
        self.temp += (heat_input * 0.1 - cooling) * dt
        return self.temp

# 實施 PID 閉迴路控制模擬
sys = ThermalSystem(initial_temp=25.0)
pid = PIDController(Kp=2.5, Ki=0.3, Kd=0.8, setpoint=100.0) # 設定目標 100 度

time_history = []
temp_history = []
target_history = []

current_time = 0.0
dt = 0.1  # 控制週期 0.1 秒

for _ in range(300): # 模擬 30 秒
    current_temp = sys.temp
    control_signal = pid.update(current_temp, dt)
    
    # 限制加熱功率範圍在 0 ~ 100% 之間
    control_signal = max(0.0, min(100.0, control_signal))
    
    # 更新系統狀態
    sys.step(control_signal, dt)
    
    time_history.append(current_time)
    temp_history.append(current_temp)
    target_history.append(pid.setpoint)
    
    current_time += dt

# 繪製溫度控制結果
plt.figure(figsize=(10, 5))
plt.plot(time_history, temp_history, label='Actual Temp (°C)', color='magenta', linewidth=2)
plt.plot(time_history, target_history, label='Target Temp (°C)', color='blue', linestyle=':')
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature (°C)')
plt.title('PID Temperature Control System Simulation')
plt.grid(True)
plt.legend()
plt.show()
```

---

### 8.3.2 機器人二軸機械手臂運動學 (Kinematics)

![二軸機械手臂正向運動學與逆向運動學](../img/ch08/gemini_nb/Python_Smart_System_Engineering.008.jpeg)

對於機器人工程師而言，必須計算手臂末端點在空間中的座標。
* **正向運動學 (Forward Kinematics)**：給定各關節的旋轉角度 $\theta_1, \theta_2$，求機械手臂末端 (End-Effector) 的平面座標 $(x, y)$。
* **逆向運動學 (Inverse Kinematics)**：給定末端座標 $(x, y)$，求解各關節角度。

```python
import numpy as np

class RoboticArm2R:
    """ 二維平面雙關節機械手臂模型 """
    def __init__(self, L1, L2):
        self.L1 = L1  # 第一節臂長 (m)
        self.L2 = L2  # 第二節臂長 (m)

    def forward_kinematics(self, theta1, theta2):
        """ 正向運動學：傳入弧度角度，回傳 (x, y) """
        x = self.L1 * np.cos(theta1) + self.L2 * np.cos(theta1 + theta2)
        y = self.L1 * np.sin(theta1) + self.L2 * np.sin(theta1 + theta2)
        return x, y

    def inverse_kinematics(self, x, y):
        """ 逆向運動學：給定 (x, y)，回傳弧度角度 [theta1, theta2] """
        # 使用餘弦定理計算 theta2
        r_sq = x**2 + y**2
        cos_theta2 = (r_sq - self.L1**2 - self.L2**2) / (2 * self.L1 * self.L2)
        
        # 限制 cos 範圍避免超出 [-1, 1] 拋出數學錯誤
        cos_theta2 = np.clip(cos_theta2, -1.0, 1.0)
        
        # theta2 (下肘/上肘有兩組解，這裡取正解，即手肘向上型)
        theta2 = np.arccos(cos_theta2)
        
        # 計算 theta1
        alpha = np.arctan2(y, x)
        beta = np.arctan2(self.L2 * np.sin(theta2), self.L1 + self.L2 * np.cos(theta2))
        theta1 = alpha - beta
        
        return theta1, theta2

# 驗證機械手臂運動計算
arm = RoboticArm2R(L1=1.0, L2=0.8)

# 1. 給定角度計算位置
t1, t2 = np.radians(30), np.radians(45) # 轉成弧度
x_end, y_end = arm.forward_kinematics(t1, t2)
print("--- 正向運動學計算結果 ---")
print(f"給定關節角度：theta1=30°, theta2=45°")
print(f"機械手臂末端座標：(x, y) = ({x_end:.4f} m, {y_end:.4f} m)")

# 2. 給定位置回求角度
sol_t1, sol_t2 = arm.inverse_kinematics(x_end, y_end)
print("\n--- 逆向運動學計算結果 ---")
print(f"給定目標座標：({x_end:.4f}, {y_end:.4f})")
print(f"解出關節角度：theta1={np.degrees(sol_t1):.2f}°, theta2={np.degrees(sol_t2):.2f}°")
```

---

### 8.3.3 隨堂測驗 (CCQ 3)

**問題**

在 PID 控制器的實作中，**積分項 (Integral Term, Ki)** 主要用來解決系統的什麼問題？

A) 減少系統在初期的大幅過沖 (Overshoot)。
B) 預測系統誤差的未來趨勢。
C) 消除系統因摩擦力或熱損失所導致的「穩態誤差/靜態誤差 (Steady-State Error)」。
D) 加快系統在初始階段的響應速度。

<details>
<summary>點擊查看【隨堂測驗】答案與解析</summary>

**正確答案：C) 消除系統因摩擦力或熱損失所導致的「穩態誤差/靜態誤差 (Steady-State Error)」。**

* **解析**：
  * **比例項 (Kp)**：主要提供基礎控制力，但若只有比例項，當誤差很小時控制力會不足以克服散熱或摩擦阻力，進而導致殘留的「穩態誤差」。
  * **積分項 (Ki)**：會隨著時間不斷累積殘留的微小誤差，使控制輸出持續放大，直到誤差完全歸零，用以消除靜態誤差。
  * **微分項 (Kd)**：主要用於預測趨勢，對變化率產生反向阻力，藉此抑制波形震盪與減少過沖。

</details>

---

## 8.4 虛擬序列埠與實體硬體互動 (pySerial)

![微控制器與硬體通訊](../img/ch08/gemini_nb/Python_Smart_System_Engineering.009.jpeg)

工程師時常要將 Python 與微控制器（Arduino / Raspberry Pi）進行整合。如果我們手邊沒有實體硬體，我們可以在 Python 中利用多執行緒（Multi-threading）模擬一個持續發送數據的「虛擬硬體串流」，以測試讀取與除錯程式。

### 8.4.1 使用多執行緒模擬硬體並讀取序列數據

![虛擬序列埠與多執行緒模擬](../img/ch08/gemini_nb/Python_Smart_System_Engineering.010.jpeg)

```python
import threading
import time
import queue

# 建立一個共享的 Thread-safe 佇列來模擬序列通訊緩衝區
virtual_serial_buffer = queue.Queue()

# 模擬硬體端：Arduino 持續回傳感測器數值 (如電壓 0.0 ~ 5.0 V)
def hardware_simulator(buffer, stop_event):
    print("[Simulator] 模擬硬體已啟動...")
    t = 0
    while not stop_event.is_set():
        # 模擬一個隨時間震盪的類比電壓數值，加上微小噪聲
        voltage = 2.5 + 2.0 * np.sin(t) + np.random.normal(0, 0.05)
        # 轉換為類似 Arduino 印出的字串格式，例如 "V:4.23"
        data_string = f"V:{voltage:.2f}\n"
        
        # 寫入共享緩衝區 (模擬硬體串口傳輸)
        buffer.put(data_string.encode('utf-8'))
        
        t += 0.2
        time.sleep(0.2) # 每 200 毫秒傳送一筆
    print("[Simulator] 模擬硬體已安全關閉。")

# 模擬電腦端：使用我們模擬出的 Serial 物件讀取資料並解析
class MockSerial:
    def __init__(self, buffer):
        self.buffer = buffer

    def readline(self):
        # 從佇列中讀取資料 (阻塞直到有資料進來)
        return self.buffer.get()

    def has_data(self):
        return not self.buffer.empty()

# 主程式運行
stop_signal = threading.Event()
# 啟動背景執行緒模擬硬體
hw_thread = threading.Thread(target=hardware_simulator, args=(virtual_serial_buffer, stop_signal))
hw_thread.daemon = True # 設定為守護執行緒，主程式結束時會一併關閉
hw_thread.start()

# 初始化虛擬序列埠讀取器
ser = MockSerial(virtual_serial_buffer)
time.sleep(1)

print("\n[電腦端] 開始監聽硬體回報數據...")
try:
    for i in range(10):
        # 模擬讀取一行
        raw_bytes = ser.readline()
        # 解碼並移除空白與換行符號
        data_str = raw_bytes.decode('utf-8').strip()
        
        # 解析協定格式
        if data_str.startswith("V:"):
            value_float = float(data_str.split(":")[1])
            print(f"[PC 接收] 第 {i+1} 次採樣電壓：{value_float:.2f} V")
        time.sleep(0.3)
finally:
    # 通知模擬器執行緒停止運行
    stop_signal.set()
    hw_thread.join()
    print("程式結束。")
```

---

### 8.4.2 隨堂測驗 (CCQ 4)

**問題**

在實體硬體控制中，若微控制器以每 10 毫秒 (10ms) 的速度高頻發送序列埠數據，而 Python 端每 100 毫秒 (100ms) 才讀取一次，在沒有加入硬體流控制（Flow Control）的情況下，通常會發生什麼現象？

A) Python 程式會自動提高讀取執行緒的 CPU 運算時脈，維持資料同步。
B) 序列埠通訊晶片的硬體或軟體接收緩衝區 (Buffer) 會溢位 (Overflow)，導致舊的數據遺失或接收到的資料出現嚴重滯後與亂碼。
C) 由於 Python 的直譯特性，程式會主動要求微控制器降低傳送頻率。
D) 電壓訊號會在傳輸線上自動做均值濾波，變成平滑數值。

<details>
<summary>點擊查看【隨堂測驗】答案與解析</summary>

**正確答案：B) 序列埠通訊晶片的硬體或軟體接收緩衝區 (Buffer) 會溢位 (Overflow)，導致舊的數據遺失或接收到的資料出現嚴重滯後與亂碼。**

* **解析**：
  * 序列通訊緩衝區大小有限。如果寫入速度（微控制器 10ms 發送）遠大於讀取速度（Python 100ms 讀取），緩衝區會迅速被塞滿。
  * 緩衝區滿載後，新進來的資料會被直接丟棄（遺失），或者 Python 讀取到的全部都是很久之前的「舊快取資料」，造成資料的嚴重遲滯。
  * 在實際的高頻數據處理中，必須使用高效的多執行緒或異步事件監聽（如 `pyserial` 的背景執行緒讀取機制）以維持同步。

</details>

---

## 8.5 網路通訊與 Socket 程式 (TCP Networking)

![網路通訊協定與 TCP/IP Socket 機制](../img/ch08/gemini_nb/Python_Smart_System_Engineering.011.jpeg)

在通訊與資訊工程中，跨電腦進行連線通訊是極為重要的基本技術。Socket 是所有應用層網路協定（如 HTTP、MQTT）底層的傳輸介面。

### 8.5.1 多用戶 TCP 聊天室 (伺服器與用戶端)

我們將展示如何寫一個簡單的多執行緒 TCP 伺服器，能同時接受多個用戶端連線，並將任何用戶端傳送的訊息廣播 (Broadcast) 給其他所有在線用戶。

#### 伺服器端 (Server) 程式碼

![TCP 伺服器與用戶端連線生命週期](../img/ch08/gemini_nb/Python_Smart_System_Engineering.012.jpeg)

```python
import socket
import threading

# 伺服器配置
HOST = '127.0.0.1'
PORT = 8080
clients = []  # 儲存所有已連線用戶端的 socket 物件

def broadcast(message, sender_client):
    """ 將訊息廣播給除了發送者之外的所有人 """
    for client in clients:
        if client != sender_client:
            try:
                client.send(message)
            except Exception as e:
                # 若發送失敗，代表連線已中斷，將其移除
                client.close()
                if client in clients:
                    clients.remove(client)

def handle_client(client_socket, client_address):
    """ 背景處理每一個單獨的用戶端連線 """
    print(f"[新連線] 連線成功：{client_address}")
    client_socket.send("歡迎加入 TCP 聊天室！請開始發言。\n".encode('utf-8'))
    
    while True:
        try:
            # 接收用戶端訊息
            message = client_socket.recv(1024)
            if not message:
                break
            
            log_msg = f"用戶 {client_address[1]}: {message.decode('utf-8')}".strip()
            print(log_msg)
            
            # 廣播給其他在線用戶
            broadcast(f"{client_address[1]} 說: {message.decode('utf-8')}".encode('utf-8'), client_socket)
        except Exception:
            break

    # 用戶端斷線處理
    print(f"[斷開連線] 用戶離線：{client_address}")
    if client_socket in clients:
        clients.remove(client_socket)
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 設置 Socket 重用選項
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[啟動] 伺服器已在 {HOST}:{PORT} 監聽連線...")

    try:
        while True:
            # 主執行緒阻塞等待新連線
            client_socket, client_address = server_socket.accept()
            clients.append(client_socket)
            
            # 為新連線建立獨立的工作執行緒
            thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            thread.daemon = True
            thread.start()
    except KeyboardInterrupt:
        print("\n[關閉] 伺服器正在關閉...")
    finally:
        server_socket.close()
```

#### 用戶端 (Client) 程式碼
```python
import socket
import threading

def receive_messages(client_socket):
    """ 背景接收來自伺服器的廣播訊息 """
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("與伺服器的連線中斷。")
                break
            print(f"\n[廣播] {message}")
        except Exception:
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('127.0.0.1', 8080))
        
        # 啟動接收背景執行緒
        recv_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        recv_thread.daemon = True
        recv_thread.start()
        
        print("已成功連線至聊天伺服器。輸入 'exit' 可離開。")
        while True:
            msg = input()
            if msg.lower() == 'exit':
                break
            client_socket.send(msg.encode('utf-8'))
    except Exception as e:
        print(f"連線失敗：{e}")
    finally:
        client_socket.close()
```

---

### 8.5.2 隨堂測驗 (CCQ 5)

**問題**

在建立 TCP 網路連線程式設計時，常會使用到 `socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`。這行設定的主要作用為何？

A) 限制同一個 IP 在同一時間內的最大連線次數。
B) 將 TCP 連線自動升級為更高傳輸頻寬的 UDP 模式。
C) 允許伺服器關閉重啟後，立即重新綁定 (bind) 相同的 Port，避免作業系統因處於 TIME_WAIT 狀態而拒絕綁定。
D) 加密傳輸的 Socket 內容以防止駭客竊聽。

<details>
<summary>點擊查看【隨堂測驗】答案與解析</summary>

**正確答案：C) 允許伺服器關閉重啟後，立即重新綁定 (bind) 相同的 Port，避免作業系統因處於 TIME_WAIT 狀態而拒絕綁定。**

* **解析**：
  * 當一個 TCP 伺服器正常關閉或異常終止時，作業系統的核心通常會將該連接埠保留在 TIME_WAIT 狀態幾分鐘，用以確保所有網路殘留包都已被丟棄。
  * 如果在此期間重新啟動伺服器並嘗試 `bind()`，會拋出 `OSError: [Errno 98] Address already in use`。
  * 設定 `SO_REUSEADDR` 為 1，可以強制允許重用該埠號，這是網路開發中非常實用的經驗設定。

</details>

---

## 8.6 本章綜合工程實作專題

![數位濾波器設計與低通濾波器模擬](../img/ch08/gemini_nb/Python_Smart_System_Engineering.013.jpeg)

### 專題任務：低通濾波器 (Low-Pass Filter) 模擬設計

**背景說明**：在訊號與系統控制中，我們常常需要消除感測器的高頻噪聲，只保留低頻訊號。最簡單的數位濾波器是**一階一階低通濾波器（RC 數位濾波器）**，其差分方程式為：

$$y[k] = \alpha \cdot x[k] + (1 - \alpha) \cdot y[k-1]$$

其中 $x[k]$ 是第 $k$ 次量測到的原始感測器噪聲值，$y[k]$ 是濾波後的平滑輸出值，$\alpha$ 是濾波係數（$0 < \alpha < 1$）。

我們使用 Python 實作此濾波器，並模擬其表現：

```python
import numpy as np
import matplotlib.pyplot as plt

class LowPassFilter:
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

# 1. 合成一個帶有高頻高斯噪聲的類比正弦波
t = np.linspace(0, 2.0, 400)
clean_signal = 10.0 * np.sin(2 * np.pi * 1.5 * t) # 1.5 Hz 乾淨訊號
noise = np.random.normal(0, 1.8, len(t))
noisy_signal = clean_signal + noise

# 2. 初始化兩個不同強度的濾波器
lpf_weak = LowPassFilter(alpha=0.2)   # 弱濾波器 (反應快)
lpf_strong = LowPassFilter(alpha=0.05) # 強濾波器 (噪音抑制佳)

filtered_weak = []
filtered_strong = []

for val in noisy_signal:
    filtered_weak.append(lpf_weak.filter_value(val))
    filtered_strong.append(lpf_strong.filter_value(val))

# 3. 繪製比較圖
plt.figure(figsize=(12, 6))
plt.plot(t, noisy_signal, color='gray', alpha=0.5, label='Raw Noisy Signal')
plt.plot(t, clean_signal, color='black', linewidth=2.5, label='Ideal Signal')
plt.plot(t, filtered_weak, color='orange', linewidth=1.8, label='LPF Weak (alpha=0.2)')
plt.plot(t, filtered_strong, color='green', linewidth=2.0, label='LPF Strong (alpha=0.05)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Real-time Digital Low-Pass Filter Simulation')
plt.grid(True)
plt.legend()
plt.show()
```

![本章工程專題與應用實作小結](../img/ch08/gemini_nb/Python_Smart_System_Engineering.014.jpeg)
