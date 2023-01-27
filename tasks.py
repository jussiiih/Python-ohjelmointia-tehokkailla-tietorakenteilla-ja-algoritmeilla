from heapq import heappush, heappop

class Tasks:

    def __init__ (self):
        self.keko = []

    def add(self, name, priority):
        heappush(self.keko, (-priority, name))

    def next(self):
        otettu = heappop(self.keko)
        return otettu[1]

if __name__ == "__main__":
    t = Tasks()
    t.add("siivous",10)
    t.add("ulkoilu",50)
    t.add("opiskelu",50)
    print(t.next()) # opiskelu
    t.add("treffit",100)
    print(t.next()) # treffit
    print(t.next()) # ulkoilu