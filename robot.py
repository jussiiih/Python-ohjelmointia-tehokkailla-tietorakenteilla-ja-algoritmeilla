#TEHTÄVÄNANTO
#Robotti on alussa ruudussa (0,0). Tämän jälkeen robotti liikkuu annetun liikesarjan mukaisesti askeleen kerrallaan.
#Liikesarja muodostuu merkeistä U (up), D (down), L (left) ja R (right). Monessako eri ruudussa robotti käy yhteensä?
#Voit olettaa, että liikesarjassa on enintään 105 komentoa.
#Toteuta tiedostoon robot.py funktio count, jolle annetaan robotin liikesarja ja joka ilmoittaa eri ruutujen määrän.

def count(s):
    x = 0
    y = 0

    joukko = set()
    joukko.add((0,0))

    for merkki in s:
        if merkki == "R":
            x += 1
        elif merkki == "L":
            x -= 1
        elif merkki == "U":
            y += 1
        elif merkki == "D":
            y -= 1
        koordinaatti = (x, y)
        joukko.add(koordinaatti)

    return len(joukko)


if __name__ == "__main__":
    print(count("LL")) # 3
    print(count("UUDLRR")) # 5
    print(count("UDUDUDU")) # 2
