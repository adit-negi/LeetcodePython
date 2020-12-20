# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def height(root):
            if root is None:
                return 0
            ld = height(root.left)
            rd = height(root.right)
            return max(ld+1, rd+1)

        def levelorder(root, level, l):
            if not root:
                return
            if level == 1:
                l.append(root.val)
            elif level > 1:
                levelorder(root.left, level-1, l)
                levelorder(root.right, level-1, l)
            return l
        h = height(root)
        l = []
        for i in range(1, h+1):
            if i % 2 == 0:
                temp = levelorder(root, i, [])
                temp = temp[::-1]
                l.append(temp)
            else:
                l.append(levelorder(root, i, []))
        return l
