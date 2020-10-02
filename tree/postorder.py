"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        output = []
        stack = [root]
        while stack:
            r = stack.pop()
            if r is not None:
                output.append(r.val)
            for c in r.children:
                stack.append(c)
        return output[::-1]
