from math import sqrt,floor
def solution(s):
    global ref2
    n = int(s)
    l=[n]
    alpha =sqrt(2)
    # beta = alpha/(alpha-1)

    while l[-1]!=0:
        l.append(frac_sqrt_2_till_100*l[-1]//(10**100))
    # print(l)17677669529663689274023919016659124224
        #     17677669529663689274023919016659124224
    # print(l)
    f=[]
    for i in range(len(l)-1):
        F = (l[i]*l[i+1] + l[i]*(l[i]+1)/2 - l[i+1]*(l[i+1]+1)/2)
        f.append(F)
    ans = 0
    for i in range(len(f)):
        if i%2:
            ans-=f[i]
        else:
            ans+=f[i]
    ref2 = f 
  
    return ans
frac_sqrt_2_till_100 = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727

def find_floor_sum(sum_till):
    global ref
    """
    Recursive function to find the floor sum as defined in the problem.
    """
    if sum_till < 1:
        return 0
    
    elif sum_till == 1:
        return 1
    
    sum_till_complement = frac_sqrt_2_till_100*sum_till//(10**100)
    saved_term = (sum_till*sum_till_complement) + (sum_till*(sum_till+1)/2) - (sum_till_complement*(sum_till_complement+1)/2)
    ref.append(saved_term)
    return  saved_term- find_floor_sum(sum_till_complement)
    
    
def solution2(s):
    """
    A detailed mathematical explanation of the used concept can be found at the below link:
    https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s
    """
    sum_till = int(s)
    return str(int(find_floor_sum(sum_till)))

from random import randint
ref = []
ref2=[]
test_str = '7784123452'
ans1=solution(test_str)
ans2=solution2(test_str)
if ans1==ans2:
    print('TRUE')
else:
    print(ans1,ans2)
ref +=[1.0]
print(ref==ref2)
woh = 0
for i in range(len(ref)):
    if i%2:
        woh -=ref[i]
    else:
        woh += ref[i]
print(woh)
print(woh==ans1)