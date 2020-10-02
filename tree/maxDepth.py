"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        stack = []
        if root is not None:
            stack.append((1,root))
        depth = 0
        while stack:
            current_d, root = stack.pop()
            
            if root is not None:
                depth = max(current_d, depth)
                for c in root.children:
                    stack.append((current_d+1, c))
        return depth
                
