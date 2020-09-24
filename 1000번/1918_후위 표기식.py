s = input()
st,a = [],""
size = {"+":1,"-":1,"/":2,"*":2,"(":0}
for i in s:
    if "A" <= i <= "Z":
        print(i,end='')
    elif i == "(":
        st.append("(")
    elif i == ")":
        while st and st[-1] != "(":
            print(st.pop(),end='')
        st.pop()
    else:
        while st and size[st[-1]] >= size[i]:
            print(st.pop(),end='')
        st.append(i)
while st:
    print(st.pop(),end='')
