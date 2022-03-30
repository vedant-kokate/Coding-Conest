from fractions import Fraction as f
def solution(pegs):
    n=len(pegs)
    t1,t2=0,0
    tot=0
    for i in range(n-1):
        tot+= (pegs[i+1]-pegs[i])*(-1)**i
    if n%2==1:
        tot = f(tot,1)*2
    else:
        tot = f(tot,1)*2/3
    gears=[tot]
    for i in range(1,n):
        gears.append(pegs[i]-pegs[i-1]-gears[-1])
    print(gears)
    for gear in gears:
        if gear<1:
            return [-1,-1]
    return [tot.numerator,tot.denominator]
    # return [-1,-1]

  

s=list(map(int,input().split()))
print(solution(s))