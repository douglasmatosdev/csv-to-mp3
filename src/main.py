from gtts import gTTS
import re
import os
import csv

FILE_NAME_SIZE = 30

os.system('rm -r ./audios/*')

with open("english-sentences.csv", newline="") as csvfile:
    file = csv.DictReader(csvfile)
    for col in file:
        text = col['English']
        print(col)

        file_name = text[:FILE_NAME_SIZE].strip().lower()
        file_name = re.sub(r"(\,|\.|\"|\'|\-|\_)", "", file_name)
        file_name = file_name.replace(" ", "_")

        audio = gTTS(text=text, lang="en", slow=False)
        audio.save(f"audios/{file_name}.mp3")
