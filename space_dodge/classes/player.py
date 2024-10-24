from file_handling.constants_and_file_loading import HEIGHT, PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_VELOCITY, \
    playerL, playerR, WIDTH


class Player:
    def __init__(self):
        self._x = 0
        self.y = HEIGHT - PLAYER_HEIGHT
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.velocity = PLAYER_VELOCITY
        self.left_image = playerL
        self.right_image = playerR
        self._image = playerL
        self.direction = 0  # The direction the player is facing( written in binary ) 0 = left, 1 = right

    @property
    def image(self):
        if self.direction == 0:
            self._image = self.left_image
        else:
            self._image = self.right_image
        return self._image

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value - self.velocity >= 0 and value + self.velocity + self.width <= WIDTH:
            self._x = value

    @property
    def pos(self):
        return self._x, self.y
