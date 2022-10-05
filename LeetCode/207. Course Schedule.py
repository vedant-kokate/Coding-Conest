from collections import defaultdict
class Solution:
    def canFinish(self, n: int, pre) -> bool:
        g=defaultdict(list)
        for x,y in pre:
            g[x].append(y)
        # print(g)
        def dfs(idx):
            # print(idx,vis)
            if vis[idx]==-1:
                return False
            
            if vis[idx]==1:
                return True
            vis[idx]=-1
            for node in g[idx]:
                if not dfs(node):
                    return False
            vis[idx]=1
            return True

        vis=[0]*n
        for i in range(n):
            if not dfs(i):
                return False

        return True
n = 2
pre = [[1,0],[0,1]]
print(Solution().canFinish(n, pre))