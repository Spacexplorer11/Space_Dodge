import time

import pygame
# Importing the crucial variables from the constants file
from file_handling.constants_and_file_loading import WINDOW, WIDTH, HEIGHT, welcome_screen_background, FONT, \
    FONT_SMALL, game_background_blurred


def keybindings_screen(lives):
    keybindText1 = FONT.render("Press M to mute/unmute or just click the symbol.", 1, "orange" if lives == 4 else "white")
    keybindText2 = FONT.render("Use A & D keys to move left & right.", 1, "orange" if lives == 4 else "white")
    keybindText3 = FONT.render("Press P or click the symbol to pause the game ", 1, "orange" if lives == 4 else "white")
    keybindText4 = FONT.render("Press I or K to bring up this screen.", 1, "orange" if lives == 4 else "white")
    WINDOW.blit(welcome_screen_background if lives == 4 else game_background_blurred, (0, 0))
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
    resumeText = FONT_SMALL.render("Click any key to " + ("continue!" if lives == 4 else "resume!"), 1,
                                   "orange" if lives == 4 else "white")
    WINDOW.blit(resumeText, (WIDTH / 2 - resumeText.get_width() / 2, 740))
    pygame.display.update()
    pauseStartTime = time.time()
    keyPress = True
    while True:
        pausedTime = int(time.time() - pauseStartTime)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                keyPress = False
            if event.type == pygame.QUIT:
                return False, 0.0
            if event.type == pygame.KEYDOWN and not keyPress:
                if lives <= 3:
                    return True, pausedTime
                startTime = time.time()
                return True, startTime
