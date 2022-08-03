class Solution:
    def maxSubArray(self, nums):
        till_now,max_till_now = 0,-10**9
        for i in nums:
            till_now += i
            max_till_now = max(max_till_now,till_now)
            if till_now<0:
                till_now = 0
            
        return max_till_now
        
nums = [-1]
print(Solution().maxSubArray(nums))