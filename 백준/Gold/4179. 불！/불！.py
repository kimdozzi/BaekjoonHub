import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 'IMPOSSIBLE'
flag = 0
for i in range(n):
    graph.append(list(input().rstrip()))
    if 'J' in graph[i]:
        queue = deque([(0, i, graph[i].index('J'))]) # (0, x, y)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'F':
            queue.append((-1, i, j)) # (-1, x, y)

while queue:
    time, x, y = queue.popleft()
    # 지훈이 탈출
    if time > -1 and graph[x][y] != 'F' and (x == 0 or y == 0 or x == n - 1 or y == m - 1):
        ans = time + 1
        flag = 1
        print(ans)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#':
            # 지훈이 이동
            if time > -1 and graph[nx][ny] == '.':
                graph[nx][ny] = '_'
                queue.append((time + 1, nx, ny))
            # 불 퍼뜨리기
            elif time == -1 and graph[nx][ny] != 'F':
                graph[nx][ny] = 'F'
                queue.append((-1, nx, ny))
if flag == 0 :
    print(ans)