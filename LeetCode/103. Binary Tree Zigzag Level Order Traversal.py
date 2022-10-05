from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        ans = []
        last=-1
        
        stack = deque([(root,0)])
        
        while stack:
            
            cur, l = stack.popleft()
            # print(ans)
            if l!=last:
                ans +=[[cur.val]]
                last = l
            else:
                ans[-1].append(cur.val)
            if cur.left: stack.append((cur.left,l + 1))
            if cur.right: stack.append((cur.right,l + 1))
        Ans = []
        for i,val in enumerate(ans):
            if i%2:
                Ans.append(val)
            else:
                Ans.append(val[::-1])
        return Ans

root =node = TreeNode(3)
node.left,node.right = TreeNode(9),TreeNode(20)
node = node.right
node.left,node.right = TreeNode(15),TreeNode(7)
print(Solution().zigzagLevelOrder(root))