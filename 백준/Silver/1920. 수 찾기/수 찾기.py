import sys
input = sys.stdin.readline
dic = {}
n = int(input())
lst1 = list(map(int,input().split()))
m = int(input())
lst2 = list(map(int,input().split()))

for i in lst1:
    dic[i] = 1
for i in lst2:
    if i in dic :
        print(1)
    else :
        print(0)