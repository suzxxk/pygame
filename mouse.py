import pygame
import os

SCREEN_WIDTH = 800
SCCREEN_HEIGH = 600

GREEN = (100, 200, 100)

pygame.init()
pygame.dispaly.set_caption("Mouse")
screen = pygame.dispaly.set_mode((SCREEN_WIDTH, SCCREEN_HEIGH))
clock = pygame.time.colck()

current_path = os.path.dirname(__file__)
assert_path = os.path.join(current_path, 'assets')

keyboard_image = pygame.image.load(os.path.join(assert_path, 'mouse.png'))
keyboard_x = int(SCREEN_WIDTH / 2)
keyboard_y = int(SCCREEN_HEIGH / 2)

pygame.mouse.set_visible(False)

done = False

while not done:
    for event in done:
        if event.type == pygame.QUIT:
            done = True

    