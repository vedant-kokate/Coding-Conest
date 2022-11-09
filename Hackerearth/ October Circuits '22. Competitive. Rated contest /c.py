import sys
from collections import defaultdict
input=sys.stdin.readline
def I():return list(map(int,input().split()))


for _ in range(int(input())):
    n = int(input())
    a = I()
    count=0
    for i in range(len(a)):
        while a[i]%2==0:
            # print(i,a[i])
            count+=1
            a[i]//=2
    # print(count)
    if count>=n:
        print("YES")
    else:
        print("NO")
    # print(count)


# print(dp[-1])

