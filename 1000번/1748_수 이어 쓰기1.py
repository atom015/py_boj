def main(n):
    result,i = 0,1
    while i <= n:
        result += (n-i+1)
        i *= 10
    return result
        
print(main(int(input())))