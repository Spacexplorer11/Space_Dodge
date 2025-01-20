import logging
import os

import pygame as p

from drawing.exception_handling.draw_exception import draw_except
from file_handling.utility import ref
from pygame import image as i
from pygame import mixer as m
from pygame import transform as t

# This to simplify the code and make it more readable
# For example, pygame.image.load("path") can be replaced with i.load("path"),
# pygame.transform.scale(image, (width, height)) can be replaced with t.scale(image, (width, height)),
# all instances of pygame can be replaced with p
# and pygame.mixer can be replaced with m.
# This is to make the code conciser and easier to understand

# Initialise pygame
p.init()
p.mixer.init()

# Window variables
WIDTH, HEIGHT = 1000, 800
WINDOW = p.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
p.display.set_caption("Space Dodge")

# All the fonts
FONT = p.font.SysFont("Arial Black", 30)
FONT_SMALL = p.font.SysFont("Cochin", 30)
FONT_ERROR = p.font.SysFont("Phosphate", 50)
FONT_BIG = p.font.SysFont("Arial Black", 100)
FONT_MEDIUM = p.font.SysFont("Arial Black", 45)
PAUSE_FONT = p.font.SysFont("Arial", 50)
PAUSE_FONT_SMALL = p.font.SysFont("Arial", 45)

# Player variables
PLAYER_HEIGHT = 100
PLAYER_WIDTH = 80
PLAYER_VELOCITY = 5

# Bullet variables
BULLET_WIDTH = 50
BULLET_HEIGHT = 70
BULLET_VELOCITY = 3

# Button variables
BUTTON_WIDTH, BUTTON_HEIGHT = 300, 200

logfile = ref('mylog.log')
logging.basicConfig(filename=logfile, level=logging.INFO)
logger = logging.getLogger(__name__)


# Function to draw the loading bar
def draw_loading_bar(screen, progress, width=392, height=30):
    bar_x = (WIDTH - width) // 2
    bar_y = (HEIGHT - height) // 2
    fill_width = int(progress * width)
    p.draw.rect(screen, (50, 50, 50), (bar_x, bar_y, width, height))
    p.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, fill_width, height))
    p.display.update()


# Decorator to calculate the pause time
def pause_time(func):
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        pausedTime = int(end_time - start_time)
        if isinstance(result, tuple):
            return result + (pausedTime,)
        return result, pausedTime

    return wrapper


# Load all the files/variables with loading bar updates
total_assets = 90  # Total number of assets to load
loaded_assets = 0


def update_loading_bar(assets_num=1):
    global loaded_assets
    for _ in range(assets_num):
        loaded_assets += 1
        draw_loading_bar(WINDOW, loaded_assets / total_assets)


