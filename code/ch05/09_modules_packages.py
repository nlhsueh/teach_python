# 09_modules_packages.py - 套件套用與 YouTube 檔案下載範例

# 1. 不同的匯入語法
# A. 直接 import 整個模組
import time
print("目前時間戳:", time.time())

# B. 匯入模組內的特定功能
from math import sqrt, pi
print("9 的平方根:", sqrt(9))
print("圓周率 pi:", pi)

# C. 帶別名匯入 (Alias)
import json as js
print("JSON 格式化轉字串:", js.dumps({"eng": 100}))

# 2. 應用範例：YouTube 下載程式說明 (使用 pytubefix 套件)
# 注意：以下程式需要安裝 pytubefix 套件才能執行
# 可在終端機中執行：pip install pytubefix
# 
# ```python
# from pytubefix import YouTube
# 
# try:
#     # 設定欲下載之 YouTube 影片連結
#     url = 'https://youtu.be/KOdfpbnWLVo'
#     yt = YouTube(url)
#     
#     print("影片標題:", yt.title)
#     print("影片長度:", yt.length, "秒")
#     
#     # 取得最高畫質的影片串流
#     stream = yt.streams.get_highest_resolution()
#     print("影片解析度:", stream.resolution)
#     
#     # 執行下載，將影片存於目前目錄下的 output 子目錄中
#     print("開始下載...")
#     stream.download(output_path='output/')
#     print("下載完成！")
# except Exception as e:
#     print("下載出錯:", e)
# ```
