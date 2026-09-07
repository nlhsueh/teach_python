# 04_json_mode_structured.py - 結構化輸出：強制 JSON 模式 (JSON Mode)

import os
import sys
import json

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

prompt = "請隨機列出三個台北市的知名景點，並回傳成一個 JSON 陣列，每個元素包含：name, type, description。"

print(f"發送結構化要求: {prompt}\n")

# 配置輸出格式為 application/json，強制模型只輸出合法 JSON 格式
response = model.generate_content(
    prompt,
    generation_config={"response_mime_type": "application/json"}
)

raw_json = response.text
print("=== 獲得的原始 JSON 字串 ===")
print(raw_json)

# 使用 Python 內建 json 解析
try:
    data = json.loads(raw_json)
    print("\n=== 解析後的 Python List/Dict 物件 ===")
    for i, place in enumerate(data, 1):
        print(f"{i}. 景點: {place.get('name')} | 類別: {place.get('type')}")
        print(f"   介紹: {place.get('description')}\n")
except json.JSONDecodeError as e:
    print(f"JSON 解析失敗: {e}")
