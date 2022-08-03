class Solution:
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        a.sort(key=lambda x:(x[0],x[1]))
        ans=[[a[0][0],a[0][1]]]
        
        for i in range(1,len(a)):
            if a[i][0]<=ans[-1][-1]:
                ans[-1][-1] = max(ans[-1][-1],a[i][1])
            else:
                ans.append([a[i][0],a[i][1]])
        return ans
            