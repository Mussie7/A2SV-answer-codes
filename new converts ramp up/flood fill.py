class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image[0]), len(image)
        starting_color = image[sr][sc]
        
        if starting_color == color:
            return image
        
        image[sr][sc] = color
        stack = [(sr, sc)]
        DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while stack:
            temp = stack.pop()
            for direction in DIRECTION:
                new_row, new_col = temp[0] + direction[0], temp[1] + direction[1]

                if new_row < 0 or new_col < 0 or new_row >= m or new_col >= n or image[new_row][new_col] != starting_color:
                    continue
                image[new_row][new_col] = color
                stack.append((new_row, new_col))
        
        return image
