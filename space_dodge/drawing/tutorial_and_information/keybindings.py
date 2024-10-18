import time

import pygame

# Importing the crucial variables from the constants file
from space_dodge.file_handling.constants_and_file_loading import WINDOW, WIDTH, HEIGHT, welcome_screen_image, FONT, \
    FONT_SMALL


def keybindings_screen(pausedTimes):
    WINDOW.blit(welcome_screen_image, (0, 0))
    keybindText1 = FONT.render("Press M to mute/unmute or just click the symbol.", 1, "orange")
    keybindText2 = FONT.render("Use A & D keys to move left & right.", 1, "orange")
    keybindText3 = FONT.render("Press P, esc or the symbol to pause the game ", 1, "orange")
    keybindText4 = FONT.render("Press I or K to bring up this screen.", 1, "orange")
    resumeText = FONT_SMALL.render("Click any key to continue!", 1, "orange")
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
    info_screen_active = True
    pauseStartTime = time.time()
    keyPress = True
    while info_screen_active:
        pausedTime = time.time() - pauseStartTime
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                keyPress = False
            if event.type == pygame.QUIT:
                running = False
                info_screen_active = False
                return running, info_screen_active
            if event.type == pygame.KEYDOWN and not keyPress:
                keyPress = True
                info_screen_active = False
                if pausedTimes is not None:
                    totalPausedTime = 0.0
                    pausedTimes.append(round(pausedTime))
                    for num in pausedTimes:
                        totalPausedTime += num
                    return totalPausedTime, pausedTime, keyPress, info_screen_active
                startTime = time.time()
                return startTime, info_screen_active, keyPress
