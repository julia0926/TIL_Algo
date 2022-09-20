# https://leetcode.com/problems/number-of-islands/

from cgitb import grey


class Solution:
    def numIslands(grid):
        def dfs(i, j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i-1, j)
                dfs(i, j-1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
        

