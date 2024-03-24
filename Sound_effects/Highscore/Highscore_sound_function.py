import simpleaudio as sa


def highscore_sound(mute):
    if not mute:
        filename = "Sound_effects/Highscore/highscore.wav"
        sound = sa.WaveObject.from_wave_file(filename)
        play_sound = sound.play()
        play_sound.wait_done()  # Wait for the sound to finish
