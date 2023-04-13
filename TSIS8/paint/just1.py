import pygame
from pygame.locals import *
import time

pygame.init()

clock = pygame.time.Clock()


def dwar_two_point(point_1, point_2, radius, main_screen, color):
    dx = abs(point_2[0] - point_1[0])
    dy = abs(point_1[1] - point_2[1])
    for i in range(0, max(dx, dy)):
        procent = i / max(dy, dx)
        x = point_1[0] + (point_2[0] - point_1[0]) * procent
        y = point_1[1] + (point_2[1] - point_1[1]) * procent
        pygame.draw.circle(main_screen, color, (x, y), radius)


color = pygame.Color("black")
size_rect = 1
flag_some = False

circuit_var_flag = False


def main():
    radius = 4
    flag_circle = False
    main_screen = pygame.display.set_mode((700, 700))
    main_screen.fill("white")
    points_list = []
    flag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        mouse_press = pygame.mouse.get_pressed()
        keyboard = pygame.key.get_pressed()
        coord_mouse = pygame.mouse.get_pos()
        if keyboard[K_r]:
            global color
            color = pygame.Color("red")
            points_list = list()
        elif keyboard[K_e]:
            color = "white"
            points_list = list()
        elif keyboard[K_k]:
            flag = True
        elif keyboard[K_c]:
            flag_circle = True
        elif keyboard[K_b]:
            color = "black"
        elif keyboard[K_y]:
            color = "yellow"
        elif keyboard[K_o]:
            color = "orange"
        elif keyboard[K_p]:
            color = pygame.Color("purple")
        elif keyboard[K_v]:
            color = "violet"

        if flag:
            global size_rect
            if keyboard[K_LSHIFT]:
                size_rect += 1
            elif keyboard[K_LCTRL]:
                size_rect = max(1, size_rect - 1)
            global flag_some
            if color== "white":
                color  = "black"
            if mouse_press[0]:
                flag_some = True
                points_list.append(coord_mouse)
            if flag_some and not mouse_press[0] and len(points_list) >= 2:
                flag = False
                v1 = points_list[0]
                v2 = points_list[-1]
                # some_rect = pygame.Rect(points_list[0], ((points_list[-1][0] - points_list[0][0]), (points_list[-1][1] - points_list[0][1])))
                size_rect = max(1, radius // 4)
                some_rect = pygame.Rect(min(v1[0], v2[0]), min(v1[1], v2[1]), abs(v1[0] - v2[0]), abs(v1[1] - v2[1]))
                pygame.draw.rect(main_screen, color, some_rect, size_rect)
                points_list = list()
        elif flag_circle:

            global circuit_var_flag
            if color == "white":
                color = "black"
            if mouse_press[0]:
                circuit_var_flag = True
                points_list.append(coord_mouse)
            if circuit_var_flag and not mouse_press[0] and len(points_list) >= 2:
                flag_circle = False
                j1 = points_list[0]
                j2 = points_list[-1]
                size_of_circuit = max(1, radius // 4)
                pygame.draw.circle(main_screen, color, (min(j1[0], j2[0]) + abs(j1[0] - j2[0]) / 2,
                                                        min(j1[1], j2[1]) + abs(j1[1] - j2[1]) / 2),
                                   max(abs(j1[1] - j2[1]), abs(j1[0] - j2[0])) / 2, size_of_circuit)
                points_list = list()
        else:
            if keyboard[K_UP]:
                radius += 1
            elif keyboard[K_DOWN]:
                radius = max(1, radius - 1)
            if not mouse_press[0]:
                points_list = list()
            if coord_mouse != (0, 0) and mouse_press[0]:
                points_list.append(pygame.mouse.get_pos())
                # points_list = points_list[-240:]

            for i in range(len(points_list) - 1):
                dwar_two_point(points_list[i], points_list[i + 1], radius, main_screen, color)

        pygame.display.update()
        clock.tick(60)


main()