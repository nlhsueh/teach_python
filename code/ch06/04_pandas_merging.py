# 04_pandas_merging.py - 資料表合併：直向合併 (concat) 與橫向合併 (merge)

import pandas as pd

# 宣告重置資料的輔助函式，方便演示
def get_demo_data():
    df1 = pd.DataFrame({
        'emp_id': [101, 102, 103],
        'name': ['Nick', 'Albert', 'Jie'],
        'dept': ['IT', 'HR', 'IT']
    })
    df2 = pd.DataFrame({
        'emp_id': [104, 105],
        'name': ['Jason', 'Allen'],
        'dept': ['Sales', 'IT']
    })
    df3 = pd.DataFrame({
        'emp_id': [101, 102, 103],
        'salary': [60000, 55000, 70000]
    })
    return df1, df2, df3

df1, df2, df3 = get_demo_data()
print("df1 (公司部門資料):")
print(df1)
print("\ndf2 (新加入員工):")
print(df2)
print("\ndf3 (薪資資料):")
print(df3)

# 1. 縱向合併 (Concat/Append) - 結構相同，筆數增加
# 注意：在現代 Pandas 中，df.append() 已被廢棄，一律改用 pd.concat()
print("\n縱向合併 (pd.concat):")
merged_vertical = pd.concat([df1, df2], ignore_index=True)
print(merged_vertical)

# 2. 橫向合併 (Merge) - 依據特定的 Key 關聯，欄位增加
print("\n依 emp_id 進行橫向合併 (pd.merge):")
merged_horizontal = pd.merge(df1, df3, on='emp_id')
print(merged_horizontal)
