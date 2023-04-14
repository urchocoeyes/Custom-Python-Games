import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)


class GameObject:
    def draw(self):
        pass

    def handle(self):
        pass


class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.draw.rect(
            SCREEN,
            WHITE,
            (self.x, self.y, 40, 40)
        )

    def draw(self):
        self.rect = pygame.draw.rect(
            SCREEN,
            WHITE,
            (self.x, self.y, 40, 40)
        )


class Pen(GameObject):
    def __init__(self, ch_color, *args, **kwargs):
        self.points = []  # [(x1, y1), (x2, y2)]
        self.ch_color = ch_color

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):  # рисуем множество точек через линии(идем до n-1)
            pygame.draw.line(
                SCREEN,
                self.ch_color,
                start_pos=point,  # self.points[idx]
                end_pos=self.points[idx + 1],
                width=5,
            )

    def handle(self, mouse_pos):
        self.points.append(mouse_pos)


class Rectangle(GameObject):
    def __init__(self, ch_color, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.ch_color = ch_color

    def draw(self):
        # print(self.start_pos[0], self.end_pos[1])
        start_pos_x = min(self.start_pos[0], self.end_pos[0])  # стартовая позиция мыщи
        # make sure that the rectangle is drawn from the top-left corner of the
        # rectangle, regardless of whether the user is dragging the mouse from
        # left to right or from right to left.
        # print(start_pos_x)
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])  # конечная позиция мыши
        end_pos_y = max(self.start_pos[1], self.end_pos[1])  # в остальных объектах все += похожее

        pygame.draw.rect(
            SCREEN,
            self.ch_color,
            (
                start_pos_x,
                start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos


class rightTriangle(GameObject):
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.polygon(
            SCREEN,
            WHITE,
            (
                (start_pos_x, start_pos_y),
                (start_pos_x, end_pos_y),
                (end_pos_x, end_pos_y),
            ),
            width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos


class equilateralTriangle(GameObject):  # triangle triangle triangle
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        # print(self.start_pos, self.end_pos)
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])
        rad = end_pos_x - start_pos_x
        # atio of the length of the side of an
        # equilateral triangle to the radius of the circumscribing circle is sqrt(3).

        pygame.draw.polygon(
            SCREEN, WHITE,
            (
                (start_pos_x, start_pos_y),
                (start_pos_x - rad // (3 ** .5 * 2), start_pos_y + rad // 2),
                (start_pos_x + rad // (3 ** .5 * 2), start_pos_y + rad // 2),
            ),
            width=5
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos


class Circle(GameObject):  # triangle triangle triangle
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])
        pygame.draw.circle(
            SCREEN,
            WHITE,
            (start_pos_x, start_pos_y),
            end_pos_x - start_pos_x,
            width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos


class Romb(GameObject):
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.polygon(
            SCREEN,
            WHITE,
            (
                (start_pos_x + (end_pos_x - start_pos_x) // 2, start_pos_y),
                (start_pos_x, start_pos_y + (end_pos_y - start_pos_y) // 2),
                (start_pos_x + (end_pos_x - start_pos_x) // 2, end_pos_y),
                (end_pos_x, start_pos_y + (end_pos_y - start_pos_y) // 2),
            ),
            width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos


class Square(GameObject):
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.rect(
            SCREEN,
            WHITE,
            (
                start_pos_x,
                start_pos_y,
                max(end_pos_x - start_pos_x, end_pos_y - start_pos_y),
                max(end_pos_x - start_pos_x, end_pos_y - start_pos_y),
            ),
            width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos


def main():
    running = True
    active_obj = None  # переменная в которой мы будем хранит объект
    # этот объект прорисовывает текущую фигуру(когда мы зажимаем мышку и двигаем ее(пока мышь не опустили),
    # этот объект рисуется в проге)
    # создаю 8 кнопок
    button = Button(20, 20)
    buttonTr = Button(70, 20)
    buttonRightTr = Button(120, 20)
    buttonR = Button(170, 20)
    buttonS = Button(220, 20) # square
    buttonC = Button(270, 20)
    buttonP = Button(320, 20)
    buttonE = Button(370, 20)
    objects = [  # массив объектов(тут кнопки и фигуры, которые мы будем рисовать
        button,
        buttonTr,
        buttonRightTr,
        buttonR,
        buttonS,
        buttonC,
        buttonP,
        buttonE,
    ]
    clock = pygame.time.Clock()
    current_shape = 'pen'  # текущий инструмент - карандаш
    ch_color = WHITE

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:  # меняется цвет для карандаша и прямоугольника на зеленый
                    ch_color = GREEN
                if event.key == pygame.K_r:
                    ch_color = RED
                if event.key == pygame.K_b:
                    ch_color = BLUE
                if event.key == pygame.K_w:
                    ch_color = WHITE
                if event.key == pygame.K_e:  # при нажатии на клавишу E, удаляются объекты из массива objects(кнпоки тоже)
                    if objects:
                        objects.pop()  # удаление последнего элемента (типа ctrl + Z)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(
                        pygame.mouse.get_pos()):  # если я нажимаю на эту кнопку текущий инструмент - прямоугольник
                    current_shape = 'rectangle'
                    ch_color = WHITE
                if buttonTr.rect.collidepoint(pygame.mouse.get_pos()):  # то же самое в других
                    current_shape = 'Trngl'
                if buttonRightTr.rect.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'eqRect'
                if buttonR.rect.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'Romb'
                if buttonS.rect.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'Square'
                if buttonC.rect.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'Circle'
                if buttonP.rect.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'pen'
                    ch_color = WHITE
                if buttonE.rect.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'eraser'
                    ch_color = (0, 0, 0)
                else:
                    if current_shape == 'pen':
                        # значение start_pos равна позиции когда мы только нажали на мышь(MOUSEBUTTONDOWN)
                        active_obj = Pen(ch_color, start_pos=event.pos)
                    elif current_shape == 'eraser':
                        active_obj = Pen(ch_color, start_pos=event.pos)
                    elif current_shape == 'rectangle':
                        active_obj = Rectangle(ch_color, start_pos=event.pos)
                    elif current_shape == 'eqRect':
                        active_obj = equilateralTriangle(start_pos=event.pos)
                    elif current_shape == 'Trngl':
                        active_obj = rightTriangle(start_pos=event.pos)
                    elif current_shape == 'Romb':
                        active_obj = Romb(start_pos=event.pos)
                    elif current_shape == 'Square':
                        active_obj = Square(start_pos=event.pos)
                    elif current_shape == 'Circle':
                        active_obj = Circle(start_pos=event.pos)

            if event.type == pygame.MOUSEMOTION and active_obj is not None:
                active_obj.handle(mouse_pos=pygame.mouse.get_pos())  # тут мы присваиваем end_pos(через mouse_pos)
                # MOUSEMOTION то есть движение мыши, end_pos activeObj равен позиции где мышь мы пока держим
                active_obj.draw()

            if event.type == pygame.MOUSEBUTTONUP and active_obj is not None:
                objects.append(active_obj)  # когда мы опустим мышь мы добавляем готовый объект в objects
                active_obj = None

        for obj in objects:  # рисуем все объекты
            obj.draw()

        clock.tick(30)
        pygame.display.flip()


if __name__ == '__main__':
    main()
