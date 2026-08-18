Ch10 AI & LLM Applications
===

# Python 人工智慧與大型語言模型 (LLM) 應用

本章將引導你進入最新穎且具顛覆性的技術領域——**生成式 AI (Generative AI)** 與 **大型語言模型 (Large Language Model, LLM)** 的應用開發。我們不僅會探討 Transformer 架構等根本觀念，還會帶領你實作如何使用 Python 整合 **Google Gemini API**，打造具備對話記憶、圖像多模態理解以及具備工具使用能力（Function Calling）的智慧 Agent。

本章包含以下核心單元：
* **10.1 大型語言模型 (LLM) 核心學術觀念**：學習 Transformer 架構、Self-Attention、Token 計費模型與超參數控制（溫度、Top-P、Top-K）。
* **10.2 Google Gemini API 快速入門**：安裝 SDK、設定 API Key 與建立基礎文本生成程式。
* **10.3 實務對話與多模態開發**：實作 Streaming 串流輸出、多輪對話歷史記憶（Chat Session）以及影像多模態分析。
* **10.4 結構化輸出與工具調用 (Function Calling)**：強制輸出 JSON 格式、設計自訂 Python 函數供模型呼叫。
* **10.5 檢索增強生成 (RAG) 基礎觀念與簡易實作**：理解 LLM 如何結合外部專屬知識庫，並用 Python 寫一個小型的記憶體檢索器。
* **10.6 綜合實作專題：終端機多功能 AI 助理**。

---

## 10.1 大型語言模型 (LLM) 核心學術觀念

生成式 AI（特別是 LLM）在近幾年取得了驚人的突破，其背後的核心基石是 2017 年由 Google 提出的 **Transformer 架構**。

### 10.1.1 Transformer 與自注意力機制 (Self-Attention)

傳統的循環神經網路 (RNN) 在處理長文本時，容易遺忘前面的字彙（梯度消失問題）。Transformer 放棄了循環結構，改用**自注意力機制 (Self-Attention)**：
* **自注意力機制**：允許模型在預測下一個 Token 時，**同時關注**輸入段落中所有字彙的關聯度。例如在句子「動物過街，因為牠累了」中，模型能精確計算出「牠」字與前面的「動物」有最高的注意力權重。
* **預測下一個標記 (Next-token Prediction)**：LLM 本質上是一個巨大的「文字接龍」機率模型。給定輸入段落，它會計算所有詞彙在庫中的機率分佈，並挑選出機率最高（或經採樣調整）的詞彙輸出。

### 10.1.2 標記 (Token) 與計費模型

* **Token 的定義**：文字被送入神經網路前，會先透過分詞器 (Tokenizer) 轉換為整數 ID。英文一單字約拆成 1~2 個 Token；中文單字或詞彙會轉成對應 ID。
* **Context Window (上下文窗口)**：指模型單次處理（輸入+輸出）的最大 Token 量。
* **Token 計費方式**：雲端 API 服務通常以「每百萬個 Token (Per 1 Million Tokens)」計算價格，且輸入（Input）與輸出（Output）的費率不同。

### 10.1.3 模型隨機性控制超參數

為了微調模型的答覆風格，我們可以設定以下三個超參數：
1. **溫度 (Temperature)**：數值在 `0.0` 到 `2.0` 之間。控制機率分佈的平滑度。設為 `0.0` 會使模型只挑選機率最高的詞（確定性最高）；設為 `1.0` 以上則使低機率詞彙有機率被選中（創造力與隨機性增加）。
2. **Top-P (Nucleus Sampling, 核心取樣)**：限制模型只在累積機率達到 $P$ 的詞彙候選池中進行取樣（例如 `top_p = 0.9` 意指只篩選出累計機率佔前 90% 的詞彙）。
3. **Top-K**：限制模型只考慮機率最高的前 $K$ 個候選詞。

---

## 10.2 Google Gemini API 快速入門

Google Gemini API 是目前性價比與推理效能極佳的選擇。我們使用 `google-generativeai` 來完成首個呼叫程式。

