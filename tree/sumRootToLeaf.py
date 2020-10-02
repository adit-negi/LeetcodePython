# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(root,number):
            nonlocal out
            if root:
           
                number += str(root.val)
                if not root.left and not root.right:
                    out +=[number]
                dfs(root.left, number)
                dfs(root.right,number)
            return out
        out = []
        array = dfs(root,"")
        print(out)
        s=0
        for i in range(len(array)):
            array[i]= int(array[i],2)
        return sum(array)
