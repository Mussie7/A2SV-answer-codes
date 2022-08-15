# Runtime: 65 ms, faster than 98.72% of Python3 online submissions for Recover Binary Search Tree.
# Memory Usage: 14.3 MB, less than 64.76% of Python3 online submissions for Recover Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs_left(node, parent):
            nonlocal ans
            if not node:
                return
            
            if node.val > parent.val:
                if ans and ans.val > node.val:
                    ans = ans
                else:
                    ans = node
                    
            dfs_left(node.left, parent), dfs_left(node.right, parent)
        
        def dfs_right(node, parent):
            nonlocal ans
            if not node:
                return
            
            if node.val < parent.val:
                if ans and ans.val < node.val:
                    ans = ans
                else:
                    ans = node
            
            dfs_right(node.left, parent), dfs_right(node.right, parent)
        
        
        stack, culprit= [root], []
        while stack:
            node = stack.pop()
            
            if not node:
                continue
            
            if node.left:
                ans = None
                dfs_left(node.left, node)
                if ans:
                    culprit.append((node, ans))
                else:
                    stack.append(node.left)
            
            if node.right:
                ans = None
                dfs_right(node.right, node)
                if ans:
                    culprit.append((node, ans))
                else:
                    stack.append(node.right)
            
            if len(culprit) == 2:
                break
            
        if len(culprit) == 1:
            culprit[0][0].val, culprit[0][1].val = culprit[0][1].val, culprit[0][0].val
        elif len(culprit) == 2:
            node1 = culprit[0][1]
            node2 = culprit[1][1]
            node1.val, node2.val = node2.val, node1.val
        
