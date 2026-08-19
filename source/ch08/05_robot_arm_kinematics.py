# 05_robot_arm_kinematics.py - 二維雙關節機械手臂運動學 (順向與逆向運動學)

import numpy as np

class RoboticArm2R:
    """ 二維平面雙關節機械手臂模型 """
    def __init__(self, L1, L2):
        self.L1 = L1  # 第一節臂長 (m)
        self.L2 = L2  # 第二節臂長 (m)

    def forward_kinematics(self, theta1, theta2):
        """ 正向運動學：傳入弧度角度，回傳末端座標 (x, y) """
        x = self.L1 * np.cos(theta1) + self.L2 * np.cos(theta1 + theta2)
        y = self.L1 * np.sin(theta1) + self.L2 * np.sin(theta1 + theta2)
        return x, y

    def inverse_kinematics(self, x, y):
        """ 逆向運動學：給定末端目標 (x, y)，回傳關節弧度角度 [theta1, theta2] """
        # 使用餘弦定理計算 theta2
        r_sq = x**2 + y**2
        cos_theta2 = (r_sq - self.L1**2 - self.L2**2) / (2 * self.L1 * self.L2)
        
        # 限制 cos 範圍避免超出 [-1, 1] 拋出數學錯誤 (不可達點保護)
        cos_theta2 = np.clip(cos_theta2, -1.0, 1.0)
        
        # theta2 (取正解，手肘向上型)
        theta2 = np.arccos(cos_theta2)
        
        # 計算 theta1
        alpha = np.arctan2(y, x)
        beta = np.arctan2(self.L2 * np.sin(theta2), self.L1 + self.L2 * np.cos(theta2))
        theta1 = alpha - beta
        
        return theta1, theta2

if __name__ == '__main__':
    arm = RoboticArm2R(L1=1.0, L2=0.8)

    # 1. 給定角度計算位置 (Forward Kinematics)
    t1_deg, t2_deg = 30.0, 45.0
    t1, t2 = np.radians(t1_deg), np.radians(t2_deg)
    x_end, y_end = arm.forward_kinematics(t1, t2)
    
    print("=== [1. 正向運動學 (Forward Kinematics)] ===")
    print(f"輸入關節角度: theta1 = {t1_deg}°, theta2 = {t2_deg}°")
    print(f"機械手臂末端座標: (x, y) = ({x_end:.4f} m, {y_end:.4f} m)")

    # 2. 給定位置回求角度 (Inverse Kinematics)
    sol_t1, sol_t2 = arm.inverse_kinematics(x_end, y_end)
    sol_t1_deg, sol_t2_deg = np.degrees(sol_t1), np.degrees(sol_t2)
    
    print("\n=== [2. 逆向運動學 (Inverse Kinematics)] ===")
    print(f"輸入目標座標: ({x_end:.4f} m, {y_end:.4f} m)")
    print(f"反解關節角度: theta1 = {sol_t1_deg:.2f}°, theta2 = {sol_t2_deg:.2f}°")
    
    # 驗證誤差
    print(f"\n驗證誤差: d_theta1 = {abs(t1_deg - sol_t1_deg):.6f}°, d_theta2 = {abs(t2_deg - sol_t2_deg):.6f}°")
