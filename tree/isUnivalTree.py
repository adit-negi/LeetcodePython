# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        seen = set()
        def dfs(root):
            if root is not None:
                seen.add(root.val)
                dfs(root.left)
                dfs(root.right)
        
            return len(seen)==1
        return dfs(root)
