import sys
input=sys.stdin.readline
from collections import deque
mod=10**9+7
for _ in range(int(input())):
    n=int(input())-1
    a=list(map(int,input().split()))
    new_a=[-1]*(n+1)
    # print(new_a)
    for i in range(n):
        new_a[i]=max(a[i],new_a[i])
        new_a[i+1]=max(a[i],new_a[i+1])
    # print(new_a)
    
    can_be_change=[]
    for i in range(n+1):
        change=new_a[i]+1
        if i==0:
            if min(change,new_a[i+1])==a[i]:
                can_be_change.append(i)
      
        elif i==n:
            if min(change,new_a[i-1])==a[i-1]:    
                can_be_change.append(i)
        else:
            if min(change,new_a[i+1])==a[i] and min(change,new_a[i-1])==a[i-1]:
                can_be_change.append(i)
   
    

    # print('can be change',can_be_change)
    print(new_a)
    print(can_be_change)
    for i in range(1,len(can_be_change)):
        
    # pair=[]
    # for i in range(len(can_be_change)-1):
    #     x1=can_be_change[i+1]
    #     x2=can_be_change[i]
    #     if x1-x2==1:
    #         cal=2*10**5-new_a[x1]-new_a[x2]+1
    #         cal%=mod
    #         pair.append(cal)
    # # print('pair',pair)
    # ans=1
    # for i in pair:
    #     ans*=i
    #     ans%=mod
    # print(ans)


        

