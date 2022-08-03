class Solution:
    def myPow(self, x: float, n: int) -> float:
        def p(x,n):
            if n==0:
                return 1.0
            if n%2:
                return x*p(x*x,n//2)
            else:
                return p(x*x,n//2)
        if n<0:
            ans = 1/p(x,-n)
        else:
            ans = p(x,n)
        return ans
x=2
n=-2
print(Solution().myPow(x, n))