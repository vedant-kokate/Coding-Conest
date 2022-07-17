class Solution:
    def search(self, a: List[int], k: int) -> int:
        n=len(a)
        l, h=0, n-1
        while l<=h:
            
            mid = (l+h)//2
            print(l,mid,h)
            if a[mid] == k:
                return mid

            if a[l]<=a[mid] :
                if a[l]<=k<=a[mid]:
                    h=mid-1
                else:
                    l=mid+1
            else:
                if a[mid]<=k<=a[h]:
                    l=mid+1
                else:
                    h = mid-1

        return -1

nums = [4,5,6,7,0,1,2,3]
target = 5
print(Solution().search(nums, target))