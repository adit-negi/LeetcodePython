# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def find(root,l=[]):
            if not root:
                return l
            if not root.left and not root.right:
                l.append(root.val)
            find(root.left,l)
            find(root.right,l)
            return l
        return find(root1,[])==find(root2,[])
