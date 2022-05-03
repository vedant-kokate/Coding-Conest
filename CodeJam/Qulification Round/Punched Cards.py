import sys
input=sys.stdin.readline
def f():return list(map(int,input().split()))
for _ in range(int(input())):
    n,m=f()
    mat = [['.']*(m*2+1) for i in range(n*2+1)]
    for i in range(n*2+1):
        for j in range(m*2+1):
            if i>1 or j>1:
                if i%2:
                    if j%2==0:
                        mat[i][j] = '|' 
                else:
                    if j%2:
                        mat[i][j] = '-'
                    else:
                        mat[i][j] = '+'
   
        
    print(f"Case #{_+1}:")
    for i in mat:
        print("".join(i))