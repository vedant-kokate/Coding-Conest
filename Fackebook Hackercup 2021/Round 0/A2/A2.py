import sys
input=sys.stdin.readline
from collections import defaultdict
def f():return list(map(int,input().split()))

for _ in range(int(input())):
    g_keys=set()
    s=input()
    count=defaultdict(int)
    for c in s:
        if c!="\n":
            count[c]+=1
            g_keys.add(c)
    
    n=int(input())
    g=[[10**10]*26 for i in range(26)]
    
    for i in range(26):g[i][i]=0
    for i in range(n):
        ab=input()
        a=ord(ab[0])-65
        b=ord(ab[1])-65
        g_keys.add(ab[0])
        g_keys.add(ab[1])
        g[a][b]=1
    
    for k in range(26):
        for i in range(26):
            for j in range(26):
                g[i][j] = min(g[i][j],g[i][k] + g[k][j])

    ans=10**8
    for change_key_to in g_keys:
        temp=0
        c1=ord(change_key_to)-65
        for change_key_from in count.keys():            
            c2=ord(change_key_from)-65
            temp+=g[c2][c1]*count[change_key_from]
        ans=min(ans,temp)
    if ans==10**8:
        ans=-1
    print(f"Case #{_+1}: {ans}")
