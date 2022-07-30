from Komutlar import*

name = input("Adınızı giriniz: ")
konus('Geldim'+name)
konus('Ne yapmak istiyorsun?')

while (True):

    ses = rec().lower()
    print(ses)
    ans(ses)
    cevap(ses)
