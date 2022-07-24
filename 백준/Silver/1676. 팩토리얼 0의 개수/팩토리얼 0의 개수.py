import sys
input = sys.stdin.readline
n = int(input())
total = 1
cnt = 0
for i in range(2, n+1) :
    total *= i
total = str(total)
for i in total[::-1]:
    if i == '0' :
        cnt += 1
        continue
    else :
        print(cnt)
        break
