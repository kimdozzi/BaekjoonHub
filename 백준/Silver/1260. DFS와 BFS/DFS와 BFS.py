import sys
input = sys.stdin.readline
from collections import deque
n, m, start = map(int,input().split())
visited = [False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

def bfs(graph, start, visited):
    queue = deque([start])
    # stack = [start]  DFS
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph, start, visited) :
    visited[start] = True
    print(start, end=' ')
    for i in graph[start] :
        if not visited[i] :
            dfs(graph,i,visited)

for _ in range(m) :
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1) :
    graph[i].sort()
    
dfs(graph,start,visited)
print()
visited = [False for _ in range(n+1)]
bfs(graph,start,visited)


