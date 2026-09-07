# 01_list_basic.py - List 建立與切片基本操作

# 1. 建立不同的 List
nick_grade = ['nick', 'S9201201', [90, 72, 100]]
albert_grade = ['albert', 'S9201202', [99, 68, 90]]
grades = [nick_grade, albert_grade]

empty_list_1 = []
empty_list_2 = list()

# 2. 索引與切片 (Slicing) 練習
grade = [11, 22, 99, 35, 59]
print('原始成績列表:', grade)
print('grade[0]  (第 1 個元素):', grade[0])
print('grade[1]  (第 2 個元素):', grade[1])
print('grade[-1] (最後 1 個元素):', grade[-1])
print('grade[1:3] (索引 1 至 2):', grade[1:3])
print('grade[1:]  (索引 1 之後):', grade[1:])
print('grade[:3]  (索引 3 之前):', grade[:3])
print('grade[-1:] (最後一個元素):', grade[-1:])
print('grade[-2:] (最後兩個元素):', grade[-2:])
print('grade[-2:-1] (倒數第 2 到倒數第 1 前):', grade[-2:-1])
