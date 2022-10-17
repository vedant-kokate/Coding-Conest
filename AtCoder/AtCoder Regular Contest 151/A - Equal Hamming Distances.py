import sys
input = sys.stdin.readline
def I():return list(map(int,input().split()))
n=int(input())
def f(a_idx,b_idx):
    a_len = len(a_idx)
    b_len = len(b_idx)
    ans=['0']*n
    i=a_len-1
    while a_len!=b_len:
        ans[a_idx[i]]= '1'
        a_len -= 1
        b_len += 1
        i-=1
    return "".join(ans)

a=input().strip()
b=input().strip()
a_idx,b_idx = [], []
for i in range(n):
    if a[i]!=b[i]:
        if a[i]=='1':
            a_idx.append(i)
        else:
            b_idx.append(i)
# a_len, b_len = len(a_idx), len(b_idx)
# print(a_idx,a_len)
if (max(len(a_idx),len(b_idx))-min(len(a_idx),len(b_idx)))%2:
    print(-1)
    exit()
if len(a_idx)>len(b_idx):
    print(f(a_idx,b_idx))
else:
    print(f(b_idx,a_idx))