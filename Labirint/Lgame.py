import pygame as pg
from random import choice
import time

pg.init()

WIDTH = 897
HEIGHT = 897

count = 28

K_WIDTH = WIDTH / count
K_HEIGHT = HEIGHT / count
FPS = 60

lvl1 = [[0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
        [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]]


class map_block:
    def __init__(self, surface, image):
        self.image = pg.image.load(image).convert_alpha()
        self.surface = surface

    def paint(self, x, y):
        self.surface.blit(self.image, (x * K_WIDTH, y * K_HEIGHT))


class Road:
    def __init__(self, lvl):
        self.lvl = lvl
        self.surface = sc
        self.road = pg.image.load('road.png').convert_alpha()
        self.road_t = pg.transform.rotate(self.road, 90)
        self.road3 = pg.image.load('road3.png').convert_alpha()
        self.road_center = pg.image.load('road_center.png').convert_alpha()
        self.road_turn = pg.image.load('road_turn.png').convert_alpha()

    def paint(self, x, y):
        up, down, left, right = False, False, False, False
        if self.lvl[x][y - 1] == 0 and y != 0:
            up = True
        if self.lvl[x][y + 1] == 0 and y != (count - 1):
            down = True
        if self.lvl[x + 1][y] == 0 and x != (count - 1):
            right = True
        if self.lvl[x - 1][y] == 0 and x != 0:
            left = True
        if left and right and up and down:
            self.surface.blit(self.road_center, (x * K_WIDTH, y * K_HEIGHT))
        elif left and right and up:
            self.surface.blit(self.road3, (x * K_WIDTH, y * K_HEIGHT))
        elif left and right and down:
            self.surface.blit(pg.transform.rotate(self.road3, 180), (x * K_WIDTH, y * K_HEIGHT))
        elif down and up and left:
            self.surface.blit(pg.transform.rotate(self.road3, 90), (x * K_WIDTH, y * K_HEIGHT))
        elif down and up and right:
            self.surface.blit(pg.transform.rotate(self.road3, -90), (x * K_WIDTH, y * K_HEIGHT))
        elif right and down:
            self.surface.blit(self.road_turn, (x * K_WIDTH, y * K_HEIGHT))
        elif left and down:
            self.surface.blit(pg.transform.rotate(self.road_turn, -90), (x * K_WIDTH, y * K_HEIGHT))
        elif up and left:
            self.surface.blit(pg.transform.rotate(self.road_turn, 180), (x * K_WIDTH, y * K_HEIGHT))
        elif up and right:
            self.surface.blit(pg.transform.rotate(self.road_turn, 90), (x * K_WIDTH, y * K_HEIGHT))
        elif up and down:
            self.surface.blit(self.road, (x * K_WIDTH, y * K_HEIGHT))
        elif right and left:
            self.surface.blit(pg.transform.rotate(self.road, 90), (x * K_WIDTH, y * K_HEIGHT))
        elif up or down:
            self.surface.blit(self.road, (x * K_WIDTH, y * K_HEIGHT))
        else:
            self.surface.blit(pg.transform.rotate(self.road, 90), (x * K_WIDTH, y * K_HEIGHT))


class Hero:
    def __init__(self, image, lvl):
        self.surface = sc
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.lvl = lvl
        self.x = 0
        self.y = 0
        self.r = Road(lvl1)
        self.right = True
        self.walk = 0

    def paint(self, x, y):
        self.x = x
        self.y = y
        self.surface.blit(self.image, (x * K_WIDTH, y * K_HEIGHT))

    def move(self, i):
        if i.key == pg.K_w:
            if self.lvl[self.x][self.y - 1] != 1 and self.y != 0:
                self.r.paint(self.x, self.y)
                self.paint(self.x, self.y - 1)
                rect = pg.Rect(self.x * K_HEIGHT, (self.y - 1) * K_WIDTH, 32, 64)
                pg.display.update(rect)
                self.walk += 1
        if i.key == pg.K_s:
            if self.lvl[self.x][self.y + 1] != 1 and self.y != count - 1:
                self.r.paint(self.x, self.y)
                rect = pg.Rect(self.x * K_HEIGHT, self.y * K_WIDTH, 32, 64)
                self.paint(self.x, self.y + 1)
                pg.display.update(rect)
                self.walk += 1
        if i.key == pg.K_d:
            if self.lvl[self.x + 1][self.y] != 1 and self.x != count - 1:
                if not self.right:
                    self.image = pg.transform.flip(self.image, 1, 0)
                    self.right = True
                self.r.paint(self.x, self.y)
                rect = pg.Rect(self.x * K_HEIGHT, self.y * K_WIDTH, 64, 32)
                self.paint(self.x + 1, self.y)
                pg.display.update(rect)
                self.walk += 1
        if i.key == pg.K_a:
            if self.lvl[self.x - 1][self.y] != 1 and self.x != 0:
                if self.right:
                    self.image = pg.transform.flip(self.image, 1, 0)
                    self.right = False
                self.r.paint(self.x, self.y)
                rect = pg.Rect((self.x - 1) * K_HEIGHT, self.y * K_WIDTH, 64, 32)
                self.paint(self.x - 1, self.y)
                pg.display.update(rect)
                self.walk += 1


clock = pg.time.Clock()
sc = pg.display.set_mode((WIDTH, HEIGHT))

wood1 = map_block(sc, 'wood1.png')
wood2 = map_block(sc, 'wood2.png')
rock = map_block(sc, 'rock.png')
rock2 = map_block(sc, 'rock2.png')

sword = map_block(sc, 'sword.png')

road = Road(lvl1)

woods = [wood1, wood2, rock, rock2]

hero = Hero('hero2.png', lvl1)


def bg():
    for i in range(count):
        for j in range(count):
            if lvl1[i][j] == 1:
                choice(woods).paint(i, j)
            if lvl1[i][j] == 0:
                road.paint(i, j)


def main():
    player1 = [(0, 0), (0, 10), (7, 7), (8, 6), (8, 15), (10, 19)]
    exit1 = [(27, 0), (25, 3), (20, 4), (21, 3), (24, 15)]

    player1 = choice(player1)
    exit1 = choice(exit1)

    time1 = time.time()

    bg()
    hero.paint(player1[0], player1[1])
    sword.paint(exit1[0], exit1[1])

    f1 = pg.font.Font(None, 72)

    pg.display.update()

    flag = True

    while flag:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit()
            if i.type == pg.KEYDOWN:
                hero.move(i)
                if i.key == pg.K_y:
                    flag = False
                if i.key == pg.K_n:
                    exit()
        if hero.x == exit1[0] and hero.y == exit1[1]:
            text1 = f1.render("Вы выиграли!", 1, (255, 0, 0))
            text2 = f1.render(f"Кол-во шагов {hero.walk}", 1, (255, 0, 0))
            text3 = f1.render(f"время {round(time.time() - time1, 2)} секунд", 1, (255, 0, 0))
            text4 = f1.render("Хотите начать новую игру? (Y/N)", 1, (255, 0, 0))
            place1 = text1.get_rect(center=(WIDTH // 2, 200))
            place2 = text2.get_rect(center=(WIDTH // 2, 300))
            place3 = text3.get_rect(center=(WIDTH // 2, 400))
            place4 = text4.get_rect(center=(WIDTH // 2, 500))
            sc.fill((0, 230, 10))
            sc.blit(text1, place1)
            sc.blit(text2, place2)
            sc.blit(text3, place3)
            sc.blit(text4, place4)
    clock.tick(FPS)
    hero.walk = 0
    main()

main()
