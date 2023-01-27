#TEHTÄVÄNANTO
#Listalla on aluksi kokonaisluku 1. Joka kierroksella poistat listalta pienimmän alkion x ja lisäät listalle alkiot 2x ja 3x.
#Mikä on listan pienin alkio n kierroksen jälkeen? Voit olettaa, että n on enintään 105.
#Esimerkiksi kun n=5, lista muuttuu näin:
#[1]→[2,3]→[3,4,6]→[4,6,6,9]→[6,6,9,8,12]→[6,9,8,12,12,18]
#Tässä tapauksessa listan pienin alkio lopussa on 6.
#Toteuta tiedostoon twothree.py funktio smallest, joka antaa vastauksen.

from heapq import heappush, heapify, heappop

def smallest(n):
    
    keko = [1]
    heapify(keko)
    for i in range (1, n+1):
        pienin = heappop(keko)
        heappush(keko, 2*pienin)
        heappush(keko, 3*pienin)
    
    return heappop(keko)


if __name__ == "__main__":
    print(smallest(1)) # 2
    print(smallest(5)) # 6
    print(smallest(123)) # 288
    print(smallest(55555)) # 663552
