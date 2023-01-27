#TEHTÄVÄNANTO
#Toteuta kurssikirjan luvussa 2.1.4 kuvattu tehokkuustesti omalla koneellasi. Toteuta algoritmit Pythonilla ja mittaa niiden suoritusaika, kun n=105.
#Käytä testissä satunnaista syötettä, jossa jokaisessa kohdassa merkin 0 ja 1 todennäköisyys tulla valituksi on yhtä suuri.

import time
import random

#muodostetaan merkkijono nollia ja ykkösiä
merkit = ""
lista =("0", "1")
for i in range (0, 10**5):
    uusimerkki = random.choice(lista)
    merkit += uusimerkki
n= len(merkit)


#O(n^2)
alku = time.time()
laskuri = 0
for i in range (0, n-1):
    for j in range (i+1, n):
        if merkit[i] == "0" and merkit[j] == "1":
            laskuri += 1
print(laskuri)
loppu = time.time()
print("aikaa kului", loppu-alku, "s")

#O(n)
alku = time.time()
laskuri2 = 0
nollat = 0
for i in range (0, n):
    if merkit[i] == "0":
        nollat += 1
    else:
        laskuri2 += nollat
print(laskuri2)
loppu = time.time()
print("aikaa kului", loppu-alku, "s")
