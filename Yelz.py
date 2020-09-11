import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

# Open file
audio_open = input("Enter path and filename: ")
song = AudioSegment.from_wav(audio_open + ".wav")

# Slicing audiofile
audio_slice = split_on_silence(song, min_silence_len=800, silence_thresh=-18)
print(len(audio_slice))

# Saving audiofile
file_sl = int (input("Enter number file: "))
one_file = audio_slice[file_sl]
one_file.export("one.wav", format="wav")

# Recognized Audiofile
rec = sr.Recognizer()
one_reco = sr.AudioFile(audio_open + ".wav")
with one_reco as source:
    audio = rec.record(source)
try:
    rec_text = rec.recognize_google(audio, language="ru-RU")
    print(rec_text)
except sr.UnknownValueError:
    print("File no recognition")
