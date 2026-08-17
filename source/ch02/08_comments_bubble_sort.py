# 08_comments_bubble_sort.py
# 知識點：程式的註解（單行註解、行內註解、多行/區塊註解）與氣泡排序法

'''
本程式用來排序一群資料
這群資料是隨機產生的
透過氣泡排序法 (Bubble Sort) 來排序

by Nick Hsueh, 2018/1/1
'''

import random

# 初始化串列
a = []

# 單行註解：隨機產生 10 個數字 (1 到 100 之間)
for i in range(10):
    a.append(random.randint(1, 100))

print("排序前原資料:", a)     # 行內註解：印出原始未排序的資料

s = len(a)   # 資料大小
r = s - 1    # 回合數

# 氣泡排序法核心邏輯
for i in range(1, r + 1):
    # 將每一回合的排序結果印出來看
    for j in range(0, s - i):
        # 將相鄰的兩個元素進行比較，若左邊大於右邊則對調
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
            
print("排序後新資料:", a)     # 行內註解：印出排序完成後的資料
