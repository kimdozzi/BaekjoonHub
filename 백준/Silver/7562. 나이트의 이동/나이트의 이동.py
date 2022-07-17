import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, -1, 1, 1, -2, -2, 2, 2]
dy = [-2, 2, -2, 2, -1, 1, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    matrix[nx][ny] = matrix[x][y] + 1
                    if nx == movePositionX and ny == movePositionY:
                        return True

res = []
T = int(input())
for _ in range(T):
    queue = deque([])
    l = int(input())
    maxNumber = 0
    matrix = [[0 for _ in range(l)] for _ in range(l)]
    visited = [[False for _ in range(l)] for _ in range(l)]
    currentPositionX, currentPositionY = map(int,input().split())
    movePositionX, movePositionY = map(int,input().split())
    visited[currentPositionX][currentPositionY] = True
    queue.append((currentPositionX,currentPositionY))
    if currentPositionX == movePositionX and currentPositionY == movePositionY :
        print(0)
        continue
        
    bfs()
    for i in matrix :
        for j in i :
            if j >= maxNumber :
                maxNumber = j
    print(maxNumber)



