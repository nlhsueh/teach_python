# 05_string_operations.py
# 知識點：字串基本運算與常用字串函式

# 1. 字串基本運算子
print("--- 字串基本運算 ---")
hello = "Hello" + ", " + "World"    # '+' 用於字串相加 (結合)
print("結合:", hello)
name = "Nick"
print("重複 (*3):", name * 3)       # '*' 用於重複字串
print("成員檢查 ('N' in name):", 'N' in name)  # True
print("成員檢查 ('J' in name):", 'J' in name)  # False

s = "0123456789"
print("字串索引 s[5]:", s[5])       # '5' (索引從 0 開始)
print("字串切片 s[3:6]:", s[3:6])   # '345' (包含索引 3，不包含索引 6)

# 2. 常用字串函式
print("\n--- 常用字串函式 (1) ---")
hello = "Hello, Nick"
h1 = hello.upper()                  # 全轉大寫
h2 = hello.lower()                  # 全轉小寫
h3 = hello.replace('Hello', 'Hi')   # 字串替換
print('upper():', h1)
print('lower():', h2)
print('replace():', h3)
print('注意：字串本身的值不會改變:', hello)

# 3. 更多字串函式與範例
print("\n--- 常用字串函式 (2) ---")
s_val = "I like Python"
print("lower():", s_val.lower())                 # "i like python"
print("upper():", s_val.upper())                 # "I LIKE PYTHON"
print("startswith('I'):", s_val.startswith('I')) # True
print("endswith('python'):", s_val.endswith('python')) # False (大小寫須相符)
print("isdigit():", s_val.isdigit())             # False
print("find('like'):", s_val.find('like'))       # 2 (尋找子字串起始位置)
print("find('hate'):", s_val.find('hate'))       # -1 (找不到回傳 -1)
print("replace('like', 'love'):", s_val.replace('like', 'love')) # "I love Python"

# 4. 字串切分 split()
print("\n--- 字串切分 split() ---")
print("s_val.split(' '):", s_val.split(' '))     # ['I', 'like', 'Python'] (以空格切分)
print("s_val.split():", s_val.split())           # ['I', 'like', 'Python'] (預設以空白切分)
print("s_val.split(','):", s_val.split(','))     # ['I like Python'] (找不到 delimiter 時回傳單一元素串列)
