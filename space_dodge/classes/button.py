import pygame as p

from space_dodge.file_handling.constants_and_file_loading import WINDOW
from space_dodge.classes.animation import Animation  # Assuming you have an Animation class


class Button:
    def __init__(self, image, x, y, duration=2):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.is_animated = isinstance(image, dict)

        if self.is_animated:
            self._image = list(image.values())[0]  # Use the first image as the default
            self.animation = Animation(x, y, list(image.values()), duration)
        else:
            self._image = image
            self.image_hover = p.transform.scale(self._image,
                                                 (self._image.get_width() + 3, self._image.get_height() + 3))

        self.width = self._image.get_width()
        self.height = self._image.get_height()
        self.rect = p.Rect(x, y, self.width, self.height)

    @property
    def image(self):
        mouse_pos = p.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if self.is_animated:
                return self.animation.get_current_frame()
            else:
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
        mouse_pos = p.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and self.is_animated:
            self.animation.update()
        WINDOW.blit(self.image, self.pos)
