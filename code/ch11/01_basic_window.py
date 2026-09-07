# 01_basic_window.py - Pygame 視窗初始化、遊戲迴圈與基礎幾何繪圖

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

# 遊戲主要迴圈 (Game Loop)
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
