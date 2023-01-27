class Mode:
    def __init__(self):
        self.lista = {}
  
    def add(self, x):
        if x not in self.lista:
            self.lista[x]=1
        else:
            self.lista[x] += 1
        
        if len(self.lista)== 1:
            self.moodi = x
            return self.moodi

        if self.lista[x] > self.lista[self.moodi]:
            self.moodi = x
        if self.lista[x] == self.lista[self.moodi] and x < self.moodi:
            self.moodi = x

        return self.moodi

if __name__ == "__main__":
    m = Mode()
    print(m.add(1)) # 1
    print(m.add(2)) # 1
    print(m.add(2)) # 2
    print(m.add(1)) # 1
    print(m.add(3)) # 1
    print(m.add(3)) # 1
    print(m.add(3)) # 3