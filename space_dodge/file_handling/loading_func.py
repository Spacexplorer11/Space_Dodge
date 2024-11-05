import pickle


def load_highscore(file_path):
    try:
        with open(file_path, "rb") as f:
            highscore = pickle.load(f)
        return highscore, True
    except FileNotFoundError:
        print("High score file not found.")
        return 0, False
