# Импорт библиотеки Pygame
import pygame
from random import*
import random as rd

# инициализация модулей библиотеки Pygame
pygame.init()
pygame.display.set_caption('Случайные точки с управлением')

# скорость движения объекта
run = True

# кадры в секунду
FPS = 60
clock = pygame.time.Clock()

# размер окна
heightY = 800
widthX = 600

# количество точек
kolvo = 100

# инициализация размера окна
screen = pygame.display.set_mode((heightY, widthX))

class Manager:
    def __init__(self, game_window, array):
        """Инициализируем окно, массив"""
        self.game_window = game_window
        self.array = array

    def redraw(self):
        """Смена позиции и перерисовка каждого элемента массива"""
        self.game_window.fill((0, 0, 0))
        for i in self.array:
            i.newPosition()

# класс параметров точки
class tPoint():
    """Модель точки"""
    def __init__(self, screen, color, X, Y, size):
        """Инициализируем окно, цвет, X, Y, размер"""
        # переменные случайного размера, цвета и позиции
        self.color = color
        self.X = X
        self.Y = Y

        # рандомная траектория точки
        self.dx = randrange(-1, 2)
        self.dy = randrange(-1, 2)

        self.size = size
        self.screen = screen
        self.draw()

    # метод отображения точек
    def draw(self):
        """Рисование точки"""
        pygame.draw.circle(self.screen, self.color, [self.X, self.Y], self.size)

    def newPosition(self):
        """Смена позиции точки"""
        # проверка равна ли траектория 0
        if event.type != pygame.KEYDOWN:
            if self.dx == 0 or self.dy == 0:
                self.dx = randrange(-1, 2)
                self.dy = randrange(-1, 2)

            # проверка на ударение в Y стену
            if self.Y > (widthX - self.size) or self.Y < self.size:
                # смена траектории
                self.dy *= -1
                self.dx = randrange(-5, 5)
            # проверка на ударение в X стену
            if self.X > (heightY - self.size) or self.X < self.size:
                # смена траектории
                self.dx *= -1
                self.dy = randrange(-5, 5)

        # событие по нажатию клавиш
        if event.type == pygame.KEYDOWN:
            # остановка движения
            self.dx = 0
            self.dy = 0
            if event.key == pygame.K_UP:
                self.Y -= 1
                print("Key UP has been pressed")
            if event.key == pygame.K_DOWN:
                self.Y += 1
                print("Key DOWN has been pressed")
            if event.key == pygame.K_RIGHT:
                self.X += 1
                print("Key RIGHT has been pressed")
            if event.key == pygame.K_LEFT:
                self.X -= 1
                print("Key LEFT has been pressed")

            # возвращение точек в другой конец экрана
            if self.Y >= (widthX - self.size):
                self.Y = self.size + 1
            if self.X >= heightY - self.size:
                self.X = self.size + 1
            if self.Y <= 0 + self.size:
                self.Y = widthX - self.size
            if self.X <= self.size:
                self.X = heightY - self.size

        # движение
        self.X += self.dx
        self.Y += self.dy
        # перерисовка
        self.draw()

# случайный цвет точки
def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    return (r, g, b)

dotsArray = []

# запись в массив
for i in range(kolvo):
    # случайные значения для точки
    X = randint(30, widthX - 30)
    Y = randint(30, heightY - 30)
    color = random_color()
    dotsArray.append(tPoint(screen, color, Y, X , randint(5, 15)))
    print('Обьектов в массиве:', i,  dotsArray, "\n")

manager = Manager(screen, dotsArray)

# отслеживание закрытия
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # обновляет дисплей
    pygame.display.flip()
    # вызов метода перерисовки массива
    manager.redraw()
pygame.quit()



