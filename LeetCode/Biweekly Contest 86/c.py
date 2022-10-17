class Solution:
    def maximumRows(self, mat, cols: int) -> int:

        n, m = len(mat) ,len(mat[0])
        ans=0
        for i in range(2**m):
            c=set()
            for j in range(m):
                if 2**j & i:
                    c.add(j)
            if len(c)>cols:
                continue
            count = 0
            # print(c)
            for row in range(n):
                flag=True
                for col in range(m):
                    if mat[row][col]==1 and col not in c:
                        flag=False
                        break
                if flag:
                    count +=1
            ans=max(count,ans)
        return ans

mat = [[0,1],[1,0]]
cols = 2
print(Solution().maximumRows(mat, cols))