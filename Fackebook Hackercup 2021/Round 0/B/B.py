import sys
input=sys.stdin.readline
from collections import defaultdict
def f():return list(map(int,input().split()))

for _ in range(int(input())):
    cell=(-1,-1)
    n=int(input())
    g=[['.']*n for i in range(n)]
    for i in range(n):
        temp=input()
        for j in range(n):
            g[i][j]=temp[j]
    ans=10**9
    num_of_ans=1
    for i in range(n):
        #rows
        count=0
        flag=True
        for j in range(n):
            if g[i][j]=='O':
                flag=False
                break
            elif g[i][j]=='.':
                cell=(i,j)
                count+=1
        if flag and count<ans:
            ans=count
            # if count==1:
            #     # cell=(i,j)            
            num_of_ans=1

        elif flag and count==ans:
            # row.add(i)
            num_of_ans+=1
        
        #column
        count=0
        flag=True
        for j in range(n):
            if g[j][i]=='O':
                flag=False
                break
            elif g[j][i]=='.':
                count+=1
                cell2=(j,i)
        # print(i,j,count)
        if flag and count<ans:
            ans=count
            # col=set()
            # col.add(i)
            num_of_ans=1
        elif flag and count==ans:
            # col.add(i)
            # print(cell,cell2)
            if ans==1 and cell==cell2:
                continue
            num_of_ans+=1

    if ans==10**9:
        print(f"Case #{_+1}: Impossible")
    else:
        print(f"Case #{_+1}: {ans} {num_of_ans}")
