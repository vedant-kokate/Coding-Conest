from collections import defaultdict
class Solution:
    def countSubgraphsForEachDiameter(self, n, edges):
        
        def dfs(use,cur):
            vis = {}
            stack =[(cur,0)]
            last_node = [cur,0]
            vis[cur] = True
            while stack:
                # print(stack)
                cur,cur_dis = stack.pop()
                if cur_dis>last_node[1]:
                    last_node = [cur,cur_dis]
                for node in g[cur]:
                    if node not in vis and use[node] ==1:
                        vis[node] = True 
                        stack.append((node,cur_dis+1))
            if len(vis)!=use.count(1):
                return [-1,-1]
            return last_node
        
        g=defaultdict(set)
        for a,b  in edges:
            g[a-1].add(b-1)
            g[b-1].add(a-1)
        # print(g)
 
        ans = [0]*n
        for i in range(1<<n):
            if i&(i-1):
                # print(bin(i)[2:])
                use = list(map(int, bin(i)[2:]))
                use = [0]*(n-len(use)) + use
                
                for j in range(n):
                    if use[j]:
                        # print(use,j)
                        last_node = dfs(use, j)
                        # print(last_node)
                        if last_node[0] ==-1:
                            break
                        # print(use)
                        # print(last_node)
                        last_node = dfs(use, last_node[0])
                        # print(last_node)
                        ans[last_node[1]]+=1
                        break 
                
        print(ans[1:])
n = 3
edges = [[1,2],[2,3]]
Solution().countSubgraphsForEachDiameter(n, edges)