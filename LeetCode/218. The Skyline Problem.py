from heapq import heapify,heappop,heappush
from collections import defaultdict
class Solution:
    def getSkyline(self, buildings):
        def clear():
            if not heap:
                return None
            old_h=-heappop(heap)
            while deleted[old_h]>0:
                deleted[old_h] -=1
                if heap:
                    old_h=-heappop(heap)
                else:
                    return None
            return old_h

        points=[]
        for s,e,h in buildings:
            points.append([s,h,0])
            points.append([e,h,1])
        points.sort(key=lambda x:(x[0],x[2]))
        # print(points)
        heap = []
        res = []
        deleted = defaultdict(int)

        for x, h, ended in points:
            # print("p=",[x,h],"h=",heap,end=" ")
            
            old_h = clear()
            # print("oh=",old_h,end=" ")
            # empty new start
            
            if not old_h:
                res.append([x,h])
                heappush(heap, -h)
            else:
                if ended:
                    deleted[h] += 1
                    heappush(heap, -old_h)
                    old_h=clear()
                    # print("oh=",old_h,end=" ")
                    if not old_h:
                        if res and res[-1][0]==x:
                            res[-1][1] = 0
                        else:
                            res.append([x,0])
                        print()
                        continue
                    # started new end > old
                    if h > old_h:
                        if res and res[-1][0]==x:
                            res[-1][1]=old_h
                        else:
                            res.append([x,old_h])

                else:
                    # started new start > old
                    if h>old_h:
                        if res and res[-1][0]==x:
                            res[-1][1] = h
                        else:
                            res.append([x,h])
                    # started new start < old
                    heappush(heap, -h)
                heappush(heap, -old_h)
            # print("r=",res[-1])

            
        return res
                    

        
        
        
         
        pass
b= [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
buildings =[[1,2,1],[1,2,2],[1,2,3],[2,3,1],[2,3,2],[2,3,3]]
b2=[[4,9,10],[4,9,15],[4,9,12],[10,12,10],[10,12,8]]
b3=[[1,38,219],[2,19,228],[2,64,106],[3,80,65],[3,84,8],[4,12,8],[4,25,14],[4,46,225],[4,67,187],[5,36,118],[5,48,211],[5,55,97],[6,42,92],[6,56,188],[7,37,42],[7,49,78],[7,84,163],[8,44,212],[9,42,125],[9,85,200],[9,100,74],[10,13,58],[11,30,179],[12,32,215],[12,33,161],[12,61,198],[13,38,48],[13,65,222],[14,22,1],[15,70,222],[16,19,196],[16,24,142],[16,25,176],[16,57,114],[18,45,1],[19,79,149],[20,33,53],[21,29,41],[23,77,43],[24,41,75],[24,94,20],[27,63,2],[31,69,58],[31,88,123],[31,88,146],[33,61,27],[35,62,190],[35,81,116],[37,97,81],[38,78,99],[39,51,125],[39,98,144],[40,95,4],[45,89,229],[47,49,10],[47,99,152],[48,67,69],[48,72,1],[49,73,204],[49,77,117],[50,61,174],[50,76,147],[52,64,4],[52,89,84],[54,70,201],[57,76,47],[58,61,215],[58,98,57],[61,95,190],[66,71,34],[66,99,53],[67,74,9],[68,97,175],[70,88,131],[74,77,155],[74,99,145],[76,88,26],[82,87,40],[83,84,132],[88,99,99]]
print(Solution().getSkyline(b2))