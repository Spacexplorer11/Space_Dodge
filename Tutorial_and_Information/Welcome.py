import os

import pygame

from Space_Dodge.Exception_Handling.draw_exception import draw_except

# Window variables
WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# Fonts
FONT = pygame.font.SysFont("Arial Black", 40)
FONT_SMALL = pygame.font.SysFont("Cochin", 30)

# Load the welcome screen image
try:
    Welcome_Screen_image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Welcome_screen.png")), (WIDTH, HEIGHT))
except FileNotFoundError:
    error = "Background"
    draw_except(error)


def welcome_screen():
    WINDOW.blit(Welcome_Screen_image, (0, 0))
    welcomeText1 = FONT.render("Welcome to Space Dodge!", 1, "orange")
    welcomeText2 = FONT.render("Use A & D keys to move left & right!", 1, "orange")
    welcomeText3 = FONT.render("Try not to hit the bullets!", 1, "orange")
    startText = FONT_SMALL.render("Click any key to continue!", 1, "orange")
    keybindingsInstructionText = FONT.render("Click I or K to check keybindings", 1, "orange")
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
