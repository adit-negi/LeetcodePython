# question link - https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        def height(root):
            if not root:
                return 0
            l = height(root.left)
            r = height(root.right)
            return max(l, r)+1

        def level(h, root, l):
            if root:
                if h == 0:
                    l.append(root)
                else:
                    level(h-1, root.left, l)
                    level(h-1, root.right, l)
            return l

        def findheight(h, q):
            nonlocal height
            temp = []

            while q:
                val = q.pop()
                if val == u:
                    height = h
                    return h
                if val.right:
                    temp.append(val.right)
                if val.left:
                    temp.append(val.left)
            findheight(h+1, temp)

        height = 0
        level_of_u = findheight(0, [root])

        list_of_nodes = level(height, root, [])
        for i in range(len(list_of_nodes)):
            if list_of_nodes[i] == u and i != len(list_of_nodes)-1:
                return list_of_nodes[i+1]
        return None
