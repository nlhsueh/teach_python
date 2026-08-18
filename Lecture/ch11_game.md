Ch11 Game Development in Python
===

# Python 視窗遊戲設計 (Pygame)

本章將帶領你探討如何使用 Python 的主流遊戲開發套件 **Pygame** 設計視窗型 2D 遊戲。當你學會了物件導向設計 (OOP) 後，遊戲設計是最能發揮這些觀念的實務領域。在遊戲中，每一個玩家、敵人、子彈、障礙物，都可以表示成一個個獨立的物件，並且藉由**遊戲迴圈 (Game Loop)** 進行高頻的狀態更新與畫面繪製。

本章包含以下核心單元：
* **11.1 Pygame 與視窗遊戲基礎**：學習 Pygame 的安裝、視窗初始化、笛卡爾螢幕座標系，以及經典遊戲迴圈的三大階段。
* **11.2 事件處理與輸入系統**：比較「事件佇列 (Event Queue)」與「按鍵狀態輪詢 (Key Polling)」在控制角色動作上的本質差異，並介紹滑鼠點擊控制。
* **11.3 精靈與碰撞偵測 (Sprites & Collisions)**：利用物件導向的 `pygame.sprite.Sprite` 類別管理多個實體，並探討 AABB 矩形碰撞檢測與 Rect 各項座標定位屬性。
* **11.4 聲音與背景音樂整合 (Sound & Mixer)**：了解 `pygame.mixer` 系統如何載入背景音樂與高頻播放音效。
* **11.5 實務專案開發：經典太空侵略者 (Space Shooter) 遊戲**：從零開始實作一個完整的、具備計分與關卡機制的視窗射擊遊戲。
* **11.6 本章綜合課後練習與專題擴充**。

---

## 11.1 Pygame 與視窗遊戲基礎

在進行視窗軟體開發時，我們需要一個能夠跨平台建立視窗、讀取顯示卡硬體加速、播放音效並接收鍵盤滑鼠訊號的框架。Pygame 就是 Python 領域最成熟的 2D 遊戲開發函式庫。

### 11.1.1 環境配置與視窗宣告

首先，請在終端機中安裝 Pygame 套件：
```bash
pip install pygame
```

宣告一個最簡單的 Pygame 視窗：
```python
import pygame
import sys

# 1. 初始化 Pygame 所有子模組 (顯示、聲音、字型等)
pygame.init()

# 2. 設定視窗大小 (寬 800 像素，高 600 像素)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 設定視窗標題
pygame.display.set_caption("我的第一個 Pygame 遊戲視窗")

# 3. 定義顏色常數 (使用 RGB 三原色組成的元組，範圍 0~255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 4. 遊戲主要控制變數
running = True
clock = pygame.time.Clock() # 建立時間控制器限制 FPS

# 遊戲主要迴圈
while running:
    # 限制遊戲每秒最高執行 60 幀 (Frame Rate)
    # 這能確保遊戲在極快速的電腦與慢速電腦上運行速度相同
    clock.tick(60)
    
    # --- 1. 事件讀取階段 (Event Polling) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # --- 2. 狀態更新階段 (Update State) ---
    # 此處暫無狀態改變
    
    # --- 3. 畫面繪製階段 (Render/Draw) ---
    # 使用黑色填滿背景
    screen.fill(BLACK)
    
    # 在螢幕中央繪製一個紅色的矩形
    # 參數: (目標畫布, 顏色, (X座標, Y座標, 寬度, 高度))
    pygame.draw.rect(screen, RED, (350, 250, 100, 100))
    
    # 在 (100, 100) 處繪製一個綠色圓形，半徑為 50 像素
    pygame.draw.circle(screen, GREEN, (100, 100), 50)
    
    # 更新雙重緩衝區顯示器 (Double Buffering)
    pygame.display.flip()

# 退出遊戲並釋放系統資源
pygame.quit()
sys.exit()
```

---

