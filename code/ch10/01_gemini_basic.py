# 01_gemini_basic.py - Google Gemini API 基礎環境配置與文字生成呼叫

import os
import sys

try:
    import google.generativeai as genai
except ImportError:
    print("[錯誤] 請先安裝 google-generativeai 套件：pip install google-generativeai")
    sys.exit(1)

# 1. 從作業系統環境變數中安全讀取 API Key
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("[提示] 找不到 GEMINI_API_KEY 環境變數！")
    print("請先在終端機執行：export GEMINI_API_KEY=\"你的_API_KEY\" (Windows 請用 set GEMINI_API_KEY=\"...\")")
    print("或在下方手動配置後測試。")
    # 此處保留示範邏輯
    sys.exit(1)

# 2. 配置 API 金鑰
genai.configure(api_key=api_key)

# 3. 初始化 Gemini 1.5 Flash 模型
model = genai.GenerativeModel('gemini-1.5-flash')

# 4. 發送提示詞並獲取回應
prompt = "請用簡單的三句話向大眾解釋什麼是物聯網 (IoT)。"
print(f"使用者提示詞: {prompt}\n")

try:
    response = model.generate_content(prompt)
    print("=== Gemini 回覆 ===")
    print(response.text)
except Exception as e:
    print(f"API 呼叫異常: {e}")
