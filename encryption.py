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