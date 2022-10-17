import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    a = I()
    d=defaultdict(int)
    ans=[]
    d2,d1=set(),set()
    for i in a:
        d[i]+=1
    for key in d:
        if key!=0:
            val=d[key]
            if val>2:
                count=val//3
                for i in range(count):
                    ans.append([key,key,key])
                val %=3
            if val==2:
                d2.add(key)
            if val==1:
                d1.add(key)


    temp=[]
    for x in d2:
            for y in d1:
                if x^y in d1:
                    temp.append([x,y])
    for i in range(11111):
        if not temp:
            break
        x,y=temp.pop()
        if x in d2 and y in d1 and x^y in d1:
            ans.append([x,x,y])
            ans.append([x^y,x^y,x^y])
            d2.remove(x)
            d1.remove(y)
            d1.remove(x^y)
        if not d1 and not d2:
            break


    # print(temp)
                    
    print(len(ans))
    for a,b,c in ans:
        print(a,b,c)





    