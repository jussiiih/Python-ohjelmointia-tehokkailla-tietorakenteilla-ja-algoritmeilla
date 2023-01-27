from collections import deque

def solve(n,k):
    lista = deque()
    for i in range (1, n+1):
        lista.append(i)

    for i in range (0, k):
        otettu1 = lista.popleft()
        otettu2 = lista.popleft()
        lista.append(otettu2)
        lista.append(otettu1)
    return lista[0]


if __name__ == "__main__":
    print(solve(4,3)) # 4
    print(solve(12,5)) # 11
    print(solve(99,555)) # 11
    print(solve(12345,54321)) # 9875