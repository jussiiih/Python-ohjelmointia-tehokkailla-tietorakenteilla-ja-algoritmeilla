import random
import time

taulu = []
n = 10
for i in range (1, n+1):
    taulu.append(i)
random.shuffle(taulu)

#tulostetaan taulu, jotta nähdään, että se on sekaisin
print(taulu)


def jarjesta(a, b):  
    if a == b:
        return
    k = (a+b)/2
    jarjesta(a,k)
    jarjesta(k+1,b)
    lomita(a,k,k+1,b)

    def lomita (a1, b1, a2, b2):
        a = a1, b = b2
        apu = []
        for i in range(a, b+1):
            if a2 > b2 or (a1 <= b1 and taulu[a1] <= taulu[a2]):
                apu[i] = taulu[a1]
                a1 += 1
            else:
                apu[i] = taulu[a2]
                a2 += 1
        for i in range(a, b+1):
            taulu[i] = apu[i]


if __name__ == "__main__":
    print(jarjesta(taulu))