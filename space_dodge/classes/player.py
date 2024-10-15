from space_dodge.file_handling.constants_and_file_loading import HEIGHT, PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_VELOCITY, \
    playerL, playerR


class Player:
    def __init__(self):
        self.x = 0
        self.y = HEIGHT - PLAYER_HEIGHT
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.velocity = PLAYER_VELOCITY
        self.left_image = playerL
        self.right_image = playerR
        self.image = playerL

    def direction(self, direction):
        if direction == 0:
            self.image = self.left_image
        else:
            self.image = self.right_image
        return self.image
