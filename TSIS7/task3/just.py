# import pygame
#
# pygame.init()
#
# print("The value of pygame.USEREVENT is:", pygame.USEREVENT)
# # The value of pygame.USEREVENT is: 32866
# import pygame
#
# # Define a custom timer event type
# MYTIMER = pygame.USEREVENT + 1
#
# # Set up the Pygame window and clock
# pygame.init()
# screen = pygame.display.set_mode((640, 480))
# clock = pygame.time.Clock()
#
# # Create a timer event that will be triggered every 1000 milliseconds
# pygame.time.set_timer(MYTIMER, 1000)
#
# # Main loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == MYTIMER:
#             # Do something when the timer event is triggered
#             print("Timer event triggered!")
#
#     # Update the screen and wait for the next frame
#     pygame.display.update()
#     clock.tick(60)

# import pygame
#
# # Define a custom input event type
# MYINPUT = pygame.USEREVENT + 2
#
# # Set up the Pygame window and clock
# pygame.init()
# screen = pygame.display.set_mode((640, 480))
# clock = pygame.time.Clock()
#
# # Main loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 # Create a custom input event when the space bar is pressed
#                 pygame.event.post(pygame.event.Event(MYINPUT))
#         elif event.type == MYINPUT:
#             # Do something when the custom input event is triggered
#             print("Custom input event triggered!")
#
#     # Update the screen and wait for the next frame
#     pygame.display.update()
#     clock.tick(60)
#
# import pygame
#
# songs = [
#     "player1.mp3",
#     "player2.mp3",
#     "player3ST.mp3"
# ]
#
# SONG_END = pygame.USEREVENT + 1
#
#
# def playing_music(i):
#     pygame.mixer.music.set_endevent(SONG_END)
#     pygame.mixer.music.load(songs[i])
#     pygame.mixer.music.play(0)  # will play only once and stop, 0 more times
#     # The -1 signals PyGame to just play forever, but, if you put, say, a 5 in there, then the music would play once and 5 more times.
#
#
# pygame.init()
#
# screen = pygame.display.set_mode((400, 300))
# pygame.display.set_caption("Nazym from KBTU!!!")
# screen.fill((0, 255, 255))
#
# running = True
# i = 0
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 pygame.mixer.music.stop()
#                 i += 1
#                 if i > len(songs) - 1:
#                     i = 0
#                 playing_music(i)
#             elif event.key == pygame.K_LEFT:
#                 pygame.mixer.music.stop()
#                 i -= 1
#                 if i < 0:
#                     i = len(songs) - 1
#                 playing_music(i)
#         if event.type == SONG_END:
#             i += 1
#             if i > len(songs) - 1:
#                 i = 0
#             playing_music(i)
#     pressed = pygame.key.get_pressed()
#     if pressed[pygame.K_SPACE]:
#         playing_music(i)
#     if pressed[pygame.K_UP]:
#         pygame.mixer.music.pause()
#     if pressed[pygame.K_DOWN]:
#         pygame.mixer.music.unpause()
#
#     pygame.display.flip()

import pygame
pygame.init()

screen_1 = pygame.display.set_mode((700, 700))
x = 25
y = 25
FPS = 60
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    bolean = True
    screen_1.fill(pygame.Color("white"))
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and y >= 45:
        y -= 20
    elif key[pygame.K_DOWN] and y <= 675:
        y += 20
    elif key[pygame.K_LEFT] and x >= 45:
        x -= 20
    elif key[pygame.K_RIGHT] and x <= 675:
        x += 20

    if bolean:
        red_ball = pygame.draw.circle(screen_1, pygame.Color('red'), (x, y), 25)
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(FPS)
