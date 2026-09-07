# 07_recursion_hanoi.py - 遞迴應用：河內塔 (Hanoi Tower) 演算法

def hanoi(n, start, temp, end):
    """
    河內塔遞迴函式
    n: 盤子數量
    start: 起始柱
    temp: 輔助柱
    end: 目標柱
    """
    if n == 1:
        # 當只有一個盤子時，直接從起始柱搬移到目標柱
        print(f"把盤子 1 從 {start} 搬移到 {end}")
    else:
        # 步驟一：先將上面的 n-1 個盤子從起始柱搬移到輔助柱 (以目標柱為輔助)
        hanoi(n - 1, start, end, temp)
        # 步驟二：將最底下的第 n 個盤子從起始柱搬移到目標柱
        print(f"把盤子 {n} 從 {start} 搬移到 {end}")
        # 步驟三：再將輔助柱上的 n-1 個盤子搬移到目標柱 (以起始柱為輔助)
        hanoi(n - 1, temp, start, end)

# 測試搬移 3 個盤子的過程
# 預期需要搬移 2^3 - 1 = 7 次
print("--- 搬移 3 個盤子的過程 (柱子分別為 A、B、C) ---")
hanoi(3, 'A', 'B', 'C')
