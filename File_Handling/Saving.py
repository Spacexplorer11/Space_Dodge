import pickle
import os


def save_object(score):
    try:
        with open(os.path.join("File_Handling", "highscore.pickle"), "wb") as f:
            pickle.dump(score, f)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
