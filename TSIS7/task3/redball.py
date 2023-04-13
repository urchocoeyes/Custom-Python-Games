import pygame
pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Nazymka from KBBTTUU!!!")

running = True
x = 25
y = 25
clock = pygame.time.Clock()

while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and x <= 655: # 700 - 25 - 20
        x += 20
    if pressed[pygame.K_LEFT] and x >= 45:
        x -= 20
    if pressed[pygame.K_UP] and y >= 45:
        y -= 20
    if pressed[pygame.K_DOWN] and y <= 655:
        y += 20

    red_ball = pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)

    clock.tick(60)
    pygame.display.flip()
