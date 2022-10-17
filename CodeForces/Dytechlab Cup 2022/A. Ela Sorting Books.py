import sys
input = sys.stdin.readline
def I():return list(map(int,input().split()))
for _  in range(int(input())):
    n,k=I()
    s=input().strip()
    a=[0]*26
    for ch in s:
        a[ord(ch)-97]+=1
    # print(a)
    ans=""
    tot=n//k
    # print(tot)
    
    for K in range(k):
        count=0
        d=[]
        for i in range(26):
            if a[i]>0:
                a[i]-=1
                count+=1
                d.append(i)
            if count==tot:
                break
        # if count<tot:
        #     for i in range(25,-1,-1):
        #         if a[i]>1:
        #             a[i]-=1
        #             count+=1
        #             d.append(i)
        #         if count==tot:
        #             break 
        # print(d)
        mex=0
        for i in d:
            if i==mex:
                mex+=1
        ans += str(chr(97+mex))
    print(ans)
        