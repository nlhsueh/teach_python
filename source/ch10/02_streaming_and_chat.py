# 02_streaming_and_chat.py - 串流輸出 (Streaming 打字機效果) 與多輪對話歷史 (Chat Session)

import os
import sys

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

# 1. 串流輸出示範 (Streaming Response)
print("=== [1. 串流輸出示範 (打字機效果)] ===")
prompt = "請寫一首關於機器人學習彈鋼琴的短詩（四句）。"
print(f"提示詞: {prompt}\n")

response_stream = model.generate_content(prompt, stream=True)
for chunk in response_stream:
    # end="" 確保不額外換行，flush=True 確保終端機即時沖刷輸出緩衝區
    print(chunk.text, end="", flush=True)
print("\n" + "=" * 40 + "\n")


# 2. 多輪對話記憶示範 (Chat Session)
print("=== [2. 多輪對話記憶示範 (Chat Session)] ===")
# 啟動具有歷史記憶的 Session
chat = model.start_chat(history=[])

# 第 1 輪
msg1 = "哈囉！我是輔仁大學電機系一年級的學生張小明。"
print(f"[學生] {msg1}")
res1 = chat.send_message(msg1)
print(f"[Gemini] {res1.text}\n")

# 第 2 輪 (未提及姓名與科系，測試模型記憶)
msg2 = "請幫我規劃適合我目前科系的 Python 學習方向。"
print(f"[學生] {msg2}")
res2 = chat.send_message(msg2)
print(f"[Gemini] {res2.text}")
