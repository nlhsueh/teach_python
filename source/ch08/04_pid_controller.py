# 04_pid_controller.py - PID 控制器設計與一階系統溫度回授控制模擬

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
        
        # 2. 比例項 (P) - 反映當前誤差
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

print(f"最終模擬溫度: {temp_history[-1]:.2f} °C (目標: {pid.setpoint:.2f} °C)")

# 繪製溫度控制結果
plt.figure(figsize=(10, 5))
plt.plot(time_history, temp_history, label='Actual Temp (°C)', color='magenta', linewidth=2)
plt.plot(time_history, target_history, label='Target Temp (°C)', color='blue', linestyle=':')
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature (°C)')
plt.title('PID Temperature Control System Simulation')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
