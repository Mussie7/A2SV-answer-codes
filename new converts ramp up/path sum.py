# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, total):
            total += node.val
            
            if node.left:
                dfs(node.left, total)
            
            if node.right:
                dfs(node.right, total)
            
            if not node.right and not node.left:
                if total == targetSum:
                    nonlocal exists
                    exists = True
        
        totalSum, exists = 0, False
        if root:
            dfs(root, totalSum)
        
        return exists
