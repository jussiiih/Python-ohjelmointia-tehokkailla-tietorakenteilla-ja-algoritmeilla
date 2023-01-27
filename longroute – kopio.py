def count(s, k):
    x = 0
    y = 0

    joukko = set()
    lista = []
    joukko.add((0,0))
    for i in range (0, k):
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
            joukko.add(koordinaatti)
        if koordinaatti == (0,0):
            return len(joukko)

    return len(joukko)


if __name__ == "__main__":
    print(count("UR", 100)) # 201
    print(count("UD", 100)) # 2
    print(count("UURRDDL", 500)) # 1506
    #print(count("L", 10**9)) # 1000000001
    print(count("DLUR", 10**9)) # 4