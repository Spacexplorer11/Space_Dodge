import pickle
from file_handling.utility import ref


def load_highscore():
    try:
        with open(ref("file_handling/highscores.pickle"), "rb") as f:
            highscores = pickle.load(f)
        return highscores
    except FileNotFoundError:
        print("High score file not found.")
        return {1: 0, 2: 0, 3: 0}
