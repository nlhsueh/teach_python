# 03_space_shooter.py - 太空射擊大戰專案 (完整物件導向與精靈群組架構)

import pygame
import random
import sys

# 1. 遊戲基礎設定
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 600
FPS = 60

# 顏色常數
BLACK = (15, 15, 25)
WHITE = (255, 255, 255)
GREEN = (0, 255, 120)
RED = (255, 70, 70)
YELLOW = (255, 230, 0)
CYAN = (0, 200, 255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("太空射擊大戰 (Space Shooter)")
clock = pygame.time.Clock()

# --- 2. 精靈類別設計 (Sprite Classes) ---

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 繪製戰機造型 (若無圖片，使用向量幾何繪製)
        self.image = pygame.Surface((40, 30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, CYAN, [(20, 0), (0, 30), (40, 30)])
        pygame.draw.polygon(self.image, WHITE, [(20, 5), (10, 28), (30, 28)])
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20
        self.speed = 6
        self.last_shot = 0
        self.shoot_delay = 200 # 射擊冷卻時間 (毫秒)

    def update(self):
        # 左右鍵盤移動
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        # 邊界限制
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def shoot(self, bullet_group, all_group):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            all_group.add(bullet)

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = random.randint(12, 22)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, RED, (self.radius, self.radius), self.radius)
        pygame.draw.circle(self.image, (200, 50, 50), (self.radius - 3, self.radius - 3), self.radius // 2)
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed_y = random.randint(2, 6)
        self.speed_x = random.randint(-1, 1)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        # 掉出螢幕底部後自動重置到頂端
        if self.rect.top > SCREEN_HEIGHT or self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.reset_position()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((4, 12))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        # 飛出螢幕頂部時銷毀精靈釋放記憶體
        if self.rect.bottom < 0:
            self.kill()

# --- 3. 遊戲本體與狀態重置 ---

def reset_game():
    all_sprites = pygame.sprite.Group()
    meteors = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    for _ in range(8):
        m = Meteor()
        all_sprites.add(m)
        meteors.add(m)

    return all_sprites, meteors, bullets, player

all_sprites, meteors, bullets, player = reset_game()
score = 0
lives = 3
game_over = False

try:
    font_name = pygame.font.match_font('arial') or pygame.font.get_default_font()
except Exception:
    font_name = None

def draw_text(surf, text, size, x, y, color=WHITE):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# --- 4. 遊戲主迴圈 ---
running = True
while running:
    clock.tick(FPS)

    # 1. 事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_over:
                    player.shoot(bullets, all_sprites)
                else:
                    # 重新開始遊戲
                    all_sprites, meteors, bullets, player = reset_game()
                    score = 0
                    lives = 3
                    game_over = False

    # 2. 遊戲狀態更新 (若未結束)
    if not game_over:
        all_sprites.update()

        # 連續按空白鍵射擊
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.shoot(bullets, all_sprites)

        # 碰撞檢測 1：子彈擊中隕石 (groupcollide)
        hits = pygame.sprite.groupcollide(meteors, bullets, True, True)
        for hit in hits:
            score += 10
            # 補回被摧毀的隕石
            m = Meteor()
            all_sprites.add(m)
            meteors.add(m)

        # 碰撞檢測 2：玩家撞到隕石 (spritecollide)
        hits = pygame.sprite.spritecollide(player, meteors, True)
        for hit in hits:
            lives -= 1
            # 補回隕石
            m = Meteor()
            all_sprites.add(m)
            meteors.add(m)
            if lives <= 0:
                game_over = True

    # 3. 畫面繪製
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # 繪製 HUD (分數與生命值)
    draw_text(screen, f"SCORE: {score}", 20, SCREEN_WIDTH // 2, 10, WHITE)
    draw_text(screen, f"LIVES: {'❤ ' * lives}", 18, 70, 10, RED)

    # 遊戲結束結算畫面
    if game_over:
        draw_text(screen, "GAME OVER", 48, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3, RED)
        draw_text(screen, f"Final Score: {score}", 24, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, YELLOW)
        draw_text(screen, "Press SPACE to Restart", 20, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 3, WHITE)

    pygame.display.flip()

pygame.quit()
sys.exit()
