# 06_input_output_format.py
# 知識點：使用者輸入、字串格式化輸出、排版對齊、逃脫字元與前綴字串

# 1. 取得使用者輸入與型態轉換
print("--- 使用者輸入與轉型 ---")
# 示範 1：正常輸入並進行整數轉型
name = input("你的姓名? ")
# 提示：為了使學生執行時不卡住，可搭配預設的邏輯
# 以下將輸入的字串進行轉型
year_str = input("你的出生年 (例如 2000)? ")
try:
    year = int(year_str)
    age = 2023 - year
    print('{} 的年齡是 {} 歲'.format(name, age))
except ValueError:
    print("輸入的年份必須是數字！")

# 2. 透過 split() 與 eval() 一次接收多個輸入
print("\n--- 接收多個輸入 ---")
multi_input = input("輸入兩個數字（以空白隔開，例如 10 20）: ")
if multi_input:
    # 透過 split 做解析
    parts = multi_input.split()
    if len(parts) >= 2:
        num1, num2 = int(parts[0]), int(parts[1])
        print(f"num1 = {num1}, num2 = {num2}, 和為 {num1 + num2}")

# 使用 eval() 接收以逗號隔開的輸入
eval_input = input("輸入兩個數字（以逗號隔開，例如 10,20）: ")
if eval_input:
    try:
        x, y = eval(eval_input)
        print(f"eval 解析結果: x = {x}, y = {y}, 相乘為 {x * y}")
    except Exception as e:
        print("eval 解析失敗:", e)

# 3. 各種輸出方式與格式化 (Formatting)
print("\n--- 格式化輸出 ---")
name = "Nick"
age = 23
print(name, age) # 簡單的輸出

# 方法 A：% 格式化連結 (舊式寫法，%s 為字串，%d 為整數)
print("%s 的年齡是 %d 歲" % (name, age))

# 方法 B：format() 函式連結
print("{} 的年齡是 {} 歲".format(name, age))

# 方法 C：f-string 格式化 (Python 3.6+ 推薦寫法)
print(f"{name} 的年齡是 {age} 歲")

# 4. 輸出排版與對齊
print("\n--- 排版與對齊 ---")
# 靠右對齊，寬度 5 格 (整數)
print("靠右對齊 (5格): '%5d'" % 12)
# 靠左對齊，寬度 5 格 (整數)
print("靠左對齊 (5格): '%-5d'" % 12)

# 浮點數寬度與小數位數設定
print("浮點數格式化 '%8.2f': '%8.2f'" % 3.14159) # 寬度 8，小數 2 位，靠右
print("浮點數格式化 '%-8.2f': '%-8.2f'" % 3.14159) # 寬度 8，小數 2 位，靠左

# 使用 format() 的排版
print("\nformat() 排版對齊：")
print("整數右對齊 (5格): '{:>5d}'".format(12))
print("整數左對齊 (5格): '{:<5d}'".format(12))
print("浮點數: '{:8.2f}'".format(3.14159))
print("字串左對齊 (10格): '{:<10s}'".format("hello"))

# 5. 逃脫字元 (Escape Characters)
print("\n--- 逃脫字元 ---")
print("換行符號 \\n:\n第一行\n第二行")
print("Tab鍵 \\t:\t欄位1\t欄位2")
print("反斜線 \\\\: c:\\users\\nick")

# 6. 字串前綴 (r 與 f)
print("\n--- 字串前綴 ---")
# r 原始字串 (raw string) -> 不解析裡面的反斜線逃脫字元
print(r"raw string (r 前綴): first line\nsecond line")
# f 格式化字串 (f-string)
hero = "Batman"
print(f"f-string (f 前綴): I am {hero}")
