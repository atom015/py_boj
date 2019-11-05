import sys
from collections import deque
from copy import deepcopy

sys.setrecursionlimit(50000000)
ip = sys.stdin.readline
n, m = map(int, ip().split())
a = [list(map(int, ip().split())) for _ in range(n)]
cnt = 0
q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] != 0:
            q.append([i, j])


def bfs(x, y, v):
    tq = deque()
    tq.append([x, y])
    v[x][y] = True
    while tq:
        x, y = tq.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = dx+x, dy+y
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if v[nx][ny] is False and a[nx][ny] > 0:
                tq.append((nx, ny))
                v[nx][ny] = True


def solve():
    global cnt
    while q:
        le = len(q)
        connection = 0
        v = [[False] * m for _ in range(n)]
        for i1 in range(n):
            for j1 in range(m):
                if a[i1][j1] and not (v[i1][j1]):
                    bfs(i1, j1, v)
                    connection += 1
                    if connection >= 2:
                        return cnt
        ca = deepcopy(a)
        for _ in range(le):
            x, y = q.popleft()
            count = 0
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                nx, ny = dx + x, dy + y
                if 0 <= nx < n and 0 <= ny < m:
                    if ca[nx][ny] == 0:
                        count += 1
            if a[x][y]-count >= 0:
                a[x][y] = a[x][y]-count
                q.append([x, y])
            elif a[x][y]-count < 0:
                a[x][y] = 0
        cnt += 1
    return 0

print(solve())
