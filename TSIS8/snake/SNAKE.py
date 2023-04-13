import random
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40

clock = pygame.time.Clock()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
       ]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            SCREEN, RED,
            pygame.Rect(head.x * BLOCK_SIZE,
                        head.y * BLOCK_SIZE,
                        BLOCK_SIZE, BLOCK_SIZE)
        )
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN, BLUE,
                pygame.Rect(body.x * BLOCK_SIZE,
                            body.y * BLOCK_SIZE,
                            BLOCK_SIZE, BLOCK_SIZE)
            )

    def move(self, dx, dy):
        for idx in range(len(self.body) - 1, 0, -1):
            # updates the x and y coordinates of each segment to be
            # the same as the x and y coordinates of the previous segment.
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y
        self.body[0].x += dx
        self.body[0].y += dy

        if self.body[0].x > WIDTH // BLOCK_SIZE:
            self.body[0].x = 0
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // BLOCK_SIZE
        elif self.body[0].y < 0:
            self.body[0].y = WIDTH // BLOCK_SIZE
        elif self.body[0].y > HEIGHT // BLOCK_SIZE:
            self.body[0].y = 0

    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True

    def check_wall(self): # check_body
        # checks if the snake's head (the first segment) has collided with any other part of the snake's body
        for i in self.body[1:]: # because the head of the snake is at index 0.
            if i.x == self.body[0].x and i.y == self.body[0].y:
                return True


def draw_grid(): # рисую сетку
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, BLACK, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, BLACK, start_pos=(0, y), end_pos=(WIDTH, y), width=1)


class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self):
        pygame.draw.rect(SCREEN, GREEN,
                         pygame.Rect(
                             self.location.x * BLOCK_SIZE,
                             self.location.y * BLOCK_SIZE,
                             BLOCK_SIZE, BLOCK_SIZE,
                         ))

def main():
    running = True
    snake = Snake()
    food = Food(5, 5)
    fps = 5
    level = 1
    score_font = pygame.font.SysFont("Verdana", 40)
    dx, dy = 0, 0
    score = 0
    isDown = False
    isRight = False
    isUp = False
    isDown = False

    while running:
        SCREEN.fill(WHITE)
        score_text = score_font.render(f" Your score: {score}", True, (0, 0, 0))
        level_text = score_font.render(f" Level: {level}", True, (0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not isDown:
                    isUp = True
                    isDown = False
                    isRight = False
                    isLeft = False
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN and not isUp:
                    dx, dy = 0, 1
                    isUp = False
                    isDown = True
                    isRight = False
                    isLeft = False
                elif event.key == pygame.K_RIGHT and not isLeft:
                    dx, dy = 1, 0
                    isUp = False
                    isDown = False
                    isRight = True
                    isLeft = False
                elif event.key == pygame.K_LEFT and not isRight:
                    dx, dy = -1, 0
                    isUp = False
                    isDown = False
                    isRight = False
                    isLeft = True

        snake.move(dx, dy)
        if snake.check_wall(): # head onto body
            running = False
        if snake.check_collision(food):
            snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))
            food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
            score += 1
            if score % 5 == 0:
                fps += 20
                level += 1

        snake.draw()
        food.draw()
        draw_grid()
        SCREEN.blit(score_text, (0, 0))
        SCREEN.blit(level_text, (0, 50))
        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    # script, the __name__ variable holds the string '__main__'
    # when the script is being executed as the main program,
    # it's not being imported as a module into another program).
    main()