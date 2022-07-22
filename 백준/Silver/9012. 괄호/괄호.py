import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n) :
    ans = []
    flag = 0
    s = input().rstrip()

    for i in s :
        if i == '(' :
            ans.append(i)

        elif i == ')' :
            if ans :
                ans.pop()
            else :
                flag = 1
                break

    if ans or flag == 1:
        print('NO')
    else :
        print('YES')

