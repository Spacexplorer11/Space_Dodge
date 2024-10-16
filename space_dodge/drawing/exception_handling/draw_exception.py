import pygame

# Window variables
WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.font.init()

FONT_ERROR = pygame.font.SysFont("Phosphate", 30)


def draw_except(error):
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        WINDOW.fill((0, 0, 0))
        if error == "background":
            errorText1 = FONT_ERROR.render("Error:", 1, "red")
            errorText2 = FONT_ERROR.render("A background image was not found", 1, "red")
            errorText3 = FONT_ERROR.render("Please create an issue on GitHub using the Help Wanted template", 1, "red")
            errorText1Place = WIDTH / 2 - errorText1.get_width() / 2, HEIGHT / 2 - errorText1.get_height() / 2
            WINDOW.blit(errorText1, errorText1Place)
            WINDOW.blit(errorText2, (WIDTH / 2 - errorText2.get_width() / 2,
                                     HEIGHT / 2 - (errorText1.get_height() - errorText2.get_height() - 30) / 2))
            WINDOW.blit(errorText3, (WIDTH / 2 - errorText3.get_width() / 2,
                                     HEIGHT / 2 - (
                                             errorText1.get_height() - errorText2.get_height() - errorText3.
                                             get_height() - 60) / 2))
            pygame.display.update()
        elif error == "Player":
            errorText1 = FONT_ERROR.render("Error:", 1, "red")
            errorText2 = FONT_ERROR.render("Player image was not found", 1, "red")
            errorText3 = FONT_ERROR.render("Please create an issue on GitHub using the Help Wanted template", 1, "red")
            errorText1Place = WIDTH / 2 - errorText1.get_width() / 2, HEIGHT / 2 - errorText1.get_height() / 2
            WINDOW.blit(errorText1, errorText1Place)
            WINDOW.blit(errorText2, (WIDTH / 2 - errorText2.get_width() / 2,
                                     HEIGHT / 2 - (errorText1.get_height() - errorText2.get_height() - 30) / 2))
            WINDOW.blit(errorText3, (WIDTH / 2 - errorText3.get_width() / 2,
                                     HEIGHT / 2 - (
                                             errorText1.get_height() - errorText2.get_height() - errorText3.
                                             get_height() - 60) / 2))
            pygame.display.update()
        elif error == "Button":
            errorText1 = FONT_ERROR.render("Error:", 1, "red")
            errorText2 = FONT_ERROR.render("A symbol( mute, unmute or pause ) was not found", 1, "red")
            errorText3 = FONT_ERROR.render("Please create an issue on GitHub using the Help Wanted template", 1, "red")
            errorText1Place = WIDTH / 2 - errorText1.get_width() / 2, HEIGHT / 2 - errorText1.get_height() / 2
            WINDOW.blit(errorText1, errorText1Place)
            WINDOW.blit(errorText2, (WIDTH / 2 - errorText2.get_width() / 2,
                                     HEIGHT / 2 - (errorText1.get_height() - errorText2.get_height() - 30) / 2))
            WINDOW.blit(errorText3, (WIDTH / 2 - errorText3.get_width() / 2,
                                     HEIGHT / 2 - (
                                             errorText1.get_height() - errorText2.get_height() - errorText3.
                                             get_height() - 60) / 2))
            pygame.display.update()
        elif error == "Lives":
            errorText1 = FONT_ERROR.render("Error:", 1, "red")
            errorText2 = FONT_ERROR.render("The image for the lives were not found", 1, "red")
            errorText3 = FONT_ERROR.render("Please create an issue on GitHub using the Help Wanted template", 1, "red")
            errorText1Place = WIDTH / 2 - errorText1.get_width() / 2, HEIGHT / 2 - errorText1.get_height() / 2
            WINDOW.blit(errorText1, errorText1Place)
            WINDOW.blit(errorText2, (WIDTH / 2 - errorText2.get_width() / 2,
                                     HEIGHT / 2 - (errorText1.get_height() - errorText2.get_height() - 30) / 2))
            WINDOW.blit(errorText3, (WIDTH / 2 - errorText3.get_width() / 2,
                                     HEIGHT / 2 - (
                                             errorText1.get_height() - errorText2.get_height() - errorText3.
                                             get_height() - 60) / 2))
            pygame.display.update()
        elif error == "Sound Effects":
            errorText1 = FONT_ERROR.render("Error:", 1, "red")
            errorText2 = FONT_ERROR.render("One or more of the sound effects weren't found", 1, "red")
            errorText3 = FONT_ERROR.render("Please create an issue on GitHub using the Help Wanted template", 1, "red")
            errorText1Place = WIDTH / 2 - errorText1.get_width() / 2, HEIGHT / 2 - errorText1.get_height() / 2
            WINDOW.blit(errorText1, errorText1Place)
            WINDOW.blit(errorText2, (WIDTH / 2 - errorText2.get_width() / 2,
                                     HEIGHT / 2 - (errorText1.get_height() - errorText2.get_height() - 30) / 2))
            WINDOW.blit(errorText3, (WIDTH / 2 - errorText3.get_width() / 2,
                                     HEIGHT / 2 - (
                                             errorText1.get_height() - errorText2.get_height() - errorText3.
                                             get_height() - 60) / 2))
            pygame.display.update()
        elif error == "Music":
            errorText1 = FONT_ERROR.render("Error:", 1, "red")
            errorText2 = FONT_ERROR.render("Some background music files weren't not found", 1, "red")
            errorText3 = FONT_ERROR.render("Please create an issue on GitHub using the Help Wanted template", 1, "red")
            errorText1Place = WIDTH / 2 - errorText1.get_width() / 2, HEIGHT / 2 - errorText1.get_height() / 2
            WINDOW.blit(errorText1, errorText1Place)
            WINDOW.blit(errorText2, (WIDTH / 2 - errorText2.get_width() / 2,
                                     HEIGHT / 2 - (errorText1.get_height() - errorText2.get_height() - 30) / 2))
            WINDOW.blit(errorText3, (WIDTH / 2 - errorText3.get_width() / 2,
                                     HEIGHT / 2 - (
                                             errorText1.get_height() - errorText2.get_height() - errorText3.
                                             get_height() - 60) / 2))
            pygame.display.update()
        elif error == "Button":
            errorText1 = FONT_ERROR.render("Error:", 1, "red")
            errorText2 = FONT_ERROR.render("One or more of the button images weren't found", 1, "red")
            errorText3 = FONT_ERROR.render("Please create an issue on GitHub using the Help Wanted template", 1, "red")
            errorText1Place = WIDTH / 2 - errorText1.get_width() / 2, HEIGHT / 2 - errorText1.get_height() / 2
            WINDOW.blit(errorText1, errorText1Place)
            WINDOW.blit(errorText2, (WIDTH / 2 - errorText2.get_width() / 2,
                                     HEIGHT / 2 - (errorText1.get_height() - errorText2.get_height() - 30) / 2))
            WINDOW.blit(errorText3, (WIDTH / 2 - errorText3.get_width() / 2,
                                     HEIGHT / 2 - (
                                             errorText1.get_height() - errorText2.get_height() - errorText3.
                                             get_height() - 60) / 2))
            pygame.display.update()
        elif error == "Bullet":
            errorText1 = FONT_ERROR.render("Error:", 1, "red")
            errorText2 = FONT_ERROR.render("The bullet images weren't found", 1, "red")
            errorText3 = FONT_ERROR.render("Please create an issue on GitHub using the Help Wanted template", 1, "red")
            errorText1Place = WIDTH / 2 - errorText1.get_width() / 2, HEIGHT / 2 - errorText1.get_height() / 2
            WINDOW.blit(errorText1, errorText1Place)
            WINDOW.blit(errorText2, (WIDTH / 2 - errorText2.get_width() / 2,
                                     HEIGHT / 2 - (errorText1.get_height() - errorText2.get_height() - 30) / 2))
            WINDOW.blit(errorText3, (WIDTH / 2 - errorText3.get_width() / 2,
                                     HEIGHT / 2 - (
                                             errorText1.get_height() - errorText2.get_height() - errorText3.
                                             get_height() - 60) / 2))
        elif error == "Bullet Animation":
            errorText1 = FONT_ERROR.render("Error:", 1, "red")
            errorText2 = FONT_ERROR.render("The explosion frames weren't found", 1, "red")
            errorText3 = FONT_ERROR.render("Please create an issue on GitHub using the Help Wanted template", 1, "red")
            errorText1Place = WIDTH / 2 - errorText1.get_width() / 2, HEIGHT / 2 - errorText1.get_height() / 2
            WINDOW.blit(errorText1, errorText1Place)
            WINDOW.blit(errorText2, (WIDTH / 2 - errorText2.get_width() / 2,
                                     HEIGHT / 2 - (errorText1.get_height() - errorText2.get_height() - 30) / 2))
            WINDOW.blit(errorText3, (WIDTH / 2 - errorText3.get_width() / 2,
                                     HEIGHT / 2 - (
                                             errorText1.get_height() - errorText2.get_height() - errorText3.
                                             get_height() - 60) / 2))
    pygame.quit()
