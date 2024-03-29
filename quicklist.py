#TEHTÄVÄNANTO
#Tehtäväsi on toteuttaa oma tehokas lista-tietorakenne, joka tarjoaa seuraavat toiminnot:
#Poista listalta listan k ensimmäistä alkiota ja siirrä ne samassa järjestyksessä listan loppuun
#Ilmoita, mikä alkio listalta löytyy indeksiltä i

#Tietorakenteen jokaisen operaation tulee olla O(1)-aikainen. Voit olettaa, että jokainen alkio on kokonaisluku väliltä 1…109.
#Toteuta tiedostoon quicklist.py luokka QuickList seuraavan mallin mukaisesti.

class QuickList:
    def __init__(self, t):
        self.t = t
        self.laskuri = 0
 
    def move(self, k):
        k = k % len(self.t)
        self.laskuri += k
 
    def get(self, i):
        indeksi = i + self.laskuri
        indeksi = indeksi % len(self.t)
        return self.t[indeksi]
 
if __name__ == "__main__":
    q = QuickList([1,2,3,4,5,6,7,8,9,10])
    print(q.get(4)) # 5
    q.move(3)
    print(q.get(4)) # 8
    q.move(3)
    print(q.get(4)) # 1
    q.move(10)
    print(q.get(4)) # 1
    q.move(7)
    q.move(5)
    print(q.get(0)) # 9
    q = QuickList(list(range(1, 10**5 + 1)))
    for i in range(10**5 - 1):
       q.move(10**5 - 1)
    print(q.get(10**4))
    print(q.get(0))
    q = QuickList(list(range(1, 10**5 + 1)))
    for i in range(5*10**4):
        q.move(2*i + 1)
        print(q.get(10**5 - 1 - i))
