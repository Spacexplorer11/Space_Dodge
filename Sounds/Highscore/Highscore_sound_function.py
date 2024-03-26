import simpleaudio as sa


def highscore_sound(mute, highscoreSound):
    if not mute:
        play_sound = highscoreSound.play()
        play_sound.wait_done()  # Wait for the sound to finish
