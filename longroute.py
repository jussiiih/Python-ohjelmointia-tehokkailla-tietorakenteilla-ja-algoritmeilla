def count(s, k):
    x = 0
    y = 0
    s = k*s
    joukko1 = set()
    joukko2 = set()
    joukko1.add((0,0))
    for merkki in s:
        if merkki == "R":
            x += 1
        elif merkki == "L":
            x -= 1
        elif merkki == "U":
            y += 1
        elif merkki == "D":
            y -= 1
        koordinaatti = (x, y)
        joukko1.add(koordinaatti)
    
    joukko2.add(koordinaatti)
    for merkki in s:
        if merkki == "R":
            x += 1
        elif merkki == "L":
            x -= 1
        elif merkki == "U":
            y += 1
        elif merkki == "D":
            y -= 1
        koordinaatti = (x, y)
        joukko2.add(koordinaatti)

        koko1 = len(joukko1)
        koko2 = len(joukko2)
        yhteensa = joukko1.union(joukko2)
        yhteiskoko = len(yhteensa)
        uusia = koko1 -(koko1+koko2-yhteiskoko)

    
    return koko1 + (k-1)*uusia
    #if koordinaatti == (0,0):
    
    #    return len(joukko1)
        


if __name__ == "__main__":
    print(count("UR", 100)) # 201
    print(count("UD", 100)) # 2
    print(count("UURRDDL", 500)) # 1506
    #print(count("L", 10**9)) # 1000000001
    print(count("DLUR", 10**9)) # 4