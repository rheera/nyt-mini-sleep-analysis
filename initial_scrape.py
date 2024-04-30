import csv
import datetime
import os
import re
from datetime import datetime

import cv2
import moviepy
import numpy as np
import pytesseract
import skimage
from moviepy.editor import VideoFileClip
from PIL import Image
from skimage.metrics import structural_similarity as ssim

dates = []


def extract_frames(video_path, output_dir, interval):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    video_clip = VideoFileClip(video_path)
    video_duration = video_clip.duration * 1000
    # Convert to seconds

    # Open the video file
    # cap = cv2.VideoCapture(video_path)

    cur_time = 0
    saved_dates = []
    prev_date = datetime.strptime("Jan 1, 1900", "%b %d, %Y")
    frames = []
    while cur_time < video_duration:
        frame = video_clip.get_frame(cur_time / 1000)
        # fstr = str(hash(frame))
        # filename = f"frame_{cur_time}.jpg"
        # frame_paths.append(filename)
        # cur_date = find_date_and_pos(frame)[0]
        # print(cur_date)
        # if cur_date != prev_date:
        #     saved_dates.append(cur_date)
        #     prev_date = cur_date
        cur_time += interval
        # cur_frame = parse_image(frame)
        # frames.append(cur_frame)
        parse_image(frame)

    lsf = len(saved_dates)
    print(f"Added {lsf} dates")

    # Release the video capture object
    # cap.release()
    video_clip.close()
    return frames


def parse_image(frame):
    input_text = pytesseract.image_to_string(Image.fromarray(frame))
    score_pattern = ".+\s\d\d:\d\d"
    date_pattern = r"(?:Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday), (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}, \d{4}"
    score_result = re.findall(score_pattern, input_text)
    date_result = (
        re.search(date_pattern, input_text).group()
        if re.search(date_pattern, input_text)
        else ""
    )
    score_rows = []
    for score in score_result:
        score_split = score.split(" ")
        if len(score_split) < 3:
            print(score_split)
        else:
            # score_rows.append(f"{score_split[0]}\t{score_split[1]}\t{score_split[2]}\t{date_result}")
            score_rows.append(
                {
                    "rank": score_split[0],
                    "user": score_split[1],
                    "time": score_split[2],
                    "date": date_result,
                }
            )

    tsv_filename = "output.tsv"

    with open(tsv_filename, "a", newline="") as output_file:
        tsv_writer = csv.writer(output_file, delimiter="\t")
        for row in score_rows:
            tsv_writer.writerow(
                [row["rank"], row["user"], row["time"], row["date"]]
            )  # Write each data row


def find_date_and_pos(frame):
    # Define the date pattern
    input_text = pytesseract.image_to_string(Image.fromarray(frame))
    print(input_text)

    # date_pattern = re.compile(r'\b(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday), \w{3} \d{1,2}, \d{4}\b')
    date_pattern = re.compile(r"\b\w{3} \d{1,2}, \d{4}\b")
    # Find all matches in the input text
    matches = [
        (match.group(), match.end()) for match in date_pattern.finditer(input_text)
    ]

    # Convert matched strings to datetime objects (optional)
    date_objects = [datetime.strptime(match[0], "%b %d, %Y") for match in matches]

    return date_objects[0], matches[0][1]


def parse_chat_string(input_string):
    # Find lines with usernames and times
    lines = [line.strip() for line in input_string.split("\n") if ":" in line]

    # Parse each line into a tuple (username, time)
    result = []
    for line in lines:
        parts = line.split()

        # Extract the rank and username
        rank = parts[0]
        username = " ".join(parts[1:-1])

        # Remove non-alphanumeric characters and leading rank from the username
        username = re.sub(r"\W+", "", username)
        username = re.sub(r"^\d+", "", username)

        time_str = parts[-1]
        minutes, seconds = map(int, time_str.split(":"))
        total_seconds = minutes * 60 + seconds

        result.append((username, total_seconds))

    return result


# if __name__ == "__main__":
#     video_path = "mini_stats.mp4"
#     output_dir = "output_frames"
#     interval = 350  # milliseconds

extract_frames("mini_stats_auto.mp4", "output_frames", 800)

t = "Switch Control\nInvalid Configuration\nTriple-click the side button to stop Switch Cor\n\nThe Mini\nSunday, Apr 14, 2024 v\n1 bigjoo 00:26\n2 ~=BigBossHog 00:29\n3 rabulrabul 01:02\n4 Ant-man© 02:17\n\nfi ail R\n\nGames Stats Leaderboard\n"
score_pattern = ".+\s\d\d:\d\d"
date_pattern = r"(?:Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday), (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}, \d{4}"
score_result = re.findall(score_pattern, t)
date_result = re.search(date_pattern, t).group()
score_rows = []
for score in score_result:
    score_split = score.split(" ")
    # score_rows.append(f"{score_split[0]}\t{score_split[1]}\t{score_split[2]}\t{date_result}")
    score_rows.append(
        {
            "rank": score_split[0],
            "user": score_split[1],
            "time": score_split[2],
            "date": date_result,
        }
    )

tsv_filename = "output.tsv"

with open(tsv_filename, "a", newline="") as output_file:
    tsv_writer = csv.writer(output_file, delimiter="\t")
    for row in score_rows:
        tsv_writer.writerow(
            [row["rank"], row["user"], row["time"], row["date"]]
        )  # Write each data row
