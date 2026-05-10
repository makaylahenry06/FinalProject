import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gojo Vs Sukuna!")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (100, 149, 237)
GREEN = (34, 177, 76)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

font = pygame.font.SysFont("Arial", 28)

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 450, 50, 70)
        self.vel_y = 0
        self.speed = 6
        self.jump_power = -16
        self.on_ground = False
        self.health = 100
        self.dragging = False

    def move(self, keys):
        dx = 0

        if keys[pygame.K_LEFT]:
            dx = -self.speed

        if keys[pygame.K_RIGHT]:
            dx = self.speed

        self.rect.x += dx
    def gravity(self):
        self.vel_y += 1
        self.rect.y += self.vel_y

        if self.rect.y >= 450:
         self.rect.y = 450
         self.vel_y = 0
         self.on_ground = True

    def jump(self):
     if self.on_ground:
        self.vel_y = self.jump_power
        self.on_ground = False

    def draw(self):
     pygame.draw.rect(screen, RED, self.rect)

   
       
    





class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.speed = random.choice([-3, 3])

    def move(self):
        self.rect.x += self.speed

        if self.rect.x <= 0 or self.rect.x >= WIDTH - 50:
            self.speed *= -1

    def draw(self):
        pygame.draw.rect(screen, BLACK, self.rect)


class Boss:
    def __init__(self):
        self.rect = pygame.Rect(750, 300, 140, 140)
        self.health = 300
        self.angle = 0

    def move(self):
        self.angle += 0.03
        self.rect.y = 250 + int(math.sin(self.angle) * 100)

    def attack(self, player):
        if self.rect.colliderect(player.rect):
            player.health -= 1

    def draw(self):
        pygame.draw.rect(screen, PURPLE, self.rect)

        pygame.draw.rect(screen, RED, (650, 40, 300, 25))
        pygame.draw.rect(screen, GREEN, (650, 40, self.health, 25))

def handle_events(player):
    running = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player.rect.collidepoint(event.pos):
                player.dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            player.dragging = False

        if event.type == pygame.MOUSEMOTION:
            if player.dragging:
                player.rect.center = event.pos

    return running

def update_game(player, enemies, boss):
    keys = pygame.key.get_pressed()

    player.move(keys)
    player.gravity()

    for enemy in enemies:
        enemy.move()

        if player.rect.colliderect(enemy.rect):
            player.health -= 0.2

    boss.move()
    boss.attack(player)

    mouse_pressed = pygame.mouse.get_pressed()

    if mouse_pressed[0]:
        mouse_pos = pygame.mouse.get_pos()

        if boss.rect.collidepoint(mouse_pos):
            boss.health -= 1


def draw_game(player, enemies, boss):
    screen.fill(BLUE)

    pygame.draw.rect(screen, GREEN, (0, 520, WIDTH, 80))
    player.draw()

    for enemy in enemies:
        enemy.draw()

    boss.draw()

    hp_text = font.render(f"Gojo HP: {int(player.health)}", True, WHITE)
    screen.blit(hp_text, (20, 20))

    info = font.render(
        "Arrow Keys = Move / SPACE = Jump / Drag Character / Click Sukuna to Attack",
        True,
        YELLOW
    )
    screen.blit(info, (20, 500))

    pygame.display.update()

def main():
    player = Player()

    enemies = [
        Enemy(300, 470),
        Enemy(500, 470),
        Enemy(650, 470)
    ]

    boss = Boss()

    running = True
    while running:
        clock.tick(60)
        running = handle_events(player)
        update_game(player, enemies, boss)
        draw_game(player, enemies, boss)

        if boss.health <= 0:
            screen.fill(BLACK)

            win_text = font.render(
                "GOJO WINS!",
                True,
                YELLOW
            )
            
            screen.blit(win_text, (300, 280))
            pygame.display.update()
            pygame.time.delay(4000)

            running = False

    pygame.quit()       

if __name__ == "__main__":
    main()