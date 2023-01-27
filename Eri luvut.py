import time
import random

lista= []
for i in range (0, 10**6):
    lista.append(random.randint(1, 10**9))

alku1 = time.time()
jarjestetty = sorted(lista)
tulos1 = 1
for i in range(0, len(jarjestetty)-1):
    if jarjestetty[i] !=jarjestetty[i+1]:
        tulos1 +=1
loppu1 = time.time()
print(f"Eri alkioita on {tulos1} kappaletta")
print(f"Aikaa kului {loppu1-alku1} sekuntia")


alku2 = time.time()
alkiot = set()
for i in range (0, len(lista)):
    alkiot.add(lista[i])
tulos2 =len(alkiot)
loppu2 = time.time()

print(f"Eri alkioita on {tulos2} kappaletta")
print(f"Aikaa kului {loppu2-alku2} sekuntia")