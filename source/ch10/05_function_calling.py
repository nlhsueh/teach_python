# 05_function_calling.py - 工具調用 (Function Calling) 機制與 Python 本地函式掛載

import os
import sys

try:
    import google.generativeai as genai
except ImportError:
    print("[錯誤] 請先安裝 google-generativeai 套件：pip install google-generativeai")
    sys.exit(1)

# 1. 定義本地工具函數 (Python 函數)
def get_current_weather(location: str) -> str:
    """取得指定城市的即時天氣資訊。
    
    Args:
        location: 城市名稱，例如 'Taipei', 'Kaohsiung', 'Tokyo'
    """
    # 模擬查詢氣象 API
    weather_db = {
        "taipei": "台北目前氣溫 28°C，陰天有短暫陣雨，濕度 75%",
        "kaohsiung": "高雄目前氣溫 32°C，晴空萬里，紫外線指數強",
        "tokyo": "東京目前氣溫 20°C，多雲舒適"
    }
    loc_clean = location.lower().strip()
    return weather_db.get(loc_clean, f"{location} 目前氣溫 25°C，天氣晴")

def calculate_gpa(scores: list) -> str:
    """計算學生平均分數與等第。
    
    Args:
        scores: 各科成績的數字清單，如 [85, 92, 78]
    """
    if not scores:
        return "無成績資料"
    avg = sum(scores) / len(scores)
    grade = "A+" if avg >= 90 else "A" if avg >= 80 else "B" if avg >= 70 else "C"
    return f"平均成績為 {avg:.1f} 分，學期總評等為 {grade}"

if __name__ == '__main__':
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("=== [Function Calling 概念演示 (本地模擬)] ===")
        print("未設定 GEMINI_API_KEY，以下展示本地工具執行結果：")
        print("1. 查詢高雄天氣:", get_current_weather("Kaohsiung"))
        print("2. 計算學期 GPA:", calculate_gpa([92, 85, 78]))
        sys.exit(0)

    genai.configure(api_key=api_key)
    
    # 2. 將 Python 函數作為 tools 傳遞給 GenerativeModel
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        tools=[get_current_weather, calculate_gpa]
    )

    # 3. 啟動支援自動調用工具的對話
    chat = model.start_chat(enable_automatic_function_calling=True)
    
    prompt = "請問高雄現在天氣如何？另外如果我三科成績是 92, 85, 78 分，我的平均成績和評等是多少？"
    print(f"使用者詢問: {prompt}\n")
    
    response = chat.send_message(prompt)
    print("=== Gemini 經由 Function Calling 整合後的回答 ===")
    print(response.text)
