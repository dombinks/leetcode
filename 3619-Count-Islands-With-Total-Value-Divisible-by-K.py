class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        def fill(grid: List[List[int]], y: int, x: int) -> int:
            out = grid[y][x]
            if grid[y][x] != 0:
                grid[y][x] = 0
                if y > 0:
                    out += fill(grid, y-1, x)
                if y < len(grid) - 1:
                    out += fill(grid, y+1, x)
                if x > 0:
                    out += fill(grid, y, x-1)
                if x < len(grid[0]) - 1:
                    out += fill(grid, y, x+1)

            return out 

        out = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    island = fill(grid, i, j)
                    if island % k == 0:
                        out += 1

        return out
