dic = {}
res = 1
for i in range(0,10):
    dic[i] = 0
for _ in range(3) :
    res *= int(input())
for i in str(res) :
    dic[int(i)] += 1
print(*dic.values(),sep='\n')