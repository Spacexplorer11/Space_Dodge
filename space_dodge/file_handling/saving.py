import json
import os

from file_handling.constants_and_file_loading import logger
from file_handling.utility import ref


def save_object(score):
    json_path = ref("file_handling/highscore.json")
    os.makedirs(os.path.dirname(json_path), exist_ok=True)

    try:
        with open(json_path, "w") as f:
            json.dump(score, f)
            f.flush()
            os.fsync(f.fileno())
            print("✅ JSON score saved:", score)
            logger.info("JSON highscore saved successfully", extra={"score": score})
    except Exception as ex:
        print("❌ JSON save error:", ex)
        logger.exception("Error saving JSON highscore:", exc_info=ex)
