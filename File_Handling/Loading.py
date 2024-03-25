import pickle


def load_highscore(filename):
    try:
        with open(filename, "rb") as f:
            highscore = pickle.load(f)
        return highscore
    except FileNotFoundError:
        print("High score file not found.")
        return 0
