import pygame
import sys
import random
from player import Player
from zombie import Zombie
from bullet import Bullet

# pygame 초기화
pygame.mixer.init()
pygame.init()
clock = pygame.time.Clock()

# 화면 생성
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont(None, 36)  # 기본 글꼴, 크기 36
pygame.display.set_caption("Zombie Survival")

# player 생성
player = Player(400, 300)

# zombie 생성 시간
zombies = []
spawn_delay = 2000  # 2초 (2000밀리초)
last_spawn_time = 0
spawn_zombies = 0
count_zombies = 0

# bullets list
bullets = []
bullet_cooldown = 400  # ms
last_shot_time = 0

# 메인 루프
running = True
while running:
    # tick
    now_bullet = pygame.time.get_ticks()
    now_zombie = pygame.time.get_ticks()
    spawn_zombies = 1 + pygame.time.get_ticks() // 10000

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # player event
    keys = pygame.key.get_pressed()
    player.move(keys)

    # bullet 생성
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:
        if now_bullet - last_shot_time >= bullet_cooldown:
            player_center_x = player.x + player.width // 2 # 중심 위치로 계산
            player_center_y = player.y + player.height // 2
            bullet = Bullet(player_center_x, player_center_y, pygame.mouse.get_pos())
            bullets.append(bullet)
            last_shot_time = now_bullet

    # bullet event
    for bullet in bullets:
        bullet.move()

    # zombie 생성 (시간 경과에 따라 늘어나는 좀비)
    if now_zombie - last_spawn_time >= spawn_delay:
        for i in range(spawn_zombies):
            rand_zombie = random.randint(0, 3)
            if rand_zombie == 0:
                zombie = Zombie(-30, random.randint(-30,600))
            elif rand_zombie == 1:
                zombie = Zombie(800, random.randint(-30,600))
            elif rand_zombie == 2:
                zombie = Zombie(random.randint(-30, 800), -30)
            else:
                zombie = Zombie(random.randint(-30,800), 600)
            zombies.append(zombie)
        last_spawn_time = now_zombie

    # zombie event
    for zombie in zombies:
        zombie.move(player)

        # player - zombie 충돌 구현
        if zombie.rect.colliderect(player.rect):
            player.current_life -= 10
            zombies.remove(zombie)

            # Game Over
            if player.current_life == 0:
                print("Game Over")
                print(f"Your Final Score is {player.score}")
                running = False

        # bullet - zombie 충돌 구현
        for bullet in bullets:
            if (zombie.x <= bullet.x <= zombie.x + zombie.width) and (zombie.y <= bullet.y <= zombie.y + zombie.height):
                zombie.life -= 10
                bullets.remove(bullet)
                
                # zombie 피격 체크
                zombie.hit()

                # zombie 사망
                if zombie.life == 0:
                    player.score += 1
                    zombies.remove(zombie)



    # 화면 업데이트
    screen.fill((255, 255, 255))
    player.draw(screen)
    player.health_bar(screen, 10, 10)
    score_text = font.render(f"Score: {player.score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 30))
    for bullet in bullets:
        bullet.draw(screen)
    for zombie in zombies:
        zombie.draw(screen)
    pygame.display.flip()
    clock.tick(60)

# pygame 종료
pygame.quit()
sys.exit()