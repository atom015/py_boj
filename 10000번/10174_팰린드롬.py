for i in range(int(input())):
    n = input().upper()
    if n == n[::-1]:
        print("Yes")
    else:
        print("No")
