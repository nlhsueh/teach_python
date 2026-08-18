# 05_pandas_plotting.py - Pandas 資料視覺化基本操作與圖表繪製

import pandas as pd
import matplotlib.pyplot as plt

# 1. 準備繪圖數據 (學生成績)
score_data = pd.DataFrame({
    'name': ['John', 'Nick', 'Albert', 'Jie', 'Lisa'],
    'eng': [12, 90, 77, 44, 85],
    'math': [23, 91, 88, 55, 90],
    'phy': [43, 92, 99, 66, 95]
}, index=['John', 'Nick', 'Albert', 'Jie', 'Lisa'])

# 由於無 GUI 伺服器通常無法直接彈出視窗，以下將各個圖表範例註解，
# 學生可以在 Colab 或本地有安裝畫圖環境 (如 Jupyter) 執行：
"""
# A. 折線圖 (Line Plot)
score_data['eng'].plot(title="English Scores Line Chart")
plt.xlabel("Students")
plt.ylabel("Score")
plt.show()

# B. 條狀圖 (Bar Chart)
score_data.plot.bar(figsize=(10, 5), title="Scores Bar Chart")
plt.ylabel("Score")
plt.show()

# C. 橫向分組條狀圖 (Horizontal Bar Chart with Subplots)
score_data[['eng', 'math']].plot.barh(subplots=True, figsize=(8, 6))
plt.show()

# D. 直方圖 (Histogram) - 呈現成績區間分佈
score_data['eng'].plot.hist(bins=5, title="English Scores Distribution")
plt.show()

# E. 圓餅圖 (Pie Chart)
gender_ratio = pd.Series([3, 2], index=['boy', 'girl'])
gender_ratio.plot.pie(autopct='%.2f%%', title="Gender Ratio")
plt.show()

# F. 箱型圖 (Boxplot) - 比較各科成績離散度
score_data.boxplot(column=['eng', 'math', 'phy'])
plt.show()
"""
print("已成功載入繪圖範例資料：")
print(score_data)
print("\n在 Jupyter 或 Colab 中執行時，可取消對應的 plt.show() 程式段註解以觀察視覺化結果。")