try:
    playerR = t.scale(i.load(ref("assets/player_r.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
    playerL = t.scale(i.load(ref("assets/player_l.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
    update_loading_bar(2)
except FileNotFoundError:
    logger.exception('Player not found')
    draw_except("Player")

try:
    muteImage = t.scale(i.load(ref("assets/mute.png")), (70, 50))
    unmuteImage = t.scale(i.load(ref("assets/unmute.png")), (70, 50))
    pauseButtonImage = t.scale(i.load(ref("assets/pause_rectangle.png")), (50, 30))
    update_loading_bar(3)

except FileNotFoundError:
    logger.exception('Button not found')
    draw_except("Button")

try:
    sadSound = m.Sound(ref("sounds/game_over/sad-trombone.mp3"))
    GameOverSound = m.Sound(ref("sounds/game_over/game-over-sound.mp3"))
    highscoreSound = m.Sound(ref("sounds/highscore/highscore.mp3"))
    update_loading_bar(3)
except FileNotFoundError:
    logger.exception('Sound not found')
    draw_except("Sound Effects")

background_music_check = os.path.exists(ref("sounds/background_music/background_music.mp3"))
pause_music_check = os.path.exists(ref("sounds/pause_screen/pause_music.mp3"))
if not (background_music_check or pause_music_check):
    logger.exception('Music not found')
    draw_except("Music")
update_loading_bar(2)

try:
    bullet_texture = t.scale(i.load(ref("assets/bullet_texture.png")), (BULLET_WIDTH, BULLET_HEIGHT))
    update_loading_bar()
except FileNotFoundError:
    logger.exception('Bullet texture not found')
    draw_except("Bullet")

try:
    threeLives = t.scale(i.load(ref("assets/lives/three_lives.png")), (200, 200))
    twoLives = t.scale(i.load(ref("assets/lives/two_lives.png")), (200, 190))
    oneLife = t.scale(i.load(ref("assets/lives/one_life.png")), (200, 180))
    update_loading_bar(3)
except FileNotFoundError:
    logger.exception('Lives not found')
    draw_except("Lives")

try:
    game_background = t.scale(i.load(ref("assets/space_background.jpg")), (WIDTH, HEIGHT))
    title_screen_background = t.scale(i.load(ref("assets/title_screen.jpg")), (WIDTH, HEIGHT))
    welcome_screen_background = t.scale(i.load(ref("assets/welcome_screen.png")), (WIDTH, HEIGHT))
    pause_background = t.scale(i.load(ref("assets/pause_background.png")), (WIDTH, HEIGHT))
    game_background_blurred = t.scale(i.load(ref("assets/space_background_blurred.png")), (WIDTH, HEIGHT))
    update_loading_bar(5)
except FileNotFoundError:
    logger.exception('background not found')
    draw_except("background")

try:
    bullet_explosion_frames = {
        1: t.scale(i.load(ref("assets/explosion_gif_frames/explosion1.png")), (BULLET_WIDTH, BULLET_HEIGHT)),
        2: t.scale(i.load(ref("assets/explosion_gif_frames/explosion2.png")), (BULLET_WIDTH, BULLET_HEIGHT)),
        3: t.scale(i.load(ref("assets/explosion_gif_frames/explosion3.png")), (BULLET_WIDTH, BULLET_HEIGHT)),
        4: t.scale(i.load(ref("assets/explosion_gif_frames/explosion4.png")), (BULLET_WIDTH, BULLET_HEIGHT)),
        5: t.scale(i.load(ref("assets/explosion_gif_frames/explosion5.png")), (BULLET_WIDTH, BULLET_HEIGHT)),
        6: t.scale(i.load(ref("assets/explosion_gif_frames/explosion6.png")), (BULLET_WIDTH, BULLET_HEIGHT)),
    }
    settings_icon_frames = {
        1: t.scale(i.load(ref("assets/settings_icon_frames/frame_00.png")), (50, 50)),
        2: t.scale(i.load(ref("assets/settings_icon_frames/frame_01.png")), (50, 50)),
        3: t.scale(i.load(ref("assets/settings_icon_frames/frame_02.png")), (50, 50)),
        4: t.scale(i.load(ref("assets/settings_icon_frames/frame_03.png")), (50, 50)),
        5: t.scale(i.load(ref("assets/settings_icon_frames/frame_04.png")), (50, 50)),
        6: t.scale(i.load(ref("assets/settings_icon_frames/frame_05.png")), (50, 50)),
        7: t.scale(i.load(ref("assets/settings_icon_frames/frame_06.png")), (50, 50)),
        8: t.scale(i.load(ref("assets/settings_icon_frames/frame_07.png")), (50, 50)),
        9: t.scale(i.load(ref("assets/settings_icon_frames/frame_08.png")), (50, 50)),
        10: t.scale(i.load(ref("assets/settings_icon_frames/frame_09.png")), (50, 50)),
        11: t.scale(i.load(ref("assets/settings_icon_frames/frame_10.png")), (50, 50)),
        12: t.scale(i.load(ref("assets/settings_icon_frames/frame_11.png")), (50, 50)),
        13: t.scale(i.load(ref("assets/settings_icon_frames/frame_12.png")), (50, 50)),
        14: t.scale(i.load(ref("assets/settings_icon_frames/frame_13.png")), (50, 50)),
        15: t.scale(i.load(ref("assets/settings_icon_frames/frame_14.png")), (50, 50)),
        16: t.scale(i.load(ref("assets/settings_icon_frames/frame_15.png")), (50, 50)),
        17: t.scale(i.load(ref("assets/settings_icon_frames/frame_16.png")), (50, 50)),
        18: t.scale(i.load(ref("assets/settings_icon_frames/frame_17.png")), (50, 50)),
        19: t.scale(i.load(ref("assets/settings_icon_frames/frame_18.png")), (50, 50)),
        20: t.scale(i.load(ref("assets/settings_icon_frames/frame_19.png")), (50, 50)),
        21: t.scale(i.load(ref("assets/settings_icon_frames/frame_20.png")), (50, 50)),
        22: t.scale(i.load(ref("assets/settings_icon_frames/frame_21.png")), (50, 50)),
        23: t.scale(i.load(ref("assets/settings_icon_frames/frame_22.png")), (50, 50)),
        24: t.scale(i.load(ref("assets/settings_icon_frames/frame_23.png")), (50, 50)),
        25: t.scale(i.load(ref("assets/settings_icon_frames/frame_24.png")), (50, 50)),
        26: t.scale(i.load(ref("assets/settings_icon_frames/frame_25.png")), (50, 50)),
        27: t.scale(i.load(ref("assets/settings_icon_frames/frame_26.png")), (50, 50)),
        28: t.scale(i.load(ref("assets/settings_icon_frames/frame_27.png")), (50, 50)),
        29: t.scale(i.load(ref("assets/settings_icon_frames/frame_28.png")), (50, 50)),
        30: t.scale(i.load(ref("assets/settings_icon_frames/frame_29.png")), (50, 50)),
        31: t.scale(i.load(ref("assets/settings_icon_frames/frame_30.png")), (50, 50)),
        32: t.scale(i.load(ref("assets/settings_icon_frames/frame_31.png")), (50, 50)),
        33: t.scale(i.load(ref("assets/settings_icon_frames/frame_32.png")), (50, 50)),
        34: t.scale(i.load(ref("assets/settings_icon_frames/frame_33.png")), (50, 50)),
        35: t.scale(i.load(ref("assets/settings_icon_frames/frame_34.png")), (50, 50)),
        36: t.scale(i.load(ref("assets/settings_icon_frames/frame_35.png")), (50, 50)),
        37: t.scale(i.load(ref("assets/settings_icon_frames/frame_36.png")), (50, 50)),
        38: t.scale(i.load(ref("assets/settings_icon_frames/frame_37.png")), (50, 50)),
        39: t.scale(i.load(ref("assets/settings_icon_frames/frame_38.png")), (50, 50)),
        40: t.scale(i.load(ref("assets/settings_icon_frames/frame_39.png")), (50, 50)),
        41: t.scale(i.load(ref("assets/settings_icon_frames/frame_40.png")), (50, 50)),
        42: t.scale(i.load(ref("assets/settings_icon_frames/frame_41.png")), (50, 50)),
        43: t.scale(i.load(ref("assets/settings_icon_frames/frame_42.png")), (50, 50)),
        44: t.scale(i.load(ref("assets/settings_icon_frames/frame_43.png")), (50, 50)),
        45: t.scale(i.load(ref("assets/settings_icon_frames/frame_44.png")), (50, 50)),
        46: t.scale(i.load(ref("assets/settings_icon_frames/frame_45.png")), (50, 50)),
        47: t.scale(i.load(ref("assets/settings_icon_frames/frame_46.png")), (50, 50)),
        48: t.scale(i.load(ref("assets/settings_icon_frames/frame_47.png")), (50, 50)),
        49: t.scale(i.load(ref("assets/settings_icon_frames/frame_48.png")), (50, 50)),
        50: t.scale(i.load(ref("assets/settings_icon_frames/frame_49.png")), (50, 50)),
        51: t.scale(i.load(ref("assets/settings_icon_frames/frame_50.png")), (50, 50)),
        52: t.scale(i.load(ref("assets/settings_icon_frames/frame_51.png")), (50, 50)),
        53: t.scale(i.load(ref("assets/settings_icon_frames/frame_52.png")), (50, 50)),
        54: t.scale(i.load(ref("assets/settings_icon_frames/frame_53.png")), (50, 50)),
        55: t.scale(i.load(ref("assets/settings_icon_frames/frame_54.png")), (50, 50)),
        56: t.scale(i.load(ref("assets/settings_icon_frames/frame_55.png")), (50, 50)),
        57: t.scale(i.load(ref("assets/settings_icon_frames/frame_56.png")), (50, 50)),
        58: t.scale(i.load(ref("assets/settings_icon_frames/frame_57.png")), (50, 50)),
        59: t.scale(i.load(ref("assets/settings_icon_frames/frame_58.png")), (50, 50)),
        60: t.scale(i.load(ref("assets/settings_icon_frames/frame_59.png")), (50, 50)),
        61: t.scale(i.load(ref("assets/settings_icon_frames/frame_60.png")), (50, 50)),
        62: t.scale(i.load(ref("assets/settings_icon_frames/frame_61.png")), (50, 50)),

    }
    update_loading_bar(68)
except FileNotFoundError:
    logger.exception('Settings icon or Explosion frames not found')
    draw_except("Animation")

try:
    start_button_image = t.scale(i.load(ref("assets/start_button.png")), (BUTTON_WIDTH, BUTTON_HEIGHT))
    update_loading_bar()
except FileNotFoundError:
    logger.exception('Start button image not found')
    draw_except("Button")

title_screen_music_check = os.path.exists(ref("sounds/background_music/title_screen/title_screen_music.mp3"))
if not title_screen_music_check:
    logger.exception('Title screen music not found')
    draw_except("Music")
update_loading_bar()

try:
    x_button_icon = t.scale(i.load(ref("assets/x_button_icon.png")), (60, 60))
    update_loading_bar()
except FileNotFoundError:
    logger.exception('X button not found')
    draw_except("Button")
