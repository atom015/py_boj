n = int(input())
a = [int(input()) for i in range(n)]
st = []
ans = []
for i in range(1,n+1):
    while st and st[-1] == a[0]:
        st.pop()
        a.pop(0)
        ans.append("-")
    st.append(i)
    ans.append("+")
while st and st[-1] == a[0]:
    st.pop()
    a.pop(0)
    ans.append("-")
if len(st) != 0:
    print("NO")
else:
    for i in ans:
        print(i)
