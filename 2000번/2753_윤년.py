n = int(input())
def compare(n):
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        return 1
    return 0
print(compare(n))
