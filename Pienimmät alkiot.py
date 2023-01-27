#TEHTÄVÄNANTO
#Toteuta testi, jossa syötteenä on n-kokoinen lista lukuja ja halutaan laskea listan n/10 pienimmän alkion summa.
#Toteuta ensin algoritmi 1, joka järjestää listan ja laskee sitten n/10 ensimmäisen luvun summan.
#Toteuta sitten algoritmi 2, joka lisää ensin luvut kekoon ja hakee sieltä sitten summaan n/10 pienintä lukua.
#Toteuta testi niin, että n=106 ja jokainen luku on arvottu satunnaisesti väliltä 1…109.

from heapq import heappush, heappop
import time
import random

n = 10**6

summa1 = 0
summa2 = 0

alku1 = time.time()
lista = []
for i in range(1, n+1):
    lista.append(random.randint(1, 10**9))
lista.sort()

for i in range(0, n//10):
    summa1 += lista[i]

loppu1 = time.time()

print(f" Summa on {summa1}")
print(f"Aikaa kului {loppu1 - alku1} sekuntia")

alku2 = time.time()
keko = []
for i in range(1, n+1):
    heappush(keko, random.randint(1, 10**9))

for i in range(0, n//10):
    summa2 += keko[i]
loppu2 = time.time()

print(f" Summa on {summa2}")
print(f"Aikaa kului {loppu2 - alku2} sekuntia")




