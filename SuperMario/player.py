from pygame import *
import pyganim
from SuperMario import block, Monsters

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
JUMP_POWER = 13
GRAVITY = 0.5
MOVE_EXTRA_SPEED = 2.5
JUMP_EXTRA_POWER = 1
ANIMATION_SUPER_SPEED_DELAY = 50
COLOR = "#888888"

ANIMATION_DELAY = 100
ANIMATION_RIGHT = [('mario/r1.png'), ('mario/r2.png'), ('mario/r3.png'), ('mario/r4.png'), ('mario/r5.png')]
ANIMATION_LEFT = [('mario/l1.png'), ('mario/l2.png'), ('mario/l3.png'), ('mario/l4.png'), ('mario/l5.png')]
ANIMATION_JUMP_LEFT = [('mario/jl.png', 100)]
ANIMATION_JUMP_RIGHT = [('mario/jr.png', 100)]
ANIMATION_JUMP_STAY = [('mario/j.png', 100)]
ANIMATION_STAY = [('mario/0.png', 100)]


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.on_ground = False
        self.start_x = x
        self.start_y = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.image.set_colorkey(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)

        #  Анимация движения вправо
        boltanim = []
        boltAnimSuperSpeed = []
        for anim in ANIMATION_RIGHT:
            boltanim.append((anim, ANIMATION_DELAY))
            boltAnimSuperSpeed.append((anim, ANIMATION_SUPER_SPEED_DELAY))
        self.bolt_anim_right = pyganim.PygAnimation(boltanim)
        self.bolt_anim_right_ss = pyganim.PygAnimation(boltAnimSuperSpeed)
        self.bolt_anim_right_ss.play()
        self.bolt_anim_right.play()

        #  Анимация движения влево
        boltanim = []
        boltAnimSuperSpeed = []
        for anim in ANIMATION_LEFT:
            boltanim.append((anim, ANIMATION_DELAY))
            boltAnimSuperSpeed.append((anim, ANIMATION_SUPER_SPEED_DELAY))
        self.bolt_anim_left_ss = pyganim.PygAnimation((boltAnimSuperSpeed))
        self.bolt_anim_left = pyganim.PygAnimation(boltanim)
        self.bolt_anim_left_ss.play()
        self.bolt_anim_left.play()

        self.bolt_anim_stay = pyganim.PygAnimation(ANIMATION_STAY)
        self.bolt_anim_stay.play()
        self.bolt_anim_stay.blit(self.image, (0, 0))

        self.bolt_anim_jump_left = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.bolt_anim_jump_left.play()

        self.bolt_anim_jump_right = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.bolt_anim_jump_right.play()

        self.bolt_anim_jump = pyganim.PygAnimation(ANIMATION_JUMP_STAY)
        self.bolt_anim_jump.play()

    def update(self, left, right, up, running, platforms):
        if up:
            if self.on_ground:
                self.yvel = -JUMP_POWER
                if running and (left or right):
                    self.yvel -= JUMP_EXTRA_POWER
            self.image.fill(Color(COLOR))
            self.bolt_anim_jump.blit(self.image, (0, 0))

        if left:
            self.xvel = -MOVE_SPEED
            self.image.fill(Color(COLOR))
            if running:
                self.xvel -= MOVE_EXTRA_SPEED
                if not up:
                    self.bolt_anim_left_ss.blit(self.image, (0, 0))
            else:
                if not up:
                    self.bolt_anim_left.blit(self.image, (0, 0))
            if up:
                self.bolt_anim_jump_left.blit(self.image, (0, 0))


        if right:
            self.xvel = MOVE_SPEED
            self.image.fill(Color(COLOR))
            if running:
                self.xvel += MOVE_EXTRA_SPEED
                if not up:
                    self.bolt_anim_right_ss.blit(self.image, (0, 0))
            else:
                if not up:
                    self.bolt_anim_right.blit(self.image, (0, 0))
            if up:
                self.bolt_anim_jump_right.blit(self.image, (0, 0))

        if not(left or right):
            self.xvel = 0
            self.image.fill(Color(COLOR))
            self.bolt_anim_stay.blit(self.image, (0, 0))

        if not self.on_ground:
            self.yvel += GRAVITY

        self.on_ground = False
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.on_ground = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0
                if isinstance(p, block.BlockDie) or isinstance(p, Monsters.Monster):
                    self.die()
                elif isinstance(p, block.BlockTeleport):
                    self.teleporting(p.goX, p.goY)

    def die(self):
        time.wait(500)
        self.teleporting(self.start_x, self.start_y)

    def teleporting(self, x, y):
        self.rect.x = x
        self.rect.y = y
