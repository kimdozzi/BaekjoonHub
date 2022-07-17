n = int(input())
lst = list(map(int,input().split()))
lst.sort()
m = lst[-1]
for _ in range(n) :
    num = (lst.pop(0) / m) * 100
    lst.append(num)
print(sum(lst)/n)