### 10.2.1 安裝 SDK 與安全金鑰配置

請在終端機中執行：
```bash
pip install google-generativeai
```

#### API 金鑰安全性原則
千萬不要把你的 API 金鑰直接寫在程式碼中（例如 `api_key = "AIzaSy..."`）。如果上傳到 GitHub，你的金鑰會在一分鐘內被盜用刷爆。
**最佳實踐**：使用作業系統環境變數。
* 在終端機執行：`export GEMINI_API_KEY="你的金鑰"`
* 在 Python 程式中讀取此變數。

### 10.2.2 文本生成範例

```python
import google.generativeai as genai
import os

# 1. 配置金鑰 (自動從系統環境變數 GEMINI_API_KEY 取得)
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    # 備用方案：如果未設定環境變數，請在此輸入以進行測試，但請勿提交此檔
    api_key = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=api_key)

# 2. 宣告模型
# 推薦：使用快速且免費額度高的新一代模型 gemini-1.5-flash
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. 呼叫 generate_content
response = model.generate_content("如何用 Python 做簡單的檔案讀寫？請用條列式說明。")
print(response.text)
```

---

### **10.2.3 隨堂測驗 (CCQ 1)**

**問題**

在設計需要嚴謹格式輸出的 AI 資料擷取系統時，超參數中的「溫度 (Temperature)」應該如何設定較為妥當？

A) 設定為高溫（如 1.5），讓模型隨意發揮創意。
B) 設定為低溫（如 0.0 或 0.1），確保模型每次都選擇最穩定、機率最高的詞彙回覆。
C) 溫度參數只與 API 的網路延遲時間有關，對生成格式無影響。
D) 將溫度設為負數（如 -0.5）。

<details>
<summary>點擊查看【隨堂測驗】答案與解析</summary>

**正確答案：B) 設定為低溫（如 0.0 或 0.1），確保模型每次都選擇最穩定、機率最高的詞彙回覆。**

* **解析**：
  * 當溫度設為 0.0 或接近 0.0 時，模型生成文本的隨機性（熵）會被壓到最低，使得回覆傾向於重複性極高且一致的語氣。這對需要穩定 JSON 格式或程式碼生成的應用至關重要，故選 B。

</details>

---

## 10.3 實務對話與多模態開發 (Chat & Multimodality)

在實際應用中，我們經常需要實作更複雜的機制：如 Streaming（打字機效果）、Chat Session（對話記憶）以及分析照片（多模態）。

### 10.3.1 串流輸出 (Streaming Response)

如果回答的文章長度極長，等待 API 全部生成完才回傳會讓使用者覺得程式卡住。我們可以使用 `stream=True` 以串流方式隨時取得生成字元：

```python
import google.generativeai as genai
import os
import sys

genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = "寫一首關於 Python 程式設計之美的小詩。"
response_stream = model.generate_content(prompt, stream=True)

print("開始串流輸出：")
for chunk in response_stream:
    # 使用 sys.stdout.write 讓文字像打字機一樣連續輸出，並立即刷新緩衝區
    sys.stdout.write(chunk.text)
    sys.stdout.flush()
print("\n串流結束。")
```

---

### 10.3.2 具有記憶的多輪對話 (Chat Session)

預設的 `generate_content` 是「無狀態 (Stateless)」的，每一次呼叫都是獨立的。如果需要實現類似 ChatGPT 的聊天記憶，我們需要使用 `start_chat()`，讓 SDK 自動在後台記錄對話歷史：

```python
import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

# 啟動對話 Session，傳入空列表作為初始歷史
chat = model.start_chat(history=[])

# 傳送第一輪訊息
print("User: 你好，我是小明。")
response1 = chat.send_message("你好，我是小明。")
print(f"AI: {response1.text}\n")

# 傳送第二輪訊息，測試模型是否有記憶
print("User: 我的名字叫什麼？")
response2 = chat.send_message("我的名字叫什麼？")
print(f"AI: {response2.text}\n")

# 列印整場對話的歷史記錄
print("=== 對話歷史記錄 ===")
for message in chat.history:
    role = message.role
    text_content = message.parts[0].text
    print(f"角色: {role} -> 內容: {text_content.strip()}")
```

