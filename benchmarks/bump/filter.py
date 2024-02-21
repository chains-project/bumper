import json
import os
from pathlib import Path
from typing import List

config = {
    "MAX_IMAGE_SIZE": 1000 * 1000000,  # 1000 Megabytes
    "MAX_IMAGE_TIME": 60 * 1000,  # 1 Minute,
}


def remove_file(path: str) -> bool:
    if os.path.exists(path):
        os.remove(path)
        return True
    return False


def filter_files_for_time_or_size():
    files_to_remove = []
    with open("./repository/RQData/image-execution-times.json") as f:
        execution_times = json.load(f)
        for key in execution_times:
            if execution_times[key]['breakingImageTime'] > config["MAX_IMAGE_TIME"]:
                files_to_remove.append(key)
            elif execution_times[key]['breakingImageSize'] > config["MAX_IMAGE_SIZE"]:
                files_to_remove.append(key)
    print(f"we should remove {len(files_to_remove)} files for time or size constraints")
    removed_count = 0
    for key in files_to_remove:
        if remove_file(f"./filtered_data/{key}.json"):
            removed_count += 1

    print(f"{removed_count} files removed")


def filter_files_for_error_type(keep: List[str]):
    directory = "./repository/reproductionLogs/successfulReproductionLogs"
    removed_count = 0

    for filename in os.scandir(directory):
        if filename.is_file():
            key = filename.name.replace(".log", "")
            path = filename.path
            with open(path) as f:
                if not it_contains_any(f.read(), keep):
                    if remove_file(f"./filtered_data/{key}.json"):
                        removed_count += 1

    print(f"{removed_count} files removed")


def it_contains_any(this: str, has_any: List[str]) -> bool:
    for s in has_any:
        if s in this:
            return True

    return False


def main():
    filter_files_for_time_or_size()
    filter_files_for_error_type(keep=[
        "incompatible types"
    ])


if __name__ == "__main__":
    main()
