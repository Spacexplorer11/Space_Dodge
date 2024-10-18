import pygame as p


class Button:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.width = image.get_width()
        self.height = image.get_height()
        self.rect = p.Rect(x, y, self.width, self.height)

    def update_rect(self, x):
        self.rect = p.Rect(x, self.y, self.width, self.height)
        return self.rect
