import sys
input = sys.stdin.readline
n = int(input())
ans = []
for i in range(n) :
    number = int(input())
    if number == 0 :
        ans.pop()
    else :
        ans.append(number)

print(sum(ans))