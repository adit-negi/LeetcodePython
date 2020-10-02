# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        l=[]
        def height(root):
            if root is None:
                return 0
            if root is not None:
                ld = height(root.left)
                rd = height(root.right)
            return max(ld+1,rd+1)
        def levelorder(root,temp=[],level=height(root)):
            if root is not None:
                if level==1:
                    temp.append(root.val)
                elif level>1:
                    levelorder(root.left,temp, level-1)
                    levelorder(root.right,temp, level-1)
            return temp
        h = height(root)
        output = []
        for i in range(1,h+1):
            l = levelorder(root,[],i)
            answer = sum(l)/len(l)
            
            output.append(answer)
        return output
        
