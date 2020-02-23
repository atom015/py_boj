s = input()
st,a = [],""
size = {"+":1,"-":1,"/":2,"*":2,"(":0}
for i in range(len(s)):
    if "A" <= s[i] <= "Z":
        print(s[i],end='')
    elif s[i] == "(":
        st.append("(")
    elif s[i] == ")":
        while st and st[-1] != "(":
            print(st.pop(),end='')
        st.pop()
    else:
        while st and size[st[-1]] >= size[s[i]]:
            print(st.pop(),end='')
        st.append(s[i])
while st:
    print(st.pop(),end='')
