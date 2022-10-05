class Solution:
    def numTrees(self, N: int) -> int:
        dp=[0]*21
        dp[0] = 1
        dp[1] = 1
        # print("hey")
        for n in range(2,21):
            for i in range(n):
                dp[n] += dp[i] * dp[n-1-i]
                # print(n,i,n-1-i)
        print(dp)
        return dp[N]

n=int(input())
print(Solution().numTrees(n))