import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph = []
for i in range(n) :
    graph.append(list(map(int, input().split())))

def bfs(x,y) :
    que = deque()
    que.append((x,y))
    cnt = 0
    while que:
        x, y = que.popleft()
        visited[x][y] = True
        cnt += 1
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    graph[nx][ny] = graph[x][y] + 1
                    que.append((nx,ny))
    return cnt

num = 0
maxNum = 0
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            num += 1
            tmp = bfs(i,j)
            if tmp > maxNum :
                maxNum = tmp
print(num, maxNum, sep='\n')