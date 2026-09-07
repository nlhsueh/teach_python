# 08_dict_basic_crud.py - 字典 Dict 的建立與基本 CRUD 操作

# 1. 建立
empty_d1 = {}
empty_d2 = dict()
family = {'dad': 'Jack', 'mom': 'LiLi', 'size': 2}
print('家庭字典:', family)

# 2. 新增、修改與刪除
grade = {1: 12, 2: 100, 3: 90}
grade[4] = 30  # 新增
print('新增 4 號成績後:', grade)

del grade[3]  # 刪除方式 1: del
print('del 3 號後:', grade)

popped_val = grade.pop(4)  # 刪除方式 2: pop (取出並移除)
print('pop 4 號後:', grade, '被 pop 出的值:', popped_val)

grade[2] = 95  # 修改 (覆蓋原有鍵值)
print('修改 2 號成績後:', grade)

# 3. 查詢與方法
simpleDict = {'book': '書籍', 'pen': '筆'}
print('所有的 Keys:', list(simpleDict.keys()))
print('所有的 Values:', list(simpleDict.values()))
print('所有的 Items:', list(simpleDict.items()))
print('字典長度 (鍵值對個數):', len(simpleDict))
