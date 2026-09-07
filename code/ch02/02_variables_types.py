# 02_variables_types.py
# 知識點：變數宣告、基本資料型態、型態檢查與型態轉換

# 1. 變數的命名與宣告方式
x = 100
y = 200
# r = 100 s = 200  # 語法錯誤：不能直接並列，需換行或以分號隔開
z = 100; w = 200   # 以分號區隔多個敘述句
p = q = 100        # 多重賦值（多個變數指向同一個值）
name, eng, math, phy = "Nick", 92, 88, 32  # 多變數同時宣告與賦值

# 有意義的命名範例
grade = 100
temperature = 8.9
name = "John"
teacher_name = 'Nick'
is_teacher = True
get_pass = False

# 2. Python 常見的基本變數型態
student_count = 40                  # 整數 (int)
score = -5                          # 整數 (int)
pi = 3.14159                        # 浮點數 (float)
temperature = 26.5                  # 浮點數 (float)
school_name = "逢甲大學"             # 字串 (str)
motto = 'Life is short, use Python.'# 字串 (str)
is_registered = True                # 布林值 (bool)
has_error = False                   # 布林值 (bool)

# 3. 為什麼需要變數型態？型態不同會影響運算的行為：
a = 1
b = 2
print("數字相加 (1 + 2):", a + b)     # 輸出 3

a_str = '1'
b_str = '2'
print("字串相連 ('1' + '2'):", a_str + b_str)  # 輸出 '12'
# print(a_str / b_str)  # Error! 字串型態無法進行除法運算

# 4. 檢查型態 (type 與 isinstance)
print("\n--- 檢查變數型態 ---")
print("grade 型態:", type(grade))            # <class 'int'>
print("temperature 型態:", type(temperature))  # <class 'float'>
print("None 型態:", type(None))               # <class 'NoneType'>

print("檢查 grade 是否為 int:", type(grade) == int)       # True
print("檢查 grade 是否為 float:", isinstance(grade, float)) # False
print("檢查 'two' 是否為 str:", isinstance('two', str))     # True
print("檢查 2==2 是否為 bool:", isinstance(2 == 2, bool))    # True

# 5. 型態轉換 (Type Casting)
print("\n--- 型態轉換 ---")
print("整數轉浮點數 float(2):", float(2))      # 2.0
print("浮點數轉整數 int(2.9):", int(2.9))      # 2 (無條件捨去小數)
print("浮點數轉字串 str(2.9):", str(2.9))      # '2.9'

# 布林值轉換規則：數值零、None、空容器會被轉換為 False
print("bool(0):", bool(0))          # False
print("bool(None):", bool(None))    # False
print("bool(''):", bool(''))        # False (空字串)
print("bool([]):", bool([]))        # False (空串列)

# 非空容器與非零數值會被轉換為 True
print("bool(2):", bool(2))          # True
print("bool('two'):", bool('two'))  # True
print("bool([2]):", bool([2]))      # True
