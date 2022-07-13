class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r= 0 , len(h)-1
        area = 0
        while l<r:
            cur_area = min(h[l],h[r])*(r-l)
            area = max(area,cur_area)

            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return area
        
        

h=[1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(h))