### 11.1.2 螢幕座標系統

在數學的笛卡爾座標系中，Y 軸向上為正數。然而在**電腦顯示器座標系統中，原點 $(0, 0)$ 位於螢幕的「左上角」**：
* **X 軸**：向「右」為正數（與數學相同）。
* **Y 軸**：向「下」為正數。如果你讓一個物體的 Y 座標增加，它會在畫面上「往下移動」。

```
(0,0) ---------------------> +X
  |
  |      (x, y)
  |        o
  |
  v
 +Y
```

---

### 11.1.3 經典遊戲迴圈的三大階段

一個視窗遊戲之所以能夠流暢播放動畫且即時回應你的操作，全靠每秒重複執行數十次的**遊戲迴圈 (Game Loop)**：

```
       +---------------------------------------------+
       |                                             |
       v                                             |
[ 事件監聽 (Event) ] -> [ 狀態更新 (Update) ] -> [ 畫面渲染 (Render) ]
```

1. **事件監聽 (Event Phase)**：讀取作業系統傳遞的鍵盤、滑鼠、視窗關閉等硬體事件。
2. **狀態更新 (Update Phase)**：計算角色移動、物理碰撞、分數增減、子彈飛行路徑等邏輯。
3. **畫面渲染 (Render Phase)**：清除上一幀的畫面，將所有物體的新位置繪製到畫面上，並更新顯示器。

---

### **11.1.4 隨堂測驗 (CCQ 1)**

**問題**

在 Pygame 遊戲設計中，關於螢幕座標系的描述，下列何者正確？

A) 原點 $(0, 0)$ 位於螢幕的中心點，向右與向上為正數。
B) 原點 $(0, 0)$ 位於螢幕的左上角，向右為 X 軸正方向，向下為 Y 軸正方向。
C) 原點 $(0, 0)$ 位於螢幕的左下角，符合傳統數學笛卡爾座標系。
D) X 座標增加物體會往左移動，Y 座標增加物體會往上移動。

<details>
<summary>點擊查看【隨堂測驗】答案與解析</summary>

**正確答案：B) 原點 $(0, 0)$ 位於螢幕的左上角，向右為 X 軸正方向，向下為 Y 軸正方向。**

* **解析**：
  * 電腦螢幕的掃描線是從左到右、從上到下進行更新的，因此大部分的視窗系統與 2D 遊戲引擎皆將左上角定義為原點 $(0,0)$。
  * 故當物體往下移動時，Y 座標會變大，這與傳統數學幾何座標系不同，必須特別注意，故選 B。

</details>

---

### **11.1.5 隨堂測驗 (CCQ 2)**

**問題**

在遊戲迴圈的主程序中，`clock.tick(60)` 這行指令的核心功用為何？

A) 限制顯示卡每秒的運算功率，維持電腦處於低溫狀態。
B) 阻塞程式執行，直到系統精準經過 60 毫秒。
C) 控制遊戲迴圈的每秒幀數 (FPS) 最高為 60，確保遊戲邏輯的更新速度在不同性能的電腦上保持一致。
D) 設定遊戲中計時器的初始倒數時間為 60 秒。

<details>
<summary>點擊查看【隨堂測驗】答案與解析</summary>

**正確答案：C) 控制遊戲迴圈的每秒幀數 (FPS)最高為 60，確保遊戲邏輯的更新速度在不同性能的電腦上保持一致。**

* **解析**：
  * 如果沒有使用 `clock.tick(60)`，遊戲迴圈會以電腦 CPU 所能跑的最快速度（例如每秒幾千次）高頻循環。
  * 這會導致遊戲中的角色以光速移動而無法遊玩，且會佔滿 CPU 的單核心資源造成發熱。
  * 限制 FPS 可以讓遊戲更新速度在任何硬體上都維持一致，故選 C。

</details>

---

## 11.2 事件處理與輸入系統 (Input Systems)

