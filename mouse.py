import pygame
import os

SCREEN_WIDTH = 800
SCCREEN_HEIGH = 600

GREEN = (100, 200, 100)

pygame.init()
pygame.display.set_caption("Mouse")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCCREEN_HEIGH))
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
assert_path = os.path.join(current_path, 'assets')

mouse_image = pygame.image.load(os.path.join(assert_path, 'mouse.png'))
mouse_x = int(SCREEN_WIDTH / 2)
mouse_y = int(SCCREEN_HEIGH / 2)

pygame.mouse.set_visible(False)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]

    screen.fill(GREEN)
    screen.blit(mouse_image, pos)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()


    










