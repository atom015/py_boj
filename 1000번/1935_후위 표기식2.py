N = int(input())
S = list(input())
arr = [float(input()) for i in range(N)]
stack = []
for i in S:
    if i not in ["*","+","-","/"]:
        stack.append(arr[ord(i)-ord("A")])
    else:
        B = stack.pop()
        A = stack.pop()
        if i == '+':
            stack.append(A+B)
        elif i == '-':
            stack.append(A-B)
        elif i == '/':
            stack.append(A/B)
        elif i == '*':
            stack.append(A*B)
print(f"{stack[0]:.2f}")
