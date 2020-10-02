"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        output = []
        stack = [root,]
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            for c in root.children[::-1]:
                stack.append(c)
        return output
        
