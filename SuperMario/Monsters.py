from pygame import *
import pyganim

MONSTER_WIDTH = 32
MONSTER_HEIGHT = 32
MONSTER_COLOR = '#2110FF'

ANIMATION_MONSTER_HORIZONTAL = [('monsters/fire1.png'), ('monsters/fire2.png')]

class Monster(sprite.Sprite):
    def __init__(self, x, y, left, up, max_len_left, max_len_up):
        sprite.Sprite.__init__(self)
        self.image = Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.image.fill(Color(MONSTER_COLOR))
        self.image.set_colorkey(Color(MONSTER_COLOR))
        self.rect = Rect(x+2, y+2, MONSTER_WIDTH-2, MONSTER_HEIGHT-2)
        self.start_x = x
        self.start_y = y
        self.max_len_left = max_len_left
        self.max_len_up = max_len_up
        self.xvel = left
        self.yvel = up
        boltAnim = []
        for anim in ANIMATION_MONSTER_HORIZONTAL:
            boltAnim.append((anim, 200))
        self.bolt_anim = pyganim.PygAnimation(boltAnim)
        self.bolt_anim.play()

    def update(self, platforms):
        self.image.fill(Color(MONSTER_COLOR))
        self.bolt_anim.blit(self.image, (0, 0))

        self.rect.x += self.xvel
        self.rect.y += self.yvel

        self.collide(platforms)

        if (abs(self.start_x - self.rect.x)) > self.max_len_left:
            self.xvel = -self.xvel

        if (abs(self.start_y - self.rect.x)) > self.max_len_up:
            self.yvel = -self.yvel

    def collide(self, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p) and self != p:
                self.xvel = -self.xvel
                self.yvel = -self.yvel
