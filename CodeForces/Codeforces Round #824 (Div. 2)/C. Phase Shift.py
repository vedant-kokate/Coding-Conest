import sys
input=sys.stdin.readline
def f():return list(map(int,input().split()))
from math import ceil
for _ in range(int(input())):
    N=int(input())
    s=input().strip()
    upper,lower,link={},{},{}
    ans=[]
    for ch in s:
        if ch in link:
            ans.append(link[ch])
            continue
        upper[ch]=True
        
        not_found=True
        for l in range(26):
            L=chr(l+97)
            if ch in lower and L in upper:
                continue
            if L in lower:
                continue
            if L==ch:
                continue
            else:
                ans.append(L)
                lower[L]=True
                link[ch]=L
                not_found=False
                break
        if not_found:
            for l in range(26):
                L=chr(l+97)
                if L not in lower:
                    ans.append(L)
                    link[ch]=L
                    lower[L]=True 


        

    print("".join(ans))
        

