def count(s):
    pituus=1
    laskuri = 0
    for i in range (0, len(s)):
        if i < len(s)-1:
            if s[i]==s[i+1]:
                laskuri += pituus
                pituus +=1
            else:
                laskuri += pituus
                pituus = 1
        elif i == len(s)-1:
            if s[i]==s[i-1]:
                laskuri += pituus
            else:
                laskuri += 1

    
    return laskuri


if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5