遊戲需要能接收玩家的鍵盤或滑鼠控制。在 Pygame 中，有兩種讀取按鍵輸入的方式，其適合的應用情境截然不同。

### 11.2.1 事件佇列 vs 按鍵狀態輪詢

1. **事件佇列 (Event Queue - `pygame.event.get()`)**：
   * 原理：當你按下一瞬間或放開一瞬間，作業系統會產生一個「單次事件」放入隊列中。
   * 特點：**只觸發一次**。
   * 適合情境：需要單次精準發動的動作，例如「按下空白鍵發射子彈」、「按下 Esc 開啟暫停選單」。
2. **按鍵狀態輪詢 (Key State Polling - `pygame.key.get_pressed()`)**：
   * 原理：在每個迴圈中，直接向硬體詢問：「目前哪一些按鍵正處於被『壓著不放』的狀態？」
   * 特點：只要按鍵被壓住，回傳值就一直是 True。
   * 適合情境：**流暢的連續移動**，例如「長按向左鍵，角色一直往左移動」。

### 11.2.2 滑鼠輸入控制

除了鍵盤，我們也可以透過滑鼠來與遊戲互動：
* `pygame.mouse.get_pos()`：取得滑鼠目前的 $(x, y)$ 座標。
* `event.type == pygame.MOUSEBUTTONDOWN`：偵測滑鼠按鍵點擊（左鍵、中鍵、右鍵）。

#### 實踐程式碼：控制方塊平滑移動與滑鼠點擊畫圓

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("鍵盤與滑鼠整合控制示範")

clock = pygame.time.Clock()

# 方塊的初始屬性
block_x = 400
block_y = 300
block_size = 50
block_speed = 5  # 每一幀移動的像素點

# 儲存滑鼠點擊生成的圓形清單
circles = []

running = True
while running:
    clock.tick(60)
    
    # 方式一：讀取事件佇列 (處理單次、離散事件，如滑鼠點擊與關閉視窗)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 測試滑鼠單次點擊事件
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # 1 代表左鍵
                # 取得點擊座標並記錄
                click_x, click_y = event.pos
                circles.append((click_x, click_y))
                print(f"滑鼠左鍵點擊於：({click_x}, {click_y})")

    # 方式二：輪詢按鍵狀態 (處理鍵盤長按、連續平滑運動)
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        block_x -= block_speed
    if keys[pygame.K_RIGHT]:
        block_x += block_speed
    if keys[pygame.K_UP]:
        block_y -= block_speed
    if keys[pygame.K_DOWN]:
        block_y += block_speed

    # 限制方塊不出邊界
    block_x = max(0, min(800 - block_size, block_x))
    block_y = max(0, min(600 - block_size, block_y))

    # 渲染畫面
    screen.fill((30, 30, 30))
    
    # 1. 繪製玩家控制的方塊 (青色)
    pygame.draw.rect(screen, (0, 255, 255), (block_x, block_y, block_size, block_size))
    
    # 2. 繪製所有滑鼠生成的圓形 (紅色)
    for center_pos in circles:
        pygame.draw.circle(screen, (255, 50, 50), center_pos, 15)
        
    pygame.display.flip()

