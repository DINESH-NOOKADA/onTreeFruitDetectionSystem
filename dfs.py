import cv2
import numpy as np
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid.size==0:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        visited = set()

        def dfs(row, col):
            if (
                row >= ROWS
                or row < 0
                or col >= COLS
                or col < 0
                or grid[row][col] != "1"
                or (row, col) in visited
            ):
                return

            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    count += 1
        return count


def numIslands(self, grid:List[List[str]]):
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

img = cv2.imread('./erodedImages/erodedImage3.png', cv2.IMREAD_GRAYSCALE)
num_mangoes, labels = cv2.connectedComponents(img)
arr = np.asarray(img)
# print(arr.size)

sol=Solution()
# print(sol.numIslands(arr))
print('Number of mangoes: ',num_mangoes-1)
# cv2.imshow("bounding_box", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
