# 07_student_analysis.py - 應用案例：大專院校學生人數資料統計與分析

import pandas as pd

# 本程式演示讀取 '107_student.csv' 大專院校學生人數資料之分析流程。
# 檔案應放置於 data/107_student.csv。

file_path = 'data/107_student.csv'

print("--- 大專院校校別學生數統計演示 ---")
print("1. 讀取 CSV 檔案。")
print("2. 檢查各欄位 (如: 學校名稱, 日間∕進修別, 等級別, 總計, 男生計, 女生計)。")
print("3. 計算全國男女生總人數比例。")
print("4. 使用 GroupBy 計算各縣市的大專院校學生總人數。")

# 模擬檔案分析程式
try:
    # 讀取大專院校資料
    df = pd.read_csv(file_path)
    print("\n[讀取成功] 資料欄位說明:")
    print(df.columns.tolist())
    
    # 進行資料清潔與型態轉換 (去除可能包含逗號的字串數字)
    # df['總計'] = df['總計'].str.replace(',', '').astype(int)
    
    # 篩選日間部學生
    day_students = df[df['日間∕進修別'] == 'D 日']
    print(f"\n[分析] 全國日間部學生總人數: {day_students['總計'].sum()}")
    
    # 依學校類別進行分組統計
    school_type_sum = df.groupby('體系別')['總計'].sum()
    print("\n[分析] 各體系大專院校學生人數加總:")
    print(school_type_sum)
except Exception as e:
    print(f"\n[提示] 欲進行實際統計，請確認 data/107_student.csv 資料已備妥。錯誤原因: {e}")
