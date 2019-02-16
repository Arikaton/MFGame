import pygame


class GameOb:
    def __init__(self, surface, image):
        self.surface = surface
        self.image = pygame.image.load(image).convert()

    def info(self, event):
        X = event.pos[0]
        Y = event.pos[1]
        i, j = 3, 3
        if event.button == 1:
            if X < 220 and Y < 180:
                i, j = 0, 0
            elif 250 < X < 420 and Y < 180:
                i, j = 0, 1
            elif X > 450 and Y < 180:
                i, j = 0, 2
            elif X < 220 and 210 < Y < 380:
                i, j = 1, 0
            elif 250 < X < 420 and 210 < Y < 380:
                i, j = 1, 1
            elif X > 450 and 210 < Y < 380:
                i, j = 1, 2
            elif X < 220 and Y > 400:
                i, j = 2, 0
            elif 250 < X < 420 and Y > 400:
                i, j = 2, 1
            elif X > 450 and Y > 400:
                i, j = 2, 2
            return i, j

    def draw(self, i, j):
        if i == 0 and j == 0:
            self.surface.blit(self.image, (30, 25))
        elif i == 0 and j == 1:
            self.surface.blit(self.image, (260, 25))
        elif i == 0 and j == 2:
            self.surface.blit(self.image, (465, 25))
        elif i == 1 and j == 0:
            self.surface.blit(self.image, (30, 225))
        elif i == 1 and j == 1:
            self.surface.blit(self.image, (260, 225))
        elif i == 1 and j == 2:
            self.surface.blit(self.image, (465, 225))
        elif i == 2 and j == 0:
            self.surface.blit(self.image, (30, 410))
        elif i == 2 and j == 1:
            self.surface.blit(self.image, (260, 410))
        elif i == 2 and j == 2:
            self.surface.blit(self.image, (465, 410))
        pygame.display.update()


pygame.init()
sc = pygame.display.set_mode((664, 597))
bg = pygame.image.load('Background.png').convert()


def win(matrix, check):
    for i in range(3):
        if matrix[i][0] == check and matrix[i][1] == check and matrix[i][2] == check:
            return True
        elif matrix[0][i] == check and matrix[1][i] == check and matrix[2][i] == check:
            return True
    if matrix[0][0] == check and matrix[1][1] == check and matrix[2][2] == check:
        return True
    elif matrix[0][2] == check and matrix[1][1] == check and matrix[2][0] == check:
        return True
    else:
        return False


def zero():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


x = GameOb(sc, 'x.png')
o = GameOb(sc, 'o.png')


def main():
    FirstX = True
    GameMat = zero()
    sc.blit(bg, (0, 0))
    pygame.display.update()
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if FirstX:
                    X, Y = x.info(i)
                    if X < 3 and Y < 3:
                        if GameMat[X][Y] == 0:
                            x.draw(X, Y)
                            GameMat[X][Y] = 1
                            FirstX = False
                            if win(GameMat, 1):
                                pygame.display.update()
                                main()
                else:
                    X, Y = o.info(i)
                    if X < 3 and Y < 3:
                        if GameMat[X][Y] == 0:
                            o.draw(X, Y)
                            GameMat[X][Y] = 2
                            FirstX = True
                            if win(GameMat, 2):
                                pygame.display.update()
                                main()
    pygame.time.delay(30)

main()