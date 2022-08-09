"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs(node, count):
            count += 1
            if node.children:
                children = node.children
                for child in children:
                    dfs(child, count)
            else:
                nonlocal deep
                deep = max(deep, count)
        
        deep = 0
        if root:
            dfs(root, deep)
        
        return deep
