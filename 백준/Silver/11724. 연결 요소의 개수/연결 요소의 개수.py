# BFS와 DFS
import sys
sys.setrecursionlimit(10**5)
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    # stack = [start]  DFS
    visited[start] = True
    while queue:
        v = queue.popleft()
        #print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def dfs(graph, start, visited):
    visited[start] = True
    #print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


input = sys.stdin.readline
n, m = map(int, input().split())
visited = [False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
ans = 0
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
'''
for i in range(1, n+1):
    graph[i].sort()
'''

for i in range(1,n+1) :
    if visited[i] == False :
        dfs(graph, i, visited)
        ans += 1

#print(*graph, sep='\n')
print(ans)