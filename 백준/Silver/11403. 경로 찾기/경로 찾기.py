# BFS와 DFS
import sys
from collections import deque

def bfs(graph, start, visited):
    chk = [0 for _ in range(n)]
    while queue :
        nx = queue.popleft()
        for i in range(n) :
            if chk[i] == 0 and graph[nx][i] == 1 :
                queue.append(i)
                chk[i] = 1
                visited[start][i] = 1

input = sys.stdin.readline
n = int(input())

visited = [[0 for _ in range(n)] for _ in range(n)]
graph = [list(map(int,input().split())) for _ in range(n)]
queue = deque([])

for row in range(n) :
    queue.append(row)
    bfs(graph,row,visited)

for i in range(n) :
    for j in range(n) :
        print(visited[i][j], end=' ')
    print()