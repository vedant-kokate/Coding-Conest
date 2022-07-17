class Solution:
    def combinationSum(self, can: List[int], target: int) -> List[List[int]]:
        def f(s,arr,idx):
            # print(s)
            if s==target:
                
                self.ans.append(arr)
            for i in range(idx,len(can)):
                if can[i]+s<=target:
                    f(s+can[i], arr+[can[i]],i)
                    
            
        self.ans=[]
        # can.sort()
        # print(can)
        f(0,[],0)
        return self.ans
can = [2,3,6,7]
target = 7

print(Solution().combinationSum(can, target))