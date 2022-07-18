import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    m, n = map(int, input().split())
    graph = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = 'IMPOSSIBLE'

    for i in range(n):
        graph.append(list(input().rstrip()))
        if '@' in graph[i]:
            queue = deque([(0, i, graph[i].index('@'))]) # (0, x, y)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == '*':
                queue.append((-1, i, j)) # (-1, x, y)

    while queue:
        time, x, y = queue.popleft()
        # 지훈이 탈출
        if time > -1 and graph[x][y] != '*' and (x == 0 or y == 0 or x == n - 1 or y == m - 1):
            ans = time + 1
            print(ans)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#':
                # 상근이 이동
                if time > -1 and graph[nx][ny] == '.':
                    graph[nx][ny] = '@'
                    queue.append((time + 1, nx, ny))
                # 불 퍼뜨리기
                elif time == -1 and graph[nx][ny] != '*':
                    graph[nx][ny] = '*'
                    queue.append((-1, nx, ny))
    else:
        print(ans)