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