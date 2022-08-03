class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [10**10]*n
        dp[0] = 0
        for i in range(n):
            for j in range(i+1,min(n,nums[i]+i+1)):
                # print(nums[i]+j)
                    
                dp[j] = min(dp[i]+1,dp[j])
        # print(dp)
        return dp[-1]


nums = [2,3,0,1,4]
print(Solution().jump(nums))