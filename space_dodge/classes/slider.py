import pygame


class Slider:
    def __init__(self, pos: list, size: tuple, initial_val: float, min: int, max: int, title):
        self.pos = pos
        self.size = size

        self.slider_left_pos = self.pos[0] - (size[0] // 2)
        self.slider_right_pos = self.pos[0] + (size[0] // 2)
        self.slider_top_pos = self.pos[1] - (size[1] // 2)

        self.min = min
        self.max = max

        # Calculate the initial position of the button based on the initial value percentage
        self.initial_val = initial_val
        self.button_x = int((self.slider_left_pos + self.initial_val * 100))

        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, size[0], size[1])
        self.button_rect = pygame.Rect(self.button_x - 5, self.slider_top_pos, 10, size[1])

        self.title = title
        self.pos[0] = self.title.get_width() + self.pos[0]

    def move_slider(self, mouse_pos):
        self.button_rect.x = mouse_pos[0] - 5

    def render(self, window):
        pygame.draw.rect(window, (255, 255, 255), self.container_rect)
        pygame.draw.rect(window, (0, 0, 0), self.button_rect)
        window.blit(self.title, (self.slider_left_pos - self.title.get_width() - 10, self.pos[1] - self.title.get_height() / 2))
        window.blit(pygame.font.SysFont("comicsans", 20).render(str(int(self.get_value())), 1, (255, 255, 255)), (self.slider_right_pos + 10, self.pos[1] - 10))

    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.x - self.slider_left_pos

        return (button_val / val_range) * (self.max - self.min) + self.min + 5
