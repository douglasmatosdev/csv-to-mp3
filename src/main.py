from gtts import gTTS
import re
import os
import csv

FILE_NAME_SIZE = 30

COLUMN_EN = "English"

INPUT_FILE = "input.csv"

os.system("rm -rf ./audios/*")

with open(INPUT_FILE, newline="") as csvfile:
    file = csv.DictReader(csvfile)
    for col in file:
        text_en = col[COLUMN_EN]

        file_name = text_en[:FILE_NAME_SIZE].strip().lower()
        file_name = re.sub(r"(\,|\.|\"|\'|\-|\_)", "", file_name)
        file_name = file_name.replace(" ", "_")

        audio = gTTS(text=text_en, lang="en", slow=False)
        audio.save(f"audios/{file_name}.mp3")
