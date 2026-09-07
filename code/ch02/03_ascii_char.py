# 03_ascii_char.py
# 知識點：電腦內部編碼 ASCII 與字元轉換 (ord 與 chr)

# 1. 使用 ord() 查詢字元的 Unicode 編碼 (整數值)
print(f"字元 'A' 的編碼是: {ord('A')}")  # 65
print(f"字元 'a' 的編碼是: {ord('a')}")  # 97
print(f"字元 '1' 的編碼是: {ord('1')}")  # 49
print(f"字元 '嗨' 的編碼是: {ord('嗨')}") # 21995

# 2. 使用 chr() 將編碼值轉回字元
print(f"編碼 66 對應的字元是: {chr(66)}")      # 'B'
print(f"編碼 21996 對應的字元是: {chr(21996)}")  # '嗨'

# 3. 實際應用：字元運算（取得下一個字母）
current_char = 'C'
current_code = ord(current_char)  # 67
next_code = current_code + 1      # 68
next_char = chr(next_code)        # 'D'
print(f"'{current_char}' 的下一個字母是 '{next_char}'")

# 4. 隨堂練習：利用 ord()、chr() 與迴圈印出 a-z 26 個字母
print("\n--- 印出 a-z 26 個字母與其編碼 ---")
a_code = ord('a')
print('The ASCII code of a is ', str(a_code))
for i in range(a_code, a_code + 26):
    print(chr(i), end=' ')
print()  # 換行
