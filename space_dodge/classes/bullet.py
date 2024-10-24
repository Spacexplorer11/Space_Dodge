import random

import pygame as p

from file_handling.constants_and_file_loading import BULLET_WIDTH, WIDTH, BULLET_HEIGHT, BULLET_VELOCITY, \
    bullet_texture


class Bullet:
    def __init__(self):
        self.x = random.randint(0 + BULLET_WIDTH, WIDTH - BULLET_WIDTH)
        self.y = 0
        self.width = BULLET_WIDTH
        self.height = BULLET_HEIGHT
        self.velocity = BULLET_VELOCITY
        self.image = bullet_texture
        self.mask = p.mask.from_surface(bullet_texture)
        self.rect = p.Rect(self.x, -self.height, self.width, self.height)
