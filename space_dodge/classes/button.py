import pygame as p

from space_dodge.file_handling.constants_and_file_loading import WINDOW


class Button:
    def __init__(self, image, x, y):
        self._image = image
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.width = image.get_width()
        self.height = image.get_height()
        self.image_hover = p.transform.scale(self._image, (self.width + 3, self.height + 3))
        self.rect = p.Rect(x, y, self.width, self.height)

    @property
    def image(self):
        mouse_pos = p.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return self.image_hover
        else:
            return self._image


    def update_rect(self, x):
        self.rect = p.Rect(x, self.y, self.width, self.height)
        self.x = x
        return self.rect

    def clicked(self):
        mouse_pos = p.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and p.mouse.get_pressed()[0]:
            return True
        else:
            return False

    def draw(self):
        WINDOW.blit(self.image, self.pos)
