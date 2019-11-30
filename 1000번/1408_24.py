h,m,s = map(int,input().split(":"))
nt = s+(m*60)+(h*3600)
h,m,s = map(int,input().split(":"))
st = s+(m*60)+(h*3600)
if nt > st:
    st += 24*60*60
ret = st-nt
h = ret//3600
ret %= 3600
m = ret//60
ret %= 60
print("%02d" % h ,end=':')
print("%02d" % m,end=':')
print("%02d" % ret)
