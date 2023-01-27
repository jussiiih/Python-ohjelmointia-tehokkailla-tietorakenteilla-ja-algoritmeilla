#TEHTÄVÄNANTO
#Sinulle annetaan lukuja yksi kerrallaan. Tehtäväsi on kertoa jokaisen luvun kohdalla, mikä on siihen mennessä annettujen
#lukujen mex-luku eli pienin puuttuva epänegatiivinen luku.
#Voit olettaa, että jokainen luku on kokonaisluku välillä 0…109 ja lukuja annetaan enintään 105.
#Toteuta tiedostoon mex.py luokka Mex, jonka funktio add lisää uuden luvun ja palauttaa lisättyjen lukujen mex-luvun.

class Mex:
    def __init__(self):
        self.joukko = set()
        self.pienin = 0

    def add(self, x):
        self.joukko.add(x)
        while True:
            if self.pienin in self.joukko:
                self.pienin += 1
            else:
                return self.pienin

        
    

if __name__ == "__main__":
    m = Mex()
    print(m.add(1)) # 0
    print(m.add(3)) # 0
    print(m.add(4)) # 0
    print(m.add(0)) # 2
    print(m.add(5)) # 2
    print(m.add(2)) # 6
