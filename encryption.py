#TERHTÄVÄNANTO
#Tehtäväsi on salata annettu merkkijono niin, että ensimmäinen merkki liikkuu aakkosissa yhden merkin eteenpäin,
#toinen merkki kaksi merkkiä eteenpäin, kolmas merkki kolme merkkiä eteenpäin, jne. Jos merkki kasvaa suuremmaksi kuin z, se palaa taas aakkosten alkuun.
#Merkkijono muodostuu merkeistä a–z ja siinä on enintään 100 merkkiä.
#Toteuta tiedostoon encryption.py funktio encrypt, joka tuottaa salatun merkkijonon.

def encrypt(s):
   tulos = ""
   indeksi = 1
   aakkoset = "abcdefghijklmnopqrstuvwxyz"
   for kirjain in s:
      kirjainindeksi = aakkoset.index(kirjain)
      uusiindeksi = kirjainindeksi+indeksi
      while  uusiindeksi > 25:
         uusiindeksi -=26
      tulos +=aakkoset[uusiindeksi]
      indeksi+=1
   return tulos


if __name__ == "__main__":
    print(encrypt("abc")) # bdf
    print(encrypt("xz")) # yb
    print(encrypt("kkkkkkkk")) # lmnopqrs
    print(encrypt("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")) # bcdefghijklmnopqrstuvwxyzabcde
