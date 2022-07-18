from collections import deque

row, col = map(int, input().split())
graph = [list(map(int, input())) for _ in range(row)]
visited = [[[0,0] for _ in range(col)] for _ in range(row)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(start_x, start_y, iscrash, visited, graph):
    #crash 0: 벽안부시고 가는경우, 1: 부신 경우
    queue = deque()
    queue.append((start_x, start_y, iscrash))
    visited[start_x][start_y][iscrash] = 1

    while queue:
        x, y, iscrash = queue.popleft()
        if x == row - 1 and y == col - 1:
            return visited[x][y][iscrash]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= row or ny <= -1 or ny >= col:
                continue
            # 벽 안부수고 이동
            if graph[nx][ny] == 0 and visited[nx][ny][iscrash] == 0:
                queue.append((nx, ny, iscrash))
                visited[nx][ny][iscrash] = visited[x][y][iscrash] + 1
            # 벽 부수고 이동
            if graph[nx][ny] == 1 and iscrash == 0:
                queue.append((nx, ny, iscrash + 1))
                visited[nx][ny][iscrash + 1] = visited[x][y][iscrash] + 1

    return -1

print(bfs(0, 0, 0, visited, graph))
