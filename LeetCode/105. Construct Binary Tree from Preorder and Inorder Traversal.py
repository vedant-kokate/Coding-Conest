# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        def build(st,e):
            nonlocal cur
            if st>e:return None

            cur_val = preorder[cur]
            node = TreeNode(cur_val)
            cur+=1
            if st==e:return node 
            
            in_idx = d[cur_val]
            
            node.left,node.right = build(st, in_idx - 1) ,build(in_idx + 1, e)
            return node

        d={}
        for i,val in enumerate(inorder):
            d[val] = i
   
        cur = 0
        return build(0, len(preorder)-1)
def printInorder(node):

	if (node == None):
		return
		
	printInorder(node.left)
	print(node.val, end = " ")
	printInorder(node.right)
preorder = ['A','B','D','E','C','F']
inorder = ['D','B','E','A','F','C']

ans = Solution().buildTree(preorder, inorder)
printInorder(ans)