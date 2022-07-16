from collections import Counter
counter = Counter(input().rstrip().upper()).most_common()
if len(counter) == 1 :
    print(counter[0][0])
    exit(0)

for i in range(len(counter)-1) :
    if counter[i][1] == counter[i+1][1] :
        print('?')
        break
    else :
        print(counter[i][0])
        break
