N,r,c = map(int,input().split())
ans = 0
while N != 0:
    w = 2 ** (N-1)
    if N > 1:
        if r < w and c >= w :
            ans += (w ** 2)
            c -= w
        elif r >= w and c < w :
            ans += (w ** 2) * 2
            r -= w
        elif r >= w and c >= w :
            ans += (w ** 2) * 3
            r -= w
            c -= w

    if N == 1 :
       if r == 0 and c == 1 :
           ans += 1
       elif r == 1 and c == 0:
           ans += 2
       elif r == 1 and c == 1:
           ans += 3

    N -= 1

print(ans)
