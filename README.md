# Python 程式設計課程導讀

歡迎來到 Python 程式設計課程！本課程專為 Python 初學者設計，帶領你從最基礎的程式語法開始，逐步學習控制結構、資料結構，並實踐進階的資料分析與物件導向程式設計。

本儲存庫（Repository）包含所有章節的**詳細課程講義（Lecture Notes）**與搭配的**簡報投影片（Slides）**。

---

## 課程學習地圖（Chapter Guide）

你可以依照以下章節順序進行學習：

### 1. [第一章：環境介紹與入門 (Intro)](Lecture/ch01_intro.md)
* **學習重點**：
  - 了解 Python 語言的歷史、優勢與應用領域
  - 開發環境建置（如 Google Colab, VS Code）與第一個 Python 程式 (`hello.py`)

### 2. [第二章：程式基本元素 (Basic Program)](Lecture/ch02_program.md)
* **學習重點**：
  - 變數的宣告、指派與命名規則
  - 基礎資料型態（整數、浮點數、字串、布林值）
  - 常用運算子（算術、比較、邏輯運算）

### 3. [第三章：流程控制 (Control Flow)](Lecture/ch03_control.md)
* **學習重點**：
  - 條件判斷式 (`if-elif-else`)
  - 迴圈結構（`for` 迴圈、`while` 迴圈）與流程中斷控制 (`break`, `continue`)

### 4. [第四章：資料容器 (Collections)](Lecture/ch04_collection.md)
* **學習重點**：
  - 常用的資料容器：列表 (List)、字典 (Dictionary)、元組 (Tuple)、集合 (Set)
  - 容器的增刪查改 (CRUD) 操作與進階應用（如 JSON 資料解析）

### 5. [第五章：函式設計與模組化 (Function & Module)](Lecture/ch05_function.md)
* **學習重點**：
  - 自訂函式 (`def`)、參數傳遞（位置、關鍵字、預設參數與 `*args`, `**kwargs`）
  - 例外處理 (`try-except`) 讓程式更健全
  - 外部模組 (Module) 的引用方式

### 6. [第六章：資料處理與分析 (Pandas Data Analysis)](Lecture/ch06_pandas.md)
* **學習重點**：
  - 使用 Pandas 套件處理表格式資料
  - 一維 Series 與二維 DataFrame 基礎操作（索引、切片、過濾、排序與 Groupby 分群）
  - 基礎 Matplotlib 繪圖與實際開放資料分析（新北 YouBike、大專院校學生統計）

### 7. [第七章：物件導向程式設計 (Object-Oriented Programming)](Lecture/ch07_OOP.md)
* **學習重點**：
  - 物件與類別的觀念（藍圖與實例）
  - 封裝機制與私有變數 (`__private`)、屬性管理 (`@property`)
  - 類別繼承 (Inheritance) 與方法覆寫 (Override)
  - 特殊方法 (Magic Methods) 與抽象類別 (`abc`) 的宣告與實作

### 8. [第八章：工程與資電應用 (Engineering Applications)](Lecture/ch08_engineering.md)
* **學習重點**：
  - 線性代數與網目電流求解（NumPy）、二階 RLC 充電暫態常微分方程求解（SciPy）
  - 快速傅立葉變換（FFT）時域與頻域分析
  - PID 控制器閉迴路系統模擬與二軸關節機器人運動學（正向與逆向運動學解）
  - 多執行緒硬體序列埠通訊模擬與數據解析（pySerial）
  - 網路 TCP 多用戶聊天室伺服器與用戶端開發
  - 實作數位低通濾波器專題

### 9. [第九章：機器學習入門 (Machine Learning)](Lecture/ch09_machine_learning.md)
* **學習重點**：
  - 機器學習基本概念（AI/ML/DL 層級、監督式與非監督式學習差異）
  - 經典 KNN 距離公式與決策樹吉尼係數（Gini Impurity）原理
  - 分類器模型優化（交叉驗證 Cross-Validation 與網格搜尋 GridSearchCV）
  - 多元線性迴歸建模與指標評估（MAE, MSE, RMSE, R2 Score）
  - 非監督式 K-Means 分群與肘部法（Elbow Method）最佳群數尋找
  - 特徵工程前處理（StandardScaler 特徵標準化、One-Hot Encoding 類別變數處理）
  - 實作紅酒品質預測多重分類器專題

### 10. [第十章：人工智慧與大型語言模型應用 (AI & LLM)](Lecture/ch10_AI_LLM.md)
* **學習重點**：
  - 生成式 AI 與大型語言模型架構原理（Transformer、Self-Attention、Next-token Prediction）
  - 模型隨機性微調超參數（溫度 Temperature、Top-P、Top-K、Tokens 計費與 Context Window）
  - Google Gemini API 安全憑證（環境變數管理）與基礎生成
  - 串流輸出（Streaming Response）、多輪對話記憶（Chat Session）與多模態分析（Image Inputs）
  - 進階開發技巧（強制輸出 JSON 模式、Function Calling 工具調用）與檢索增強生成（RAG）架構概念
  - 實作終端機多功能 AI 助理代理人（Agent）專題

---

## 講義與投影片對照表

每個章節皆提供「課程詳細講義」以及「簡報投影檔」，兩者互為搭配：
* 課程詳細講義位於 [Lecture/](Lecture/) 資料夾下，檔名如 `ch0X_xxxx.md`。
* 簡報的 PDF 與 HTML 輸出位於 [Slide/](Slide/) 資料夾下，檔名如 `ch0Xs_xxxx.pdf` 與 `ch0Xs_xxxx.html`。
