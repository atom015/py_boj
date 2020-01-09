n = int(input())
cnt = 0
for i in range(1,n+1):
    st = str(i)
    cnt += st.count("3")+st.count("6")+st.count("9")
print(cnt)
