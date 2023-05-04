import pygame
from pygame.locals import *
import time
import random
import psycopg2
import csv

pygame.init()


class Snake(pygame.sprite.Sprite):
    def __init__(self, size_of_main_screen):
        super().__init__()
        self.size_of_main_screen = size_of_main_screen
        self.size_block = 20
        self.start_pos = (random.randint(5, size_of_main_screen[0] // self.size_block - 1),
                          random.randint(5, size_of_main_screen[1] // self.size_block - 1))
        self.massive_snake = [self.start_pos]
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.gameover = False
        self.flag = False
        self.add_part = 0
        self.rand_score = random.randint(1, 5)

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
            if self.massive_snake[0][1] >= self.size_of_main_screen[1] // self.size_block - 1:
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

    def add_random_score(self):
        self.rand_score = random.randint(1, 5)

    def eda(self):
        self.steak = (random.randint(5, self.size_of_main_screen[0] // self.size_block - 1),
                      random.randint(5, self.size_of_main_screen[1] // self.size_block - 1))

    def build_eda(self):
        self.draw_block("yellow", self.steak[0], self.steak[1], self.main_screen)
        self.font_for_score = pygame.font.SysFont("Verdana", self.size_block)
        self.text_of_score_eda = self.font_for_score.render(str(self.rand_score), True, pygame.Color("Blue"))
        self.main_screen.blit(self.text_of_score_eda,
                              (self.size_block * self.steak[0] + 3, self.size_block * self.steak[1] - 3))

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


# input data
print("Пожалуйста введите свое имя: ")
name = input()
print("Пожалуйста введите свою фамилию: ")
surname = input()
print("Спасибо, готовы играть? ")
check_ready = input()
connect = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="nn22913705"
)
cur = connect.cursor()
cur.execute(f"SELECT record FROM snake_data WHERE name = '{name}' AND surname = '{surname}'")
rec_data = cur.fetchall()
some_score = 0
exists_flag = True
if not rec_data:
    some_score = 0
    exists_flag = False
else:
    some_score = rec_data[0][0]
    exists_flag = True

while check_ready != "yes":
    check_ready = input()

points = 0
point_font = pygame.font.SysFont("Vergana", 30)
level_font = pygame.font.SysFont("Vergana", 30)
main_screen = pygame.display.set_mode((700, 700))
image = pygame.image.load("background.png")
image = pygame.transform.scale(image, main_screen.get_rect().size)
some_snake = Snake(main_screen.get_rect().size)
level = 1
FramePerSecond = pygame.time.Clock()
cnt = 0
FPS = 10
flag = True


# cur.execute(f"INSERT INTO snake_data (name,surname, tel) VALUES ('{name}', '{surname}', {})")

def draw_play_desk():
    for i in range(71):
        for j in range(71):
            if i % 4 == 0 and j % 4 == 0:
                color = "black"
            else:
                color = "red"
            some_snake.draw_block(color, i, j, main_screen)


some_event = pygame.USEREVENT + 1
pygame.time.set_timer(some_event, 1000)
timer = 6
copy_of_timer = int(timer)
flag_to_pause = False
while True:
    if cnt == 4:
        cnt = 0
        if FPS <= 20:
            FPS += 2
            level += 1
            timer = max(2, timer - 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == some_event:
            copy_of_timer -= 1
    key = pygame.key.get_pressed()
    if key[pygame.K_TAB]:
        if flag_to_pause:
            flag_to_pause = False
        else:
            flag_to_pause = True

    if flag_to_pause:
        pause_font = pygame.font.SysFont("Vergena", 50)
        main_screen.fill(pygame.Color("white"))
        pause = pause_font.render("Pause, touch TAB to continue", True, pygame.Color("Black"))
        main_screen.blit(pause, (150, main_screen.get_rect().center[1] - 100))
    else:
        if some_snake.gameover:
            main_screen.fill(pygame.Color("red"))
            game_over_font = pygame.font.SysFont("Vergena", 50)
            game_over = game_over_font.render("Ooops, Game over", True, pygame.Color("white"))
            main_screen.blit(game_over, (185, main_screen.get_rect().center[1] - 100))
            score_overall = game_over_font.render("Your score is: " + str(points), True, pygame.Color("white"))
            main_screen.blit(score_overall, (main_screen.get_rect().center[0] - 130, main_screen.get_rect().center[1]))
            pygame.display.update()
            if exists_flag:
                if points > some_score:
                    cur.execute(
                        f"UPDATE snake_data SET record = '{points}' WHERE name = '{name}' AND surname = '{surname}'")
            else:
                cur.execute(f"INSERT INTO snake_data (name,surname, record) VALUES ('{name}', '{surname}', {points})")
            connect.commit()
            time.sleep(3)
            pygame.quit()
            exit()
        text_of_timer = level_font.render("Timer: " + str(copy_of_timer), True, "Green")
        timer_flag = False
        txt_of_score = level_font.render("Last score of user: " + str(some_score), True, "Blue")
        if copy_of_timer <= 0:
            timer_flag = True
            copy_of_timer = int(timer)
        if flag or timer_flag:
            some_snake.eda()
            some_snake.add_random_score()
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
                    some_snake.add_random_score()

        # draw_play_desk()
        # main_screen.fill(pygame.Color(159,241 , 220))
        main_screen.blit(image, (0, 0))
        some_snake.paint(main_screen)
        pic_coin = point_font.render("Score: " + str(points), True, pygame.Color("blue"))
        pic_level = level_font.render("Level: " + str(level), True, pygame.Color("yellow"))
        main_screen.blit(pic_coin, (some_snake.size_of_main_screen[0] - 95, 18))
        main_screen.blit(pic_level, (some_snake.size_of_main_screen[0] - 92, 45))
        some_snake.move()
        some_snake.add_part_of_snake()
        some_snake.collide_by_yourself()
        main_screen.blit(text_of_timer, (25, 25))
        main_screen.blit(txt_of_score, (25, 50))
        if not flag:
            some_snake.build_eda()

        if some_snake.massive_snake[0] == some_snake.steak:
            flag = True
            points += some_snake.rand_score
            cnt += 1
            some_snake.add_part += 1
            copy_of_timer = int(timer)

    pygame.display.update()

    FramePerSecond.tick(FPS)

