class Solution:
    def spiralOrder(self, mat) :
        i,j=0,0
        ans = []
        while 0<=i<len(mat) and 0<=j<len(mat[0])and mat[i][j]!=-1000:
            while j<len(mat[0]) and mat[i][j]!=-1000:
                # print(i,j)
                ans.append(mat[i][j])
                mat[i][j] = -1000
                j+=1
            j-=1
            i+=1
            # print(ans)
            while i<len(mat) and mat[i][j]!=-1000:
                # print(i,j)
                ans.append(mat[i][j])
                mat[i][j] = -1000
                i+=1
            i-=1
            j-=1
            # print(ans)
            while j>=0 and mat[i][j]!=-1000:
                ans.append(mat[i][j])
                mat[i][j] = -1000
                j-=1
            j+=1
            i-=1
            # print(ans,i,j)
            while i>=0 and mat[i][j]!=-1000:
                ans.append(mat[i][j])
                mat[i][j] = -1000
                i-=1
            i+=1
            j+=1
            
        return ans
mat = [[1]]
for i in mat:
    print(i)
print()
print(Solution().spiralOrder(mat))