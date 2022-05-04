import pygame
from random import*
import random as rd

pygame.init()

# скорость движения объекта
run = True

FPS = 60
clock = pygame.time.Clock()

# размер окна
heightY = 800
widthX = 600

# количество точек
kolvo = 100

# инициализация размера окна
screen = pygame.display.set_mode((heightY, widthX))

class GameManager:
    def __init__(self, game_window, array):
        self.game_window = game_window
        self.array = array

    def redraw(self):
        self.game_window.fill((0, 0, 0))
        for star in self.array:
            star.set_new_position()

# класс параметров точки
class tPoint():
    def __init__(self, screen, color, X, Y, size):
        # присвоение рандомного размера, цвета и позиции
        self.color = color
        self.X = X
        self.Y = Y

        self.dx = randrange(-1, 2)
        self.dy = randrange(-1, 2)

        while (self.dx or self.dy) == 0:
            self.dx = randrange(-1, 2)
            self.dy = randrange(-1, 2)


        self.size = size
        self.screen = screen
        self.draw()

    # метод отображения точек
    def draw(self):
        pygame.draw.circle(self.screen, self.color, [self.X, self.Y], self.size)

    def set_new_position(self):

        # проверка на ударение в Y стену
        if self.Y > (600 - self.size) or self.Y < self.size:
            # смена траектории
            self.dy *= -1
            self.dx = randrange(-5, 5)
        # проверка на ударение в X стену
        if self.X > (800 - self.size) or self.X < self.size:
            # смена траектории
            self.dx *= -1
            self.dy = randrange(-5, 5)
        # движение
        self.X += self.dx
        self.Y += self.dy

        self.draw()

#метод для рандомного цвета точки
def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    return (r, g, b)

myArray = []

#запись в массив
for i in range(kolvo):
    # рандомные координаты для каждого элемента массива
    X = randint(30, widthX - 30)
    Y = randint(30, heightY - 30)
    color = random_color()
    myArray.append(tPoint(screen, color, Y, X, randint(5, 15)))
    print('Обьекты в массиве:', myArray, "\n")

manager = GameManager(screen, myArray)

#при запуске программы
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
    manager.redraw()
pygame.quit()



