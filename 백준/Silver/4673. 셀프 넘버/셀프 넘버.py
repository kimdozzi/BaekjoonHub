num = set(range(1,10001))
res = set()
for i in range(1,10001) :
    for j in str(i) :
        i += int(j)
    res.add(i)
selfNumber = sorted(num - res)
print(*selfNumber, sep='\n')