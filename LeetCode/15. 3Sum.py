class Solution(object):

    def threeSum(self, nums):
        nums.sort()
        result = []
        for n1 in range(len(nums) - 2):
            if n1 > 0 and nums[n1] == nums[n1 - 1]:
                continue
            if nums[n1]>0:
                break
            n2, n3 = (n1 + 1, len(nums) - 1)

            while n2 < n3:
                s = nums[n1] + nums[n2] + nums[n3]

                if s == 0:
                    result.append((nums[n1], nums[n2],
                                  nums[n3]))

                    n3 -= 1
                    while n2 < n3 and nums[n3]== nums[n3 + 1]:
                        n3 -= 1
                elif s > 0:

                    n3 -= 1
                else:
                    n2 += 1
        return result
nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))