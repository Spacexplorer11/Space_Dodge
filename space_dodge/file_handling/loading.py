import json

from file_handling.utility import ref

from space_dodge.file_handling.constants_and_file_loading import logger


def load_highscore():
    try:
        with open(ref("file_handling/highscore.json"), "r") as f:
            score = json.load(f)
        print("✅ JSON highscore loaded:", score)
        logger.info("JSON highscore loaded successfully", extra={"score": score})
        return score
    except (FileNotFoundError, json.JSONDecodeError) as ex:
        print("❌ Failed to load JSON highscore:", ex)
        print("Returning 0 as this means the game probably has never been played before, which is OK")
        logger.exception("Error loading JSON highscore:", exc_info=ex)
        logger.info("The game has probably never been played before, returning 0")
        return 0  # Return 0 as this probably means the game has never been played before
