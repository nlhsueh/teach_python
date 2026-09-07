# 07_file_io.py
# 知識點：讀寫文字檔與 with open 的用法

# 1. 寫入檔案：with 的用法
# 執行後會建立一個 grade.txt 檔案，並寫入張三與李四的成績
print("--- 寫入 grade.txt ---")
with open("grade.txt", "w", encoding="utf-8") as f:
    print('張三', file=f)
    print('100, 20, 40', file=f)
    print('李四', file=f)
    print('90, 50, 100', file=f)
print("grade.txt 寫入完成！")

# 2. 讀取檔案與處理數據：readline()
print("\n--- 讀取 grade.txt 並計算平均 ---")
try:
    with open("grade.txt", "r", encoding="utf-8") as f2:
        # 讀取第一個學生的資料 (張三)
        st1 = f2.readline().replace('\n', '')     # 讀取姓名並去除換行符號
        # 透過 eval() 將字串 '100, 20, 40' 轉換成三個數字
        st1a, st1b, st1c = eval(f2.readline())
        st1d = (st1a + st1b + st1c) / 3           # 計算平均
        print("{} 的國英數成績是: {}, {}, {}, 平均為: {:5.1f}".format(st1, st1a, st1b, st1c, st1d))

        # 讀取第二個學生的資料 (李四)
        st2 = f2.readline().replace('\n', '')     # 讀取姓名並去除換行符號
        st2a, st2b, st2c = eval(f2.readline())
        st2d = (st2a + st2b + st2c) / 3           # 計算平均
        print("{} 的國英數成績是: {}, {}, {}, 平均為: {:5.1f}".format(st2, st2a, st2b, st2c, st2d))
except FileNotFoundError:
    print("找不到 grade.txt 檔案，請確認是否已成功寫入。")
