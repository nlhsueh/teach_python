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

# Python 視窗遊戲設計 (Pygame)

### 第十一章：2D 遊戲引擎、精靈系統與物理碰撞實作

講師：Python 程式設計教學團隊

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/Architecture_of_Play.002.jpeg" alt="遊戲世界的物件導向宇宙" />
</div>

---

# 11.1 Pygame 與視窗遊戲基礎

* **2D 遊戲開發框架 (Pygame)**：
  - 整合圖形渲染、硬體加速、音訊控制與輸入裝置監聽。
* **螢幕座標系統**：
  - 原點 $(0, 0)$ 位於螢幕**左上角**。
  - 向右為 $+X$，向下為 $+Y$。
* **經典遊戲迴圈 (Game Loop)**：
  - 每秒數十次高速循環：**事件讀取 $\rightarrow$ 狀態更新 $\rightarrow$ 畫面渲染**。

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/Architecture_of_Play.003.jpeg" alt="螢幕座標空間與數學笛卡爾座標比較" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/02_coordinate_system.jpeg" alt="Pygame 螢幕座標系統圖解" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/Architecture_of_Play.004.jpeg" alt="遊戲迴圈的脈動：輸入、更新、渲染與 FPS 控制" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/03_game_loop.jpeg" alt="經典遊戲迴圈三大階段流程圖" />
</div>

---

## 基礎視窗初始化與幾何繪圖

```python
import pygame, sys
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Pygame Window")
clock = pygame.time.Clock()

while True:
    clock.tick(60) # 限制 60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            
    screen.fill((0, 0, 0)) # 黑色背景
    pygame.draw.rect(screen, (255, 0, 0), (350, 250, 100, 100)) # 紅色方塊
    pygame.draw.circle(screen, (0, 255, 0), (100, 100), 50)     # 綠色圓形
    pygame.display.flip() # 雙重緩衝區刷新
```

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/01_basic_window.jpeg" alt="基礎視窗幾何繪製執行成果" />
</div>

---

## Concept Check Question (CCQ 1)

<div class="ccq-columns">
  <div class="ccq-text">

**在 Pygame 遊戲設計中，關於螢幕座標系的描述，下列何者正確？**

* **A.** 原點 $(0, 0)$ 位於螢幕中心點，向上與向右為正數
* **B.** 原點 $(0, 0)$ 位於螢幕左上角，向右為 $+X$，向下為 $+Y$
* **C.** 原點 $(0, 0)$ 位於左下角，符合傳統數學幾何座標
* **D.** 當 $Y$ 座標增加時，物體會在畫面上向上移動

  </div>
  <div class="ccq-logo">
    <img src="../img/ch01/question_icon.svg" alt="Question" />
  </div>
</div>

---

## CCQ 1 - 答案與解析

<div class="ccq-columns">
  <div class="ccq-text">

### **正確答案：B. 原點在左上角，向右為 $+X$，向下為 $+Y$**

* **解析**：
  - 電腦顯示器硬體是由左至右、由上至下依序掃描成像的。
  - 因此 2D 視窗座標系的 $Y$ 軸正方向是「垂直向下」，增加 $Y$ 值會使物體向下移動，故選 B。

  </div>
  <div class="ccq-logo">
    <img src="../img/ch01/answer_icon.svg" alt="Answer" />
  </div>
</div>

---

## Concept Check Question (CCQ 2)

<div class="ccq-columns">
  <div class="ccq-text">

**在遊戲主迴圈中，`clock.tick(60)` 指令的核心用途為何？**

* **A.** 限制 CPU 最大時脈以減少耗電
* **B.** 強制等待 60 毫秒後再繼續
* **C.** 限制每秒最大幀數 (FPS) 為 60，使遊戲在不同性能電腦上速度一致
* **D.** 設定遊戲倒數計時器為 60 秒

  </div>
  <div class="ccq-logo">
    <img src="../img/ch01/question_icon.svg" alt="Question" />
  </div>
</div>

---

## CCQ 2 - 答案與解析

<div class="ccq-columns">
  <div class="ccq-text">

### **正確答案：C. 控制 FPS 幀率，確保跨硬體速度一致**

* **解析**：
  - 若未限制幀率，遊戲迴圈會在高效能 CPU 上以每秒數千次狂飆，導致物體瞬間移動且耗盡單核 CPU。
  - `clock.tick(60)` 能維持固定的時間步長，確保遊戲節奏在各平台均勻流暢，故選 C。

  </div>
  <div class="ccq-logo">
    <img src="../img/ch01/answer_icon.svg" alt="Answer" />
  </div>
