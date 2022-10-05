from collections import defaultdict
class Solution:
    def maxPoints(self, points) -> int:
        def mc(i,j):
            x1,x2,y1,y2=points[i][0],points[j][0],points[i][1],points[j][1]
            if x1==x2:
                m=10**10
            else:
                m = (y1-y2)/(x1-x2)
            c = y1 - x1*m
            return (m,c)
        d = defaultdict(set)
        n = len(points)

        for i in range(n):
            for j in range(i):
                d[mc(i,j)].add(i)
                d[mc(i,j)].add(j)
        # print(d)
        return max(len(v) for v in d.values())
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(Solution().maxPoints(points))