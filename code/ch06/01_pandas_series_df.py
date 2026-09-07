# 01_pandas_series_df.py - Pandas Series 與 DataFrame 的建立、定位 (loc/iloc) 與切片

import pandas as pd

# 1. 建立 Series (一維帶標籤陣列)
s = pd.Series([10, 12, 15, 8], index=['Apple', 'Banana', 'Orange', 'Cherry'])
print("Series s:")
print(s)

# 2. 建立 DataFrame (二維資料表)
f = {
    'name': ['Apple', 'Banana', 'Orange', 'Cherry'],
    'price': [10, 12, 15, 8],
    'quantity': [90, 87, 60, 45]
}
df = pd.DataFrame(f)
print("\n預設數字索引 DataFrame:")
print(df)

# 自訂標籤索引 (以 name 欄位作為索引)
df_labeled = pd.DataFrame(f, index=f['name'])
print("\n自訂標籤索引 DataFrame:")
print(df_labeled)

# 3. 欄位與資料擷取 (loc 與 iloc)
# A. 取得欄位
print("\n取得單一欄位 (price):")
print(df_labeled['price']) # 或 df_labeled.price

# B. 標籤定位 (loc) - 依據自訂的 index
print("\n使用 loc 取得單一列 (Apple):")
print(df_labeled.loc['Apple'])
print("\n使用 loc 取得多列 (Apple, Banana):")
print(df_labeled.loc[['Apple', 'Banana']])

# C. 位置定位 (iloc) - 依據 0 開始的數字順序位置
print("\n使用 iloc 取得前兩列 (位置 0 到 1):")
print(df_labeled.iloc[0:2])
print("\n使用 iloc 取得前兩列的 1-2 欄位:")
print(df_labeled.iloc[0:2, 1:3])

# D. 取得頭尾與隨機資料
print("\n前兩筆資料 (head):")
print(df_labeled.head(2))
print("\n後一筆資料 (tail):")
print(df_labeled.tail(1))
print("\n隨機抽樣一筆 (sample):")
print(df_labeled.sample(1))
