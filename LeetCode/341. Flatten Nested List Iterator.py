# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
from collections import deque
class NestedIterator:
    def __init__(self, nestedList):
        stack = deqdeque(nestedList[::-1])
        self.i = 0
        self.ans = []
        while stack:
            cur = stack.pop()
            if cur.isInteger:
                self.ans.append(cur)
            else:
                stack.append(cur.getList()[::-1])

        

    def next(self) -> int:
        return self.ans[self.i]
        
    
    def hasNext(self) -> bool:
        return self.i+1<len(self.ans)


nestedList = [[1,1],2,[1,1]]
x=NestedIterator(nestedList)
print(x.ans)
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())