pygame.quit()
sys.exit()
```

---

### **11.2.3 隨堂測驗 (CCQ 3)**

**問題**

在遊戲畫面繪製結束後，我們會呼叫 `pygame.display.flip()`。這項操作背後的圖學機制「雙重緩衝區 (Double Buffering)」主要為解決什麼問題？

A) 減少系統記憶體佔用。
B) 防止螢幕更新時畫面閃爍與撕裂，讓玩家看不到圖畫繪製的過程。
C) 將 2D 座標轉換為 3D 渲染。
D) 自動執行物理碰撞演算法。

<details>
<summary>點擊查看【隨堂測驗】答案與解析</summary>

**正確答案：B) 防止螢幕更新時畫面閃爍與撕裂，讓玩家看不到圖畫繪製的過程。**

* **解析**：
  * 在雙重緩衝區機制下，系統有兩個畫布：前台緩衝區（顯示在螢幕上）與後台緩衝區（隱藏在記憶體中）。
  * 所有的 `pygame.draw` 繪圖動作都是畫在後台緩衝區。
  * 當呼叫 `flip()` 時，前後台畫布會瞬間切換。這能保證玩家看到的是一張完整畫好的成品幀，避免看到物體一個個被畫出來的殘影與閃爍，故選 B。

</details>

---

## 11.3 精靈與碰撞偵測 (Sprites & Collisions)

當遊戲中有數十個敵人和數百顆子彈時，如果用獨立的變數（如 `enemy1_x`, `enemy2_x`）去管理，程式碼會迅速失控。我們必須使用 Pygame 的 `Sprite`（精靈）系統進行物件導向開發。

### 11.3.1 精靈類別 (`pygame.sprite.Sprite`)

`Sprite` 是 2D 遊戲中所有活動實體的基類。一個自訂的精靈子類別，內部必須包含兩個最核心的屬性：
1. `self.image`：代表該精靈的畫布或外觀（可以是一張圖片，或是一個自定義形狀畫布）。
2. `self.rect`：一個 `pygame.Rect` 物件，代表該精靈在螢幕上的位置、寬度與高度。

### 11.3.2 深入認識 Rect 物件定位屬性

`pygame.Rect` 不僅包含 $X, Y$、寬與高，它還內建了極為方便的定位屬性，當你修改其中一個，其他屬性會自動關聯更新：
* `rect.x` / `rect.y`：左上角座標。
* `rect.left` / `rect.right`：最左側與最右側的 X 座標。
* `rect.top` / `rect.bottom`：最頂部與最低部的 Y 座標。
* `rect.center`：代表中心點的 $(x, y)$ 元組。
* `rect.centerx` / `rect.centery`：中心點的 X 與 Y 座標。

使用這些屬性可以非常輕易地定位物體，例如讓子彈發射在玩家的上方正中央：
`bullet.rect.centerx = player.rect.centerx; bullet.rect.bottom = player.rect.top`。

---

### **11.3.3 隨堂測驗 (CCQ 4)**

**問題**

在 Pygame 中，一個自訂的精靈類別（繼承自 `pygame.sprite.Sprite`）在初始化時，**必須**設定哪兩個變數屬性，才能被精靈群組 (Sprite Group) 正確管理與繪製？

A) `self.x` 與 `self.y`
B) `self.image`（外觀 Surface）與 `self.rect`（邊框位置 Rect）
C) `self.speed` 與 `self.direction`
D) `self.width` 與 `self.height`

<details>
<summary>點幕查看【隨堂測驗】答案與解析</summary>

**正確答案：B) `self.image`（外觀 Surface）與 `self.rect`（邊框位置 Rect）**

* **解析**：
  * Pygame 的 `SpriteGroup.draw()` 方法在繪製成員時，會依序讀取每個 Sprite 的 `self.image` 作為畫布，並讀取 `self.rect` 作為畫面上繪製的 $X, Y$ 座標。
  * 如果缺少這兩個屬性中的任何一個，群組的繪製或更新功能就會拋出錯誤，故選 B。

</details>

---

### **11.3.4 隨堂測驗 (CCQ 5)**

**問題**

在太空射擊遊戲中，若要檢測「所有的子彈群組 (bullets)」與「所有的隕石群組 (meteors)」之間的多對多碰撞，並讓相撞的子彈與隕石同時消失，下列哪一個內建函數是最佳且最有效率的選擇？

A) `pygame.Rect.colliderect()`
B) `pygame.sprite.spritecollide()`
C) `pygame.sprite.groupcollide(bullets, meteors, True, True)`
D) 寫雙重 `for` 迴圈手動計算每一個子彈與隕石的幾何距離。

<details>
<summary>點擊查看【隨堂測驗】答案與解析</summary>

**正確答案：C) `pygame.sprite.groupcollide(bullets, meteors, True, True)`**

* **解析**：
  * `groupcollide` 是專門設計用來處理「群組對群組」碰撞的方法。
  * 後面的兩個 `True` 參數分別代表：當發生碰撞時，自動將第 1 個群組（子彈）與第 2 個群組（隕石）的碰撞成員從其各自的群組中刪除（kill）。
  * 這能用一行程式碼高效替代雙重迴圈，故選 C。

</details>

---

## 11.4 聲音與背景音樂整合 (Sound & Mixer)

一個沒有聲音的遊戲是不完整的。Pygame 的 `pygame.mixer` 模組可以讓我們輕鬆載入並控制音效：

### 11.4.1 背景音樂與音效的區別

1. **背景音樂 (`pygame.mixer.music`)**：
   * 用於較長、大檔案的音樂（如 mp3, ogg 格式）。
   * 原理：**串流播放**（一邊解碼一邊播），避免一次載入巨大音樂檔案佔滿系統記憶體。
2. **獨立音效 (`pygame.mixer.Sound`)**：
   * 用於極短、需要高頻重複播放的聲音（如爆炸聲、射擊雷射聲，通常為 wav 格式）。
   * 原理：**一次性完整讀入記憶體**，確保低延遲即時播放。

#### 聲音配置程式語法示範
```python
# 初始化音樂播放器
pygame.mixer.init()

