def func(a,b,m) :
    if b == 1 :
        return a % m
    val = func(a, b//2, m)
    val = val * val % m
    if b % 2 == 0:
        return val
    return val * a % m

a,b,c = map(int,input().split())
print(func(a,b,c))
