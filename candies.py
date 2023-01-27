#TEHTÄVÄNANTO
#Kaupassa on myytävänä n karkkia, joilla jokaisella on tietty hinta. Montako karkkia voit ostaa enintään, kun sinulla on rahaa x?
#Karkkien määrä on enintään 105, ja jokaisen karkin hinta ja x on välillä 1…109. Tavoitteena on, että algoritmin aikavaativuus on O(n) tai O(nlogn).
#Toteuta tiedostoon candies.py funktio solve, joka ilmoittaa, montako karkkia voit ostaa enintään.

def solve(prices, x):
    prices.sort()
    laskuri = 0
    for i in range (0, len(prices)):
        if x >= prices[i]:
            laskuri += 1
            x -= prices[i]
            if i == len(prices)-1:
                return laskuri
        else:
            return laskuri


if __name__ == "__main__":
    print(solve([1, 1, 1, 1], 2)) # 2
    print(solve([2, 5, 3, 2, 8, 7], 10)) # 3
    print(solve([2, 3, 4, 5], 1)) # 0
    print(solve([2, 3, 4, 5], 10**9)) # 4
    print(solve([10**9, 1, 10**9], 10**6)) # 1
