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
    
    
'''
# 입력
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 플로이드-워셜 알고리즘
for k in range(N):  # 경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1
            print(*graph,sep='\n')
            print()

# 출력
for row in graph:
    for col in row:
        print(col, end=" ")
    print()
    
'''
    
