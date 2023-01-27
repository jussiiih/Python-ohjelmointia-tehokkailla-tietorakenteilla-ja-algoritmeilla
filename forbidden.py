def count(s, c):
    pituus = 0
    laskuri = 0
    for kirjain in s:
        if kirjain != c:
            pituus +=1
            laskuri += pituus
        else:
            pituus = 0

    return laskuri

       


if __name__ == "__main__":
    print(count("abacabb", "b")) # 7
    print(count("abcdef", "g")) # 21
    print(count("xxxxxxxxx", "x")) # 0
    print(count("pupujussikainen", "u")) # 48