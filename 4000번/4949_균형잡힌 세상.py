def func(s):
    st = []
    for i in s:
        if i == "(" or i == "[":
            st.append(i)
        elif i == ")":
            if len(st) != 0 and st[-1] == "(":
                st.pop()
            else:
                return "no"
        elif i == "]":
            if len(st) != 0 and st[-1] == "[":
                st.pop()
            else:
                return "no"
    if len(st) >= 1:
        return "no"
    return "yes"
while 1:
    s = input()
    if s == ".":
        break
    print(func(s))
