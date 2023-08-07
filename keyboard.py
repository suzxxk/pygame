import pygame
import os
# 게임 스크린 크기
SCREEN_WIDTH = 800
SCCREEN_HEIGH = 600
#색 정의
GRAY = (200, 200, 200)
#pygame 초기화
pygame.init()
#윈도우 제목
pygame.display.set_caption("Keyboard")
#스크린 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCCREEN_HEIGH))
#게임 화면 업데이트 속도
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
assert_path = os.path.join(current_path, 'assets')

keyboard_image = pygame.image.load(os.path.join(assert_path, 'keyboard.png'))
keyboard_x = int(SCREEN_WIDTH / 2)
keyboard_y = int(SCCREEN_HEIGH / 2)
keyboard_dx = 0
keyboard_dy = 0

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keyboard_dx = -3
            elif event.key == pygame.K_RIGHT:
                keyboard_dx = 3
            elif event.key == pygame.K_UP:
                keyboard_dy = -3
            elif event.key == pygame.K_DOWN:
                keyboard_dy = 3

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                keyboard_dx = 0

            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                keyboard_dy = 0

    keyboard_x += keyboard_dx
    keyboard_y += keyboard_dy

    screen.fill(GRAY)
    screen.blit(keyboard_image, [keyboard_x, keyboard_y])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

