#TEHTÄVÄNANTO
#Sinulle annetaan kaksi listaa A ja B, joissa molemmissa on lukujen 1…n jokin permutaatio (eli molemmat listat sisältävät luvut 1…n jossain järjestyksessä).
#Tehtäväsi on laskea, moniko luvuista 1…n esiintyy aiemmin listalla A kuin listalla B. Tavoitteena on, että algoritmin aikavaativuus on O(n)
#Toteuta tiedostoon permutations.py funktio count, joka palauttaa halutun tuloksen.

def count(a, b):
    laskuri = 0
    sanakirjaa ={}
    sanakirjab ={}
    for i in range (0, len(a)):
        sanakirjaa[a[i]] = i
        sanakirjab[b[i]] = i
    for i in range (1, len(a)+1):
        if sanakirjaa[i]< sanakirjab[i]:
            laskuri +=1
    return laskuri


if __name__ == "__main__":
    print(count([1,2,3], [1,2,3])) # 0
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5
