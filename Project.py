import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gojo Vs Sukuna!")

clock = pygame.time.clock()

WHITE = (255, 255, 255)
BLUE = (100, 149, 237)
GREEN = (34, 177, 76)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

font = pygame.font.SysFont("Arial", 28)

class Player:
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