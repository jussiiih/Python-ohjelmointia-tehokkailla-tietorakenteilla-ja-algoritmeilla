def solve(t):
    laskuri = 0
    while True:
        for i in range (0, int(len(t)/2)):
            if t[i]>len(t)/2 and  t[i+1]<=len(t)/2:
                t[i], t[i+1] = t[i+1], t[i]
                laskuri +=1


        for i in range(len(t)-1, int(len(t)/2)-1, -1):
            if t[i]<=len(t)/2 and t[i-1]>len(t)/2:
                t[i-1], t[i] = t[i], t[i-1]
                laskuri +=1

        pienet = []
        suuret = []
        if len(t)== 2:
            maksimi = t[0]
            minimi = t[1]
        else:
            for k in range(0, int(len(t)/2)):
                pienet.append(t[k])
            maksimi = max(pienet)

            for k in range(int(len(t)/2), len(t)):
                suuret.append(t[k])
            minimi = min(suuret)

        if maksimi < minimi:
            break


    return laskuri

if __name__ == "__main__":
    print(solve([1, 4, 6, 5, 2, 3])) # 6