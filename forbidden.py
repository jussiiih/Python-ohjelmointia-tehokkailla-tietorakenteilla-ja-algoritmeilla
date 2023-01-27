#TEHTÄVÄNANTO
#Tehtäväsi on laskea, moniko merkkijonon osajono ei sisällä kiellettyä merkkiä. Syötteenä sinulle annetaan merkkijono ja merkki, jota osajonot eivät saa sisältää.
#Voit olettaa, että merkkijono muodostuu merkeistä a–z, siinä on enintään 105 merkkiä ja kielletty merkki on jokin merkeistä a–z.
#Tavoitteena on, että algoritmin aikavaativuus on O(n).
#Toteuta tiedostoon forbidden.py funktio count, joka palauttaa halutun tuloksen.

def count(s, c):
    pituus = 0
    laskuri = 0
    for kirjain in s:
        if kirjain != c:
            pituus +=1
            laskuri += pituus
        else:
            pituus = 0

    return laskuri

       


if __name__ == "__main__":
    print(count("abacabb", "b")) # 7
    print(count("abcdef", "g")) # 21
    print(count("xxxxxxxxx", "x")) # 0
    print(count("pupujussikainen", "u")) # 48
