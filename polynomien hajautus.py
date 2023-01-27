def hajautus (mjono):
    tulos = 0
    kerroin = len(mjono)-1
    for kirjain in mjono:
        tulos += (19**kerroin)*ord(kirjain)
        kerroin -= 1
    
    return tulos%(10**6)

print(hajautus("maanantai"))
print(hajautus("tiistai"))
print(hajautus("keskiviikko"))
print(hajautus("torstai"))
print(hajautus("perjantai"))
print(hajautus("lauantai"))
print(hajautus("sunnuntai"))
