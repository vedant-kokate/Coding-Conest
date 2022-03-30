def solution(n):
    def val(n):
        temp = "{0:b}".format(int(n))
        return temp.count('1')*2+temp.count('0')
    n=int(n)
    ans=0
    while n>1:
        if n%2:
            if val(n-1)<val(n+1):
                n-=1
                ans+=1
            else:
                n+=1
                ans+=1
        else:
            n//=2
            ans+=1
    return ans
n = int(input())
print(solution(n))