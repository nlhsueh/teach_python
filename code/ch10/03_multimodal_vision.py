# 03_multimodal_vision.py - 多模態分析：傳入圖片與文字進行視覺理解 (Multimodality)

import os
import sys
from PIL import Image

try:
    import google.generativeai as genai
except ImportError:
    print("[錯誤] 請先安裝 google-generativeai 套件：pip install google-generativeai")
    sys.exit(1)

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("[錯誤] 請先設定 GEMINI_API_KEY 環境變數！")
    sys.exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 1. 建立一個模擬的純色圖像 (300x200 像素，深天藍色)
img = Image.new('RGB', (300, 200), color=(14, 165, 233))

# 2. 呼叫多模態內容生成 (同時傳入文字提示詞與 PIL 影像物件)
prompt = "這是一張圖片，請告訴我這張圖片的主色調是什麼？並用英文形容這種藍色給人什麼感覺。"
print(f"發送多模態請求: 文字 + 圖像物件...")

try:
    response = model.generate_content([prompt, img])
    print("\n=== 多模態圖片分析結果 ===")
    print(response.text)
except Exception as e:
    print(f"多模態呼叫失敗: {e}")
