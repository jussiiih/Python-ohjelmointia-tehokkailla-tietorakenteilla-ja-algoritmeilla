from collections import deque

def solve(s):
 
    l = list(s) 
    n = len(l) 
    i = 0
    edellinen_indeksi = 0
 
    while i < n:
        if i+1 < n:
            if l[i] == l[i+1]:
                edellinen_indeksi = i-1
                k = ord(l[i])
                uusi = chr(k+1)
                if uusi == chr(123):
                    uusi =  chr(97)
                l.pop(i)
                l[i] = uusi
                n = len(l)
                i = edellinen_indeksi
                if i < 0:
                    i = 0
            else:
                i += 1
                if i == n:
                    break
        else:
            break 
 
    sana = ""
    return (sana.join(l))
 

if __name__ == "__main__":
    #s = 'zq'*10**4 + 'ee'*10**4 + 'bb'*10**4 + 'yy'*10**4 + 'nn'*10**4
    #print(solve(s))
    #s = 'a' * 10**5
    #print(solve(s))
    #print(solve("outo"))
    #print(solve("nnnnoop"))
    #print(solve("zaaazzzaaz"))
    print(solve("aazxawww"))  # bzxaxw mutta oli bzxawx
    print(solve("auto"))  # auto
    print(solve("ddqqirr"))  # eris
    print(solve("aaaaaa"))  # cb
    print(solve("wsstuva"))  # xa
    print(solve("zzzzzzzz"))  # c
    print(solve("mlkjihgfedcbb"))  # n
    print(solve("kkkjjiikjkjiikjjiijkjji"))  # mjkjmlki