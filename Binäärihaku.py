from collections import namedtuple
import random

n = 10**5
lista = []
for i in range (1, n+1):
    lista.append(i)
random.shuffle(lista)

laskuri = 0
maksimi = -1

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def lisaa (self, alkio):
        global maksimi
        global laskuri
        
        if self.value is None:
            self.value = alkio
            maksimi = max(maksimi, laskuri)
            laskuri = 0
        else:
            if alkio < self.value:
                if self.left is None:
                    self.left = Node(alkio)
                    laskuri +=1
                    maksimi = max(maksimi, laskuri)
                    laskuri = 0
                else:
                    self.left.lisaa(alkio)
                    laskuri +=1
            
            elif alkio > self.value:
                if self.right is None:
                    self.right = Node(alkio)
                    self.left = Node(alkio)
                    laskuri +=1
                    maksimi = max(maksimi, laskuri)
                    laskuri = 0
                else:
                    self.right.lisaa(alkio)
                    laskuri +=1



root = Node(lista[0])
lista.pop(0)
for alkio in lista:
    root.lisaa(alkio)

print(maksimi)