# 05_feature_engineering.py - 特徵工程：特徵標準化與類別獨熱編碼 (One-Hot Encoding)

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

print("=== [1. 類別特徵獨熱編碼 (One-Hot Encoding)] ===")
# 建立包含非數值類別欄位的 DataFrame
df = pd.DataFrame({
    'CustomerID': [101, 102, 103, 104],
    'City': ['Taipei', 'Taichung', 'Kaohsiung', 'Taipei'],
    'Gender': ['Male', 'Female', 'Male', 'Female'],
    'AnnualIncome': [85, 120, 65, 95] # 萬元
})

print("原始表格資料：")
print(df)

# 使用 pandas get_dummies 轉為獨熱編碼
df_encoded = pd.get_dummies(df, columns=['City', 'Gender'], dtype=int)
print("\nOne-Hot 編碼後的表格：")
print(df_encoded)


print("\n=== [2. 數值特徵縮放 (StandardScaler vs MinMaxScaler)] ===")
raw_features = np.array([
    [10.0, 2000.0],
    [20.0, 4000.0],
    [30.0, 6000.0],
    [40.0, 8000.0]
])

# Z-Score 標準化 (平均值 0, 標準差 1)
std_scaler = StandardScaler()
std_scaled = std_scaler.fit_transform(raw_features)

# MinMax 縮放 (縮放至 0 ~ 1 區間)
minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(raw_features)

print("原始特徵矩陣：\n", raw_features)
print("\nStandardScaler (Z-Score 標準化) 結果：\n", std_scaled)
print("\nMinMaxScaler (0~1 縮放) 結果：\n", minmax_scaled)
