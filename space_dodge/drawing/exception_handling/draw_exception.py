import pygame

# Window variables
WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.font.init()
FONT_ERROR = pygame.font.SysFont("Phosphate", 30)
FONT_ERROR_SMALL = pygame.font.SysFont("Phosphate", 20)


def draw_except(error):
    run = True
    clock = pygame.time.Clock()
    error_messages = {
        "background": "A background image was not found",
        "Player": "Player image was not found",
        "Button": "A symbol  was not found",
        "Lives": "The image for the lives were not found",
        "Sound Effects": "One or more of the sound effects weren't found",
        "Music": "Some background music files weren't found",
        "Bullet": "The bullet images weren't found",
        "Animation": "The frames for an animation weren't found"
    }

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WINDOW.fill((0, 0, 0))
        if error in error_messages:
            errorText1 = FONT_ERROR.render("Error:", 1, "red")
            errorText2 = FONT_ERROR.render(error_messages[error], 1, "red")
            errorText3 = FONT_ERROR_SMALL.render(
                "Please create an issue on GitHub using the Help Wanted template and attach the mylog.log file", 1,
                "red")
            errorText1Place = WIDTH / 2 - errorText1.get_width() / 2, HEIGHT / 2 - errorText1.get_height() / 2
            WINDOW.blit(errorText1, errorText1Place)
            WINDOW.blit(errorText2,
                        (WIDTH / 2 - errorText2.get_width() / 2, HEIGHT / 2 - errorText2.get_height() / 2 + 30))
            WINDOW.blit(errorText3,
                        (WIDTH / 2 - errorText3.get_width() / 2, HEIGHT / 2 - errorText3.get_height() / 2 + 60))
            pygame.display.update()

    pygame.quit()
