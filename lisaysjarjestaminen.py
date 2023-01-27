#TEHTÄVÄNANTO
#Toteuta kurssikirjan luvussa 3.1.1 kuvattu lisäysjärjestäminen Pythonilla. Mittaa algoritmin suoritusaika, kun n=105 ja syöte sisältää satunnaisessa järjestyksessä luvut 1,2,…,n.
#Varmista, että algoritmin suorituksen jälkeen syöte on tosiaan järjestyksessä, mutta älä ota tätä mukaan suoritusajan mittaukseen.

import random
import time

taulu = []
n = 10**5
for i in range (1, n+1):
    taulu.append(i)
random.shuffle(taulu)

#tulostetaan taulu, jotta nähdään, että se on sekaisin
print(taulu)

alku = time.time()
for i in range (1, n):
    j = i-1
    while j >= 0 and taulu[j] > taulu[j+1]:
        taulu[j],taulu[j+1] = taulu[j+1],taulu[j]
        j -= 1
loppu = time.time()

print (taulu)
print("Aikaa kului", loppu-alku, "sekuntia.")
