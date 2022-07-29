from Komutlar import *
from komutlar2 import *

name = input("Adınızı giriniz: ")
konus('Geldim'+name)
konus('Ne yapmak istiyorsun?')

while (True):

    ses = rec()
    print(ses)
    response(ses)
