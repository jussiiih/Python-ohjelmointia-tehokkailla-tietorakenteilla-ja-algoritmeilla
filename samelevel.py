from collections import namedtuple


def count(node, level):
    sanakirja = {}
    i=1
    mjono = str(node)
    for j in range(0, len(mjono)):
        if mjono[j] == "N" and mjono[j+1] == "o" and mjono[j+2] == "d" and mjono[j+3] == "e":
            if i not in sanakirja:
                sanakirja[i] = 1
            else:
                sanakirja[i] += 1
        if mjono[j] == "(":
            i += 1
        if mjono[j] == ")":
            i -= 1
    if level not in sanakirja:
        return 0
    return sanakirja[level]


    
    return mjono



    #return count(node.left)+count(node.right)


if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree,1)) # 1
    print(count(tree,2)) # 1
    print(count(tree,3)) # 2
    print(count(tree,4)) # 0