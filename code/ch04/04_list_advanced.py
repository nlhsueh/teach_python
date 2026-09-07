# 04_list_advanced.py - 列表推導式、多元排序、 equality 與 氣泡排序法

# 1. 列表推導式 (List Comprehension)
a = [i for i in range(10)]
print('列表推導式 [0..9]:', a)

b = []
for i in range(10):
    b.append(i)
print('傳統 append 迴圈 [0..9]:', b)

c = [i for i in range(0, 10, 2)]
print('偶數推導式:', c)

# 2. 多元排序與 Lambda
grade_data = [[11, 22, 33], [90, 91, 92], [77, 88, 99], [44, 55, 66]]

# 預設排序 (依據各子列表第一個元素)
print('預設首項排序:', sorted(grade_data))

# 依據總和排序 (使用 lambda)
g_sum_sorted = sorted(grade_data, key=lambda x: sum(x))
print('依各科總和排序:', g_sum_sorted)

# 依據最後一科成績排序
g_last_sorted = sorted(grade_data, key=lambda x: x[-1])
print('依最後一科成績排序:', g_last_sorted)

# 3. == (值比較) 與 is (參考比較) 的區別
grade = [11, 22, 99, 35, 59]
g = grade
gc = grade.copy()
print('grade == g (值相等):', grade == g)
print('grade is g (同記憶體參考):', grade is g)
print('grade == gc (值相等):', grade == gc)
print('grade is gc (同記憶體參考):', grade is gc)

# 4. 氣泡排序法 (Bubble Sort) 實作
import random
# 建立 10 個 1~100 隨機數的列表進行演示
rand_list = [random.randint(1, 100) for _ in range(10)]
print('隨機數排序前:', rand_list)

size = len(rand_list)
for i in range(1, size):
    for j in range(0, size - i):
        if rand_list[j] > rand_list[j + 1]:
            rand_list[j], rand_list[j + 1] = rand_list[j + 1], rand_list[j]
print('隨機數氣泡排序後:', rand_list)
