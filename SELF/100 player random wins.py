initial_score=100
num=10
a=[initial_score]*num
games=1000

from random import randint as r 
def f(diff,score):
    # diff = int(input())
    a=diff/400
    b=10**a
    c=b+1
    d=1/c
    e=100*(score-d)
    return e

for _ in range(games):
    p1=r(0,num-1)
    p2=r(0,num-1)
    while p2==p1:
        p2=r(0,num-1)
    p1_win=r(0,2)/2
    change=f(a[p2]-a[p1],p1_win)
    a[p1] = round(change + a[p1],1)
    a[p2] = round( -change + a[p1],1)
    # print(p1,p2,change)
a.sort()
m=a[0]
a=[round(a[i]-m,1) for i in range(num)]
print(a)
    



