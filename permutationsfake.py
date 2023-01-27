def count(a, b):
    lista = []
    laskuri = 0
    for i in range (0, len(a)):
        lista.append(a[i])
        if b[i] == a[i]:
            continue
        if b[i] in lista:
            laskuri += 1

    return laskuri
            



if __name__ == "__main__":
    print(count([1,2,3], [1,2,3])) # 0
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5