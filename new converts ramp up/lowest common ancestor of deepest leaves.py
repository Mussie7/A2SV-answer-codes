# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node, depth):
            if not node.left and not node.right:
                return (depth, node)
            
            if node.left and node.right:
                depth += 1
                l, r = dfs(node.left, depth), dfs(node.right, depth)
                
                if l[0] > r[0]:
                    return l
                elif r[0] > l[0]:
                    return r
                else:
                    return (l[0], node)

            depth += 1
            return dfs(node.left, depth) if node.left else dfs(node.right, depth)
                    
        return dfs(root, 0)[1]
