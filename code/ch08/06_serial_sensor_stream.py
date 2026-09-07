# 06_serial_sensor_stream.py - 虛擬序列埠 (Virtual Serial Port) 與多執行緒感測器數據流讀取

import threading
import time
import queue
import numpy as np

# 建立共享的 Thread-safe 佇列來模擬序列通訊緩衝區 (Serial Buffer)
virtual_serial_buffer = queue.Queue()

# 模擬硬體端：Arduino / ESP32 持續回傳類比感測器數值 (如電壓 0.0 ~ 5.0 V)
def hardware_simulator(buffer, stop_event):
    print("[Simulator] 模擬微控制器已啟動，開始發送感測數據...")
    t = 0.0
    while not stop_event.is_set():
        # 模擬一個隨時間震盪的類比電壓數值，加上微小雜訊
        voltage = 2.5 + 2.0 * np.sin(t) + np.random.normal(0, 0.05)
        # 轉換為常見的串口通訊字串格式，例如 "V:4.23\n"
        data_string = f"V:{voltage:.2f}\n"
        
        # 寫入共享緩衝區 (模擬硬體串口傳輸)
        buffer.put(data_string.encode('utf-8'))
        
        t += 0.2
        time.sleep(0.15) # 每 150 毫秒傳送一筆
    print("[Simulator] 模擬微控制器已安全關閉。")

# 模擬電腦端：封裝 Serial 讀取介面
class MockSerial:
    def __init__(self, buffer):
        self.buffer = buffer

    def readline(self):
        # 從佇列中讀取資料 (阻塞直到有資料進來)
        return self.buffer.get()

    def has_data(self):
        return not self.buffer.empty()

if __name__ == '__main__':
    stop_signal = threading.Event()
    
    # 啟動背景執行緒模擬硬體微控制器
    hw_thread = threading.Thread(target=hardware_simulator, args=(virtual_serial_buffer, stop_signal))
    hw_thread.daemon = True
    hw_thread.start()

    # 初始化序列埠讀取器
    ser = MockSerial(virtual_serial_buffer)
    time.sleep(0.5)

    print("\n[電腦端 (Python)] 開始監聽並解析序列埠封包...")
    try:
        for i in range(12):
            raw_bytes = ser.readline()
            data_str = raw_bytes.decode('utf-8').strip()
            
            # 解析通訊協定
            if data_str.startswith("V:"):
                value_float = float(data_str.split(":")[1])
                print(f"[PC 接收] 第 {i+1:02d} 次採樣電壓: {value_float:.2f} V")
            time.sleep(0.2)
    finally:
        stop_signal.set()
        hw_thread.join()
        print("\n序列埠讀取示範結束。")
