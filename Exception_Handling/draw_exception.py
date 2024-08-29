import pygame

pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")
FONT_ERROR = pygame.font.SysFont("Phosphate", 40)


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
        if error == "Background":
            errorText1 = FONT_ERROR.render("Error:", 1, "red")
            errorText2 = FONT_ERROR.render("Background image was not found", 1, "red")
            errorText3 = FONT_ERROR.render("Please check you have downloaded it", 1, "red")
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
            errorText3 = FONT_ERROR.render("Please check you have downloaded it", 1, "red")
            errorText1Place = WIDTH / 2 - errorText1.get_width() / 2, HEIGHT / 2 - errorText1.get_height() / 2
            WINDOW.blit(errorText1, errorText1Place)
            WINDOW.blit(errorText2, (WIDTH / 2 - errorText2.get_width() / 2,
                                     HEIGHT / 2 - (errorText1.get_height() - errorText2.get_height() - 30) / 2))
            WINDOW.blit(errorText3, (WIDTH / 2 - errorText3.get_width() / 2,
                                     HEIGHT / 2 - (
                                             errorText1.get_height() - errorText2.get_height() - errorText3.
                                             get_height() - 60) / 2))
            pygame.display.update()
        elif error == "Symbol":
            errorText1 = FONT_ERROR.render("Error:", 1, "red")
            errorText2 = FONT_ERROR.render("A symbol( mute, unmute or pause ) was not found", 1, "red")
            errorText3 = FONT_ERROR.render("Please check you have downloaded it", 1, "red")
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
            errorText2 = FONT_ERROR.render("The image for the lives was not found", 1, "red")
            errorText3 = FONT_ERROR.render("Please check you have downloaded it", 1, "red")
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
            errorText3 = FONT_ERROR.render("Please check you have downloaded them", 1, "red")
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
            errorText2 = FONT_ERROR.render("Some music files weren't not found", 1, "red")
            errorText3 = FONT_ERROR.render("Please check you have downloaded it", 1, "red")
            errorText1Place = WIDTH / 2 - errorText1.get_width() / 2, HEIGHT / 2 - errorText1.get_height() / 2
            WINDOW.blit(errorText1, errorText1Place)
            WINDOW.blit(errorText2, (WIDTH / 2 - errorText2.get_width() / 2,
                                     HEIGHT / 2 - (errorText1.get_height() - errorText2.get_height() - 30) / 2))
            WINDOW.blit(errorText3, (WIDTH / 2 - errorText3.get_width() / 2,
                                     HEIGHT / 2 - (
                                             errorText1.get_height() - errorText2.get_height() - errorText3.
                                             get_height() - 60) / 2))
            pygame.display.update()
    pygame.quit()
