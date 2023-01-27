#TEHTÄVÄNANTO
#Tehtäväsi on laskea suurin ero vasemman ja oikean alipuun solmujen määrässä jossain binääripuun solmussa. Voit olettaa, että puussa on enintään 100 solmua.
#Tehtäväpohjassa esimerkkinä on seuraava puu:
#Tässä puussa suurin ero on juuressa: vasemmalla on 0
#solmua ja oikealla on 3
#solmua, joten ero on 3.
#Toteuta tiedostoon subtrees.py funktio diff, joka palauttaa suurimman eron.

from collections import namedtuple



#valitaan listalta suurin erotus
def diff (node):
    lista = []
    lapikaynti(node, lista)
    return max(lista)

#käydään läpi kaikki solmut ja viedään ne erotus-funktiolle
def lapikaynti (node, lista):
    if not node:
        return 0
    lapikaynti(node.right, lista)
    erotus(node, lista)
    lapikaynti(node.left, lista)

#lasketaan solmun vasemman ja oikean puolen alasolmujen erotus, ja lisätään listaan
def erotus (node, lista):
    if not node:
        return 0
    oikea = count(node.right)
    vasen = count(node.left)
    lista.append(abs(vasen - oikea))

#lasketaan solmujen määrä edellisessä funktiossa
def count(node):
    if not node:
        return 0
    return count(node.left)+count(node.right)+1


if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree2 = Node(left=None, right=Node(left=Node(left=None, right=None), right=Node(left=None, right=None)))
    print(diff(tree2))
