import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque([])

for _ in range(n) :
    s = input().rstrip()
    if ' ' in s :
        a, b = s.split()
        queue.append(b)
    else :
        if s == 'pop' :
            if queue:
                num = queue.popleft()
                print(num)
            else :
                print(-1)

        elif s == 'size' :
            print(len(queue))

        elif s == 'empty' :
            if queue :
                print(0)
            else :
                print(1)

        elif s == 'front' :
            if queue :
                print(queue[0])
            else :
                print(-1)

        elif s == 'back' :
            if queue :
                print(queue[-1])
            else :
                print(-1)

