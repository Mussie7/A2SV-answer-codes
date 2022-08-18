# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)
        ans = []
        
        while q:
            val, n = 0, len(q)
            
            for _ in range(n):
                node = q.popleft()
                val += node.val
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            ans.append(val/n)
        
        return ans
