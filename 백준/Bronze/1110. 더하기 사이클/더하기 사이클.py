s = input()
if len(s) == 1 :
    s = '0' + s
ans = s
total, cnt = 0, 0
while True:
    total = str(int(s[0]) + int(s[-1]))
    s = s[-1] + total[-1]
    cnt += 1
    if ans == s :
        print(cnt)
        break