</div>

---

# 11.2 事件處理與輸入系統

* **事件佇列 (Event Queue - `pygame.event.get()`)**：
  - 紀錄單次、瞬間的離散硬體觸發（如按下空白鍵射擊、點擊滑鼠、關閉視窗）。
* **按鍵狀態輪詢 (Key State Polling - `pygame.key.get_pressed()`)**：
  - 每個幀即時檢查按鍵是否「長按壓住」，適合平滑連續運動（如左右操控飛船）。
* **滑鼠控制**：
  - `pygame.mouse.get_pos()` 取得即時游標座標。

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/Architecture_of_Play.005.jpeg" alt="事件佇列與按鍵狀態輪詢機制比較" />
</div>

---

## 鍵盤連續移動與滑鼠點擊控制

```python
# 1. 處理單次事件 (滑鼠左鍵點擊生成圓形)
for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        circles.append(event.pos)

# 2. 處理長按輪詢 (鍵盤平滑運動)
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:  block_x -= 5
if keys[pygame.K_RIGHT]: block_x += 5
if keys[pygame.K_UP]:    block_y -= 5
if keys[pygame.K_DOWN]:  block_y += 5

# 繪製畫面
screen.fill((30, 30, 30))
pygame.draw.rect(screen, (0, 255, 255), (block_x, block_y, 50, 50))
for pos in circles:
    pygame.draw.circle(screen, (255, 50, 50), pos, 15)
pygame.display.flip()
```

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/04_input_control.jpeg" alt="鍵盤長按平滑運動與滑鼠點擊畫圓成果" />
</div>

---

## Concept Check Question (CCQ 3)

<div class="ccq-columns">
  <div class="ccq-text">

**在遊戲每幀繪圖完成後呼叫 `pygame.display.flip()`，其底層「雙重緩衝區 (Double Buffering)」機制主要解決什麼問題？**

* **A.** 釋放顯示卡未使用的暫存記憶體
* **B.** 防止螢幕閃爍與撕裂，讓玩家看到完整繪製好的成品幀
* **C.** 自動計算精靈之間的碰撞
* **D.** 將 2D 向量自動渲染為 3D 視角

  </div>
  <div class="ccq-logo">
    <img src="../img/ch01/question_icon.svg" alt="Question" />
  </div>
</div>

---

## CCQ 3 - 答案與解析

<div class="ccq-columns">
  <div class="ccq-text">

### **正確答案：B. 防止螢幕閃爍與撕裂**

* **解析**：
  - 雙重緩衝區由「前台顯示畫布」與「後台繪製畫布」組成。
  - 所有 `draw` 操作都在後台默默進行，完成後透過 `flip()` 瞬間翻轉前台，避免玩家看到圖形逐一畫上的過程與殘影，故選 B。

  </div>
  <div class="ccq-logo">
    <img src="../img/ch01/answer_icon.svg" alt="Answer" />
  </div>
</div>

---

# 11.3 精靈與碰撞偵測 (Sprites & Collisions)

* **`pygame.sprite.Sprite` 類別**：
  - 物件導向遊戲實體基類，必須具備 `self.image` (Surface) 與 `self.rect` (Rect)。
* **`pygame.sprite.Group` 精靈群組**：
  - 一行指令 `group.update()` 批次更新所有成員。
  - 一行指令 `group.draw(screen)` 批次渲染所有實體。
* **AABB 矩形邊界碰撞偵測**：
  - `groupcollide(g1, g2, dokill1, dokill2)` 高效多對多檢測。

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/Architecture_of_Play.006.jpeg" alt="精靈類別的解剖：Surface 與 Rect 邊框" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/Architecture_of_Play.007.jpeg" alt="精靈群組與批次渲染管理" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/Architecture_of_Play.009.jpeg" alt="Rect 物件座標錨點定位系統" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/05_rect_properties.jpeg" alt="pygame.Rect 內建座標定位屬性詳解" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/Architecture_of_Play.008.jpeg" alt="AABB 邊界碰撞檢測原理" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/06_collision_detection.jpeg" alt="Pygame 碰撞檢測機制圖解" />
</div>

---

## Concept Check Question (CCQ 4)

<div class="ccq-columns">
  <div class="ccq-text">

**在 Pygame 中，一個繼承自 `pygame.sprite.Sprite` 的自訂類別，初始化時必須設定哪兩個變數屬性，才能被 Sprite Group 正確管理與繪製？**

