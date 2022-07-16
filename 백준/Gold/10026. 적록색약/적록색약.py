import sys
from collections import deque
input = sys.stdin.readline

def bfs() :
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if matrix[x][y] == 'G' :
                store.append((x,y))
            if 0 <= nx < n and 0 <= ny < n and matrix[x][y] == matrix[nx][ny] and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny))
    return True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
store, ans = [], []
queue = deque([])
res = 0

n = int(input())
matrix = []
for i in range(n):
    matrix.append([s for s in (input().rstrip())])

visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            visited[i][j] = True
            queue.append((i, j))
            res += bfs()

ans.append(res)
visited = [[False for _ in range(n)] for _ in range(n)]
res = 0

for x,y in store :
    matrix[x][y] = 'R'

for i in range(n) :
    for j in range(n) :
        if visited[i][j] == False :
            visited[i][j] = True
            queue.append((i,j))
            res += bfs()

ans.append(res)
print(*ans,sep=' ')
