from bisect import bisect_left
class Solution:
    def increasingTriplet(self, nums) -> bool:
        stack=[0]*len(nums)
        stack[0] = nums[0]
        l = 1
        for i in nums:
            if i>stack[l-1]:
                stack[l] = i
                l+=1
                if l==3:
                    return True
            else:
                stack[bisect_left(stack, i, 0, l-1)] = i
        return False

nums = [6,5,3,4,4]  
print(Solution().increasingTriplet(nums))