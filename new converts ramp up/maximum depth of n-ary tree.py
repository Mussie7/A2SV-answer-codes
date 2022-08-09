# Runtime: 38 ms, faster than 99.39% of Python3 online submissions for Maximum Depth of N-ary Tree.
# Memory Usage: 15.9 MB, less than 93.83% of Python3 online submissions for Maximum Depth of N-ary Tree.


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
                for child in node.children:
                    dfs(child, count)
            else:
                nonlocal deep
                deep = max(deep, count)
        
        deep = 0
        if root:
            dfs(root, deep)
        
        return deep
