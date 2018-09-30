import requests
from xml.etree import ElementTree
import os
import tempfile
#from Speak import speak
#from wav import wavplay

def TTS(sentence):
    # 在 header 中附帶 key(金鑰)，並用 post 的方法發送 request
    headers = {'Ocp-Apim-Subscription-Key': '614602375c2a488099fdccacf0181bf0'}
    response = requests.post('https://api.cognitive.microsoft.com/sts/v1.0/issueToken', headers=headers)
    # Status Code 不是 200 就報錯
    if response.status_code != 200:
        print('取得 token 失敗')
        return

    # 取得 token(權杖)
    access_token = response.text
    # header 包含了 request 內容類型的宣吿、輸出音檔的格式、token
    # Bing Speech API 都是使用 SSML(語音合成標記語言) 來表達產生音檔的內容及語音特徵
    headers = {'Content-type': 'application/ssml+xml',
               'X-Microsoft-OutputFormat': 'riff-16khz-16bit-mono-pcm',
               'Authorization': 'Bearer ' + access_token}

    #<speak version="1.0" xml:lang="zh-TW"> <voice xml:lang="zh-TW" name="Microsoft Server Speech Text to Speech Voice (zh-TW, Yating, Apollo)"> </voice> </speak>
    body = ElementTree.Element('speak', version='1.0')
    body.set('xml:lang', 'zh-TW')
    voice = ElementTree.SubElement(body, 'voice')
    voice.set('xml:lang', 'zh-TW')
    voice.set('xml:gender', 'Female')
    voice.set('name', 'Microsoft Server Speech Text to Speech Voice (zh-TW, Yating, Apollo)')

    #傳入欲轉換之文字
    voice.text = sentence

    # 發出請求，由於是下載檔案，所以設置 stream = True
    response = requests.post('https://speech.platform.bing.com/synthesize', data=ElementTree.tostring(body), headers=headers, stream=True)

    # Status Code 不是 200 就報錯
    if response.status_code != 200:
        print('取得音檔失敗')
        return

    # 存檔為暫存wav
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        with open('{}.wav'.format(fp.name), 'wb') as f:
            for chunk in response:
                f.write(chunk)
    sound = '{}.wav'.format(fp.name)
    #print(sound)
    #播放wav
    wavplay(sound)

TTS('123')
