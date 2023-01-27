def count(t):
    t.sort()
    t = list(dict.fromkeys(t))
    laskuri = 1
    maksimi =1
    for i in range (0, len(t)-1):
        if t[i+1] - t[i] == 1:
            laskuri += 1
        else:
            if laskuri > maksimi:
                maksimi = laskuri 
            laskuri = 1
    if laskuri > maksimi:
        maksimi = laskuri 
    
    return maksimi


if __name__ == "__main__":
    print(count([1, 1, 1, 1])) # 1
    print(count([10, 4, 8])) # 1
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    print(count([987654, 12345678, 987653, 999999, 987655])) # 3