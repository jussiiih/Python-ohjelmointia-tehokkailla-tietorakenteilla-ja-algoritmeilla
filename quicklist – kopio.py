from collections import deque

class QuickList:
    def __init__(self, t):
        lista = deque()
        for i in range (0, len(t)):
            lista.append(t[i])
        t =lista
        self.t = t

    def move(self, k):
        for i in range(0, k):
            self.t[0]=self.t[-1]
            self.t.popleft()
            #otettu = self.t.popleft()
            #self.t.append(otettu)

    def get(self, i):
        if i == 0:
            return self.t[0]
        else:
            tulos = 0
            for k in range(0, len(self.t)):
                siirra = self.t.popleft()
                if k == i-1:
                    tulos = self.t[0]
                self.t.append(siirra)
        
        return tulos

if __name__ == "__main__":
    q = QuickList([1,2,3,4,5,6,7,8,9,10])
    print(q.get(4)) # 5
    q.move(3)
    print(q.get(4)) # 8
    q.move(3)
    print(q.get(4)) # 1
    q.move(10)
    print(q.get(4)) # 1
    q.move(7)
    q.move(5)
    print(q.get(0)) # 9
    #q = QuickList(list(range(1, 10**5 + 1)))
    #for i in range(10**5 - 1):
     #   q.move(10**5 - 1)
    #print(q.get(10**4))