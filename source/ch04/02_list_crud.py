# 02_list_crud.py - List 元素的新增、修改與刪除 (CRUD)

# 1. 基本增刪改查
aList = [1, 2, 'a', 'b']
aList.append('d')  # 新增
print('append 後:', aList)
aList.remove('a')  # 刪除
print('remove 後:', aList)
aList[0] = 100     # 修改
print('修改第一個元素後:', aList)
print('查詢索引 2:', aList[2])

# 2. 新增方法的比較: append, extend, insert
students = ['01-nick', '02-albert', '03-jie']
st = ['04-jason', '05-allen']

# append 單一元素
students.append('06-lisa')
print('append 06-lisa 後:', students)

# extend 合併另一個 list
students = ['01-nick', '02-albert', '03-jie']
students.extend(st)
print('extend st 後:', students)

# append 另一個 list (作為單一巢狀元素)
students = ['01-nick', '02-albert', '03-jie']
students.append(st)
print('append st 後:', students)

# insert 指定位置插入
students = ['01-nick', '02-albert', '03-jie']
students.insert(0, '07-maggie')
print('在位置 0 insert 後:', students)

# 3. 刪除方法: remove vs pop
students = ['nick', 'albert', 'jie']
st_copy = students.copy()

students.remove('nick')
print('remove nick 後:', students)

students = st_copy.copy()
popped_val = students.pop()  # 取出並移除最後一個
print('pop 最後一個:', popped_val, '剩餘:', students)

students = st_copy.copy()
popped_first = students.pop(0)  # 取出並移除第一個
print('pop(0) 第一個:', popped_first, '剩餘:', students)
