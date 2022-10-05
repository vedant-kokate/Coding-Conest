class Solution:
    def findPeakElement(self, nums) -> int:
        n=len(nums)
        l,h=0,n-1
        
        while l<h:
            mid = (l+h)//2
            # print(mid)
            if (mid+1<n and nums[mid+1]<nums[mid])or mid==n-1:
                if (mid-1>=0 and nums[mid-1]<nums[mid])or mid==0:
                    return mid
                h=mid
            else:
                l=mid+1
        return l
        
nums=[1]            
print(Solution().findPeakElement(nums))