# 1. 播放背景音樂
# pygame.mixer.music.load("background_bgm.mp3")
# pygame.mixer.music.play(-1) # 傳入 -1 代表無限循環播放
# pygame.mixer.music.set_volume(0.4) # 設定音量大小 (0.0 ~ 1.0)

# 2. 載入並播放射擊音效
# shoot_sound = pygame.mixer.Sound("laser_shoot.wav")
# shoot_sound.play() # 需要發射時呼叫此行
```

---

## 11.5 太空射擊遊戲專案開發 (Space Shooter)

現在，我們將前面學到的所有觀念：**遊戲迴圈、事件處理、狀態更新、Sprite群組、AABB 碰撞以及字型繪製**，融會貫通成一個完整的經典太空射擊遊戲。

本程式不依賴外部圖片檔案，改以向量幾何繪圖（如多邊形、圓形）作為飛船與隕石的 fallback 繪製，確保學生在複製程式碼後即可直接在本機執行。

```python
import pygame
import random
import sys

# 1. 遊戲常數初始化
WIDTH = 600
HEIGHT = 800
FPS = 60

# 顏色定義
BLACK = (10, 10, 15)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 50, 50)
GREEN = (50, 255, 50)

# ==================================================
# 精靈物件設計 (OOP Components)
# ==================================================

class Player(pygame.sprite.Sprite):
    """ 玩家太空船 """
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40), pygame.SRCALPHA)
        # 用畫多邊形方式畫一個三角形太空船，不需外部圖檔
        pygame.draw.polygon(self.image, GREEN, [(25, 0), (0, 40), (50, 40)])
        
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speed_x = 8

    def update(self):
        # 鍵盤控制連續左右運動
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed_x
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed_x

        # 限制邊界
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


class Meteor(pygame.sprite.Sprite):
    """ 敵軍隕石 """
    def __init__(self):
        super().__init__()
        self.radius = random.randint(15, 30)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, RED, (self.radius, self.radius), self.radius)
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-150, -40)
        self.speed_y = random.randint(3, 8)
        self.speed_x = random.randint(-2, 2)

    def update(self):
        # 往下方與側邊飄移
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        
        # 若出下邊界或左/右邊界，重新在上方隨機生成
        if self.rect.top > HEIGHT or self.rect.right < -50 or self.rect.left > WIDTH + 50:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speed_y = random.randint(3, 8)
            self.speed_x = random.randint(-2, 2)