* **A.** `self.x` 與 `self.y`
* **B.** `self.image` (Surface 外觀) 與 `self.rect` (Rect 座標邊框)
* **C.** `self.speed` 與 `self.direction`
* **D.** `self.width` 與 `self.height`

  </div>
  <div class="ccq-logo">
    <img src="../img/ch01/question_icon.svg" alt="Question" />
  </div>
</div>

---

## CCQ 4 - 答案與解析

<div class="ccq-columns">
  <div class="ccq-text">

### **正確答案：B. `self.image` 與 `self.rect`**

* **解析**：
  - `SpriteGroup.draw()` 在遍歷成員繪圖時，會讀取每個物件的 `image` 取得畫布，並讀取 `rect` 取得繪製位置。
  - 缺少任一屬性都會引發 AttributeError，故選 B。

  </div>
  <div class="ccq-logo">
    <img src="../img/ch01/answer_icon.svg" alt="Answer" />
  </div>
</div>

---

## Concept Check Question (CCQ 5)

<div class="ccq-columns">
  <div class="ccq-text">

**在太空射擊遊戲中，檢測「所有子彈群組」與「所有隕石群組」的碰撞並讓相撞兩者同時消滅，最佳指令為何？**

* **A.** `pygame.Rect.colliderect()`
* **B.** `pygame.sprite.spritecollide()`
* **C.** `pygame.sprite.groupcollide(bullets, meteors, True, True)`
* **D.** 撰寫雙重 for 迴圈計算每顆子彈與隕石的歐幾里得距離

  </div>
  <div class="ccq-logo">
    <img src="../img/ch01/question_icon.svg" alt="Question" />
  </div>
</div>

---

## CCQ 5 - 答案與解析

<div class="ccq-columns">
  <div class="ccq-text">

### **正確答案：C. `groupcollide(bullets, meteors, True, True)`**

* **解析**：
  - `groupcollide` 是專為群組對群組碰撞優化的高效函式。
  - 傳入 `True, True` 可在碰撞發生時自動調用雙方成員的 `kill()` 方法將其從群組移除，一行代碼替代複雜迴圈，故選 C。

  </div>
  <div class="ccq-logo">
    <img src="../img/ch01/answer_icon.svg" alt="Answer" />
  </div>
</div>

---

# 11.4 聲音與背景音樂整合 (Sound & Mixer)

* **`pygame.mixer.music` (背景音樂)**：
  - 適合長音訊 (mp3, ogg)。
  - **串流解碼播放**，節省記憶體，支援循環播放 (`play(-1)`)。
* **`pygame.mixer.Sound` (獨立音效)**：
  - 適合短促高頻聲音 (wav)。
  - **一次性載入記憶體**，超低延遲即時觸發 (如射擊、爆炸)。

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/Architecture_of_Play.010.jpeg" alt="Pygame 音訊管線與背景音樂/音效控制" />
</div>

---

# 11.5 太空射擊遊戲專案開發 (Space Shooter)

* **三大核心實體設計**：
  - **Player**：受鍵盤左右控制，限制於螢幕邊界。
  - **Meteor**：由螢幕頂端隨機生成，隨機速度飄移墜落。
  - **Bullet**：按下空白鍵生成於玩家正上方，高速向上飛行。
* **遊戲生命週期與狀態機**：
  - 玩家生命值 (Lives)、計分板 (Score) 與 Game Over 重開機制。

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/Architecture_of_Play.011.jpeg" alt="太空射擊遊戲架構與實體關聯圖" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/Architecture_of_Play.012.jpeg" alt="遊戲狀態機切換機制" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/07_space_shooter_gameplay.jpeg" alt="太空射擊遊戲實戰進行畫面" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/08_space_shooter_gameover.jpeg" alt="太空射擊遊戲 Game Over 與重啟畫面" />
</div>

---

# 11.6 課後進階挑戰專題 (Particle FX)

* **粒子系統 (Particle System)**：
  - 擊中隕石時向四周迸發具備隨機初速度的小方塊粒子。
  - 粒子每幀衰減生命期 (`lifetime -= 1`)，結束時自動 `kill()`。
* **增添遊戲打擊感 (Visual Juice)**：
  - 賦予 2D 復古遊戲豐富的視覺反饋與震撼感。

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/Architecture_of_Play.013.jpeg" alt="粒子系統與爆炸視覺特效" />
</div>

---

<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="../img/ch11/gemini_nb/09_particle_explosion.jpeg" alt="粒子爆炸特效展示" />
</div>
