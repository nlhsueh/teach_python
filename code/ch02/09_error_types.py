# 09_error_types.py
# 知識點：程式錯誤類型（語法錯誤、執行錯誤、邏輯錯誤）與常數宣告最佳實踐

# 1. 語法錯誤 (Syntax Error)
# 說明：程式碼不符合 Python 的語法規則，解析器無法編譯。
# 例如以下程式碼 radius 右側少了一個括號：
# radius = int(input("The radius? ")  # 少了右括號，會引發 SyntaxError
# area = radius * radius * 3.14

# 2. 執行錯誤 (Runtime Error / Execution Error)
# 說明：程式語法完全正確，但執行時因為特定輸入或環境引發錯誤崩潰。
# 比如我們把輸入轉為 int，但使用者卻輸入了浮點數 "1.1"：
print("--- 模擬執行期錯誤 (Runtime Error) ---")
print("提示：如果在此處輸入 '1.1'，int() 無法解析將會引發 ValueError 崩潰。")
user_input = input("請輸入一個整數半徑 (輸入 1.1 可測試錯誤，或按 Enter 跳過): ")
if user_input:
    try:
        radius = int(user_input)
        area = radius * radius * 3.14
        print(f"半徑為 {radius} 的圓面積為: {area}")
    except ValueError as e:
        print(f"引發執行期錯誤：{e}")

# 3. 邏輯錯誤 (Logic Error)
# 說明：程式執行沒有拋出任何錯誤，但計算結果是錯誤的（語意錯誤）。
# 例如：本來要算圓面積 radius * radius * 3.14，卻不小心寫成 radius ** radius * 3.14：
print("\n--- 邏輯錯誤 (Logic Error) 示範 ---")
radius = 2.0
wrong_area = radius ** radius * 3.14  # 誤用 ** 做平方（當半徑為 2 時剛好 wrong_area == 12.56 與正解相同，但半徑為 3 時就會算出錯的答案！）
correct_area = radius * radius * 3.14
print(f"當半徑為 {radius} 時，")
print(f"錯誤的算法 (radius ** radius * 3.14) 算出: {wrong_area}")
print(f"正確的算法 (radius * radius * 3.14) 算出: {correct_area}")

# 4. 更好的程式碼實踐 (使用常數)
# 將 3.14 宣告為一個具名常數 PI，以提高程式的可讀性與維護性：
print("\n--- 良好程式碼實踐 (使用常數) ---")
PI = 3.14159  # 定義常數
radius = 3.0
area = radius * radius * PI
print(f"使用常數 PI ({PI}) 計算半徑 {radius} 的圓面積為: {area}")
