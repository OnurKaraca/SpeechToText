from gtts import gTTS
from playsound import playsound
import os
import sys
from random import choice


class Komut():
    
    def __init__(self,gelenses):
        self.ses = gelenses.upper()
        self.sesblokları = self.ses.split()
        print(self.sesblokları)
        self.komutlar = ["MERHABA","NASILSIN","TAMAMDIR","KAPAT","ARAMA YAP"]



    def seslendirme(self,yazi):
        tts = gTTS(text=yazi,lang='tr')
        tts.save("ses.mp3")
        playsound("ses.mp3")
        os.remove("ses.remove")
        print(yazi)
    

    def kapat(self):
        self.seslendirme("Kapatıyorum o zaman kendimi, görüşürüz...")
        sys.exit()

    def sohbet(self):
        sozler=["merhaba canım","iyiyim sorduğun için sağol","buralarda yeniyim sen yaz ben öğreniyim"]
        secim = choice(sozler)
        self.seslendirme(secim)
    

    def komutbul(self):
        for komut in self.komutlar:
            if komut in self.sesblokları:
                self.komutcalistir(komut)

    
    def komutcalistir(self,komut):
        if komut=="KAPAT":
            self.kapat()
        if komut== "MERHABA" or komut=="NASILSIN":
            self.sohbet()

    