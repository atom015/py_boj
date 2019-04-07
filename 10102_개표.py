A = 0
B = 0
V = int(input())
score = list(input())
for scores in score:
    if scores == "A":
        A += 1
    elif scores == "B":
        B += 1
    else:
        pass
if A > B:
    print("A")
elif B > A:
    print("B")
else:
    print("Tie")
