# 06_exception_handling.py - 例外處理 try-except-else-finally 結構與主動拋出 raise

import time

# 1. 基礎 try-except-else-finally 與除以 0 異常
def test_div(a, b):
    try:
        print("--- 開始運算 ---")
        result = a / b
    except ZeroDivisionError as e:
        print("補獲除以 0 的錯誤:", e)
        result = None
    else:
        print("沒有發生錯誤，順利執行！")
    finally:
        print("無論有無錯誤，此區塊皆會執行。")
    return result

print("結果 1:", test_div(10, 2))
print("結果 2:", test_div(10, 0))

# 2. 檔案讀取的例外處理
t1 = time.time()
try:
    f = open('data/non_existent.txt', 'r')
    line = f.readline()
    print('讀取成功')
except FileNotFoundError:
    print("找不到指定的檔案！")
except ZeroDivisionError:
    # 也可以補獲其他類型的錯誤
    print("除以 0 的錯誤")
else:
    # 沒有發生錯誤時執行
    print(line)
    f.close()
finally:
    # 不管有沒有錯誤都記錄結束時間
    t2 = time.time()
    print("檔案處理處理總時間:", round(t2 - t1, 4), "秒")

# 3. 使用 raise 主動拋出例外
def set_age(age):
    if age < 0 or age > 150:
        raise ValueError("不合法的年齡範圍，年齡必須介於 0 至 150 之間")
    print(f"年齡設定為: {age}")

try:
    set_age(200)
except ValueError as e:
    print("補獲主動拋出的錯誤:", e)
