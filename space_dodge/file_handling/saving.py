import pickle

from file_handling.utility import ref


def save_object(scores):
    try:
        with open(ref("file_handling/highscores.pickle"), "wb") as f:
            pickle.dump(scores, f)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
