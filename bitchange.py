#TEHTÄVÄNANTO
#Bittijonossa on aluksi n bittiä ja jokainen bitti on 0. Sitten bittijonoa muutetaan k kertaa.
#Joka muutoksessa bittijonoa käydään läpi vasemmalta oikealle. Jos bitti on 1, siitä tulee 0 ja läpikäynti jatkuu.
#Jos taas bitti on 0, siitä tulee 1ja läpikäynti päättyy. Millainen bittijono on lopuksi?
#Voit olettaa, että n on välillä 1…20 ja k on välillä 0…1000 . Lisäksi voit olettaa, että k<2n eli joka muutoksessa bittijonossa on ainakin yksi bitti 0
#Toteuta tiedostoon bitchange.py funktio create, joka palauttaa lopullisen bittijonon merkkijonona.

def create(n, k):
    lista = []
    for i in range  (0, n):
        lista.append(0)
    
    for m in range (0, k):
        for j in range (0, len(lista)):
            if lista[j] == 1:
                lista[j] = 0
            elif lista[j] == 0:
                lista[j] = 1
                break

    mjono =""
    for alkio in lista:
        mjono += str(alkio)

    return mjono
    
            
   

if __name__ == "__main__":
    print(create(5, 0)) # 00000
    print(create(5, 1)) # 10000
    print(create(5, 2)) # 01000
    print(create(5, 3)) # 11000
    print(create(5, 4)) # 00100
    print(create(5, 31)) # 11111
