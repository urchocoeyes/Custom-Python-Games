import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Nazym from KBTU")
screen.fill((255, 255, 255))

center = screen.get_rect().center
# print(center) # (450, 350) --> tuple
mickey_main = pygame.image.load("images//clock_main.png")
transformed_mickey_clock = pygame.transform.scale(mickey_main, screen.get_size())
# print(transformed_mickey_clock) --> <Surface(900x700x32 SW)>
image_seconds = pygame.image.load("images//clock_seconds_hand.png")
image_minutes = pygame.image.load("images//clock_minutes_hand.png")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(transformed_mickey_clock, (0, 0))
    time_now = datetime.datetime.now()
    seconds_now = time_now.second
    minutes_now = time_now.minute

    image_seconds_rotation = pygame.transform.rotate(image_seconds, 135 + seconds_now * 6)
    image_minutes_rotation = pygame.transform.rotate(image_minutes, 135 + minutes_now * 6)

    def_image_seconds_rotation_center = image_seconds_rotation.get_rect().center
    def_image_minutes_rotation_center = image_minutes_rotation.get_rect().center

    screen.blit(image_seconds_rotation, (center[0] - def_image_seconds_rotation_center[0], center[1] - def_image_seconds_rotation_center[1]))
    screen.blit(image_minutes_rotation, (center[0] - def_image_minutes_rotation_center[0], center[1] - def_image_minutes_rotation_center[1]))
    pygame.display.flip()
