#TEHTÄVÄNANTO
#Annettuna on lista, josta tulee poimia mahdollisimman monta lukua. Ensimmäinen luku saa olla mikä tahansa listan luku
#ja tämän jälkeen seuraavan poimitun luvun tulee olla tasan yhden suurempi kuin edellinen. Kuinka monta lukua voidaan näin korkeintaan poimia?
#Voit olettaa, että listalla on enintään 105 lukua ja että jokainen luku on väliltä 1…109. Tavoitteena on, että algoritmin aikavaativuus on O(n)tai O(nlogn).
#Toteuta tiedostoon interval.py funktio count, joka ilmoittaa, montako lukua listalta voidaan enintään poimia halutulla tavalla.

def count(t):
    t.sort()
    t = list(dict.fromkeys(t))
    laskuri = 1
    maksimi =1
    for i in range (0, len(t)-1):
        if t[i+1] - t[i] == 1:
            laskuri += 1
        else:
            if laskuri > maksimi:
                maksimi = laskuri 
            laskuri = 1
    if laskuri > maksimi:
        maksimi = laskuri 
    
    return maksimi


if __name__ == "__main__":
    print(count([1, 1, 1, 1])) # 1
    print(count([10, 4, 8])) # 1
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    print(count([987654, 12345678, 987653, 999999, 987655])) # 3
