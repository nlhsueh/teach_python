# 06_youbike_analysis.py - 應用案例：新北市 YouBike 資料篩選與視覺化

import pandas as pd

# 本程式說明在 Jupyter/Colab 下，讀入並處理 YouBike 資料之過程。
# 請注意：欲正確執行本程式，需將 'youbike_newTPE.csv' 放置在 data/ 目錄下。

# 模擬檔案路徑
file_path = 'data/youbike_newTPE.csv'

print("--- YouBike 資料分析與操作演示 ---")
print("1. 程式會使用 pd.read_csv(file_path, header=0, dtype={'sno': str}) 讀取資料表。")
print("   - sno 代表站點編號，指定為字串避免自動轉為整數。")
print("2. 進行篩選 (例如：板橋區且可借車輛數 > 20 的站點):")
print("   - query = df[(df.sarea == '板橋區') & (df.sbi > 20)]")
print("3. 分組統計 (例如：計算各行政區的 YouBike 站點數量):")
print("   - station_counts = df.groupby('sarea')['sno'].count()")
print("4. 繪製條狀圖與圓餅圖呈現各區分布。")

# 以下提供在資料就緒時的實際執行程式碼參考，目前以 Try-Except 封裝，
# 即使檔案未下載也不會使程式崩潰：
try:
    df = pd.read_csv(file_path, header=0, dtype={'sno': str})
    print("\n[讀取成功] 資料前三筆如下:")
    print(df.head(3))
    
    # 各區站點統計
    counts = df.groupby('sarea')['sno'].count().sort_values(ascending=False)
    print("\n[統計] 各行政區站點數量前五名:")
    print(counts.head(5))
    
    # 篩選板橋區站點
    banqiao = df[df.sarea == '板橋區']
    print(f"\n[篩選] 板橋區總站點數: {len(banqiao)}")
except Exception as e:
    print(f"\n[提示] 欲執行實際檔案解析，請將 YouBike CSV 檔案置於該目錄中。錯誤原因: {e}")
