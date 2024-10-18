import pygame


class Slider:
    def __init__(self, x, y, width, height, min_value, max_value, value, line_image, circle_image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.value = value
        self.line_image = line_image
        self.circle_image = circle_image
        self.line_rect = line_image.get_rect(topleft=(x, y))
        self.circle_rect = circle_image.get_rect(
            center=(x + (value - min_value) / (max_value - min_value) * width, y + height // 2))

    def update_slider(self):
        pos = pygame.mouse.get_pos()
        if self.line_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.value = (pos[0] - self.x) / self.width * (self.max_value - self.min_value) + self.min_value
            self.value = max(self.min_value, min(self.max_value, self.value))
            self.circle_rect.centerx = self.x + (self.value - self.min_value) / (
                        self.max_value - self.min_value) * self.width
        return self.value

    def draw(self, surface):
        surface.blit(self.line_image, self.line_rect.topleft)
        surface.blit(self.circle_image, self.circle_rect.topleft)