---

### 10.3.3 影像多模態分析 (Multimodal)

Gemini 支援原生多模態。你可以將圖片物件直接傳遞給模型，要求模型對圖片進行描述或回答有關圖片的問題。

```python
import google.generativeai as genai
from PIL import Image
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

# 確保本地有放置圖片，這裡用模擬方式載入
try:
    img = Image.open('sample_diagram.jpg')
    print("成功載入圖片。正在傳送至 Gemini 分析...")
    
    # 將圖片物件與 Prompt 包成 list 傳入
    response = model.generate_content([
        img, 
        "請詳細描述這張圖表中的資料趨勢，並列出三個主要結論。"
    ])
    print(response.text)
except FileNotFoundError:
    print("找不到 'sample_diagram.jpg' 圖片。多模態程式碼架構正確，請確認圖片路徑。")
```

---

### **10.3.4 隨堂測驗 (CCQ 2)**

**問題**

在使用 SDK 開發聊天機器人時，若使用 `chat = model.start_chat()` 初始化連線，下列哪一個描述是錯誤的？

A) 我們可以使用 `chat.send_message()` 來送出新對話，並自動將問答記錄附加到對話歷史中。
B) `chat.history` 物件儲存了目前為止所有的連線歷史對話內容。
C) SDK 會自動在後台跟伺服器保持長連接 (Websocket)，因此不需要處理任何斷線例外。
D) `chat.history` 中的每個訊息物件都包含 `role`（如 user 或 model）與 `parts` 特性。

<details>
<summary>點擊查看【隨堂測驗】答案與解析</summary>

**正確答案：C) SDK 會自動在後台跟伺服器保持長連接 (Websocket)，因此不需要處理任何斷線例外。**

* **解析**：
  * SDK 的 `start_chat()` 與對話紀錄只是在客戶端本地記憶體中維護一個對話歷史列表（List）。
  * 當調用 `send_message()` 時，SDK 會將「歷史記錄 + 新訊息」打包成一併送給 API 伺服器，仍然是走傳統的 HTTP POST 請求。
  * 它並不是建立長連線，若網路不穩依然會拋出異常，開發者仍需用 `try-except` 包裹，故選 C。

</details>

---

## 10.4 結構化輸出與工具調用 (Function Calling)

本節介紹如何將 AI 模型深度融入自動化軟體管線中。

### 10.4.1 強制輸出 JSON 模式 (JSON Mode)

我們在 `generation_config` 中將 `response_mime_type` 指定為 `"application/json"`，即可保證模型必定回傳合法 JSON 字串：

```python
import google.generativeai as genai
import json
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY"))

model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    generation_config={"response_mime_type": "application/json"}
)

prompt = """
請提供三本關於 Python 學習的經典書籍。
並以下列格式的 JSON array 回傳：
[
  {"title": "書名", "author": "作者", "level": "適合等級 (入門/進階)"}
]
"""

response = model.generate_content(prompt)
data = json.loads(response.text) # 安全解析
print(data)
```

### 10.4.2 工具調用 (Function Calling) 實作流程

當模型發現用戶的要求（例如查詢本機計算）時，它會回傳函數名稱與需要傳入的引數。我們的程式在本地執行該函數，並將結果傳回給模型：

```python
import google.generativeai as genai
import os

# 1. 定義一個可在本地執行的計算工具函數
def db_user_query(user_id: str) -> str:
    """查詢資料庫中特定使用者 ID 的專長資訊"""
    # 這裡模擬資料庫查詢
    db = {
        "101": "張小明，專長為半導體電路設計與 Python 科學計算。",
        "102": "李美華，專長為機器學習影像分割與特徵工程。"
    }
    return db.get(user_id, "查無此使用者。")

genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY"))

# 2. 將函數物件包入 tools 清單中傳給 model
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    tools=[db_user_query]
)

chat = model.start_chat(enable_automatic_function_calling=True)
response = chat.send_message("幫我查詢 ID 為 101 的員工專長是什麼？")
print(response.text)
```

