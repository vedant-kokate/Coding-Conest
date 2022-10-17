import math
class Solution:
    def numSquares2(self,n):
        dp=[0]
        while len(dp)<=n:
            m=len(dp)
            val =5
            for i in range(1,int(math.sqrt(m)+1)):
                val = min(val,dp[m-i*i] + 1)
            dp.append(val)
        return dp[-1]

    def numSquares(self, n: int) -> int:
        l=[]
        for i in range(1,int(math.sqrt(n))+1):
            l.append(i*i)

        dp=[1] + [0]*n

        for i in range(n):
            if dp[i]!=0:
                for j in l:
                    if i+j>n:
                        break
                    if dp[i+j]==0:
                        dp[i + j] = dp[i]+dp[j]
                    else:
                        dp[i + j] = min(dp[i]+dp[j],dp[i+j])
        return(dp[-1])
n=int(input())
print(Solution().numSquares2(n))