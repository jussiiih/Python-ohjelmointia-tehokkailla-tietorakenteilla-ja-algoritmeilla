from heapq import heappush, heapify, heappop

def smallest(n):
    
    keko = [1]
    heapify(keko)
    for i in range (1, n+1):
        pienin = heappop(keko)
        heappush(keko, 2*pienin)
        heappush(keko, 3*pienin)
    
    return heappop(keko)


if __name__ == "__main__":
    print(smallest(1)) # 2
    print(smallest(5)) # 6
    print(smallest(123)) # 288
    print(smallest(55555)) # 663552