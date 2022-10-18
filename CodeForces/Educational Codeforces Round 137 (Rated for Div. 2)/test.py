import sys
input=sys.stdin.readline
from collections import defaultdict
def I():return list(map(int,input().split()))
from random import randint
for _ in range(1000):
    n=1000
    test=[]
    for xx in range(n):
        test.append(str(randint(0,1)))
    test="".join(test)

    
    # n = int(input())
    n=len(test)
    # temp=input().strip()
    temp = test
    # print(temp)
    def brute():
        # print("here")
        ans=int(test,2)
        for i in range(n):
            # print(i,test[i:])
            for j in range(i):
                ans=max(int(test,2)|int(test[j:i],2),ans)
        return (bin(ans)[2:])
    ans2=brute()
    s=[]
    s[:]=temp
    one_idx=-1
    for i in range(n):
        if s[i]=='1':
            one_idx=i
            break
    # print(one_idx)
    if one_idx==-1:
        print(0)
        exit()

    zeros=[]
    for i in range(one_idx,n):
        if s[i]=='0':
            zeros.append(i)
    if len(zeros)==0:
        print(temp)
        exit()
    first=zeros[0]
    l=n-first
    for i in range(len(zeros)):
        zeros[i]-=first
    zeros=zeros[1:]
    # print(zeros,l)
    max_=0
    for i in range(one_idx,first):
        if s[i]=='1':
            cur=0
            for idx,val in enumerate(zeros):
                if s[i+val]=='1':
                    cur += 2**(len(zeros)-idx-1)
                else:
                    if cur + 2**(len(zeros)-idx-1)-1<max_:
                        break
                    # print(idx,i,max_,len(zeros)-idx-1)
            # print(i,cur)
            max_=max(max_,cur)
    # print(max_)
    temp=bin(max_)[2:]
    change=[]
    change[:]=temp
    change = ['0']*(len(zeros)-len(change))+change
    # print(change)
    s[first]='1'
    for idx,val in enumerate(change):
        if change[idx]=='1':
            s[first+zeros[idx]]='1'
    ans1="".join(s)
    
    if ans1!=ans2:
        print(test)
        print("Wrong")
        print(ans1)
        print(ans2)
        exit()
print("done")