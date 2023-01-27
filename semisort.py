def solve(t):
    laskuri = 0
    i=0
    plus = len(t)-1
    while i != len(t)/2:
            if t[i]> (len(t)/2) and t[i+1]<= (len(t)/2):
                t[i], t[i+1] = t[i+1], t[i]
                laskuri +=1
                i += plus
                plus -= len(t)+1

        suurinpienista = 1
        pieninsuurista = 10**5
        if len(t)== 2 and t[0]< t[1]:
            break
        else:
            for k in range(0, int(len(t)/2)):
                suurinpienista = max(suurinpienista, t[k])

            for k in range(int(len(t)/2), len(t)):
                pieninsuurista =min(pieninsuurista, t[k])

        if suurinpienista < pieninsuurista:
            break
    
    return laskuri

if __name__ == "__main__":
    print(solve([2, 1, 4, 3])) # 0
    print(solve([5, 3, 4, 1, 6, 2])) # 6
    print(solve([6, 5, 4, 3, 2, 1])) # 9
    print(solve([10, 1, 9, 2, 8, 3, 7, 4, 6, 5])) # 15