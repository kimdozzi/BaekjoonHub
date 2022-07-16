import sys
from collections import deque
input = sys.stdin.readline

def bfs() :
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny))
    return True

T = int(input()) # 테스트 케이스
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while T :
    pet = 0
    T -= 1
    n, m, k = map(int, input().split()) # 행,열, 배추 개수
    matrix = [[0 for _ in range(m)] for _ in range(n)] # 땅
    visited = [[False for _ in range(m)] for _ in range(n)] # 방문여부

    queue = deque([])

    for i in range(k) :
        r, c = list(map(int, input().split()))
        matrix[r][c] = 1

    for i in range(n) :
        for j in range(m) :
            if matrix[i][j] == 1 and visited[i][j] == False:
                visited[i][j] = True
                queue.append((i,j))
                pet += bfs()
    print(pet)