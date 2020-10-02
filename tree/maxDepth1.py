# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def maxDepth(self, node: TreeNode) -> int:

        if node is None: 
            return 0 ;  

        else : 

            # Compute the depth of each subtree 
            lDepth = self.maxDepth(node.left) 
            rDepth = self.maxDepth(node.right) 

            # Use the larger one 
            return max(lDepth+1,rDepth+1)

        
