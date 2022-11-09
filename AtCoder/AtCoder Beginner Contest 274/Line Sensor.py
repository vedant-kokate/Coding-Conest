import sys
input = sys.stdin.readline
def I():return list(map(int,input().split()))
n,m=I()
ans=[0]*m
mat=[]
for i in range(n):
    mat.append(input().strip())
for i in range(n):
    for j in range(m):
        if mat[i][j]=='#':
            ans[j]+=1
print(*ans)