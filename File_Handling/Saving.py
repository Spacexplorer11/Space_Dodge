import pickle

def save_object(score):
    try:
        with open("File_Handling/highscore.pickle", "wb") as f:
            pickle.dump(score, f)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)