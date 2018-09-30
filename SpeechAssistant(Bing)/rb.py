
#Course 87
import speech_recognition

def listenTo():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        print("Say something:")
        audio = r.listen(source)

    return r.recognize_google(audio, language='zh-TW')
#Course 88
import tempfile
from gtts import gTTS
from pygame import mixer
mixer.init()

def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang='zh-TW')
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()

#speak('咩修幹謀')

#speak(listenTo())

qa = {
  '你今天好嗎': '我很好',
  '你好美'    : '你也很帥',
  '誰是世界上最帥的人' : '當然是你壓'
}

speak(qa.get(listenTo(), '我現在還在學習, 等我變聰明以後, 我再回答你'))