---

## 10.5 檢索增強生成 (RAG) 基礎觀念與實作

RAG (Retrieval-Augmented Generation) 架構允許 LLM 讀取外部專屬或私有的知識庫。本節我們不使用外部向量資料庫，而是手動在 Python 中實作一個簡單的記憶體「文件搜尋器」，將搜尋到的內容附加給 Gemini 模型。

```python
import google.generativeai as genai
import numpy as np
import os

# 1. 模擬知識庫文檔
documents = [
    "資工系助教辦公室位於資電大樓 302 室，值班時間為每週二下午 2 點到 5 點。",
    "學期專題報告的截止日期是 2026 年 12 月 20 日中午 12 點，逾期不予收件。",
    "本學期課程評分標準為：期中考 30%、期末考 40%、平時作業與小考佔 30%。"
]

# 2. 定義一個超簡單的關鍵字檢索器
def retrieve_context(query, docs):
    # 簡單搜尋包含關鍵字的句子
    matched_docs = []
    for doc in docs:
        # 分詞模糊匹配
        if any(word in doc for word in ["辦公室", "截止", "評分", "時間", "報告", "標準"] if word in query):
            matched_docs.append(doc)
    return "\n".join(matched_docs) if matched_docs else "未尋找到相關背景資訊。"

# 3. 執行 RAG 發問
query = "請問助教辦公室在哪裡？值班時間是什麼時候？"
context = retrieve_context(query, documents)

# 4. 合成 Prompt 並傳給 Gemini
prompt = f"""
請根據以下背景資料回答用戶的問題。如果背景資料中沒有提到，請回答「我不知道」。

背景資料：
{context}

問題：
{query}
"""

genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(prompt)
print("RAG 生成回答：")
print(response.text)
```

---

## 10.6 本章綜合實作專題

### 專題任務：終端機多功能 AI 助理代理人 (Agent)

**背景說明**：我們將實作一個在終端機運行的多輪對話 AI 助理，並將配置 JSON 輸出與例外處理。

```python
import google.generativeai as genai
import os
import sys

def init_agent():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[警告] 未偵測到環境變數 GEMINI_API_KEY。請設定後再啟動。")
        sys.exit(1)
        
    genai.configure(api_key=api_key)
    
    # 設定系統指令，建立助理的角色人設
    system_prompt = (
        "你是一個親切的資工系導師助教 (Agent)。"
        "請使用繁體中文回覆學生的程式設計問題。"
        "回答時要條理清晰，並在代碼範例中附上中文註解。"
    )
    
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=system_prompt
    )
    return model

def main():
    model = init_agent()
    chat = model.start_chat(history=[])
    
    print("==================================================")
    print("  歡迎使用 Python 資電系 AI 導師助理！(Ch10 專案)")
    print("  請輸入你的程式設計疑問。輸入 'quit' 可關閉連線並退出。")
    print("==================================================")
    
    while True:
        try:
            user_input = input("\n學生 [You] >>> ").strip()
            if not user_input:
                continue
            if user_input.lower() == 'quit':
                print("助教：祝你編譯順利，下次見！")
                break
                
            print("助教正在思考中...", end="", flush=True)
            
            # 使用串流方式，即時在終端機輸出助教的回答
            response_stream = chat.send_message(user_input, stream=True)
            print("\r助教 [AI] >>> ", end="", flush=True)
            
            for chunk in response_stream:
                sys.stdout.write(chunk.text)
                sys.stdout.flush()
            print() # 換行
            
        except Exception as e:
            print(f"\n[連線錯誤] 呼叫 API 時發生異常，請檢查網路或金鑰狀態：{e}")
            break

if __name__ == "__main__":
    main()
```
