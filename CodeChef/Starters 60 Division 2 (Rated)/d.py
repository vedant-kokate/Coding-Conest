import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
def I():return list(map(int,input().split()))
mod=998244353 
lim=2*10**3+10

numberOfPaths=[[1]*lim for i in range(lim)]
for i in range(1,lim):
    for j in range(1,lim):
        numberOfPaths[i][j] = numberOfPaths[i-1][j] + numberOfPaths[i][j-1]
        numberOfPaths[i][j] %= mod 


f=[1]*lim
inv_f=[1]*lim
for i in range(2,lim):
    f[i] = f[i-1]*i
    f[i]%=mod
    inv_f[i] = pow(f[i],mod-2,mod)


for _ in range(int(input())):
    n,m=I()
    l = n + m - 1
    if l%2:
        print(0)
        continue

    tp=numberOfPaths[n-1][m-1]
    # print(total_paths,'tp',n,m)
    path_comb = f[l]*inv_f[l//2]*inv_f[l//2]
    path_comb %= mod   

    out_l = m*n-l 
    if out_l!=0:
        out_comb = pow(out_l,2,mod)
    else:
        out_comb = 1
    out_comb%=mod
    # print(out_comb)
    print(tp,path_comb,out_comb)


    