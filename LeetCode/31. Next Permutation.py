class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                nums[i+1:] = sorted(nums[i+1:])
                
                
                for j in range(i+1,n):
                    if nums[j]>nums[i]:
                        temp=nums[i]
                        nums[i]=nums[j]
                        nums[j] =temp
                        break
                nums[i+1:] = sorted(nums[i+1:])
                # print(nums)
                return
        nums[0:] = sorted(nums)
        
nums = [1,3,2,5,1,7,3,2,1]
print(Solution().nextPermutation(nums))
# print(nums)