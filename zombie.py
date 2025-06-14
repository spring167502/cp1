import pygame
import math

class Zombie:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.life = 30
        self.color = (255, 0, 0)
        self.speed = 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(self.surface, self.color, (0, 0, self.width, self.height))

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def move(self, target):
        dx = target.x - self.x
        dy = target.y - self.y
        dist = math.hypot(dx, dy)

        if dist != 0:
            dx /= dist
            dy /= dist
            self.x += dx * self.speed
            self.y += dy * self.speed
            
        # rect 수정정
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def hit(self):
        if self.life == 20:
            self.color = (255, 110, 110)
            pygame.draw.rect(self.surface, self.color, (0, 0, self.width, self.height))
        elif self.life == 10:
            self.color = (255, 220, 220)
            pygame.draw.rect(self.surface, self.color, (0, 0, self.width, self.height))
