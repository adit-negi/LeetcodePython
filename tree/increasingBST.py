# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root,l=[]):
            if root:
                inorder(root.left,l)
                l.append(root.val)
                inorder(root.right,l)
            return l
        l = inorder(root)
        ans = root = TreeNode(None)
        while l:
            v= l.pop(0)
            root.right = TreeNode(v)
            root=root.right
        return ans.right
