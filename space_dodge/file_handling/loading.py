import json

from file_handling.utility import ref

from space_dodge.file_handling.constants_and_file_loading import logger


def load_highscore():
    try:
        with open(ref("file_handling/highscore.json"), "r") as f:
            score = json.load(f)
        print("✅ JSON highscore loaded:", score)
        logger.info("JSON highscore loaded successfully", extra={"score": score})
        return score, True
    except (FileNotFoundError, json.JSONDecodeError) as ex:
        print("❌ Failed to load JSON highscore:", ex)
        logger.exception("Error loading JSON highscore:", exc_info=ex)
        return 0, False
