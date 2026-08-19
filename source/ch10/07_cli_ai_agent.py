# 07_cli_ai_agent.py - 綜合實作專題：終端機多功能 AI 助教代理人 (CLI AI Agent)

import os
import sys

try:
    import google.generativeai as genai
except ImportError:
    print("[錯誤] 請先安裝 google-generativeai 套件：pip install google-generativeai")
    sys.exit(1)

def run_cli_agent():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("=" * 60)
        print("[提示] 請先設定 GEMINI_API_KEY 環境變數以啟用 AI 助教！")
        print("設定方法：")
        print("  macOS/Linux: export GEMINI_API_KEY=\"你的_API_KEY\"")
        print("  Windows:     set GEMINI_API_KEY=\"你的_API_KEY\"")
        print("=" * 60)
        sys.exit(1)
        
    genai.configure(api_key=api_key)
    
    # 定義系統提示詞 (System Instruction)，強制規範助教行為模式與引導風格
    helper_instruction = """
    你是一位專業且耐心的 Python 程式設計課程助教。你的任務是協助資電學院的大一與大二學生學習 Python。
    當學生提出程式問題或貼上錯誤代碼時：
    1. 不要直接給出完整的正確答案或寫好的程式碼。
    2. 引導學生思考程式中的邏輯漏洞，指出可疑行號並給予思考方向。
    3. 語氣必須親切、帶有鼓勵性，使用繁體中文 (正體中文) 回答。
    """
    
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=helper_instruction
    )
    
    # 建立多輪對話工作階段 (Session)
    chat = model.start_chat(history=[])
    
    print("=" * 55)
    print("  🎓 Python 程式設計課程 - CLI AI 助教代理人已上線")
    print("  輸入 'exit' 或 'quit' 可退出對話")
    print("=" * 55)
    
    while True:
        try:
            user_input = input("\n[學生] >>> ").strip()
            if not user_input:
                continue
            if user_input.lower() in ['exit', 'quit']:
                print("\n[助教] 再見！程式設計路上繼續加油！祝學習愉快！")
                break
                
            print("\n[助教] 回答中：", end="", flush=True)
            
            # 呼叫串流發送 (Stream)，展現即時打字機效果
            response = chat.send_message(user_input, stream=True)
            for chunk in response:
                print(chunk.text, end="", flush=True)
            print()
            
        except KeyboardInterrupt:
            print("\n\n[助教] 系統結束連線，祝學習順利！")
            break
        except Exception as e:
            print(f"\n[系統錯誤] 發生異常：{e}")
            break

if __name__ == '__main__':
    run_cli_agent()
