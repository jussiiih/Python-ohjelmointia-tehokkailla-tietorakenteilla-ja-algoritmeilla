def find(t, x):
    t.sort()

    for i in range (0, len(t)-1):
        laskuri = 1
        j = i + 1
        k= i - 1
        while t[j]- t[i] <=x and j <= len(t)-1 and i <=len(t)-2:
            laskuri +=1
            j += 1
        while i > 0 and t[i] - t[k] <=x:
            laskuri +=1
            k -= 1
        maksimi = max(maksimi, laskuri)

    return maksimi
            
if __name__ == "__main__":
    print(find([10, 10, 10, 10], 0)) # 4
    #print(find([4, 2, 7, 1], 0)) # 1
    print(find([7, 3, 1, 5, 2], 2)) # 3
    print(find([7, 3, 1, 5, 2], 1000)) # 5
    print(find([19, 4, 7, 17, 3, 15, 10], 5)) # 3
    #print(find([10000, 987654, 123456, 139562, 13613225], 50000)) # 2