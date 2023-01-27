#TEHTÄVÄNANTO
#Tehtäväsi on selvittää, kuinka pitkä on lyhin merkkijono, jota toistamalla voidaan muodostaa annettu merkkijono.
#Esimerkiksi kun merkkijono on abcabcabcabc, lyhin toistettava merkkijono on abc.
#Merkkijono muodostuu merkeistä a–z ja siinä on enintään 100 merkkiä.
#Toteuta tiedostoon repeat.py funktio find, joka antaa toistettavan merkkijonon pituuden.

def find(s):
    pituus = len(s)
    indeksi = 0
    kerroin = 1
    while indeksi < pituus:
        mjono= s[0:indeksi]
        while kerroin <=pituus:
            if kerroin * mjono == s:
                return len(mjono)
            else:
                kerroin +=1
        kerroin = 1
        indeksi +=1
    return pituus




if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7
