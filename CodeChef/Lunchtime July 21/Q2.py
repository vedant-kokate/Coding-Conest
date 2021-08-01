import sys
# from typing import Counter
input=sys.stdin.readline
def I():return list(map(int,input().split()))
for _ in range(int(input())):
    n=int(input())
    a=I()
    b=I()
    
    # if all ele of b are same
    if all(b[0] == x for x in b):
        for x in range(n):
            print((a[x]+b[x])%n,end=" ")
        print()
        continue
    minimum=list(range(n))
    # print("mini",minimum)

    i=0
    while True and i<n:        
        min_val=10**9

        for j in minimum:

            if (a[i]+b[j])%n==min_val:
                minimum.append((j+1)%n)

            elif (a[i]+b[j])%n<min_val:
                min_val=(a[i]+b[j])%n
                minimum=[(j+1)%n]

        # print(minimum,min_val)
        if len(minimum)<2:
            break
        i+=1



    # print(i)
    cur_val=(minimum[0]-1)%n
    # print(cur_val,i)
    # print(*c)
    if cur_val==i:
        for i in range(n):
            print((a[i]+b[i])%n,end=" ")
    else:
        j=cur_val-i 
        for i in range(n):
            print((a[i]+b[(i+j)%n])%n,end=" ")
 
    print()

