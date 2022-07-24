import sys
input = sys.stdin.readline
while True :
    stk = []
    flag = 0
    ans = list(input().rstrip())
    if ans[0] == '.' :
        exit(0)
    for i in ans :
        if i == '(' or i == '[' :
            stk.append(i)

        elif i == ')' :
            if stk and stk[-1] == '(' :
                stk.pop()
            else :
                flag = 1
                break

        elif i == ']' :
            if stk and stk[-1] == '[' :
                stk.pop()
            else :
                flag = 1
                break

        else :
            continue

    if stk or flag == 1:
        print('no')
    else :
        print('yes')