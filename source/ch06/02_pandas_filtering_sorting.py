# 02_pandas_filtering_sorting.py - Pandas 資料過濾 (布林索引) 與排序

import pandas as pd

f = {
    'name': ['Apple', 'Banana', 'Orange', 'Cherry'],
    'price': [10, 12, 15, 8],
    'quantity': [90, 87, 60, 45]
}
df = pd.DataFrame(f, index=f['name'])

# 1. 資料過濾 (Boolean Indexing)
# 價格 > 10 的布林遮罩 (Boolean Mask)
cond = df.price > 10
print("布林遮罩:")
print(cond)

# 傳入遮罩篩選
print("\n篩選出價格大於 10 的水果:")
filtered_df = df[cond] # 等價於 df[df.price > 10]
print(filtered_df)

# 2. 資料排序 (Sorting)
df_unsorted = pd.DataFrame({
    'c1': ['A', 'A', 'B', 'Z', 'D', 'C'],
    'c2': [2, 1, 9, 8, 7, 4],
    'c3': [0, 1, 9, 4, 2, 3],
    'c4': ['a', 'B', 'c', 'D', 'e', 'F']
})
print("\n原始未排序 DataFrame:")
print(df_unsorted)

# 單一欄位排序 (遞增)
print("\n依 c1 欄位遞增排序:")
print(df_unsorted.sort_values(by='c1'))

# 單一欄位排序 (遞減)
print("\n依 c2 欄位遞減排序:")
print(df_unsorted.sort_values(by='c2', ascending=False))

# 多欄位複合排序 (c1 遞增，c1 相同時依 c2 遞增)
print("\n複合排序 (c1, c2):")
print(df_unsorted.sort_values(by=['c1', 'c2']))
