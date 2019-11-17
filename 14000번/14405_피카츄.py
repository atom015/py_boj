s = list(input())
arr = s+["0" for i in range(5001-len(s))]
def solve():
    ix,ans = 0,0
    while ix < len(s):
        if arr[ix] == "p" and arr[ix+1] == "i":
            ix += 2

        elif arr[ix] == "k" and arr[ix+1] == "a":
            ix += 2

        elif arr[ix] == "c" and arr[ix+1] == "h" and arr[ix+2] == "u":
            ix += 3
        else:
            return "NO"
    return "YES"

print(solve())
