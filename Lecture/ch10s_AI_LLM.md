---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #f5f5f5
color: #333
style: |
  section {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    padding: 40px;
    font-size: 24px;
  }
  h1 {
    color: #0b3c5d;
  }
  h2 {
    color: #328cc1;
  }
  footer {
    position: absolute;
    left: 40px;
    bottom: 40px;
    text-align: left;
    font-size: 0.5em;
    color: #777;
  }
  header {
    font-size: 0.5em;
    color: #aaa;
    text-align: right;
  }
  blockquote {
    background: transparent;
    border-left: 4px solid #328cc1;
    margin: 1em 0;
    padding: 5px 20px;
    font-style: italic;
    color: inherit;
    opacity: 0.85;
  }
  blockquote::before {
    content: none !important;
  }
  table {
    font-size: 20px;
  }
  section:has(div.ccq-columns),
  section:has(div.discussion-columns),
  section:has(div.fill-blank-columns) {
    display: flex;
    flex-direction: column;
  }
  div.ccq-columns {
    display: flex;
    align-items: center;
    gap: 30px;
    margin-top: auto;
    margin-bottom: auto;
  }
  div.ccq-text {
    flex: 70%;
  }
  div.ccq-logo {
    flex: 30%;
    text-align: center;
  }
  div.ccq-logo img {
    width: 100%;
    max-width: 180px;
  }
  div.discussion-columns {
    display: flex;
    align-items: center;
    gap: 30px;
    margin-top: auto;
    margin-bottom: auto;
  }
  div.discussion-text {
    flex: 75%;
    font-size: 1.25em;
    line-height: 1.4;
  }
  div.discussion-logo {
    flex: 25%;
    text-align: center;
  }
  div.discussion-logo img {
    width: 100%;
    max-width: 150px;
  }
  div.fill-blank-columns {
    display: flex;
    align-items: center;
    gap: 30px;
    margin-top: auto;
    margin-bottom: auto;
  }
  div.fill-blank-text {
    flex: 75%;
  }
  div.fill-blank-logo {
    flex: 25%;
    text-align: center;
  }
  div.fill-blank-logo img {
    width: 100%;
    max-width: 150px;
  }
  div.split64, div.split46, div.split55 {
    display: flex;
    align-items: center;
    gap: 20px;
  }
  div.split64 > div.left {
    flex: 60%;
  }
  div.split64 > div.right {
    flex: 40%;
    text-align: center;
  }
  div.split64 > div.right img {
    width: 100%;
    max-width: 320px;
  }
  div.split46 > div.left {
    flex: 40%;
  }
  div.split46 > div.right {
    flex: 60%;
    text-align: center;
  }
  div.split46 > div.right img {
    width: 100%;
    max-width: 480px;
  }
  div.split55 > div.left {
    flex: 50%;
  }
  div.split55 > div.right {
    flex: 50%;
    text-align: center;
  }
  div.split55 > div.right img {
    width: 100%;
    max-width: 400px;
  }
  section.full-image-slide {
    padding: 0 !important;
  }
  section.full-image-slide::after {
    display: none !important;
  }
  section.full-image-slide header,
  section.full-image-slide footer {
    display: none !important;
  }
  section.full-image-slide div.centered-image {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 720px;
  }
  section.full-image-slide div.centered-image img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }
  section.title-image-slide {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: stretch;
  }
  section.title-image-slide h2 {
    margin-top: 0;
    margin-bottom: 10px;
  }
  section.title-image-slide div.image-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-grow: 1;
    height: 480px;
  }
  section.title-image-slide div.image-wrapper img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
  }
  section.lead {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  section.lead h1 {
    margin: 0 0 20px 0;
  }
  section.lead h2 {
    margin: 0 0 20px 0;
  }
  section.lead p {
    margin: 0;
    font-size: 0.7em;
    line-height: 1.5;
  }
  section.lead p strong {
    color: #328cc1;
  }
  footer {
    position: absolute;
    left: 40px;
    bottom: 40px;
    text-align: left;
  }
  section.lead header {
    display: none !important;
  }
---

# Python 人工智慧與 LLM 應用

### 第十章：Google Gemini API 串接與 Agent 開發

講師：Python 程式設計教學團隊

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch10/gemini_nb/Python_AI_Agent_Engineering.002.jpeg" alt="人工智慧與LLM應用" />
</div>

---

# 10.1 生成式 AI 與大型語言模型架構原理

* **Transformer & Self-Attention**：
  - **Self-Attention** (自注意力機制)：動態計算詞與上下文中其他詞的權重關聯度，克服長距離記憶退化。
  - **Next-token Prediction** (文字接龍)：模型基於概率預測下一個最可能的標記並輸出。
* **標記與計費**：
  - 以 Token 量計費，長度受限於 Context Window 窗口大小。
* **超參數控制**：
  - **Temperature** (溫度)：控制概率分佈平滑度。接近 0 輸出確定性強；接近 1 具隨機與創造性。
  - **Top-P & Top-K**：篩選候選 Token 集合範圍。

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch10/gemini_nb/Python_AI_Agent_Engineering.003.jpeg" alt="Transformer自注意力機制" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch10/gemini_nb/Python_AI_Agent_Engineering.004.jpeg" alt="Token計費模型" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch10/gemini_nb/Python_AI_Agent_Engineering.005.jpeg" alt="隨機性控制超參數" />
</div>

---

## Concept Check Question (CCQ 1)

<div class="ccq-columns">
  <div class="ccq-text">

**在設計一個用來進行「自動寫程式與編譯 Debug」的 AI 代理人時，你應該如何調整 Gemini API 的 `temperature` (溫度) 參數以確保程式碼穩定？**

* **A.** 調高溫度至 1.0 或以上，以激發 AI 的無限創造力
* **B.** 調低溫度至 0.0 或接近 0，使模型生成最確定、最符合語法邏輯的代碼
* **C.** 關閉 Top-P 與 Top-K，只使用 Temperature=1.5
* **D.** 將溫度設為 -1.0

  </div>
  <div class="ccq-logo">
    <img src="../img/ch01/question_icon.svg" alt="Question" />
  </div>
</div>

---

## CCQ 1 - 答案與解析

<div class="ccq-columns">
  <div class="ccq-text">

### **正確答案：B. 調低溫度至 0.0 或接近 0，使模型生成最確定、最符合語法邏輯的代碼**

* **解析**：
  - 對於數值計算、語法編寫與邏輯推理，必須要求「高一致性」與「高可重現性」，因此需要將 Temperature 設定為 0。
  - 溫度太高會讓模型從概率較低的備選詞中抽選，造成邏輯混亂或產生程式語法幻覺，故選 B。

  </div>
  <div class="ccq-logo">
    <img src="../img/ch01/answer_icon.svg" alt="Answer" />
  </div>
</div>

---

# 10.2 Google Gemini API 開發入門

* **金鑰安全保護**：
  - 嚴禁將金鑰寫死，必須存放在系統環境變數中，使用 `os.environ.get("GEMINI_API_KEY")` 來載入。
* **Google 官方 SDK**：
  - 套件名稱為 `google-generativeai`。
* **開發技巧**：
  - **串流輸出 (Streaming Response)**：
    - `generate_content_stream()`：展示打字機動態刷新效果，優化使用者體驗。
  - **多輪對話歷史 (Chat Session)**：
    - `start_chat()`：在記憶體中維護前後對話狀態。

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch10/gemini_nb/Python_AI_Agent_Engineering.006.jpeg" alt="GeminiAPI開發入門" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch10/gemini_nb/Python_AI_Agent_Engineering.007.jpeg" alt="基礎文字生成呼叫" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch10/gemini_nb/Python_AI_Agent_Engineering.008.jpeg" alt="串流輸出與打字效果" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch10/gemini_nb/Python_AI_Agent_Engineering.009.jpeg" alt="多輪對話歷史記憶" />
</div>

---

# 10.3 進階開發技巧與 API 串接

* **多模態辨識 (Multimodality)**：
  - Gemini 可原生同時處理文字提示詞與 PIL 影像圖片輸入。
* **結構化 JSON 輸出模式 (JSON Mode)**：
  - 設定 `generation_config={"response_mime_type": "application/json"}`。
  - 強制模型回傳可被 `json.loads` 解析的合法格式，方便對接系統資料庫。
* **工具調用 (Function Calling)**：
  - 讓 LLM 自動識別使用者意圖，決定何時呼叫本地 Python 自訂工具函數並擷取對應參數。

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch10/gemini_nb/Python_AI_Agent_Engineering.010.jpeg" alt="多模態影像分析" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch10/gemini_nb/Python_AI_Agent_Engineering.011.jpeg" alt="強制輸出JSON模式" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch10/gemini_nb/Python_AI_Agent_Engineering.012.jpeg" alt="工具調用運作流程" />
</div>

---

## Concept Check Question (CCQ 2)

<div class="ccq-columns">
  <div class="ccq-text">

**關於大型語言模型 (LLM) 的「Function Calling (工具調用)」機制，下列敘述何者正確？**

* **A.** 該機制允許 LLM 繞過作業系統權限，在本地下載並執行 Python 原始碼
* **B.** LLM 不直接執行該函數；僅負責識別使用者意圖，並輸出包含「函數名稱與引數數值」的指令，由開發者本地執行
* **C.** Function Calling 是一種用於微調 (Fine-Tuning) 模型參數的演算法
* **D.** 它會將模型本身的硬體推論速度提升 100 倍

  </div>
  <div class="ccq-logo">
    <img src="../img/ch01/question_icon.svg" alt="Question" />
  </div>
</div>

---

## CCQ 2 - 答案與解析

<div class="ccq-columns">
  <div class="ccq-text">

### **正確答案：B. LLM 不直接執行該函數；僅負責識別使用者意圖，並輸出包含「函數名稱與引數數值」的指令，由開發者本地執行**

* **解析**：
  - 模型本身無法與外部伺服器或本機環境直接發生實體互動。
  - 機制本質是：模型輸出結構化指令指引，要求開發者的本地系統執行該函數並將返回值發送給模型進行下一輪分析，故選 B。

  </div>
  <div class="ccq-logo">
    <img src="../img/ch01/answer_icon.svg" alt="Answer" />
  </div>
</div>

---

# 10.4 檢索增強生成 (Retrieval-Augmented Generation)

* **為什麼需要 RAG**：
  - 解決模型幻覺 (Hallucination)。
  - 提供時效性與內部私人機密文件的知識參考。
* **RAG 工作流架構**：
  1. **檢索 (Retrieve)**：利用相似度計算（如向量/關鍵字交集）在資料庫中找出最相關的文字段落。
  2. **增強 (Augment)**：將檢索文字併入 System / Prompt 上下文中。
  3. **生成 (Generate)**：要求 LLM 僅基於給定的上下文回答使用者問題。

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch10/gemini_nb/Python_AI_Agent_Engineering.013.jpeg" alt="RAG檢索增強生成" />
</div>

---

## Concept Check Question (CCQ 3)

<div class="ccq-columns">
  <div class="ccq-text">

**在實作 RAG (檢索增強生成) 系統時，將檢索到的私人參考文件作為背景 Context 放入 Prompt 中，主要是為了解決什麼痛點？**

* **A.** 網路傳輸頻寬不足的問題
* **B.** 解決模型因為訓練資料截止或缺乏私人知識而產生的幻覺 (Hallucination) 問題，以提供有憑有據的解答
* **C.** 提升本地顯示卡的硬體推論算力
* **D.** 自動將輸入的程式碼進行最佳化編譯

  </div>
  <div class="ccq-logo">
    <img src="../img/ch01/question_icon.svg" alt="Question" />
  </div>
</div>

---

## CCQ 3 - 答案與解析

<div class="ccq-columns">
  <div class="ccq-text">

### **正確答案：B. 解決模型因為訓練資料截止或缺乏私人知識而產生的幻覺 (Hallucination) 問題，以提供有憑有據的解答**

* **解析**：
  - 將檢索到的相關內容以上下文形式提供給模型，相當於「開卷考試」，模型能從中提取資料回答，免除隨意亂猜导致的幻覺，並可提供準確的出處來源，故選 B。

  </div>
  <div class="ccq-logo">
    <img src="../img/ch01/answer_icon.svg" alt="Answer" />
  </div>
</div>

---

# 10.5 本章綜合實作專題

* **終端機 AI 課程助教 Agent**：
  - 設定 `system_instruction`，限定其角色語氣為正體中文的「程式設計助教」。
  - 限制：禁止直接給出正確解答代碼，應逐步給予提示並引導學生除錯思考。
  - 使用多輪對話歷史追蹤學生提交的錯誤。

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch10/gemini_nb/Python_AI_Agent_Engineering.014.jpeg" alt="終端機AI助理代理人專案" />
</div>
