import pygame
pygame.init()

screen = pygame.display.set_mode((800, 800))


def round_line(canvas, color, start, end, radius=1) :
    x_axis = end[0] - start[0]
    y_axis = end[1] - start[1]
    dist = max(abs(x_axis), abs(y_axis))
    for i in range(dist):
        x = int(start[0] + float(i) / dist * x_axis)
        y = int(start[1] + float(i) / dist * y_axis)
        pygame.draw.circle(canvas, color, (x, y), radius)


def draw_rect(ch_color):
    pos = pygame.mouse.get_pos()
    print("pos", pos)
    rect_size = (50, 50)
    print("rect_size[0]", rect_size[0])
    rect_pos = (pos[0] - rect_size[0] / 2, pos[1] - rect_size[1] / 2)
    print("rect_pos", rect_pos)
    pygame.draw.rect(screen, ch_color, (rect_pos, rect_size))


def draw_circle(ch_color):
    pos = pygame.mouse.get_pos()
    radius = 25
    pygame.draw.circle(screen, ch_color, pos, radius)


def main():
    running = True
    draw_on = False
    last_pos = (0, 0)
    radius = 5
    ch_color = (255, 255, 255)
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN:
                if e.key == ord("b"):
                    ch_color = (0, 0, 255)
                if e.key == ord("y"):
                    ch_color = (255, 255, 0)
                if e.key == ord("g"):
                    ch_color = (0, 255, 0)
                if e.key == ord("w"):
                    ch_color = (255, 255, 255)
                if e.key == ord("r"):
                    draw_rect(ch_color)
                if e.key == ord("c"):
                    draw_circle(ch_color)
                if e.key == ord("e"):
                    ch_color = (0, 0, 0)

            if e.type == pygame.MOUSEBUTTONDOWN: # нажатие = круг
                color = ch_color
                pygame.draw.circle(screen, color, e.pos, radius)
                draw_on = True
            if e.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if e.type == pygame.MOUSEMOTION: # all motion constructed with circles
                if draw_on:
                    pygame.draw.circle(screen, color, e.pos, radius)
                    round_line(screen, color, e.pos, last_pos, radius)
                last_pos = e.pos
        pygame.display.flip()


if __name__ == '__main__':
    main()



# import pygame
# from pygame.locals import *
# import time
#
# pygame.init()
#
# clock = pygame.time.Clock()
#
#
# def dwar_two_point(point_1, point_2, radius, main_screen, color):
#     dx = abs(point_2[0] - point_1[0])
#     dy = abs(point_1[1] - point_2[1])
#     for i in range(0, max(dx, dy)):
#         procent = i / max(dy, dx)
#         x = point_1[0] + (point_2[0] - point_1[0]) * procent
#         y = point_1[1] + (point_2[1] - point_1[1]) * procent
#         pygame.draw.circle(main_screen, color, (x, y), radius)
#
#
# color = pygame.Color("black")
# size_rect = 1
# flag_some = False
#
# circuit_var_flag = False
#
#
# def main():
#     radius = 4
#     flag_circle = False
#     main_screen = pygame.display.set_mode((700, 700))
#     main_screen.fill("white")
#     points_list = []
#     flag = False
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#         mouse_press = pygame.mouse.get_pressed()
#         keyboard = pygame.key.get_pressed()
#         coord_mouse = pygame.mouse.get_pos()
#         if keyboard[K_r]:
#             global color
#             color = pygame.Color("red")
#             points_list = list()
#         elif keyboard[K_e]:
#             color = "white"
#             points_list = list()
#         elif keyboard[K_k]:
#             flag = True
#         elif keyboard[K_c]:
#             flag_circle = True
#         elif keyboard[K_b]:
#             color = "black"
#         elif keyboard[K_y]:
#             color = "yellow"
#         elif keyboard[K_o]:
#             color = "orange"
#         elif keyboard[K_p]:
#             color = pygame.Color("purple")
#         elif keyboard[K_v]:
#             color = "violet"
#
#         if flag:
#             global size_rect
#             if keyboard[K_LSHIFT]:
#                 size_rect += 1
#             elif keyboard[K_LCTRL]:
#                 size_rect = max(1, size_rect - 1)
#             global flag_some
#             if color == "white":
#                 color = "black"
#             if mouse_press[0]:
#                 flag_some = True
#                 points_list.append(coord_mouse)
#             if flag_some and not mouse_press[0] and len(points_list) >= 2:
#                 flag = False
#                 v1 = points_list[0]
#                 v2 = points_list[-1]
#                 # some_rect = pygame.Rect(points_list[0], ((points_list[-1][0] - points_list[0][0]), (points_list[-1][1] - points_list[0][1])))
#                 size_rect = max(1, radius // 4)
#                 some_rect = pygame.Rect(min(v1[0], v2[0]), min(v1[1], v2[1]), abs(v1[0] - v2[0]), abs(v1[1] - v2[1]))
#                 pygame.draw.rect(main_screen, color, some_rect, size_rect)
#                 points_list = list()
#         elif flag_circle:
#
#             global circuit_var_flag
#             if color == "white":
#                 color = "black"
#             if mouse_press[0]:
#                 circuit_var_flag = True
#                 points_list.append(coord_mouse)
#             if circuit_var_flag and not mouse_press[0] and len(points_list) >= 2:
#                 flag_circle = False
#                 j1 = points_list[0]
#                 j2 = points_list[-1]
#                 size_of_circuit = max(1, radius // 4)
#                 pygame.draw.circle(main_screen, color, (min(j1[0], j2[0]) + abs(j1[0] - j2[0]) / 2,
#                                                         min(j1[1], j2[1]) + abs(j1[1] - j2[1]) / 2),
#                                    max(abs(j1[1] - j2[1]), abs(j1[0] - j2[0])) / 2, size_of_circuit)
#                 points_list = list()
#         else:
#             if keyboard[K_UP]:
#                 radius += 1
#             elif keyboard[K_DOWN]:
#                 radius = max(1, radius - 1)
#             if not mouse_press[0]:
#                 points_list = list()
#             if coord_mouse != (0, 0) and mouse_press[0]:
#                 points_list.append(pygame.mouse.get_pos())
#                 # points_list = points_list[-240:]
#
#             for i in range(len(points_list) - 1):
#                 dwar_two_point(points_list[i], points_list[i + 1], radius, main_screen, color)
#
#         pygame.display.update()
#         clock.tick(60)
#
#
# main()
print(max(5, 10))