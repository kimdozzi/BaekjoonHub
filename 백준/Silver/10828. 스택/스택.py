import sys
input = sys.stdin.readline
n = int(input())
ans = []
for _ in range(n) :
    s = input().rstrip()
    if ' ' in s :
        a, b = s.split()
        ans.append(b)
    else :
        if s == 'pop' :
            if ans:
                num = ans.pop()
                print(num)
            else :
                print(-1)

        elif s == 'size' :
            print(len(ans))

        elif s == 'empty' :
            if ans :
                print(0)
            else :
                print(1)

        elif s == 'top' :
            if ans :
                print(ans[-1])
            else :
                print(-1)


