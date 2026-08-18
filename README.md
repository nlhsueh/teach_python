# Python 程式設計課程導讀

歡迎來到 Python 程式設計課程！本課程專為 Python 初學者設計，帶領你從最基礎的程式語法開始，逐步學習控制結構、資料結構，並實踐進階的資料分析與物件導向程式設計。

本儲存庫（Repository）包含所有章節的**詳細課程講義（Lecture Notes）**與搭配的**簡報投影片（Slides）**。

---

## 課程學習地圖（Chapter Guide）

你可以依照以下章節對照表進行學習，表中提供了各章節的學習重點、詳細講義連結與編譯好的 PDF 簡報下載：

| 章節 (Chapter) | 主題 (Topic) | 學習重點 (Learning Highlights) | 課程講義 (Lecture Note) | 簡報投影片 (Slides PDF) |
| :--- | :--- | :--- | :--- | :--- |
| **Ch01** | 環境介紹與入門 | • Python 歷史、優勢與應用領域<br>• 開發環境建置（Google Colab, VS Code）<br>• 第一個 Python 程式 (`hello.py`) | [ch01_intro.md](Lecture/ch01_intro.md) | [ch01s_intro.pdf](Slide/ch01s_intro.pdf) |
| **Ch02** | 程式基本元素 | • 變數宣告、指派與命名規則<br>• 基礎資料型態（整數、浮點數、字串、布林值）<br>• 常用運算子（算術、比較、邏輯運算） | [ch02_program.md](Lecture/ch02_program.md) | [ch02s_program.pdf](Slide/ch02s_program.pdf) |
| **Ch03** | 流程控制 | • 條件判斷式 (`if-elif-else`)<br>• 迴圈結構（`for` 迴圈、`while` 迴圈）與流程中斷控制 (`break`, `continue`) | [ch03_control.md](Lecture/ch03_control.md) | [ch03s_control.pdf](Slide/ch03s_control.pdf) |
| **Ch04** | 資料容器 | • 常用容器：列表 (List)、字典 (Dictionary)、元組 (Tuple)、集合 (Set)<br>• 容器增刪查改 (CRUD) 操作與 JSON 資料解析 | [ch04_collection.md](Lecture/ch04_collection.md) | [ch04s_collection.pdf](Slide/ch04s_collection.pdf) |
| **Ch05** | 函式設計與模組化 | • 自訂函式 (`def`)、參數傳遞（位置、關鍵字、預設參數與可變參數）<br>• 例外處理 (`try-except`) 讓程式更健全<br>• 外部模組 (Module) 的引用方式 | [ch05_function.md](Lecture/ch05_function.md) | [ch05s_function.pdf](Slide/ch05s_function.pdf) |
| **Ch06** | 資料處理與分析 | • 使用 Pandas 處理 Series 與 DataFrame<br>• 基礎操作（索引、切片、過濾、排序與 Groupby 分群）<br>• Matplotlib 繪圖與開放資料分析 | [ch06_pandas.md](Lecture/ch06_pandas.md) | [ch06s_pandas.pdf](Slide/ch06s_pandas.pdf) |
| **Ch07** | 物件導向程式設計 | • 物件與類別觀念、封裝機制與私有變數 (`__private`)<br>• 屬性管理 (`@property`)、類別繼承與方法覆寫 (Override)<br>• 特殊魔術方法 (Magic Methods) 與抽象類別 (`abc`) | [ch07_OOP.md](Lecture/ch07_OOP.md) | [ch07s_OOP.pdf](Slide/ch07s_OOP.pdf) |
| **Ch08** | 工程與資電應用 | • 線性聯立方程式（NumPy）與二階 RLC 充電暫態 ODE 求解（SciPy）<br>• 快速傅立葉變換（FFT）頻域分析、自訂 PID 控制器<br>• 機械手臂正逆向運動學、多執行緒串口通訊模擬（pySerial）<br>• 網路 TCP 多用戶聊天室與數位低通濾波器專題 | [ch08_engineering.md](Lecture/ch08_engineering.md) | [ch08s_engineering.pdf](Slide/ch08s_engineering.pdf) |
| **Ch09** | 機器學習入門 | • 機器學習基本概念（AI/ML/DL、監督與非監督差異、Bias-Variance 折衷）<br>• 經典 KNN 距離、決策樹吉尼不純度與隨機森林集成學習<br>• 交叉驗證與網格搜尋參數調優（GridSearchCV）<br>• 多元線性迴歸、L1/L2 正規化（Lasso/Ridge）與迴歸評估指標<br>• 非監督式 K-Means 分群、肘部法與特徵前處理 | [ch09_machine_learning.md](Lecture/ch09_machine_learning.md) | [ch09s_machine_learning.pdf](Slide/ch09s_machine_learning.pdf) |
| **Ch10** | 人工智慧與 LLM 應用 | • Transformer、Self-Attention、Next-token prediction 概念與 Temperature 設定<br>• Gemini API 串接、打字機串流輸出與連貫對話記憶（Chat Session）<br>• 多模態影像分析、強格式 JSON 輸出控制與 Function Calling（工具調用）<br>• 檢索增強生成（RAG）概念與本地相似度檢索知識庫、CLI AI 代理人專題 | [ch10_AI_LLM.md](Lecture/ch10_AI_LLM.md) | [ch10s_AI_LLM.pdf](Slide/ch10s_AI_LLM.pdf) |
| **Ch11** | 視窗遊戲設計 | • Pygame 視窗、座標與遊戲迴圈（事件、狀態更新、雙重緩衝渲染）<br>• 鍵盤滑鼠事件佇列（Event Queue）與按鍵狀態輪詢（Key Polling）<br>• 繼承 Sprite 類別與 Sprite Group 管理、AABB 碰撞檢測與 Rect 定位<br>• Mixer 音效與背景音樂、太空射擊（Space Shooter）專案 | [ch11_game.md](Lecture/ch11_game.md) | *製作中 (TBD)* |
| **Ch12** | Python Web 開發基礎 | • 用戶端-伺服器端（Client-Server）請求-回應與 HTTP 協定（GET/POST, 狀態碼）<br>• Flask 微型框架、路由（Routing）系統與動態 URL 參數抓取<br>• Jinja2 模板渲染與表單 POST 資料接收處理（`request.form`）<br>• 「學生學籍與成績查詢系統」專案與 RESTful JSON API 開發 | [ch12_web.md](Lecture/ch12_web.md) | *製作中 (TBD)* |
