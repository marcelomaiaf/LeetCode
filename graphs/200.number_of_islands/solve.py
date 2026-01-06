class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(i,j):
            if (i,j) in visited:
                return True
            if i < 0 or i > (m - 1):
                return True
            elif j < 0 or j  > (n - 1):
                return True
            elif grid[i][j] == "0":
                return True
                
            visited.add((i,j))
            return dfs(i - 1, j) and dfs(i+1, j) and dfs(i, j-1) and dfs(i, j+1)

        visited = set()
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i,j) in visited or grid[i][j] == "0":
                    continue
                if dfs(i,j):
                    count += 1
                    
        return count
        