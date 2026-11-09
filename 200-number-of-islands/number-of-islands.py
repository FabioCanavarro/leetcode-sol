class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid[0])
        col = len(grid)

        visited = [[0 for _ in range(row)] for _ in range(col)]

        direction = [(0,1),(0,-1),(1,0),(-1,0)]

        def traverse(x,y):
            if not ((0 <= x < col) and (0 <= y < row)):
                return 0

            if (grid[x][y] == "0") or (visited[x][y] == 1):
                return 0

            visited[x][y] = 1

            for dx,dy in direction:
                traverse(x+dx,y+dy)

            return 1

        a = 0


        for i in range(row):
            for j in range(col):
                a += traverse(j,i)
        return a
    

        