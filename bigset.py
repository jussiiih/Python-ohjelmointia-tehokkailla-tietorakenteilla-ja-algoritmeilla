#TEHTÄVÄNANTO
#Annettuna on lista lukuja ja tehtäväsi on selvittää, montako lukua listalta voidaan valita siten, että minkään kahden valitun luvun erotus ei ole suurempi kuin x.
#Voit olettaa, että listalla on enintään 105 lukua ja x ja jokainen listan luku on väliltä 0…109. Tavoitteena on, että algoritmin aikavaativuus on O(n)tai O(nlogn).
#Toteuta tiedostoon bigset.py funktio find, joka ilmoittaa montako lukua listalta voidaan enintään valita.

def find(t, x):
    t.sort()
    maksimi = 1
    laskuri = 0
    alku = 0
    i = 0
    while i < len(t):
        if t[i] - t[alku] <=x:
            laskuri = i - alku +1
            maksimi = max(maksimi, laskuri)
            i +=1
        else:
            alku +=1

    return maksimi


if __name__ == "__main__":
    print(find([10, 10, 10, 10], 0)) # 4
    print(find([4, 2, 7, 1], 0)) # 1
    print(find([7, 3, 1, 5, 2], 2)) # 3
    print(find([7, 3, 1, 5, 2], 1000)) # 5
    print(find([19, 4, 7, 17, 3, 15, 10], 5)) # 3
    print(find([10000, 987654, 123456, 139562, 13613225], 50000)) # 2
