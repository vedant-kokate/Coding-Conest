import sys
input = sys.stdin.readline
from bisect import bisect_left
def I():return list(map(int,input().split()))
n = int(input())
A = I()
B = I()

a=[]
for i in range(n):
    a.append((A[i],B[i]))
a.sort(key=lambda x:(x[0],x[1]))

stack=[]

for i in range(n):
    val=a[i][1]
    if not stack or stack[-1]<val:
        stack.append(val)
    else:
        stack[bisect_left(stack, val)]=val
print(len(stack)+n)




