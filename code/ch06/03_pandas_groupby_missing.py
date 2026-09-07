# 03_pandas_groupby_missing.py - 分組聚合 (GroupBy)、遺失值處理 (dropna/fillna) 與現代型態轉換

import pandas as pd
import numpy as np

# 1. 分組聚合 (GroupBy)
student_data = pd.DataFrame({
    'class': ['A', 'A', 'B', 'B', 'C', 'C'],
    'sex': ['boy', 'girl', 'boy', 'girl', 'boy', 'girl'],
    'score': [90, 85, 78, 92, 60, 72]
})
print("學生班級成績表:")
print(student_data)

# 計算各班的平均成績
print("\n各班的平均成績:")
print(student_data.groupby('class')['score'].mean())

# 多層分組 (依班級和性別分組)
print("\n依班級與性別加總分數:")
print(student_data.groupby(['class', 'sex'])['score'].sum())

# 2. 遺失值處理 (NaN)
missing_data = pd.DataFrame({
    'name': ['A', 'B', 'C', 'D', 'E'],
    'price': [10.0, 12.0, np.nan, 30.0, np.nan],
    'quantity': [90.0, 87.0, 60.0, 45.0, np.nan]
}, index=['A', 'B', 'C', 'D', 'E'])
print("\n含缺失值 (NaN) 的原始資料:")
print(missing_data)

# 策略一：刪除含有空值的列 (dropna)
print("\n刪除含有 NaN 的列 (dropna axis=0):")
print(missing_data.dropna(axis=0))

# 策略二：填補空值 (fillna)
# 用 dict 指定不同欄位的填補值
replace_values = {'price': 10, 'quantity': 40}
print("\n填補空值後的資料 (fillna):")
print(missing_data.fillna(value=replace_values))

# 3. 現代型態轉換 (convert_dtypes)
# 將內建型態自動轉換為 modern Nullable 型態 (例如 float 轉成帶空值的 Int64)
print("\n傳統資料型態:")
print(missing_data.dtypes)
print("\n轉換為現代原生 Nullable 型態 (convert_dtypes):")
print(missing_data.convert_dtypes().dtypes)
