import time

import pygame

# Window variables
WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# Fonts
FONT = pygame.font.SysFont("Arial Black", 30)
FONT_SMALL = pygame.font.SysFont("Cochin", 30)


def welcome_text():
    WINDOW.fill((0, 0, 0))
    welcomeText1 = FONT.render("Welcome to Space Dodge!", 1, "white")
    welcomeText2 = FONT.render("Use A & D keys to move left & right!", 1, "white")
    welcomeText3 = FONT.render("Try not to hit the bullets!", 1, "white")
    startText = FONT_SMALL.render("Click any key to continue!", 1, "white")
    keybindingsInstructionText = FONT.render("Click I or K to check keybindings", 1, "white")
    welcomeText1Place = WIDTH / 2 - welcomeText1.get_width() / 2, HEIGHT / 2 - welcomeText1.get_height() / 2
    WINDOW.blit(welcomeText1, welcomeText1Place)
    WINDOW.blit(welcomeText2, (WIDTH / 2 - welcomeText2.get_width() / 2,
                               HEIGHT / 2 - (welcomeText1.get_height() - welcomeText2.get_height() - 30) / 2))
    WINDOW.blit(welcomeText3, (WIDTH / 2 - welcomeText3.get_width() / 2,
                               HEIGHT / 2 - (
                                       welcomeText1.get_height() - welcomeText2.get_height() - welcomeText3.
                                       get_height() - 60) / 2))
    WINDOW.blit(keybindingsInstructionText, (WIDTH / 2 - keybindingsInstructionText.get_width() / 2,
                                      HEIGHT / 2 - (
                                              welcomeText1.get_height() - welcomeText2.get_height() -
                                              welcomeText3.
                                              get_height() - keybindingsInstructionText.get_height() - 90) / 2))
    WINDOW.blit(startText, (WIDTH / 2 - startText.get_width() / 2, 740))
    pygame.display.update()
    startTime, welcome = time.time(), False
    return startTime, welcome
