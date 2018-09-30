import time
from gtts import gTTS
#from pygame import mixer
import tempfile
import wave
from pydub import AudioSegment
import pyaudio

def speak(sentence, lang, loops=1):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts=gTTS(text=sentence, lang=lang)
        tts.save('{}.mp3'.format(fp.name))
        #mixer.init()
        #mixer.music.load('{}.mp3'.format(fp.name))
        #mixer.music.play(loops)
        #while mixer.music.get_busy()==True:
        #    time.sleep(1)
        #mp3 to wav
        AudioSegment.from_mp3(("{}.mp3".format(fp.name))).export(("{}.wav".format(fp.name)), format="wav")

        #play wav
        chunk=1024
        file =("{}.wav".format(fp.name))
        print(file)
        f = wave.open(file,"rb")
        p = pyaudio.PyAudio()
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),
                rate = f.getframerate(),
                output = True)
        data = f.readframes(chunk)
        #while len(data)>0:
        #while data != "":
        while True:
            stream.write(data)
            data = f.readframes(chunk)
        #stream.stop_stream()
        stream.close()
        p.terminate()
        #end
