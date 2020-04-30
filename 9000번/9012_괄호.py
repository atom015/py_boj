def func(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        if i == ")":
            if "(" in stack:
                stack.pop()
            else:
                return "NO"
    if len(stack) >= 1:
        return "NO"
    return "YES"
for i in range(int(input())):
    print(func(input()))
