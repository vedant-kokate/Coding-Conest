from collections import defaultdict
class Solution:
    def solve(self, A, K):
        index = defaultdict(list)
        for i, x in enumerate(A):
            index[x].append(i)

        ans = 0
        for row in index.values():
            print(row)
            i = 0
            for j, y in enumerate(row):
                while row[j] - row[i] - (j - i) > K:
                    i += 1
                ans = max(ans, j - i + K + 1)
                print(ans,i,j)

        return min(ans, len(A))
        
            
a= [7, 5, 5, 3, 2, 5, 5]

k = 1
print(Solution().solve(a, k))