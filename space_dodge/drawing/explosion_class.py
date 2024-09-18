class Explosion:
    def __init__(self, x, y, frames, duration):
        self.x = x
        self.y = y
        self.frames = frames
        self.duration = duration
        self.current_frame = 0
        self.time_per_frame = duration / len(frames)
        self.time_accumulator = 0

    def update(self, dt):
        self.time_accumulator += dt
        if self.time_accumulator >= self.time_per_frame:
            self.time_accumulator -= self.time_per_frame
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                self.current_frame = len(self.frames)  # Mark as finished

    def draw(self, surface):
        if self.current_frame < len(self.frames):
            surface.blit(self.frames[self.current_frame], (self.x, self.y))

    def is_finished(self):
        return self.current_frame >= len(self.frames) - 1