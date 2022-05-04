class Solution:
    def maxArea(self, height: List[int]) -> int:
        lt , rt = 0, len(height) - 1
        area = min(height[lt], height[rt]) * (rt - lt)
        while lt < rt:
            if height[lt] < height[rt]:
                lt += 1
            else:
                rt -= 1
            area = max(area, min(height[lt], height[rt])*(rt-lt))
        
        return area
