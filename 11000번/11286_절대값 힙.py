import sys,heapq
ip = sys.stdin.readline
a = []
for _ in range(int(ip())):
    n = int(ip())
    if n:
        heapq.heappush(a,(abs(n),-1 if n < 0 else 1))
    else:
        if a:
            ans = heapq.heappop(a)
            print(ans[0]*ans[1])
        else:
            print(0)
#절대값이 작은것을 뽑는데 더작은것을뽑는다고 했으니 음수였으면 -1아니면 1을
#넣어줘서 절대값이같으면 -1과1을 비교해서 작은것을 넣어준다.
#출력할때는 절대값과 -1혹은 1을 곱해서 원래값으로 만들어준다.
