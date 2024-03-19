from gtts import gTTS
import os
import csv

with open('english-sentences.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for i, row in enumerate(spamreader):
        text = ' '.join(row)
        
        file_name = text.lower().replace(' ', '_').replace(',', '').replace('.', '').replace('\'', '').replace('"', '').replace('-', '')
        
        audio = gTTS(text=text, lang="en", slow=False)
        audio.save(f'audios/{file_name}.mp3')
