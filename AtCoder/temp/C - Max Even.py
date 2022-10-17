import sys
input = sys.stdin.readline
from collections import defaultdict
def I():return list(map(int,input().split()))

n = int(input())
a = I()
odd,even=[],[]
for i in a:
    if i%2:
        odd.append(i)
    else:
        even.append(i)

odd.sort()
even.sort()
a1,a2=-1,-1
if len(odd)>1 :
    a1=odd[-1]+odd[-2]
if len(even)>1:
    a2=even[-1]+even[-2]

print(max(a1,a2))




