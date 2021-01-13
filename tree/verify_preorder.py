class Solution:
    def verifyPreorder(self, preorder):
        stack = []
        lower = -10e19
        for x in preorder:
            if x < lower:
                return False
            while stack and x > stack[-1]:
                lower = stack.pop()
            stack.append(x)
        return True
