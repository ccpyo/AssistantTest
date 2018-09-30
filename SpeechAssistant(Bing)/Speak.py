import time
from gtts import gTTS
from pygame import mixer
import tempfile

def speak(sound, loops=1):
    print(sound)
    mixer.init()
    mixer.music.load(sound)
    mixer.music.play(loops)
    while mixer.music.get_busy()==True:
        time.sleep(1)
