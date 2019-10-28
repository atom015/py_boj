import heapq,sys
ip = sys.stdin.readline
heap = []
for i in range(int(ip())):
    n = int(ip())
    if n == 0:
        if heap:
            print(abs(heapq.heappop(heap)))
        else:
            print(0)
    else:
        heapq.heappush(heap,-n)
# heapq는 pop할때 가장각은값을 뽑으니까 음수에서 가장각은값의 절대값은 양수로 가장큰값이니까
# 음수로 작은값을 구한다음 abs로 절대값을 구해줬다.
