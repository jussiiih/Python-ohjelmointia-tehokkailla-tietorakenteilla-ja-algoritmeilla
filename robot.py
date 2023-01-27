def count(s):
    x = 0
    y = 0

    joukko = set()
    joukko.add((0,0))

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

    return len(joukko)


if __name__ == "__main__":
    print(count("LL")) # 3
    print(count("UUDLRR")) # 5
    print(count("UDUDUDU")) # 2