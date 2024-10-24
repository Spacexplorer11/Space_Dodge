import pickle

from file_handling.utility import ref


def save_object(score):
    try:
        with open(ref("file_handling/highscore.pickle"), "wb") as f:
            pickle.dump(score, f)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
