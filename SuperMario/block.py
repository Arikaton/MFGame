from pygame import *
import pyganim

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

ANIMATION_BLOCK_TELEPORT = [('blocks/portal2.png'), ('blocks/portal1.png')]


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = image.load('platform.png')
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class BlockDie(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load('blocks/dieBlock.png')


class BlockTeleport(Platform):
    def __init__(self, x, y, goX, goY):
        Platform.__init__(self, x, y)
        self.goX = goX
        self.goY = goY
        boltanim = []
        for anim in ANIMATION_BLOCK_TELEPORT:
            boltanim.append((anim, 300))
        self.bolt_anim = pyganim.PygAnimation(boltanim)
        self.bolt_anim.play()

    def update(self):
        self.image.fill(Color(PLATFORM_COLOR))
        self.bolt_anim.blit(self.image, (0, 0))