class Bullet(pygame.sprite.Sprite):
    """ 玩家雷射子彈 """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((6, 15))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -12

    def update(self):
        # 往上飛
        self.rect.y += self.speed_y
        # 越界自動刪除，釋放記憶體
        if self.rect.bottom < 0:
            self.kill()

# ==================================================
# 遊戲主控制程式 (Game Controller)
# ==================================================

def draw_text(surf, text, size, x, y):
    """ 繪製文字與計分板 """
    # 使用系統預設字型
    font = pygame.font.SysFont("arial", size, bold=True)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("太空射擊大戰 - Python 2D 遊戲專題")
    clock = pygame.time.Clock()

    # 1. 建立精靈群組
    all_sprites = pygame.sprite.Group()
    meteors = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # 2. 建立玩家並加入管理
    player = Player()
    all_sprites.add(player)

    # 3. 產生 8 個初始隕石
    for _ in range(8):
        m = Meteor()
        all_sprites.add(m)
        meteors.add(m)

    score = 0
    lives = 3
    game_over = False

    # ==================== 遊戲主迴圈 ====================
    while True:
        clock.tick(FPS)
        
        # --- 1. 事件讀取 ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    # 按下空白鍵發射子彈 (單次事件觸發)
                    b = Bullet(player.rect.centerx, player.rect.top)
                    all_sprites.add(b)
                    bullets.add(b)
                elif event.key == pygame.K_r and game_over:
                    # 遊戲結束後按 R 重開
                    run_game()

        # --- 2. 邏輯狀態更新 ---
        if not game_over:
            all_sprites.update()

            # 檢測：子彈與隕石的碰撞
            # groupcollide(g1, g2, kill1, kill2)
            hits = pygame.sprite.groupcollide(bullets, meteors, True, True)
            for hit in hits:
                score += 10
                # 被摧毀後重新生成一個新隕石補上
                new_m = Meteor()
                all_sprites.add(new_m)
                meteors.add(new_m)

            # 檢測：玩家與隕石的碰撞 (使用圓形半徑碰撞提高精準度)
            player_hits = pygame.sprite.spritecollide(player, meteors, True)
            for hit in player_hits:
                lives -= 1
                print(f"太空船被隕石撞擊！剩餘生命：{lives}")
                # 重新補上隕石
                new_m = Meteor()
                all_sprites.add(new_m)
                meteors.add(new_m)
                if lives <= 0:
                    game_over = True

        # --- 3. 畫面繪製渲染 ---
        screen.fill(BLACK)
        
        # 繪製所有精靈物件
        all_sprites.draw(screen)
        
        # 繪製計分板與生命值
        draw_text(screen, f"SCORE: {score}", 30, WIDTH // 2, 10)
        draw_text(screen, f"LIVES: {lives}", 24, 60, 10)

        # 遊戲結束畫面覆蓋
        if game_over:
            draw_text(screen, "GAME OVER", 60, WIDTH // 2, HEIGHT // 3)
            draw_text(screen, "Press [R] to Restart", 30, WIDTH // 2, HEIGHT // 2)

        pygame.display.flip()

if __name__ == "__main__":
    run_game()
```

---

## 11.6 本章課後進階挑戰專題

為了加深你的程式實力，可以嘗試在現有的太空射擊遊戲中擴充以下機制：

### 挑戰 1：難度隨分數動態增加
在遊戲的 `update` 階段，當分數 (`score`) 達到特定門檻時，自動加快隕石的墜落速度：
```python
# 模擬在更新隕石時調用
# self.speed_y += (score // 100) * 0.5
```

### 挑戰 2：粒子爆炸效果 (Particle Effect)
當子彈撞擊隕石時，不要只讓隕石瞬間消失，而是向四周產生數個隨機飄散的小圓形粒子：
```python
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((6, 6))
        self.image.fill((255, 150, 0)) # 橘色爆炸火焰
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_x = random.randint(-4, 4)
        self.speed_y = random.randint(-4, 4)
        self.lifetime = 20 # 存活幀數
        
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()
```
