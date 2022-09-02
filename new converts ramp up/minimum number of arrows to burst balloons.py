class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows, point = 0, points[0]
        for i in range(1, len(points)):
            if point[1] >= points[i][0]:
                point[0] = max(point[0], points[i][0])
                point[1] = min(point[1], points[i][1])
            else:
                arrows += 1
                point = points[i]
                
        return arrows + 1
