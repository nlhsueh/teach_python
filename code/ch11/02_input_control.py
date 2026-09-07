# 02_input_control.py - 鍵盤連續控制與滑鼠事件處理

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("鍵盤與滑鼠整合控制示範")

clock = pygame.time.Clock()

# 玩家方塊屬性
player_x = 400
player_y = 300
player_speed = 5
player_size = 40

# 滑鼠點擊標記清單
clicks = []

running = True
while running:
    clock.tick(60)
    
    # --- 1. 單次觸發事件處理 (Event Queue) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # 監聽滑鼠按下事件 (適合觸發單次動作，如射擊或點擊選單)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # 1 代表滑鼠左鍵
                mouse_pos = event.pos # (x, y)
                clicks.append(mouse_pos)
                
    # --- 2. 持續按鍵狀態輪詢 (Key Polling - 適合流暢人物移動) ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += player_speed
        
    # 邊界限制 (Clamp Boundary)
    player_x = max(0, min(800 - player_size, player_x))
    player_y = max(0, min(600 - player_size, player_y))
    
    # --- 3. 繪製畫面 ---
    screen.fill((30, 30, 40))
    
    # 繪製滑鼠歷史點擊標記 (橘色圓點)
    for pos in clicks:
        pygame.draw.circle(screen, (255, 165, 0), pos, 8)
        
    # 繪製由玩家控制的藍色方塊
    pygame.draw.rect(screen, (0, 150, 255), (player_x, player_y, player_size, player_size))
    
    pygame.display.flip()

pygame.quit()
sys.exit()
