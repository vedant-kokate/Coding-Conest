from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        prime=[1]*(n)
        prime[0]=prime[1]=0
        for i in range(int(sqrt(n))+1):
            if prime[i]:
                prime[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)

        return sum(prime)
n=int(input())
print(Solution().countPrimes(n))