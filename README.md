# Python 程式設計與實務應用全攻略 (Python Programming & Practical Applications)

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Slides](https://img.shields.io/badge/Marp-Gaia%20Theme-orange.svg)](https://marp.app/)
[![Course](https://img.shields.io/badge/Course-12%20Chapters-purple.svg)](Lecture/)

歡迎來到 **Python 程式設計與實務應用** 課程開源儲存庫！本課程專為資訊科技、理工資電與跨領域初學者量身打造，內容涵蓋由淺入深的 Python 基礎語法、運算思維、控制結構、資料分析、物件導向，並延伸至工程模擬、機器學習、現代生成式 AI (LLM / Agent)、Pygame 視窗遊戲設計與 Flask 全端 Web 應用。

本儲存庫包含完整的 **12 章詳細講義 (Lecture Handbooks)**、**12 套精美 Marp Gaia 簡報 (Slide PDFs)**，以及可直接於本機執行的 **範例程式碼 (Source Code)**。

---

## 🗺️ 課程學習地圖（Chapter Guide）

本課程劃分為 12 個核心單元，你可以依據需求點擊對應講義閱讀，或下載編譯好的簡報 PDF 進行授課與自學：

| 章節 (Chapter) | 單元主題 (Topic) | 核心學習重點 (Highlights) | 講義 (Handbook) | 簡報 (PDF) | 範例程式 (Code) |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **Ch01** | **導論與環境建置** | • 運算思維四大基石、直譯 vs 編譯語言機制<br>• Google Colab 雲端體驗、VS Code + Python 本機開發<br>• 虛擬環境 (`venv`)、REPL 互動體驗與新手 5 大避坑指南 | [ch01_intro.md](Lecture/ch01_intro.md) | [ch01s_intro.pdf](Slide/ch01s_intro.pdf) | - |
| **Ch02** | **程式基本元素** | • 變數宣告、動態型別、指派運算與識別字規則<br>• 數值運算、布林邏輯、字串格式化 (`f-string`)<br>• 輸入輸出 (`input`/`print`) 與型態轉換 | [ch02_program.md](Lecture/ch02_program.md) | [ch02s_program.pdf](Slide/ch02s_program.pdf) | [source/ch02/](source/ch02/) |
| **Ch03** | **流程控制結構** | • 條件分支 (`if-elif-else`) 與巢狀判斷<br>• 迭代迴圈 (`for-in`、`range`) 與計數控制<br>• 條件迴圈 (`while`)、中斷控制 (`break`, `continue`, `else`) | [ch03_control.md](Lecture/ch03_control.md) | [ch03s_control.pdf](Slide/ch03s_control.pdf) | - |
| **Ch04** | **資料容器與結構** | • 列表 (List)、元組 (Tuple)、集合 (Set)、字典 (Dict)<br>• 容器生成式 (List/Dict Comprehension)<br>• 容器增刪查改 (CRUD)、巢狀結構走訪與 JSON 解析 | [ch04_collection.md](Lecture/ch04_collection.md) | [ch04s_collection.pdf](Slide/ch04s_collection.pdf) | [source/ch04/](source/ch04/) |
| **Ch05** | **函式設計與模組化** | • 自訂函式 (`def`)、位置參數、關鍵字與預設參數<br>• 可變參數 (`*args`, `**kwargs`) 與 Lambda 匿名函式<br>• 變數作用域 (LEGB)、例外處理 (`try-except`) 與自建模組 | [ch05_function.md](Lecture/ch05_function.md) | [ch05s_function.pdf](Slide/ch05s_function.pdf) | [source/ch05/](source/ch05/) |
| **Ch06** | **資料處理與分析 (Pandas)** | • Pandas Series 與 DataFrame 核心結構<br>• 資料切片篩選 (`loc`, `iloc`)、缺失值處理、Groupby 分群<br>• 表格合併 (`merge`/`concat`)、Matplotlib 視覺化與開放資料實戰 | [ch06_pandas.md](Lecture/ch06_pandas.md) | [ch06s_pandas.pdf](Slide/ch06s_pandas.pdf) | [source/ch06/](source/ch06/) |
| **Ch07** | **物件導向設計 (OOP)** | • 物件與類別本質、屬性與方法 (`__init__`)<br>• 封裝與存取控制 (`__private`)、屬性裝飾器 (`@property`)<br>• 繼承 (`super()`)、多型、魔術方法與抽象基底類別 (`abc`) | [ch07_OOP.md](Lecture/ch07_OOP.md) | [ch07s_OOP.pdf](Slide/ch07s_OOP.pdf) | [source/ch07/](source/ch07/) |
| **Ch08** | **工程與資電應用實務** | • 線性聯立方程 (NumPy) 與二階 RLC 電路 ODE 求解 (SciPy)<br>• 快速傅立葉變換 (FFT)、自製 PID 溫控模擬器<br>• 機械手臂正逆向運動學、虛擬序列埠 (pySerial) 與 TCP 聊天室 | [ch08_engineering.md](Lecture/ch08_engineering.md) | [ch08s_engineering.pdf](Slide/ch08s_engineering.pdf) | [source/ch08/](source/ch08/) |
| **Ch09** | **機器學習入門實踐** | • 機器學習流程 (AI/ML/DL、監督 vs 非監督、偏差-方差折衷)<br>• 分類演算法：KNN 距離、決策樹吉尼不純度、隨機森林集成<br>• 迴歸演算法：多元線性迴歸、L1/L2 正規化 (Lasso/Ridge)<br>• 非監督分群：K-Means、肘部法與特徵前處理 | [ch09_machine_learning.md](Lecture/ch09_machine_learning.md) | [ch09s_machine_learning.pdf](Slide/ch09s_machine_learning.pdf) | [source/ch09/](source/ch09/) |
| **Ch10** | **生成式 AI 與 LLM 應用** | • 大型語言模型本質、Transformer、Self-Attention、溫度參數<br>• Gemini API 串接、打字機串流輸出與多輪對話 Session<br>• 多模態影像辨識、強制結構化 JSON 輸出與 Function Calling<br>• 檢索增強生成 (RAG) 本地知識庫檢索與 CLI AI 代理人專題 | [ch10_AI_LLM.md](Lecture/ch10_AI_LLM.md) | [ch10s_AI_LLM.pdf](Slide/ch10s_AI_LLM.pdf) | [source/ch10/](source/ch10/) |
| **Ch11** | **Pygame 視窗遊戲設計** | • 2D 遊戲引擎基礎、螢幕座標系、經典遊戲迴圈三階段<br>• 事件佇列 (`event.get`) vs 按鍵長按輪詢 (`key.get_pressed`)<br>• Sprite 精靈系統、AABB 碰撞檢測、Rect 錨點定位、音效混音器<br>• 經典「太空射擊大戰 (Space Shooter)」與粒子爆炸特效實作 | [ch11_game.md](Lecture/ch11_game.md) | [ch11s_game.pdf](Slide/ch11s_game.pdf) | [source/ch11/](source/ch11/) |
| **Ch12** | **Python Web 開發 (Flask)** | • Client-Server 架構、HTTP 狀態碼、GET vs POST 語意<br>• Flask 微型框架、路由分派 (`@app.route`)、動態 URL 參數<br>• Jinja2 模板渲染、表單處理與 Post-Redirect-Get (PRG) 模式<br>• 「學生學籍與成績登記系統」專案與 RESTful JSON API 實踐 | [ch12_web.md](Lecture/ch12_web.md) | [ch12s_web.pdf](Slide/ch12s_web.pdf) | [source/ch12/](source/ch12/) |

---

## 📁 儲存庫結構（Directory Layout）

```text
teach_python/
├── Lecture/              # 12 章 Markdown 講義與 Marp 簡報原始碼
│   ├── ch01_intro.md ~ ch12_web.md       # 詳細課本講義 (含生活實例與 CCQ 解析)
│   └── ch01s_intro.md ~ ch12s_web.md     # Marp Gaia 簡報原始檔
├── Slide/                # 編譯完成的高解析度簡報 PDF 檔案 (全 12 章)
│   └── ch01s_intro.pdf ~ ch12s_web.pdf
├── source/               # 各章節完整可執行的 Python 範例程式碼
│   ├── ch02/ ~ ch12/
├── img/                  # 講義插圖、架構圖解與程式執行成果截圖
│   ├── ch01/ ~ ch12/
└── README.md             # 本導讀文件
```

---

## 🚀 快速開始（Getting Started）

### 1. 下載本專案
```bash
git clone https://github.com/nlhsueh/teach_python.git
cd teach_python
```

### 2. 建立並啟用 Python 虛擬環境 (推薦 Python 3.10+)
* **macOS / Linux**：
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
* **Windows (PowerShell)**：
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```

### 3. 安裝常用相依套件
```bash
pip install numpy scipy pandas matplotlib scikit-learn pygame flask requests google-genai
```

### 4. 執行範例程式
例如執行第 11 章的太空射擊遊戲：
```bash
python source/ch11/04_space_shooter.py
```

或啟動第 12 章的 Flask 學生學籍管理系統：
```bash
python source/ch12/04_grade_system.py
```
在瀏覽器開啟 `http://127.0.0.1:5000` 即可進入系統。

---

## 🛠️ 簡報編譯指南 (Marp CLI)

本課程所有簡報均使用 [Marp](https://marp.app/) 撰寫，並搭配定製的 Gaia 資電風格主題。若欲自行修改並重新編譯投影片為 PDF：

```bash
# 透過 npm / brew 安裝 marp-cli
brew install marp-cli   # 或 npm install -g @marp-team/marp-cli

# 編譯單一簡報為 PDF
marp --no-stdin --pdf --allow-local-files Lecture/ch01s_intro.md -o Slide/ch01s_intro.pdf
```

---

## 👨‍🏫 授課與使用授權

本教材專為大專院校、高中職程式設計課程及個人自學開放。歡迎在保留原作者與專案來源標註的前提下自由引用與教學使用。
