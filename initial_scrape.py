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


# TODO: if the next frame contains the same date as previously recorded ignore it and move on to the next
def extract_frames(video_path, output_dir, interval):
    video_clip = VideoFileClip(video_path)
    # Convert to seconds
    video_duration = video_clip.duration * 1000

    cur_time = 0
    saved_dates = []
    prev_date = datetime.strptime("Jan 1, 1900", "%b %d, %Y")
    frames = []
    while cur_time < video_duration:
        frame = video_clip.get_frame(cur_time / 1000)
        cur_time += interval
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
            score_rows.append(
                {
                    "rank": score_split[0],
                    "user": score_split[1],
                    "time": score_split[2],
                    "date": date_result,
                }
            )

    # since the date contains commas, I'm writing to a tsv instead of a csv
    tsv_filename = "output.tsv"

    with open(tsv_filename, "a", newline="") as output_file:
        tsv_writer = csv.writer(output_file, delimiter="\t")
        for row in score_rows:
            tsv_writer.writerow(
                [row["rank"], row["user"], row["time"], row["date"]]
            )  # Write each data row
