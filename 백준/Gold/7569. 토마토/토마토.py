import sys
from collections import deque
# 3차원 배열 토마토
input = sys.stdin.readline
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if graph[nz][nx][ny] == 0 and visited[nz][nx][ny] == False:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    visited[nz][nx][ny] = True
                    queue.append((nz, nx, ny))



m, n, h = map(int, input().split())
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

queue = deque([])
res = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                visited[i][j][k] = True
                queue.append((i, j, k))

bfs()

for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
            res = max(res, k)

print(res-1)
