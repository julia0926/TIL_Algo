#https://leetcode.com/problems/number-of-islands/description/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            #종료 조건
            if x < 0 or y < 0 or \
                x >= len(grid) or y >= len(grid[0]) or \
                grid[x][y] != '1':
                    return 
            grid[x][y] = '0' #방문처리
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    result += 1
        return result