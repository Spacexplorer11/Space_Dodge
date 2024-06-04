import pygame

# Window variables
WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# Fonts
FONT = pygame.font.SysFont("Arial Black", 36)
FONT_SMALL = pygame.font.SysFont("Cochin", 30)


def info_screen():
    WINDOW.fill((0, 0, 0))
    keybindText1 = FONT.render("Press M to mute/unmute or just click the symbol.", 1, "white")
    keybindText2 = FONT.render("Use A & D keys to move left & right.", 1, "white")
    keybindText3 = FONT.render("Press P, esc or the symbol to pause the game ", 1, "white")
    keybindText4 = FONT.render("Press I or K to bring up this screen.", 1, "white")
    resumeText = FONT_SMALL.render("Click any key to continue!", 1, "white")
    keybindText1Place = WIDTH / 2 - keybindText1.get_width() / 2, 300
    WINDOW.blit(keybindText1, keybindText1Place)
    WINDOW.blit(keybindText2, (WIDTH / 2 - keybindText2.get_width() / 2,
                               HEIGHT / 2 - (keybindText1.get_height() - keybindText2.get_height()) / 2 - 30))
    WINDOW.blit(keybindText3, (WIDTH / 2 - keybindText3.get_width() / 2,
                               HEIGHT / 2 - (
                                       keybindText1.get_height() - keybindText2.get_height() - keybindText3.
                                       get_height()) / 2 + 30))
    WINDOW.blit(keybindText4, (WIDTH / 2 - keybindText4.get_width() / 2,
                               HEIGHT / 2 - (
                                       keybindText1.get_height() - keybindText2.get_height() - keybindText3.
                                       get_height() - keybindText4.get_height() - 160) / 2))
    WINDOW.blit(resumeText, (WIDTH / 2 - resumeText.get_width() / 2, 740))
    pygame.display.update()
