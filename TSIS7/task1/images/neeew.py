import pygame
import datetime

# def rot_center(image, angle, x, y):

#     rotated_image = pygame.transform.rotate(image, angle)
#     new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

#     return rotated_image, new_rect


pygame.init()

screen = pygame.display.set_mode((900, 700))
h = pygame.image.load("clock_main.png")
h = pygame.transform.scale(h, screen.get_size())

clock_second = pygame.image.load("clock_second-removebg-preview (1).png")
cl = screen.get_rect().center

clock_minute = pygame.image.load("roma_clock-removebg-preview.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(h, (0, 0))
    time_now = datetime.datetime.now()
    seconds_time = time_now.second
    minutes_time = time_now.minute
    # some_second, pos_second = rot_center(clock_second, 135 - seconds_time * 6, *cl)
    # some_minute, pos_minute = rot_center(clock_minute, 135 - minutes_time * 6, *cl)
    # screen.blit(some_second, pos_second)
    # screen.blit(some_minute, pos_minute)
    k1 = pygame.transform.rotate(clock_second, назымка)
    k2 = pygame.transform.rotate(clock_minute, 135 - minutes_time * 6)
    g1 = k1.get_rect().center
    g2 = k2.get_rect().center
    screen.blit(k1, (cl[0] - g1[0], cl[1] - g1[1]))
    screen.blit(k2, (cl[0] - g2[0], cl[1] - g2[1]))
    pygame.display.update()