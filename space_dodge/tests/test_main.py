import os
import sys
import threading

# Add root folder to sys.path (if not already)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import main
import pygame

# Helper to simulate pygame events for testing
class EventSimulator:
    def __init__(self):
        self.frame_count = 0
        self.max_frames = 600  # Run ~10 seconds at 60 FPS

    def get_events(self):
        events = []

        # Simulate QUIT event after max_frames
        if self.frame_count >= self.max_frames:
            events.append(pygame.event.Event(pygame.QUIT))

        # Before that, simulate key presses / mouse clicks to advance game:

        # On first frame: simulate a click on the start button to exit title screen
        if self.frame_count == 0:
            events.append(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=(351, 301)))

        # Simulate a double key press after starting
        if self.frame_count == 1:
            events.append(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a))
        if self.frame_count == 2:
            events.append(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a))

        # Press 'i' to see keybindings
        if self.frame_count == 10:
            events.append(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_i))

        # Press a key to exit keybindings
        if self.frame_count == 15:
            events.append(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a))

        # Simulate pressing 'm' (mute)
        if self.frame_count == 20:
            events.append(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_m))

        # Simulate pressing 'm' again (to unmute)
        if self.frame_count == 30:
            events.append(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_m))

        # Simulate moving right
        if self.frame_count == 40:
            events.append(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_d))
        if self.frame_count == 100:
            events.append(pygame.event.Event(pygame.KEYUP, key=pygame.K_d))

        # Simulate moving left
        if self.frame_count == 101:
            events.append(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a))
        if self.frame_count == 160:
            events.append(pygame.event.Event(pygame.KEYUP, key=pygame.K_a))

        # Simulate pressing 'p' (pause) around frame 300
        if self.frame_count == 300:
            events.append(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_p))

        # Click settings button in pause menu
        if self.frame_count == 310:
            events.append(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=(210, 190)))

        # Click X button in settings menu
        if self.frame_count == 320:
            events.append(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=(670, 180)))

        # Simulate pressing 'p' again around frame 350 (to unpause)
        if self.frame_count == 350:
            events.append(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_p))

        # You can add more simulated inputs here if you want to test menus etc.

        self.frame_count += 1
        return events


def test_main_runs():
    # Patch pygame.event.get to use our simulator events
    simulator = EventSimulator()
    original_event_get = pygame.event.get
    pygame.event.get = simulator.get_events

    def run_game():
        try:
            main.main()
        except Exception as e:
            # Restore event.get before raising
            pygame.event.get = original_event_get
            raise e

    # Run the game in a thread to allow timeout
    thread = threading.Thread(target=run_game)
    thread.daemon = True
    thread.start()
    thread.join(timeout=15)  # 15 seconds max

    # Restore the original pygame.event.get function
    pygame.event.get = original_event_get

    # If thread is still alive, test failed due to hang
    assert not thread.is_alive(), "Game did not exit in time, test failed"
