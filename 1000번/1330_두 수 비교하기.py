a,b = map(int,input().split())
def compare(a,b):
    if a < b:
        return '<'
    elif a > b:
        return ">"
    return "=="
print(compare(a,b))
