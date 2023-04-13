# working code
import pygame
import random
import time
from pygame.locals import *

pygame.init()
coins = 0


class Anti_cars(pygame.sprite.Sprite):
    def __init__(self, size_of_main_screen):
        super().__init__
        self.size_of_main_screen = size_of_main_screen
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.start_pos = (random.randint(5, self.size_of_main_screen[0]), 5)
        self.rect.center = self.start_pos
        self.some_value = 2

    def walk(self):
        if self.rect.center[1] > self.size_of_main_screen[1]:
            self.rect.center = (random.randint(5, self.size_of_main_screen[0]), 5)
        else:
            self.rect.center = (self.rect.center[0], self.rect.center[1] + self.some_value)

    def build(self, main_image):
        self.main_image = main_image
        self.main_image.blit(self.image, self.rect.center)


class Cars(pygame.sprite.Sprite):
    def __init__(self, size_of_main_screen):
        super().__init__
        self.size_of_main_screen = size_of_main_screen
        self.image = pygame.image.load("Player.png")
        self.start_pos = (random.randint(5, self.size_of_main_screen[0]), self.size_of_main_screen[1] * 0.8)
        self.rect = self.image.get_rect()
        self.rect.center = self.start_pos
        self.speed = 4
        self.some_coin = pygame.image.load("coin.png")
        self.image_coin = pygame.transform.scale(self.some_coin, (40, 40))
        self.rect_coin = self.image_coin.get_rect()

    def walk(self):
        if self.rect.center[0] > self.size_of_main_screen[0]:
            self.rect.center = (5, self.rect.center[1])
        elif self.rect.center[1] > self.size_of_main_screen[1]:
            self.rect.center = (self.rect.center[0], 5)
        elif self.rect.center[0] < 0:
            self.rect.center = (self.size_of_main_screen[0] - 5, self.rect.center[1])
        elif self.rect.center[1] < 0:
            self.rect.center = (self.rect.center[0], self.size_of_main_screen[1] - 5)
        else:
            key_put = pygame.key.get_pressed()
            if key_put[K_LEFT]:
                self.rect.move_ip(-self.speed, 0)
            elif key_put[K_RIGHT]:
                self.rect.move_ip(self.speed, 0)
            elif key_put[K_UP]:
                self.rect.move_ip(0, -self.speed)
            elif key_put[K_DOWN]:
                self.rect.move_ip(0, self.speed)

    def build(self, main_image):
        self.main_image = main_image
        self.main_image.blit(self.image, self.rect.center)

    def coin(self):
        self.rect_coin.center = (random.randint(2, self.size_of_main_screen[0] - 10),
                                 random.randint(2, self.size_of_main_screen[1] - 10))

    def build_coin(self, main_image):
        self.main_image = main_image
        self.main_image.blit(self.image_coin, self.rect_coin.center)


some_picture = pygame.image.load("AnimatedStreet.png")

main_screen = pygame.display.set_mode(some_picture.get_size())
a_car = Anti_cars(some_picture.get_size())
player = Cars(some_picture.get_size())

pygame.mixer.music.load("snowman.mp3")
pygame.mixer.music.play(-1)
font = pygame.font.SysFont("Verdana", 20)

FramePerSec = pygame.time.Clock()
FPS = 60
bonus = pygame.USEREVENT + 1
pygame.time.set_timer(bonus, 1000)
difficult = pygame.USEREVENT + 2
pygame.time.set_timer(difficult, 2000)

bolean = True
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == difficult:
            if a_car.some_value < 8:
                a_car.some_value += 1
    main_screen.blit(some_picture, (0, 0))

    if bolean:
        player.coin()
        player.build_coin(some_picture)
        bolean = False

    shadow_coin = font.render(str(coins), True, pygame.Color("yellow"))
    main_screen.blit(shadow_coin, (player.size_of_main_screen[0] - 20, 10))
    a_car.build(main_screen)
    player.build(main_screen)
    a_car.walk()
    player.walk()
    if a_car.rect.colliderect(player.rect):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("crash.wav")
        pygame.mixer.music.play(1)
        main_screen.fill(pygame.Color("red"))
        game_over_font = pygame.font.SysFont("Vergena", 50)
        game_over = game_over_font.render("Ooops, Game over", True, pygame.Color("white"))
        main_screen.blit(game_over, (30, main_screen.get_rect().center[1]))
        score_overall = game_over_font.render("Your score is: " + str(coins), True, pygame.Color("white"))
        main_screen.blit(score_overall,
                         (main_screen.get_rect().center[0] - 170, main_screen.get_rect().center[1] - 100))
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        exit()

    if (player.rect_coin).colliderect(player.rect):
        coins += 1
        bolean = True
        some_picture = pygame.image.load("AnimatedStreet.png")

    pygame.display.update()
    FramePerSec.tick(FPS)

