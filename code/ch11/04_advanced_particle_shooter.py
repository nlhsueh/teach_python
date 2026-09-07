# 04_advanced_particle_shooter.py - 太空射擊進階版 (加入粒子爆炸特效與動態難度增強)

import pygame
import random
import math
import sys

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 600
FPS = 60

BLACK = (15, 15, 25)
WHITE = (255, 255, 255)
GREEN = (0, 255, 120)
RED = (255, 70, 70)
YELLOW = (255, 230, 0)
CYAN = (0, 200, 255)
ORANGE = (255, 140, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("太空射擊大戰 - 粒子特效增強版")
clock = pygame.time.Clock()

# --- 粒子爆炸效果類別 (Particle) ---
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.size = random.randint(3, 7)
        self.image = pygame.Surface((self.size, self.size))
        self.color = random.choice([YELLOW, ORANGE, RED, WHITE])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        # 隨機向四周發散的速度向量
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 6)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        
        # 粒子存活幀數 (Lifetime)
        self.lifetime = random.randint(15, 30)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        self.lifetime -= 1
        # 壽命結束時自動移除精靈
        if self.lifetime <= 0:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, CYAN, [(20, 0), (0, 30), (40, 30)])
        pygame.draw.polygon(self.image, WHITE, [(20, 5), (10, 28), (30, 28)])
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20
        self.speed = 6
        self.last_shot = 0
        self.shoot_delay = 180

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(SCREEN_WIDTH, self.rect.right)

    def shoot(self, bullet_group, all_group):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            all_group.add(bullet)

class Meteor(pygame.sprite.Sprite):
    def __init__(self, speed_bonus=0):
        super().__init__()
        self.radius = random.randint(12, 22)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, RED, (self.radius, self.radius), self.radius)
        pygame.draw.circle(self.image, (220, 70, 70), (self.radius - 3, self.radius - 3), self.radius // 2)
        self.rect = self.image.get_rect()
        self.speed_bonus = speed_bonus
        self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed_y = random.randint(2, 5) + self.speed_bonus
        self.speed_x = random.randint(-1, 1)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
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
        self.speed = -12

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

def spawn_explosion(x, y, all_group, count=20):
    """產生一團粒子爆炸效果"""
    for _ in range(count):
        p = Particle(x, y)
        all_group.add(p)

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

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_over:
                    player.shoot(bullets, all_sprites)
                else:
                    all_sprites, meteors, bullets, player = reset_game()
                    score = 0
                    lives = 3
                    game_over = False

    if not game_over:
        all_sprites.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.shoot(bullets, all_sprites)

        # 碰撞檢測 1：子彈擊中隕石
        hits = pygame.sprite.groupcollide(meteors, bullets, True, True)
        for hit in hits:
            score += 10
            # 觸發粒子爆炸特效
            spawn_explosion(hit.rect.centerx, hit.rect.centery, all_sprites, count=18)
            
            # 動態難度：隨著分數增加，增加新隕石速度
            speed_bonus = min(score // 100, 4)
            m = Meteor(speed_bonus=speed_bonus)
            all_sprites.add(m)
            meteors.add(m)

        # 碰撞檢測 2：玩家撞到隕石
        hits = pygame.sprite.spritecollide(player, meteors, True)
        for hit in hits:
            lives -= 1
            # 觸發玩家受傷大爆炸
            spawn_explosion(hit.rect.centerx, hit.rect.centery, all_sprites, count=30)
            
            m = Meteor()
            all_sprites.add(m)
            meteors.add(m)
            if lives <= 0:
                spawn_explosion(player.rect.centerx, player.rect.centery, all_sprites, count=50)
                game_over = True

    screen.fill(BLACK)
    all_sprites.draw(screen)

    draw_text(screen, f"SCORE: {score}", 20, SCREEN_WIDTH // 2, 10, WHITE)
    draw_text(screen, f"LIVES: {'❤ ' * lives}", 18, 70, 10, RED)

    if game_over:
        draw_text(screen, "GAME OVER", 48, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3, RED)
        draw_text(screen, f"Final Score: {score}", 24, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, YELLOW)
        draw_text(screen, "Press SPACE to Restart", 20, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 3, WHITE)

    pygame.display.flip()

pygame.quit()
sys.exit()
