# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sortedArrayToBST(self, arr: List[int]) -> TreeNode:
      
        if not arr: 
            return None
        mid = (len(arr)) / 2
        root = TreeNode(arr[int(mid)]) 
        root.left = self.sortedArrayToBST(arr[:int(mid)]) 
        root.right = self.sortedArrayToBST(arr[int(mid+1):]) 
        return root 
