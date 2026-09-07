# 03_list_loops_functions.py - List 走訪、常用統計函式與二維/巢狀 List

# 1. 走訪與統計運算
students = ['nick', 'albert', 'jie']
for st in students:
    print('學生姓名:', st)

grade = [11, 22, 99, 35, 59]
total = 0
for g in grade:
    total += g
print(f'成績: {grade}, 筆數: {len(grade)}, 平均: {total // len(grade)}')

# 2. 走訪並更新 (使用 enumerate)
grade = [11, 22, 99, 35, 59, 78]
print('調分前:', grade)
for i, g in enumerate(grade):
    if g < 60:
        grade[i] = 60
print('調分後 (不及格者皆調整為 60):', grade)

# 3. 常用內建函式與方法
age = [12, 56, 40]
print(f'年齡列表: {age}, 長度: {len(age)}, 最大值: {max(age)}, 最小值: {min(age)}')
print('students 中 nick 的數量:', students.count('nick'))
print('albert 的索引位置:', students.index('albert'))

# 4. 二維 List 與雙重迴圈
grade_matrix = [[11, 22, 33], [44, 55, 66], [77, 88, 99], [90, 91, 92]]
print('取得學生 2 的成績列表 (grade_matrix[2]):', grade_matrix[2])
print('取得學生 2 的第一個科目成績 (grade_matrix[2][0]):', grade_matrix[2][0])

print('雙重迴圈遍歷二維 List:')
for row in grade_matrix:
    for element in row:
        print(element, end=' ')
    print()

print('使用 enumerate 輸出帶座標的二維 List:')
for i, row in enumerate(grade_matrix):
    for j, element in enumerate(row):
        print(f'grade[{i}][{j}]={element}', end='; ')
    print()

# 5. 二維 List 橫向與縱向加總
# 橫向：計算每個學生的各科總和
st_sum = [0, 0, 0, 0]
for idx, st in enumerate(grade_matrix):
    st_sum[idx] = sum(st)
print('每個學生的各科總和:', st_sum)

# 縱向：計算每個科目的總和
subj_sum = [0, 0, 0]
for st in grade_matrix:
    for i, g in enumerate(st):
        subj_sum[i] += g
print('每個科目的總和分別為:', subj_sum)
