ans = ""
def conv(num,base):
    global ans
    if num >= base:
        ans += str(num%base)
        conv(num//base,base)
    else:
        ans += str(num)
conv(int(input()), 9)
print(ans[::-1])
