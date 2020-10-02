# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trim(root):
            if not root:
                return None
            if root.val<low:
                return trim(root.right)
            if root.val>high:
                return trim(root.left)
            root.left = trim(root.left)
            root.right = trim(root.right)
            return root
        return trim(root)
