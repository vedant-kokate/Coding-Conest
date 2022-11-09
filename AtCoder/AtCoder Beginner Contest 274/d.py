import sys
input = sys.stdin.readline
def I():return list(map(int,input().split()))
def f(idx,i,target):
    # print(idx,i,target)
    global mem
    if (idx,i) in mem:
        return mem[(idx,i)]
    if idx>=n and i==target:
        return True
    if idx>=n:
        return False
    ans = f(idx+2,i+a[idx],target) or f(idx+2,i - a[idx],target)
    mem[(idx,i)] = ans 
    return ans
n, x, y = I()
a = I()

mem={}
ans1 = f(2,a[0],x)
if not ans1:
    print("No")
    exit()
mem={}
ans2= f(1,0,y)
if ans2:
    print("Yes")
else:
    print("No")
