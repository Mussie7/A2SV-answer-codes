# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node.left:
                dfs(node.left)
                left = node.left.val
            else:
                left = 0
                
            if node.right:
                dfs(node.right)
                right = node.right.val
            else:
                right = 0
                
            nonlocal tilt
            if left - right != 0:
                tilt += abs(left - right)
            
            node.val += left + right
                    
        tilt = 0
        if root:
            dfs(root)
        
        return tilt
