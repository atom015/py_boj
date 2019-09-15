"""
문제
창영이는 크로스워드 퍼즐을 만들려고 한다.

두 단어 A와 B가 주어진다. A는 가로로 놓여야 하고, B는 세로로 놓어야 한다. 또, 두 단어는 서로 교차해야 한다. (정확히 한 글자를 공유해야 한다) 공유하는 글자는 A와 B에 동시에 포함되어 있는 글자여야 하고, 그런 글자가 여럿인 경우 A에서 제일 먼저 등장하는 글자를 선택한다. 마찬가지로 이 글자가 B에서도 여러 번 등장하면 B에서 제일 처음 나오는 것을 선택한다. 예를 들어, A = "ABBA"이고, B = "CCBB"라면, 아래와 같이 만들 수 있다.

.C..
.C..
ABBA
.B..
입력
첫째 줄에 두 단어 A와 B가 주어진다. 두 단어는 30글자 이내이고, 공백으로 구분되어져 있다. 또, 대문자로만 이루어져 있고, 적어도 한 글자는 두 단어에 포함되어 있다.

출력
A의 길이를 N, B의 길이를 M이라고 했을 때, 출력은 총 M줄이고, 각 줄에는 N개 문자가 있어야 한다. 문제 설명에 나온 것 같이 두 단어가 교차된 형태로 출력되어야 한다. 나머지 글자는 '.'로 출력한다.

예제 입력 1
BANANA PIDZAMA
예제 출력 1
.P....
.I....
.D....
.Z....
BANANA
.M....
.A....
"""
a,b = input().split()
aix,bix = -1,-1
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            aix,bix = i,j
            break
    if aix >= 0 and bix >= 0:
        break
for i in range(len(b)):
    for j in range(len(a)):
        if j == aix and i != bix:
            print(b[i],end='')
        elif i == bix:
            for k in range(len(a)):
                print(a[k],end='')
            break
        else:
            print(".",end='')
    print()
