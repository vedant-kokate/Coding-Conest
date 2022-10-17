class Solution:
    def coinChange(self, coins, amount):
        dp = [1] +[0]*amount
        if amount==0:
            return 0
        coins.sort()
        for i in range(amount+1):
            if dp[i]!=0:
                for c in coins:
                    if i+c>amount:
                        break
                    if dp[i+c]==0:
                        dp[i+c] = dp[i] + dp[c]
                    else:
                        dp[i+c] = min(dp[i] + dp[c],dp[i+c])
        print(dp)
        return dp[-1] if dp[-1]!=0 else -1
        
coins = [474,83,404,3]

amount = 264
print(Solution().coinChange(coins, amount))