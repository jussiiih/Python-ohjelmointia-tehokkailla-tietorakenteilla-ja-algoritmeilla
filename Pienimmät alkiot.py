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




