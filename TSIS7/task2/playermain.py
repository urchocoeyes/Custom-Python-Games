import pygame

pygame.init()

songs = [
    "player1.mp3",
    "player2.mp3",
    "player3ST.mp3"
]

SONG_END = pygame.USEREVENT + 1

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Nazym from KBTU!!!")
screen.fill((0, 255, 255))

running = True
i = 0


def playing_music(i):
    # pygame.mixer.music.set_endevent(SONG_END)
    pygame.mixer.music.load(songs[i])
    pygame.mixer.music.play(0)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pygame.mixer.music.stop()
                i += 1
                if i > len(songs) - 1:
                    i = 0
                playing_music(i)
            elif event.key == pygame.K_LEFT:
                pygame.mixer.music.stop()
                i -= 1
                if i < 0:
                    i = 0
                playing_music(i)
        if event.type == SONG_END:
            i += 1
            if i > len(songs) - 1:
                i = 0
            playing_music(i)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            playing_music(i)
        if pressed[pygame.K_UP]:
            pygame.mixer.music.pause()
        if pressed[pygame.K_DOWN]:
            pygame.mixer.music.unpause()

    pygame.display.flip()
