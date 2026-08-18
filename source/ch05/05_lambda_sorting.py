# 05_lambda_sorting.py - Lambda 匿名函式與客製化排序

# 1. 巢狀成績列表
# 每個學生的成績包含：[英文, 數學, 物理]
grades = [[12, 23, 43], [9, 4, 10], [100, 22, 1]]

# 2. 預設排序 (依據首個欄位，即英文成績)
print("預設首項排序:")
print(sorted(grades))

# 3. 依據最後一個欄位 (物理成績) 排序
# key=lambda x: x[-1] 表示以子串列最後一個元素做為比較的 Key
print("依據物理成績排序:")
print(sorted(grades, key=lambda x: x[-1]))

# 4. 依據自訂比重總分排序 (英文*0.3 + 數學*0.4 + 物理*0.4)
print("依據比重總分排序:")
weighted_sorted = sorted(grades, key=lambda x: x[0]*0.3 + x[1]*0.4 + x[2]*0.4)
print(weighted_sorted)
