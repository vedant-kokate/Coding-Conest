import sys
input = sys.stdin.readline
def I():return list(map(int,input().split()))
n=int(input())
a=I()
count=0
for i,val in enumerate(a):
    if i+n>=len(a):
        break
    if val==a[i+n]:
        count+=1
print(count)
