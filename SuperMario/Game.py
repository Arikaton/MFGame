import pygame
from pygame import *
from SuperMario import player, block, Monsters

WIN_WIDTH = 800
WIN_HEIGHT = 640
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#000000"
hero = player.Player(55, 55)


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)
    l = max(-(camera.width-WIN_WIDTH), l)
    t = max(-(camera.height-WIN_HEIGHT), t)
    t = min(0, t)
    return Rect(l, t, w, h)


def main():
    pygame.init()
    timer = pygame.time.Clock()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Super Mario Boy")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))

    monsters = pygame.sprite.Group()
    animated_entities = pygame.sprite.Group()
    entities = pygame.sprite.Group()
    platforms = []
    entities.add(hero)
    running = False

    left = right = False
    up = False

    level = [
        "----------------------------------",
        "-                                -",
        "-                       --       -",
        "-        *                       -",
        "-                                -",
        "-            --                  -",
        "--                               -",
        "-                                -",
        "-                   ----     --- -",
        "-                                -",
        "--                               -",
        "-            *                   -",
        "-                            --- -",
        "-                                -",
        "-                                -",
        "-  *   ---                  *    -",
        "-                                -",
        "-   -------         ----         -",
        "-                                -",
        "-                         -      -",
        "-                            --  -",
        "-           ***                  -",
        "-                                -",
        "----------------------------------"]

    total_level_width = len(level[0])*PLATFORM_WIDTH
    total_level_height = len(level)*PLATFORM_HEIGHT

    camera = Camera(camera_configure, total_level_width, total_level_height)

    tp = block.BlockTeleport(128, 512, 800, 64)
    entities.add(tp)
    platforms.append(tp)
    animated_entities.add(tp)

    mn = Monsters.Monster(200, 200, 4, 4, 40, 40)
    entities.add(mn)
    platforms.append(mn)
    monsters.add(mn)

    x, y = 0, 0
    for row in level:
        for col in row:
            if col == '-':
                pf = block.Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == '*':
                bd = block.BlockDie(x, y)
                entities.add(bd)
                platforms.append(bd)
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

    while 1:
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN and event.key == K_LEFT:
                left = True
            if event.type == KEYDOWN and event.key == K_RIGHT:
                right = True
            if event.type == KEYUP and event.key == K_LEFT:
                left = False
            if event.type == KEYUP and event.key == K_RIGHT:
                right = False
            if event.type == KEYDOWN and event.key == K_UP:
                up = True
            if event.type == KEYUP and event.key == K_UP:
                up = False
            if event.type == KEYDOWN and event.key == K_LSHIFT:
                running = True
            if event.type == KEYUP and event.key == K_LSHIFT:
                running = False

        hero.update(left, right, up, running, platforms)
        camera.update(hero)
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        animated_entities.update()
        monsters.update(platforms)
        pygame.display.update()
        timer.tick(60)


if __name__ == '__main__':
    main()
