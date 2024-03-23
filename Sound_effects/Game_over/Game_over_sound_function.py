import simpleaudio as sa


def game_over_sound():
    sadsound = sa.WaveObject.from_wave_file("Sound_effects/Game_over/sad-trombone.wav")
    filename = "Sound_effects/Game_over/game-over-sound.wav"
    sound = sa.WaveObject.from_wave_file(filename)
    play_sound = sound.play()
    play_sadsound = sadsound.play()
    play_sadsound.wait_done()
    play_sound.wait_done()  # Wait until sound has finished playing
