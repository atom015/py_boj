from math import *
import sys
sys.setrecursionlimit(5000000)
ip = sys.stdin.readline
n = int(ip())
MAX = 100001
pii = []
max_level = 0

def getTree(nd,parent):
	global max_level
	depth[nd] = depth[parent]+1

	ac[nd][0] = parent


	max_level = floor(log2(MAX))

	for i in range(1,max_level+1):
		tmp = ac[nd][i-1]
		ac[nd][i] = ac[tmp][i-1]

	for i in graph[nd]:
		if i != parent:
			getTree(i,nd)

graph =[[] for i in range(n+1)]
depth = [0 for i in range(n+1)]
ac = [[0 for i in range(20)] for i in range(n+1)]

for i in range(n-1):
	a,b = map(int,ip().split())
	graph[a].append(b)
	graph[b].append(a)

depth[0] = -1

getTree(1,0)

m = int(ip())


for i in range(m):
	a,b = map(int,ip().split())
	if depth[a] != depth[b]:
		if depth[a] > depth[b]:
			a,b = b,a
		for i in range(max_level,-1,-1):
			if depth[a] <= depth[ac[b][i]]:
				b = ac[b][i]
	lca = a
	if a != b:
		for i in range(max_level,-1,-1):
			if ac[a][i] != ac[b][i]:
				a = ac[a][i]
				b = ac[b][i]
			lca = ac[a][i]
	print(lca)
