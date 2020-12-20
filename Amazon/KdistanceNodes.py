# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        def dfs(node, par=None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        seen = {target}
        queue = collections.deque([(target, 0)])
        while queue:
            if queue[0][1] == K:
                return [node.val for node, value in queue]
            node, value = queue.popleft()
            for n in (node.left, node.right, node.par):
                if n and n not in seen:
                    seen.add(n)
                    queue.append((n, value+1))
        return []
