class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2:return False
        target //=2
        
        dp = [True] + [False]*target
        
        nums.sort()
        
        for coin in nums:
            for i in range(coin,target +1):
                dp[i] = dp[i] or dp[i-coin] 
        return dp[-1]
        
        