import pygame
import math

class Bullet:
    def __init__(self, x, y, mouse_pos):
        self.x = x
        self.y = y
        self.radius = 5
        self.color = (0, 0, 0)
        self.speed = 4

        # direction 계산산
        dx = mouse_pos[0] - x
        dy = mouse_pos[1] - y
        dist = math.hypot(dx, dy)

        if dist != 0:
            dx /= dist
            dy /= dist

        self.direction = (dx, dy)

    def move(self):
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)