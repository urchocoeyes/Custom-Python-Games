import pygame
from pygame.locals import *
import time
import random

pygame.init()


class Snake(pygame.sprite.Sprite):
    def __init__(self, size_of_main_screen):
        super().__init__()
        self.size_of_main_screen = size_of_main_screen
        self.size_block = 20
        self.start_pos = (random.randint(5, size_of_main_screen[0] // self.size_block),
                          random.randint(5, size_of_main_screen[1] // self.size_block))
        self.massive_snake = [self.start_pos]
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.gameover = False
        self.flag = False
        self.add_part = 0

    def move(self):
        self.touch_buttom = pygame.key.get_pressed()
        if self.touch_buttom[K_UP] and not self.down:
            self.up = True
            self.left = False
            self.right = False
            self.down = False
        elif self.touch_buttom[K_DOWN] and not self.up:
            self.up = False
            self.left = False
            self.right = False
            self.down = True
        elif self.touch_buttom[K_LEFT] and not self.right:
            self.up = False
            self.left = True
            self.right = False
            self.down = False
        elif self.touch_buttom[K_RIGHT] and not self.left:
            self.up = False
            self.left = False
            self.right = True
            self.down = False

        tmp = tuple(self.massive_snake[0])
        if self.up:
            if self.massive_snake[0][1] <= 0:
                self.gameover = True
            else:

                self.massive_snake[0] = (self.massive_snake[0][0], self.massive_snake[0][1] - 1)

        if self.down:
            if self.massive_snake[0][1] >= self.size_of_main_screen[1] // self.size_block:
                self.gameover = True
            else:
                # self.rect.center = (self.rect.center[0], self.rect.center[1] + self.speed)
                self.massive_snake[0] = (self.massive_snake[0][0], self.massive_snake[0][1] + 1)

        if self.left:
            if self.massive_snake[0][0] <= 0:
                self.gameover = True
            else:
                # self.rect.center = (self.rect.center[0] - self.speed, self.rect.center[1])
                self.massive_snake[0] = (self.massive_snake[0][0] - 1, self.massive_snake[0][1])
        if self.right:
            if self.massive_snake[0][0] >= self.size_of_main_screen[0] // self.size_block - 1:
                self.gameover = True
            else:
                self.massive_snake[0] = (self.massive_snake[0][0] + 1, self.massive_snake[0][1])

        tmp2 = 0
        if self.flag:
            for i in range(1, len(self.massive_snake)):
                tmp2 = tuple(self.massive_snake[i])
                self.massive_snake[i] = tmp
                tmp = tuple(tmp2)

    def draw_block(self, color, x, y, main_screen):
        pygame.draw.rect(main_screen, color,
                         (x * self.size_block, y * self.size_block, self.size_block, self.size_block))

    def paint(self, main_screen):
        self.main_screen = main_screen

        for i in self.massive_snake:
            self.draw_block("green", i[0], i[1], main_screen)

    def eda(self):
        self.steak = (random.randint(5, self.size_of_main_screen[0] // self.size_block - 1),
                      random.randint(5, self.size_of_main_screen[1] // self.size_block - 1))

    def build_eda(self):
        self.draw_block("yellow", self.steak[0], self.steak[1], self.main_screen)

    def add_part_of_snake(self):
        if self.add_part >= 1:
            self.last_element = self.massive_snake[-1]
            self.massive_snake.append((self.last_element[0], self.last_element[1] + 1))
            self.add_part = 0
            self.flag = True

    def collide_by_yourself(self):
        for i in range(3, len(self.massive_snake)):
            if self.massive_snake[0] == self.massive_snake[i]:
                self.gameover = True


points = 0
point_font = pygame.font.SysFont("Vergana", 30)
level_font = pygame.font.SysFont("Vergana", 30)
main_screen = pygame.display.set_mode((700, 700))

some_snake = Snake(main_screen.get_rect().size)
level = 0
FramePerSecond = pygame.time.Clock()
cnt = 0
FPS = 10
flag = True


def draw_play_desk():
    for i in range(71):
        for j in range(71):
            if (i + j) % 2 == 0:
                color = "black"
            else:
                color = "red"
            some_snake.draw_block(color, i, j, main_screen)


while True:
    if cnt == 4:
        cnt = 0
        if FPS <= 20:
            FPS += 2
            level += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if some_snake.gameover:
        main_screen.fill(pygame.Color("red"))
        game_over_font = pygame.font.SysFont("Vergena", 50)
        game_over = game_over_font.render("Ooops, Game over", True, pygame.Color("white"))
        main_screen.blit(game_over, (185, main_screen.get_rect().center[1] - 100))
        score_overall = game_over_font.render("Your score is: " + str(points), True, pygame.Color("white"))
        main_screen.blit(score_overall, (main_screen.get_rect().center[0] - 130, main_screen.get_rect().center[1]))
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        exit()

    if flag:
        some_snake.eda()
        flag = False
        mini_flag = True
        while mini_flag:
            super_mini_flag = True
            for n in some_snake.massive_snake:
                if n == some_snake.steak:
                    super_mini_flag = False
            if super_mini_flag:
                mini_flag = False
            else:
                some_snake.eda()

    draw_play_desk()
    some_snake.paint(main_screen)
    pic_coin = point_font.render("Score: " + str(points), True, pygame.Color("blue"))
    pic_level = level_font.render("Level: " + str(level), True, pygame.Color("yellow"))
    main_screen.blit(pic_coin, (some_snake.size_of_main_screen[0] - 95, 18))
    main_screen.blit(pic_level, (some_snake.size_of_main_screen[0] - 79, 45))
    some_snake.move()
    some_snake.add_part_of_snake()
    some_snake.collide_by_yourself()
    if not flag:
        some_snake.build_eda()

    if some_snake.massive_snake[0] == some_snake.steak:
        flag = True
        points += 1
        cnt += 1
        some_snake.add_part += 1
    pygame.display.update()

    FramePerSecond.tick(FPS)
