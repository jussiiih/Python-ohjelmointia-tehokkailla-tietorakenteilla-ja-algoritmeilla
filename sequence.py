#TEHTÄVÄNANTO
#Lukujonon jokainen alkio on pienin positiivinen kokonaisluku, jota ei ole vielä esiintynyt lukujonossa ja jossa on yksi tai useampi toistuva numero.
#Lukujono alkaa näin: 11,22,33,44,55,66,77,88,99,100,101,110,111,112,113,114,…
#Tehtäväsi on etsiä lukujonon kohdassa n oleva luku. Voit olettaa, että n on enintään 1000.
#Toteuta tiedostoon sequence.py funktio generate, joka palauttaa halutun lukujonon alkion.

def generate(n):
    lista =[]
    numerot = ["0", "1","2","3","4","5","6","7","8","9"]
    
    for alkio1 in numerot:
            for alkio2 in numerot:
                    if alkio1 == alkio2 and alkio1 != "0":
                        sallittu = (alkio1+alkio2)
                        lista.append(int(sallittu))
    
    
    for alkio1 in numerot:
        for alkio2 in numerot:
            for alkio3 in numerot:
                if alkio1 == alkio2 or alkio2 == alkio3 or alkio1 == alkio3:
                    if alkio1 != "0":
                        sallittu = (alkio1+alkio2+alkio3)
                        lista.append(int(sallittu))

    for alkio1 in numerot:
        for alkio2 in numerot:
            for alkio3 in numerot:
                for alkio4 in numerot:
                    if alkio1 == alkio2 or alkio2 == alkio3 or alkio1 == alkio3 or alkio1 == alkio4 or alkio2 == alkio4 or alkio3 == alkio4:
                        if alkio1 != "0":
                            sallittu = (alkio1+alkio2+alkio3+alkio4)
                            lista.append(int(sallittu))
    return lista[n-1]
                


if __name__ == "__main__":
    print(generate(1000)) # 11
    #print(generate(2)) # 22
    #print(generate(3)) # 33
    #print(generate(10)) # 100
    #print(generate(123)) # 505
