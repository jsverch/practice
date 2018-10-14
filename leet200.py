class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        for x in range(0, len(grid)):
            for y in range(0, len(grid[0])):
                print grid[x][y]


grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]


Solution().numIslands(grid)
