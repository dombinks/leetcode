class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rowsFlipped = 0
        colsFlipped = 0

        for row in grid:
            left = 0
            right = len(row) - 1

            while left < right:
                if row[left] != row[right]:
                    rowsFlipped += 1

                left += 1
                right -= 1

        for i in range(len(grid[0])):
            upper = 0
            lower = len(grid) - 1

            while upper < lower:
                if grid[upper][i] != grid[lower][i]:
                    colsFlipped += 1

                upper += 1
                lower -= 1

        return min(rowsFlipped, colsFlipped)
