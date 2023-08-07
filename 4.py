import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption("pygame")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

ball_x = SCREEN_WIDTH//2
ball_y = SCREEN_HEIGHT//2
ball_dx = 0
ball_dy = 0
ball_size = 40

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_dx = -3
            elif event.key == pygame.K_RIGHT:
                ball_dx = 3
            elif event.key == pygame.K_UP:
                ball_dy = -3
            elif event.key == pygame.K_DOWN:
                ball_dy = 3

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ball_dx = 0

            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ball_dy = 0

    screen.fill(WHITE)    
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit