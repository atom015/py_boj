n = int(input())
if n % 2 == 0:
    print("I LOVE CBNU")
else:
    mid_s = 1
    front_s = n//2
    print("*"*n)
    print(" "*front_s+"*")
    front_s -= 1
    while mid_s+2 <= n:
        print((" "*front_s)+"*"+(" "*mid_s)+"*")
        mid_s += 2
        front_s -= 1
