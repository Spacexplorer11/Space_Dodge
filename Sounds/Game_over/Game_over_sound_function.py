import simpleaudio as sa


def game_over_sound(mute, sadSound, GameOverSound):
    if not mute:
        play_sound = GameOverSound.play()
        play_sadsound = sadSound.play()
        play_sadsound.wait_done()
        play_sound.wait_done()  # Wait until sound has finished playing
