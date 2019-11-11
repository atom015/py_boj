def check_anagrams(n,m):
    if len(n) != len(m):return "{} & {} are NOT anagrams.".format(n,m)
    if sorted(list(n)) == sorted(list(m)):
        return "{} & {} are anagrams.".format(n,m)
    return "{} & {} are NOT anagrams.".format(n,m)
for i in range(int(input())):
    n,m = input().split()
    print(check_anagrams(n,m))