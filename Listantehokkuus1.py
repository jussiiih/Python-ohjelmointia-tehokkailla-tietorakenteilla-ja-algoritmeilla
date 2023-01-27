import time

lista = []
n = 10**5

alku1 = time.time()
for i in range (1, n+1):
    lista.append(i)
loppu1 = time.time()

print(f"Lisäämiseen meni aikaa {loppu1 - alku1} sekuntia")

alku2 = time.time()
for i in range (1, n+1):
    lista.pop(0)
loppu2 = time.time()

print(f"Poistamiseen meni aikaa {loppu2 - alku2} sekuntia")