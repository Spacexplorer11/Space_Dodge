import pygame as p


class Animation:
    def __init__(self, x, y, frames, total_duration):
        self.x = x
        self.y = y
        self.frames = frames
        self.total_duration = total_duration
        self.frame_duration = total_duration * 1000 / len(frames)
        self.current_frame = 0
        self.time_accumulator = 0
        self.last_update_time = p.time.get_ticks()

    def update(self):
        current_time = p.time.get_ticks()
        delta_time = current_time - self.last_update_time
        self.last_update_time = current_time

        self.time_accumulator += delta_time
        if self.time_accumulator >= self.frame_duration:
            self.time_accumulator -= self.frame_duration
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    @property
    def is_finished(self):
        return self.current_frame == len(self.frames) - 1

    def get_current_frame(self):
        return self.frames[self.current_frame]

    def draw(self, surface):
        surface.blit(self.get_current_frame(), (self.x, self.y))
