import json
import os

config = {
    "MAX_IMAGE_SIZE": 1000 * 1000000, # 1000 Megabytes
    "MAX_IMAGE_TIME": 60 * 1000, # 1 Minute,
}

files_to_remove = []

with open("./repository/RQData/image-execution-times.json") as f:
    execution_times = json.load(f)

for key in execution_times:
    if execution_times[key]['breakingImageTime'] > config["MAX_IMAGE_TIME"]:
        files_to_remove.append(key)
    elif execution_times[key]['breakingImageSize'] > config["MAX_IMAGE_SIZE"]:
        files_to_remove.append(key)

print(f"we should remove {len(files_to_remove)} files for time or size constraints")