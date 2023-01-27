#TEHTÄVÄNANTO
#Tehtäväsi on laskea, montako lehteä on annetussa binääripuussa. Voit olettaa, että puussa on enintään 100 solmua.
#Tehtäväpohjassa on esimerkkinä seuraava puu, jossa on kaksi lehteä:
#Toteuta tiedostoon leaves.py funktio count, joka palauttaa lehtien määrän.

from collections import namedtuple

def count(node):
    if node is None:
        return 0 
    if node.left is None and node.right is None:
        return 1 
    else:
        return count(node.left) + count(node.right)

if __name__ == "__main__":
    Node = namedtuple("Node",["left","right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree)) # 2
