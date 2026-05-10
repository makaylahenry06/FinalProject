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
        dx = self.speed
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
        for event.type == pygame.QUIT:
            running = False