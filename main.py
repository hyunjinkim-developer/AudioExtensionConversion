import os
from pydub import AudioSegment

# NFD-> NFC(Normalization Form Composition)
# pip install unicodedata2
import unicodedata

EXT = ".mp3"

base_path = os.path.abspath(os.getcwd())

directory = os.listdir("Guitar")
for song in directory:
    song_name_splited = song.split(".")
    song_name, extension = song_name_splited[0].strip(), song_name_splited[1]
    song_name = unicodedata.normalize('NFC', song_name)

    song = f"{song_name}.{extension}" #debug: remove space
    # song = song_name + ".wma"
    print(song)
    if extension == "wma":
        print(song_name)
        wav_audio = AudioSegment.from_file(song, format="wma")

# # wave and raw don’t use ffmpeg

# raw_audio = AudioSegment.from_file("audio.wav", format="raw",
#                                    frame_rate=44100, channels=2, sample_width=2)
#
# wav_audio.export("audio.mp3", format="mp3")
# raw_audio.export("audio1.mp3", format="mp3")