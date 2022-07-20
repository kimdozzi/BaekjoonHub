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
    global ans
    ans += 1
    #print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


input = sys.stdin.readline
v = int(input())
e = int(input())
visited = [False for _ in range(v+1)]
graph = [[] for _ in range(v+1)]
ans = 0
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
'''
for i in range(1, n+1):
    graph[i].sort()
'''
dfs(graph,1,visited)
#print(*graph, sep='\n')
print(ans-1)