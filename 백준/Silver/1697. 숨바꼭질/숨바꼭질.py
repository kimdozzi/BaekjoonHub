import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
distance = [-1 for _ in range(100001)]
visited = [False for _ in range(100001)]
dx = [-1, 1, 2]
flag = 1
queue = deque([(0,n)])

if n == k :
    print(0)
    exit(0)
    
while queue and flag:
    time, x = queue.popleft()
    time += 1

    for i in range(3):
        if i == 2 :
            subin = x * dx[i]
        else :
            subin = x + dx[i]

        if 0 <= subin <= 100000 and visited[subin] == False:
            distance[subin] = time
            queue.append((time,subin))
            visited[subin] = True
            if subin == k :
                print(time)
                flag = 0
                break

