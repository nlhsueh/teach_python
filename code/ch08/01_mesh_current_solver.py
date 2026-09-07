# 01_mesh_current_solver.py - 網目電流與節點電壓求解 (線性代數應用)

import numpy as np

# 1. 定義電路常數
R1, R2, R3, R4, R5 = 5, 10, 15, 20, 25
V1, V2 = 24, 12

# 2. 建立係數矩陣 A (電阻矩陣)
# 第一列: [ R1+R2,  -R2,       0 ]
# 第二列: [ -R2,    R2+R3+R4,  -R4 ]
# 第三列: [ 0,      -R4,       R4+R5 ]
A = np.array([
    [R1 + R2, -R2, 0],
    [-R2, R2 + R3 + R4, -R4],
    [0, -R4, R4 + R5]
])

# 3. 建立常數矩陣 B (電壓矩陣)
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
