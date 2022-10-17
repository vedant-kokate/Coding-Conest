# Definition for a binary tree node.
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) :
        
        d = defaultdict(list)
        
        d[1].append(TreeNode())
        for i in range(3,n+1,2):
            r = 1
            l = i-1-r 
            while r<i:
                for right in d[r]:
                    for left in d[l]:
                        d[i].append(TreeNode(left=left,right=right))
                        # d[i].append(TreeNode(left=right,right=left))
                # print(r,l)
                r+=2
                l-=2
           
                    
        for i in range(1,n+1):
            print(len(d[i]),i)
        # print(d[5])
        return d[n]
Solution().allPossibleFBT(19)