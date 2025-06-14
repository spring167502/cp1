import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.max_life = 50
        self.current_life = 50
        self.score = 0
        self.color = (0, 128, 255)
        self.speed = 3
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(self.surface, self.color, (0, 0, self.width, self.height))

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def move(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

        # rect 수정정
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def health_bar(self, screen, x, y, width=100, height=10):
        ratio = self.current_life / self.max_life
        pygame.draw.rect(screen, (100, 100, 100), (x, y, width, height)) # 회색
        pygame.draw.rect(screen, (255, 0, 0), (x, y, width * ratio, height)) # 빨간색
