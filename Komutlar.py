import webbrowser
import os
from datetime import datetime
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import random
import sys

r = sr.Recognizer()

def konus(string):
    tts = gTTS(string,lang='tr')
    rand = random.randint(1,10)
    file = 'ses-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)



def rec(ask=False):

    if ask:
        konus(ask)

    with sr.Microphone() as myvoice:

        r.adjust_for_ambient_noise(myvoice, duration=1)
        audio = r.listen(myvoice)

        ses=''
        try:
            ses = r.recognize_google(audio, language="tr-tr")
        except sr.UnknownValueError:
            konus('anlayamadım')
        except sr.RequestError:
            konus('sistemde sorun var galiba')
        return ses


def cevap(ses):

    if 'saat kaç' in ses:
        konus('Saati yazdım')
        print(datetime.now().strftime('%H:%M:%S'))

    elif 'arama yap' in ses:
        search = rec('söyle hemen bulayım şak diye')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        konus(search + 'için bunları buldum!')

    elif 'kapat' in ses:
        konus('hadi kaçtım ben')
        sys.exit()

def ans(ses):
    komutlar = {"merhaba":'merhaba',"nasılsın":'iyidir, sen nasılsın?',"iyiyim":'iyi olmana sevindim'
    ,"aferin sana":'sağol canım'}
    for i,j in komutlar.items():
        if i in ses:
            konus(j)
            break
