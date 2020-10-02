# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        def help_(root,l=[]):
            if not root:
                return
            if root.left and not root.right:
                l.append(root.left.val)
            if root.right and not root.left:

                l.append(root.right.val)
            help_(root.left,l)
            help_(root.right,l)
            

            return l
        return help_(root)
