# 04_basic_operations.py
# 知識點：基本算術運算、銀行家捨入法、關係運算與邏輯運算

import math

# 1. 算術運算
print("--- 算術運算 ---")
print("10 + 4 =", 10 + 4)      # 14 (加法)
print("10 - 4 =", 10 - 4)      # 6  (減法)
print("10 * 4 =", 10 * 4)      # 40 (乘法)
print("10 / 4 =", 10 / 4)      # 2.5 (除法，一定回傳浮點數)
print("10 // 4 =", 10 // 4)    # 2  (整數除法/取整數商)
print("6 % 4 =", 6 % 4)        # 2  (取餘數)
print("10 ** 4 =", 10 ** 4)    # 10000 (次方運算)
print("無條件進位 math.ceil(10.1) =", math.ceil(10.1)) # 11

# 2. round() 銀行家捨入法 (四捨六入五成雙)
print("\n--- round() 銀行家捨入法 ---")
print("round(3.7) =", round(3.7))    # 4 (小數大於0.5 -> 進位)
print("round(3.2) =", round(3.2))    # 3 (小數小於0.5 -> 捨去)
# 恰好等於 0.5 時，捨入到最近的「偶數」
print("round(2.5) =", round(2.5))    # 2 (2是偶數，捨去)
print("round(3.5) =", round(3.5))    # 4 (3是奇數，進位到偶數4)
print("round(4.5) =", round(4.5))    # 4 (4是偶數，捨去)

# 3. 實用範例：時間與距離計算
print("\n--- 時間運算範例 ---")
dist = 384400                           # 地球到月亮距離 (km)
speed = 1225                            # 馬赫速度 (km/h)
total_hours = dist / speed              # 計算總小時數

# 計算天與小時
days = total_hours // 24
hours = total_hours % 24
print('共需 {} 天 {} 小時'.format(days, hours))

# 使用 divmod() 同時取得商與餘數
days, hours = divmod(total_hours, 24)
xmins = 60 * (hours - int(hours))
mins, secs = divmod(xmins, 60)
secs = 60 * (secs - int(secs))
h, m, s = int(hours), int(xmins), int(secs)
print('精確時間：共需 {} 天 {} 小時 {} 分 {} 秒'.format(days, h, m, s))

# 4. 關係運算 (關係運算子回傳 True/False)
print("\n--- 關係運算 ---")
print("11 > 2:", 11 > 2)        # True
print("11 >= 11:", 11 >= 11)    # True
print("11 != 2:", 11 != 2)      # True
a, b = 11, 12
print("a >= b (11 >= 12):", a >= b) # False

# 5. 邏輯運算 (and, or, not)
print("\n--- 邏輯運算 ---")
t = 11 > 2                      # True
f = 1 > 9                       # False
print("t and f:", t and f)      # False (兩者皆為 True 才為 True)
print("t or f:", t or f)        # True (只要有一者為 True 即為 True)
print("not t:", not t)          # False (邏輯反轉)

is_student = True
is_kid = False
print("is_student and is_kid:", is_student and is_kid)  # False
print("is_student or is_kid:", is_student or is_kid)    # True
