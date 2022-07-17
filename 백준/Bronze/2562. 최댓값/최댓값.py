lst = []
idx = 0
maxNum = 0
for _ in range(9) :
    lst.append(int(input()))
for i in range(1,len(lst)+1) :
    if lst[i-1] >= maxNum :
        maxNum = lst[i-1]
        idx = i
print(maxNum)
print(idx)
