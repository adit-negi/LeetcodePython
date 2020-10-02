# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def help_(root,L,R):
            nonlocal sum_
            if root is None:
                return
            if root.val>=L and root.val<=R: 
                sum_+= root.val
            help_(root.left,L,R)
            help_(root.right,L,R)
            return sum_
        sum_=0
        return help_(root,L,R)
