import sys
input = sys.stdin.readline
cal=[]

for _  in range(int(input())):
    temp=input().strip()
    s=[]
    s[:0]=temp
    # s=list(map(int,))
    n=len(s)
    ans=0
    
    for i in range(n):
        if s[i]=='1' or s[i]=='0':
            # print('huh',i)
            for j in range(i-1,-1,-1):
                # print("why?")
                if s[j+1]=='1':
                    s[j]='0'
                    # print('okay',s[j],j)
                else:
                    s[j]='1'
            break
    s2=s.copy()
    # print(s)
    # exit()
    if i==n-1:
        print(n*(n-1))
        continue
    start=0
    start2=0
    # print(s,i)
    for i in range(1,n):
        if s[i]=='?':
            if s[i-1]=='0':
                s[i]='1'
                s2[i]='0'
            else:
                s[i]='0'
                s2[i]='1'
            start2=i
        elif s[i]==s[i-1]:
            dis=i-start
            ans+=(dis-1)*dis//2
            start=i
        elif s2[i]==s2[i-1]:
            if start2>start:
                start2=i
            else:
                dis=i-start2
                ans+=(dis-1)*dis//2
                start2=i
        print(i,ans)
        print(s)
        print(s2)
    if start!=n-1 and start<start2:
        dis=i-start
        ans+=(dis-1)*dis//2
    if start2!=n-1 and start>start2:
        dis=i-start2+1
        ans+=(dis-1)*dis//2
    # print(start2,start)
    print(ans+n)

   