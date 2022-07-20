# BFS와 DFS
import sys
sys.setrecursionlimit(10**5)
from collections import deque

def bfs(graph, start, visited):
    cnt = 0
    queue = deque([(start, 0)])
    visited[start] = True
    while queue:
        v, dist = queue.popleft()
        if dist <= 2 :
            cnt += 1
        #print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append((i,dist+1))
                visited[i] = True
    return cnt - 1

input = sys.stdin.readline
v = int(input())
e = int(input())
visited = [False for _ in range(v+1)]
graph = [[] for _ in range(v+1)]

for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(bfs(graph, 1, visited))
