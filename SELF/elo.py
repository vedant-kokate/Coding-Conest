def f(diff,score):
    # diff = int(input())
    a=diff/400
    b=10**a
    c=b+1
    d=1/c
    e=round(100*(score-d),1)
    print(e)

p1=int(input())
p2=int(input())
p1_won = float(input())
print(p1,p2,p1_won)
f(p2-p1,p1_won)

    # print(e)