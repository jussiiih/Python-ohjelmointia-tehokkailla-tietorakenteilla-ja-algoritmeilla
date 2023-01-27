def find(t, k):
    t.sort()
    maksimi = 0
    for i in range (0, len(t)-1):
        if (t[i+1]+t[i])//2 - t[i] >maksimi: 
            maksimi = (t[i+1]+t[i])//2 - t[i]
    return max(t[0] - 1, maksimi, k - t[len(t)-1])


if __name__ == "__main__":
    print(find([1, 2, 9], 11)) # 3
    print(find([2, 1, 3], 3)) # 0
    print(find([7, 4, 10, 4], 10)) # 3
    print(find([15, 2, 6, 4, 18], 20)) # 4
    print(find([41222388, 392676742, 307110407, 775934683, 25076911], 809136843)) # 191628970