import threading
import time
from collections import deque

import pygame
import pygame_widgets
from classes.button import Button
from file_handling.constants_and_file_loading import (
    WINDOW, pause_background, muteImage, unmuteImage, PAUSE_FONT, x_button_icon)
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

mutePauseButton = Button(pygame.transform.scale(muteImage, (120, 80)), 180, 430)
unmutePauseButton = Button(pygame.transform.scale(unmuteImage, (120, 80)), 180, 430)
slider_title = pygame.font.SysFont("comicsans", 30).render("Volume", 1, (255, 255, 255))
xButton = Button(x_button_icon, 665, 175)

# Volume update optimization
_volume_update_queue = deque(maxlen=1)  # Only keep the latest volume update
_volume_thread = None


def update_volume_async(volume):
    """Asynchronously update volume using a single reusable thread"""
    global _volume_thread

    # Add volume to queue (replaces any previous pending update)
    _volume_update_queue.clear()
    _volume_update_queue.append(volume)

    # Only create new thread if none exists or previous one finished
    if _volume_thread is None or not _volume_thread.is_alive():
        _volume_thread = threading.Thread(target=_process_volume_updates, daemon=True)
        _volume_thread.start()


def _process_volume_updates():
    """Process volume updates from queue"""
    while _volume_update_queue:
        volume = _volume_update_queue.popleft()
        pygame.mixer.music.set_volume(volume)
        time.sleep(0.01)  # Small delay to prevent excessive updates


def settings_menu(mute):
    slider = Slider(WINDOW, 350, 400, 100, 30, min=0, max=100, initial=pygame.mixer.music.get_volume() * 100)
    output = TextBox(WINDOW, 500, 395, 75, 50, fontSize=30)

    output.disable()
    pause = True
    last_volume = slider.getValue()  # Track last volume for debouncing


    while pause:
        time.sleep(6.5 / 1000)
        WINDOW.blit(pause_background, (0, 0))
        WINDOW.blit(PAUSE_FONT.render("SETTINGS MENU", 1, "white"), (250, 176))

        if mute:
            mutePauseButton.draw()
        else:
            unmutePauseButton.draw()

        if pygame.mixer.music.get_busy() is False and mute is False:
            pygame.mixer.music.load("assets/sounds/background_music/pause_screen/pause_music.mp3")
            pygame.mixer.music.play(-1)

        WINDOW.blit(slider_title, (200, 390))
        xButton.draw()
        slider.draw()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return False, mute
            elif event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_m] or unmutePauseButton.clicked() or mutePauseButton.clicked():
                    mute = not mute
                    pygame.mixer.music.pause() if mute else pygame.mixer.music.unpause()
                elif keys[pygame.K_ESCAPE] or xButton.clicked():
                    return pause, mute

        slider.listen(events)
        output.setText(slider.getValue())
        pygame_widgets.update(events)

        # Only update volume when slider value changes (debouncing)
        current_volume = slider.getValue()
        if current_volume != last_volume:
            update_volume_async(current_volume / 100)
            last_volume = current_volume

        pygame.display.update()


def update_volume(volume):
    pygame.mixer.music.set_volume(volume)
