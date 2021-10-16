import sys
input=sys.stdin.readline
def I():return list(map(int,input().split()))


for _ in range(int(input())):
    n,k=I()
    a=input().strip()
    first=a[0]
    last=a[0]
    step=0
    last_1,last_0=-1,-1
    for i in range(1,n):
        if a[i]=='1':
            last_1=i
        else:
            last_0=i
        if last=='1' and a[i]=='0':
            step+=1
            last='0'
        if last=='0' and a[i]=='1': 
            step+=1
            last='1'
    # print('step',step,last_0,last_1)
    if step<k:
        print(-1)
    else:
        if k%2:
            if first=='1':
                print(last_0+1)
            else:
                print(last_1+1)
        else:
            if first=='1':
                print(last_1+1)
            else:
                print(last_0+1)
        

